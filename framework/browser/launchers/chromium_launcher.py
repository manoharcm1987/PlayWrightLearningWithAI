

from playwright.sync_api import Browser, Playwright

from framework.browser.browser_config import BrowserConfig
from framework.browser.launchers.browser_launcher import BrowserLancher


class ChromiumLauncher(BrowserLancher):
    """Launch a Chromium browser instance."""

    def launch(self, playwright: Playwright, config: BrowserConfig) -> Browser:
        return playwright.chromium.launch(headless=config.headless, slow_mo=config.slow_mo )