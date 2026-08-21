from abc import ABC, abstractmethod
from playwright.sync_api import Playwright, Browser
from framework.browser.browser_config import BrowserConfig

class BrowserLancher(ABC):

    @abstractmethod
    def launch(self, playwright: Playwright, config: BrowserConfig) -> Browser:
        """
        
        Launches a browser instance based on the provided configuration."""
        pass

