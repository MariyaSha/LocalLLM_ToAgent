from tools import (
    ask,
    choose,
    search_query,
    check_websites,
    search_homepage,
    research_webpages,
    save_report,
)
import time

CITY = "Vancouver, BC"
TRADE = "HVAC"

# record execution time
total_start = time.perf_counter()

# Find competitors
print("\n🐍 Searching businesses...")
results = search_query(CITY, TRADE)
results = check_websites(results)

print("🧠 Choosing competitors...")
start = time.perf_counter()

competitors = choose(
    "0_choose_competitors.md",
    city=CITY,
    trade=TRADE,
    results=results,
)

for competitor in competitors:
    print("   ✓", competitor["name"])

print(f"⏱ Competitors selected ({time.perf_counter() - start:.1f}s)")

# Research competitors
research = []

for i, competitor in enumerate(competitors, 1):
    name = competitor["name"]
    website = competitor["url"]

    print(f"\n🐍 Exploring {name}...")
    homepage, pages = search_homepage(website)

    print("🧠 Choosing pages...")
    start = time.perf_counter()

    pages = choose(
        "1_choose_pages.md",
        trade=TRADE,
        name=name,
        website=website,
        homepage=homepage,
        pages=pages,
    )

    elapsed = time.perf_counter() - start

    if not pages:
        pages = [website]
        print(f"🐍 No pages chosen - using homepage ({elapsed:.1f}s)")
    else:
        print(f"   ✓ {len(pages)} pages selected ({elapsed:.1f}s)")

    print("✨ Researching pages...")
    notes = research_webpages(
        TRADE,
        name,
        website,
        pages,
    )

    print("✨ Creating competitor overview...")
    start = time.perf_counter()

    company = ask(
        "3_create_competitor_overview.md",
        trade=TRADE,
        name=name,
        website=website,
        notes=notes,
    )

    filename = f"competitor_{i}.md"
    save_report(filename, company)
    print(f"🐍 Saved {filename} ({time.perf_counter() - start:.1f}s)")

    research.append({
        "name": name,
        "website": website,
        "overview": company,
    })

    del notes, company, homepage, pages

# Create final report
print("\n✨ Creating final market research report...")
start = time.perf_counter()

report = ask(
    "4_create_final_report.md",
    max_tokens=3000,
    city=CITY,
    trade=TRADE,
    research=research,
)

save_report("market_research.md", report)
print(f"🐍 Saved market_research.md ({time.perf_counter() - start:.1f}s)")
print("\n✓ Research complete!")
print(f"⏱ Total execution time: {time.perf_counter() - total_start:.1f}s")
