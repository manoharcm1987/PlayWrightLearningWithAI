pytest_plugins = [
    "framework.fixtures.browser_fixtures"
]


# import pytest
# from playwright.sync_api import sync_playwright

# from framework.browser.browser_factory import BrowserFactory
# from framework.config.browser_config_loader import BrowserConfigLoader


# @pytest.fixture(scope="session")
# def browser():
#     """
#      Create a browser instance for the test session.
#      """
#     config = BrowserConfigLoader.load()

#     with sync_playwright() as playwright:

#         browser = BrowserFactory.create(
#             playwright,
#             config
#         )

#         yield browser

#         browser.close()
        
# @pytest.fixture
# def context(browser):

#     context = browser.new_context()

#     yield context

#     context.close()
    

# @pytest.fixture
# def page(context):

#     page = context.new_page()

#     yield page

#     page.close()
        

# @pytest.fixture(scope="session")
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         browser.close()