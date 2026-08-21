from playwright.sync_api import Browser, Playwright

from framework.browser.browser_config import BrowserConfig
from framework.browser.launchers.browser_launcher import BrowserLancher

class FirefoxLauncher(BrowserLancher):


    def launch(self, playwright: Playwright, config: BrowserConfig) -> Browser:
        """Launch a Firefox browser instance."""
        return playwright.firefox.launch(headless=config.headless, slow_mo=config.slow_mo)