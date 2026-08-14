
from framework.browser.launchers.chromium_launcher import ChromiumLauncher
from framework.browser.launchers.firefox_launcher import FirefoxLauncher
from framework.browser.launchers.web_kit_launcher import WebKitLauncher

from framework.browser.browser_type import BrowserType



class BrowserFactory:

    _launchers = {BrowserType.CHROMIUM: ChromiumLauncher(), BrowserType.FIREFOX: FirefoxLauncher(), BrowserType.WEBKIT: WebKitLauncher()}


    # launcher = self._launchers[BrowserType.CHROMIUM]
    # return launcher.launch(playwright, browser_config)