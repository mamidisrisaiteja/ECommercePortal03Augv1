import pytest
from playwright.sync_api import sync_playwright
import yaml

@pytest.fixture(scope="session")
def config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
