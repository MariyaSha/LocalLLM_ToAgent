from tools import (
    ask,
    choose,
    search_query,
    search_homepage,
    research_webpages,
    save_report
)

CITY = "Vancouver"
TRADE = "pub"


# Find competitors
results = search_query(CITY, TRADE)

websites = choose(
    "competitors.md",
    city=CITY,
    trade=TRADE,
    results=results
)


# Research competitors
research = []

for i, website in enumerate(websites, 1):

    homepage, pages = search_homepage(website)

    pages = choose(
        "pages.md",
        trade=TRADE,
        website=website,
        homepage=homepage,
        pages=pages
    )

    notes = research_webpages(
        TRADE,
        website,
        pages
    )

    company = ask(
        "company.md",
        trade=TRADE,
        website=website,
        notes=notes
    )

    save_report(
        f"competitor_{i}.md",
        company
    )

    research.append(company)


# Create final report
report = ask(
    "report.md",
    city=CITY,
    trade=TRADE,
    research=research
)

save_report(
    "market_research.md",
    report
)