import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree

import requests
import torch
from bs4 import BeautifulSoup
from transformers import pipeline
from transformers.utils import logging


logging.set_verbosity_error()

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


# LOAD MODEL

llm = pipeline(
    "text-generation",
    model="nvidia/NVIDIA-Nemotron-Nano-9B-v2",
    device_map="auto",
    dtype=torch.bfloat16,
)


# AI TOOLS

def ask(file, max_tokens=2000, **data):
    data = {
        key: json.dumps(value, indent=2)
        if isinstance(value, (list, dict))
        else value
        for key, value in data.items()
    }

    prompt = Path(
        "prompts",
        file
    ).read_text().format(**data)

    output = llm(
        [{"role": "user", "content": prompt}],
        max_new_tokens=max_tokens
    )

    text = output[0]["generated_text"][-1]["content"]

    if "</think>" in text:
        text = text.split("</think>", 1)[1]

    return text.strip()


def choose(file, **data):
    answer = ask(file, **data)

    match = re.search(
        r"\[[\s\S]*?\]",
        answer
    )

    if not match:
        print("\nNemotron replied:")
        print(answer)
        raise ValueError("Nemotron did not return a list.")

    return json.loads(match.group())


# SEARCH TOOLS

def search_query(city, trade):
    query = f"{city} {trade} official website services contact"

    response = requests.post(
        "https://html.duckduckgo.com/html",
        data={"q": query},
        headers={
            **HEADERS,
            "Referer": "https://html.duckduckgo.com/",
        },
        timeout=20,
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    results = []

    for link in soup.select(".result__a")[:10]:
        results.append({
            "title": link.get_text(" ", strip=True),
            "url": link.get("href"),
        })

    return results


def search_homepage(website):
    homepage = read_page(website)
    pages = discover_pages(website)

    return homepage, pages


def discover_pages(website):
    pages = {website.rstrip("/")}

    sitemap = requests.get(
        urljoin(website, "/sitemap.xml"),
        headers=HEADERS,
        timeout=20,
    )

    try:
        root = ElementTree.fromstring(sitemap.text)

        for item in root.iter():
            if not (
                item.tag.endswith("loc")
                and item.text
            ):
                continue

            url = item.text.strip()

            if url.endswith(".xml"):
                child = requests.get(
                    url,
                    headers=HEADERS,
                    timeout=20,
                )

                try:
                    child_root = ElementTree.fromstring(
                        child.text
                    )

                    for child_item in child_root.iter():
                        if (
                            child_item.tag.endswith("loc")
                            and child_item.text
                        ):
                            pages.add(
                                child_item.text.strip()
                            )

                except ElementTree.ParseError:
                    pass

            else:
                pages.add(url)

    except ElementTree.ParseError:
        pass

    soup = BeautifulSoup(
        requests.get(
            website,
            headers=HEADERS,
            timeout=20,
        ).text,
        "html.parser",
    )

    host = urlparse(
        website
    ).netloc.replace("www.", "")

    for link in soup.find_all("a", href=True):
        url = urljoin(
            website,
            link["href"],
        )

        parsed = urlparse(url)

        if (
            parsed.netloc.replace("www.", "")
            == host
        ):
            pages.add(
                f"{parsed.scheme}://"
                f"{parsed.netloc}"
                f"{parsed.path}"
            )

    return sorted(pages)


def read_page(url):
    soup = BeautifulSoup(
        requests.get(
            url,
            headers=HEADERS,
            timeout=20,
        ).text,
        "html.parser",
    )

    for tag in soup(
        ["script", "style", "svg", "noscript"]
    ):
        tag.decompose()

    return soup.get_text(
        "\n",
        strip=True,
    )[:12000]


# RESEARCH TOOLS

def research_webpages(trade, name, website, pages):
    notes = []

    for url in pages:
        content = read_page(url)

        notes.append(
            ask(
                "research.md",
                trade=trade,
                name=name,
                website=website,
                url=url,
                content=content
            )
        )

    return notes


def save_report(file, content):
    Path(file).write_text(
        content,
        encoding="utf-8"
    )

def check_websites(results):
    valid = []

    for result in results:
        try:
            content = read_page(result["url"])

            blocked = any(word in content.lower() for word in [
                "cloudflare",
                "access denied",
                "security verification",
                "just a moment"
            ])

            if content and not blocked:
                valid.append(result)

        except:
            pass

    return valid