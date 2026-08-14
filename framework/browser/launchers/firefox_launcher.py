

class FirefoxLauncher:


    def launch(self, playwright, browser_config):
        return playwright.firefox.launch(headless=browser_config.headless, slow_mo=browser_config.slow_mo)