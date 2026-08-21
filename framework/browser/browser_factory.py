
from playwright.sync_api import Playwright
from framework.browser.browser_config import BrowserConfig
from framework.browser.launchers.chromium_launcher import ChromiumLauncher
from framework.browser.launchers.firefox_launcher import FirefoxLauncher
from framework.browser.launchers.web_kit_launcher import WebKitLauncher

from framework.browser.browser_type import BrowserType
from framework.exceptions.browser_exceptions import BrowserNotRegisteredError


class BrowserFactory:

    _launchers = {
        BrowserType.CHROMIUM: ChromiumLauncher,
        BrowserType.FIREFOX: FirefoxLauncher,
        BrowserType.WEBKIT: WebKitLauncher,
    }

    @classmethod
    def create(cls, playwright: Playwright, config: BrowserConfig):
        """
            Creates a Playwright browser using the registered launcher.
            Args:
                playwright (Playwright): The Playwright instance.
                config (BrowserConfig): The configuration for the browser."""
        # launcher_class = cls._launchers.get(config.browser)
        # if not launcher_class:
        #     raise BrowserNotRegisteredError(f"No launcher registered for browser type: {config.browser}")
        # return launcher_class().launch(playwright, config)
        try:
            launcher_class = cls._launchers[config.browser]
        except KeyError as ex:
            raise BrowserNotRegisteredError(f"No launcher registered for '{config.browser}'. 'Register a launcher before calling BrowserFactory.create().'") from ex
        return launcher_class().launch(playwright, config)

    @classmethod
    def register_launcher(cls, browser_type: BrowserType, launcher_class: type) -> None:
        cls._launchers[browser_type] = launcher_class