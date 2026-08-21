from framework.browser.browser_config import BrowserConfig
from framework.browser.browser_factory import BrowserFactory
from framework.browser.browser_type import BrowserType
from framework.browser.launchers.browser_launcher import BrowserLancher

class FakeBrowser:
    pass



class FakeLauncher(BrowserLancher):
    received_playwright = None
    received_config = None
    browser_to_return = None
   
    def launch(self, playwright, config) -> FakeBrowser:
        FakeLauncher.received_playwright = playwright
        FakeLauncher.received_config = config
        return self.browser_to_return

def test_create_delegates_to_registered_launcher(monkeypatch):
    fake_browser = FakeBrowser()
    FakeLauncher.browser_to_return = fake_browser
    # Arrange
    config = BrowserConfig(browser=BrowserType.CHROMIUM)
    monkeypatch.setitem(BrowserFactory._launchers, BrowserType.CHROMIUM, FakeLauncher)

    # Act
    browser = BrowserFactory.create(playwright=None, config=config)

    # Assert
    assert browser is fake_browser
    assert FakeLauncher.received_config is config
