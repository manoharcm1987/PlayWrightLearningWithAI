from dataclasses import dataclass

from framework.browser.browser_type import BrowserType

@dataclass(frozen=True, slots=True)
class BrowserConfig:
    browser: BrowserType = BrowserType.CHROMIUM
    headless: bool = False
    slow_mo: float = 0.0