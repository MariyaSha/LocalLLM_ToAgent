from tools import (
    ask,
    choose,
    search_query,
    check_websites,
    search_homepage,
    research_webpages,
    save_report,
)

CITY = "Vancouver, BC"
TRADE = "HVAC"


# Find competitors
print("\n🐍 Searching businesses...")
results = search_query(CITY, TRADE)
results = check_websites(results)

print("🧠 Choosing competitors...")
competitors = choose(
    "competitors.md",
    city=CITY,
    trade=TRADE,
    results=results,
)

for competitor in competitors:
    print("   ✓", competitor["name"])


# Research competitors
research = []

for i, competitor in enumerate(competitors, 1):
    name = competitor["name"]
    website = competitor["url"]

    print(f"\n🐍 Exploring {name}...")
    homepage, pages = search_homepage(website)

    print("🧠 Choosing pages...")
    pages = choose(
        "choose_pages.md",
        trade=TRADE,
        name=name,
        website=website,
        homepage=homepage,
        pages=pages,
    )

    if not pages:
        pages = [website]
        print("🐍 No pages chosen - using homepage")
    else:
        print(f"   ✓ {len(pages)} pages selected")

    print("✨ Researching pages...")
    notes = research_webpages(
        TRADE,
        name,
        website,
        pages,
    )

    print("✨ Creating competitor overview...")
    company = ask(
        "company.md",
        trade=TRADE,
        name=name,
        website=website,
        notes=notes,
    )

    filename = f"competitor_{i}.md"
    save_report(filename, company)
    print(f"🐍 Saved {filename}")

    research.append({
        "name": name,
        "website": website,
        "overview": company,
    })


# Create final report
print("\n✨ Creating final market research report...")
report = ask(
    "report.md",
    max_tokens=3000,
    city=CITY,
    trade=TRADE,
    research=research,
)

save_report("market_research.md", report)
print("🐍 Saved market_research.md")
print("\n✓ Research complete!")
