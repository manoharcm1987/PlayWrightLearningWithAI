


from enum import Enum

from framework.browser.browser_type import BrowserType


class ExecutionContext:
    browser : BrowserType = BrowserType.CHROMIUM
    launch_time_ms : int = 0
    started_at : str = ""
    
