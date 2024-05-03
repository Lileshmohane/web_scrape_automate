import asyncio
import pprint

from ai_extractor import extract
from schemas import SchemaNewsWebsites, ecommerce_schema
from scrape import ascrape_playwright

# TESTING
if __name__ == "__main__":
    token_limit = 4000

    # News sites mostly have <span> tags to scrape
    cnn_url = "https://www.bakersfieldcity.us/518/Projects-Programs"
    wsj_url = "https://www.cityofarcata.org/413/Current-City-Construction-Projects"
    nyt_url = "https://www.ci.richmond.ca.us/1404/Major-Projects"

    project_url = "https://www.eurekaca.gov/744/Current-Projects"

    async def scrape_with_playwright(url: str, tags, **kwargs):
        html_content = await ascrape_playwright(url, tags)

        print("Extracting content with LLM")

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(**kwargs,
                                    content=html_content_fits_context_window_llm)

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM
    asyncio.run(scrape_with_playwright(
        url=wsj_url,
        tags=["span"],
        # schema_pydantic=SchemaNewsWebsites
        schema= ecommerce_schema
    ))
