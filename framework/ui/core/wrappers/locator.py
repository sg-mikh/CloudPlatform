from selenium.webdriver.common.by import By


class Locator:

    @staticmethod
    def id(value):
        return By.ID, value

    @staticmethod
    def xpath(value):
        return By.XPATH, value

    @staticmethod
    def class_name(value):
        return By.CLASS_NAME, value

    @staticmethod
    def css(value):
        return By.CSS_SELECTOR, value
