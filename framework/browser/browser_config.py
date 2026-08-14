from dataclasses import dataclass
from enum import Enum

from framework.browser.browser_type import BrowserType

@dataclass(frozen=True, slots=True)
class BrowserConfig:
    browser : Enum = BrowserType.CHROMIUM
    headless : bool = False
    slow_mo : float = 0.0