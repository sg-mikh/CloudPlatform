import re

from selenium import webdriver

from framework.helpers.wait import wait_while
from framework.ui.pageobjects.base_page import BasePage


class Browser:

    def __init__(self, host: str):
        self.host = host

        capabilities = {
            "browserName": "chrome",
            "platform": "ANY",
            "goog:chromeOptions": {
                "binary": "",
                "args": ["--window-size=1920,1080"]
            }
        }
        self.web_driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                           desired_capabilities=capabilities)

    @property
    def current_url(self):
        return self.web_driver.current_url

    def navigate_to(self, page: BasePage):
        page_obj = page(self.web_driver)
        self.web_driver.get(self.host + page_obj.page_path)
        return page_obj

    def is_page_current(self, page: BasePage):
        result = False

        def f():
            current_url = self.web_driver.current_url
            return current_url.replace(self.host, "")

        if wait_while(lambda: f().startswith(page(self.web_driver).page_path), timeout=10):
            result = True
        return result

    def is_url_include_str(self, expected_str: str):
        return wait_while(lambda: re.search(fr"{expected_str}", self.current_url))

    def switch_to_tab(self, tab_number: int):
        wait_while(lambda: len(self.web_driver.window_handles) >= 2)
        tab_handler = self.web_driver.window_handles[tab_number]
        self.web_driver.switch_to.window(tab_handler)

    def close_current_tab(self):
        self.web_driver.close()

    def refresh(self):
        self.web_driver.refresh()

    def quit(self):
        self.web_driver.quit()
