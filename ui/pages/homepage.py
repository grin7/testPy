from ui.base.basepage import BasePage
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.__searchInput: str = 'q'
        self.__searchButton: str = 'btnK'
        self.__resultLinks: str = '//div[@id="res"]//g-menu-item//a'

    def do_search(self):
        self.open()
        self.is_visible('name', self.__searchInput, 'Search field').send_keys('test')
        self.is_visible('name', self.__searchButton, 'Search button').click()

    def get_result_links(self) -> List[WebElement]:
        return self.are_present('xpath', self.__resultLinks, 'Result links')
