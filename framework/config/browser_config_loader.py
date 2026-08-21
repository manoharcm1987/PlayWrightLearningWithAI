

from framework.browser.browser_config import BrowserConfig


class BrowserConfigLoader:

    @classmethod
    def load(cls)->BrowserConfig:
        """
        Loads the browser configuration.
        """

        return BrowserConfig()
