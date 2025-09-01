import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture

def setup_swarovski():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.swarovski.com/en-AA/")

        yield page
        page.close()
        browser.close()
        print("test end")