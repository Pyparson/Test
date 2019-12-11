from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class TestSelenium:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # sleep(2)
        # self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skip(reason="用例已失效")
    def test_one(self):
        self.driver.get("https://testerhome.com/")
        sleep(5)
        # topics = self.driver.find_elements(By.XPATH,"//*[@class='title media-heading']")
        # sleep(5)
        # topics[1].click()
        topic = self.driver.find_element_by_link_text("TesterHome 上海 & UWA & Jenkins 中文社区 2019年10月 沙龙活动")
        topic.click()
        sleep(2)
        windows = self.driver.window_handles
        print(windows)
        self.driver.switch_to.window(windows[-1])
        sleep(20)

    @allure.title("作业")
    def test_0728home1(self):
        self.driver.get("https://testerhome.com/topics/19832")
        self.driver.find_element(By.CSS_SELECTOR, 'button[class*="btn btn-default"]').click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'整体架构')]").click()
        sleep(3)
