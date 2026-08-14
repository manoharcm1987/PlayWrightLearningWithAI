

from playwright.sync_api import Browser, Playwright

from framework.browser.browser_config import BrowserConfig
from framework.browser.launchers.browser_launcher import BrowserLancher


class ChromiumLauncher(BrowserLancher):

    def launch(self, playwright: Playwright, browser_config: BrowserConfig) -> Browser:
        return playwright.chromium.launch(headless=browser_config.headless, slow_mo=browser_config.slow_mo )