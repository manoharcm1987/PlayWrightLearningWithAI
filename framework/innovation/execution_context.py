


from datetime import datetime

from framework.browser.browser_type import BrowserType


class ExecutionContext:
    browser : BrowserType = BrowserType.CHROMIUM
    launch_time_ms : float = 0
    started_at : datetime
    
