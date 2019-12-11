#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Parson
from time import sleep
import pytest
import allure
from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)


class TestWork:
    @pytest.fixture(autouse=True)
    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com")
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    # def setup_method(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("https://testerhome.com")
    #     self.driver.implicitly_wait(10)
    #     # yield
    #     # self.driver.quit()
    #
    # def teardown_method(self):
    #     self.driver.quit()

    def find_element_until_visibility(self, locator, timeout=10):
        try:
            ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return ele
        except NoSuchElementException:
            logging.info("Retrying to find element by %s: %s" % (locator[0], locator[1]))
        raise NoSuchElementException

    @allure.description("课间作业")
    def test_work01(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[title*="议题征集"]').click()
        # self.driver.find_element(By.CSS_SELECTOR,'button[class*="btn btn-default"]').click()
        self.find_element_until_visibility((By.CSS_SELECTOR, 'button[class*="btn btn-default"]')).click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'征集议题范围')]").click()
        text = self.find_element_until_visibility((By.CSS_SELECTOR, 'h2[id*="议题征集"]')).text
        logging.info(text)
        assert "征集流程" == text, "Test Failed!!!"

    @allure.description("最新发布的帖子浏览")
    def test_work02(self):
        self.find_element_until_visibility((By.CSS_SELECTOR, 'a[href*="last"]')).click()
        sleep(3)
        topic = self.find_element_until_visibility((By.CSS_SELECTOR, 'a[href="/topics/last"]')).text
        logging.info(topic)
        assert "最新发布" == topic, "Test Failed!!!"

    def test_work03(self):
        """社区访问霍格沃兹测试学院，断言未登录是被拒绝的"""
        # self.driver.find_element(By.CSS_SELECTOR, 'a[href="/teams"]').click()
        # self.driver.find_element(By.CSS_SELECTOR, 'a[data-name="霍格沃兹测试学院"]').click()
        # self.driver.find_element(By.XPATH, '(//a[contains(@title,"第十期")])[1]').click()
        self.find_element_until_visibility((By.CSS_SELECTOR, 'a[href="/teams"]')).click()
        self.find_element_until_visibility((By.CSS_SELECTOR, 'a[data-name="霍格沃兹测试学院"]')).click()
        self.find_element_until_visibility((By.XPATH, '(//a[contains(@title,"第十期")])[1]')).click()
        sleep(3)
        toast = self.driver.find_element_by_css_selector('.alert-danger').text
        assert "访问被拒绝，你可能没有权限或未登录。" == toast, "Test Failed!!!"
        assert "访问被拒绝，你可能没有权限或未登录。" in self.driver.page_source, "Test Failed!!!"

    @pytest.mark.parametrize("email,password", [("111111", "222222"),
                                                ("22222@33.com", "ASDDFFFF")])
    def test_work04(self, email, password):
        """错误用户名和密码登陆"""
        self.find_element_until_visibility((By.CSS_SELECTOR, 'a[href="/account/sign_in"]')).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="user_login"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="user_password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        # self.find_element_until_visibility(By.XPATH,'//*[@id="user_login"]').send_keys(email)
        # self.find_element_until_visibility(By.XPATH,'//*[@id="user_password"]').send_keys(password)
        # self.find_element_until_visibility(By.CSS_SELECTOR, 'input[type="submit"]').click()
        sleep(3)
        toast = self.driver.find_element_by_css_selector('.alert-warning').text
        assert "没有该用户，请您重新注册。" in self.driver.page_source, "Test Failed!!!"
        assert "没有该用户，请您重新注册。" == toast, "Test Failed!!!"

    def test_work05(self):
        """搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的"""
        self.find_element_until_visibility((By.CSS_SELECTOR, '.form-control')).send_keys("测试媛")
        self.find_element_until_visibility((By.CSS_SELECTOR, '.form-control')).send_keys(Keys.ENTER)
        # self.find_element_until_visibility((By.CSS_SELECTOR,'.fa-search')).click()
        # sleep(3)
        topic = self.find_element_until_visibility((By.XPATH, '//div/a[contains(@href,"4331")]'))
        topic_text = topic.text
        logging.info(topic_text)
        topic.click()
        title = self.find_element_until_visibility((By.CSS_SELECTOR, 'h1[class="media-heading"]'))
        title_text = title.text
        logging.info(title_text)
        assert topic_text in title_text, "Test Failed!!!"

    def test_work06(self):
        """切换handles"""
        self.find_element_until_visibility((By.CSS_SELECTOR, 'a[title*="议题征集"]')).click()
        self.find_element_until_visibility((By.XPATH, '//h2/a[contains(@href,"6038911")]')).click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        text = self.find_element_until_visibility((By.XPATH, '//div[contains(@class,"attend")]/a')).text
        logging.info(text)
        self.driver.switch_to.window(handles[0])
        link = self.find_element_until_visibility((By.XPATH, '//h2/a[contains(@href,"6038911")]')).text
        logging.info(link)
        assert "我要报名" == text, "Test Failed!!!"
        assert "https://www.bagevent.com/event/6038911" == link, "Test Failed!!!"

    # TODO  切换frame
    @pytest.mark.skip(reason="此用例暂时有问题,没有找到很好的frame例子")
    def test_work07(self):
        self.driver.get("https://testerhome.com/topics/19664")
        sleep(5)
        self.driver.switch_to.frame(1)
        sleep(5)
        text = self.find_element_until_visibility((By.XPATH, "//h1")).text
        logging.info(text)
        # self.driver.switch_to.default_content()
        # total = self.find_element_until_visibility(By.CSS_SELECTOR, ".total").text
        # logging.info(total)
        assert "【MTSC2019】我最喜欢的议题评选（有奖投票）" == text, "Test Failed!!!"
        # assert "【MTSC2019】我最喜欢的议题评选（有奖投票）" == total, "Test Failed!!!"

    def test_work08(self):
        """窗口滑动"""
        self.find_element_until_visibility((By.CSS_SELECTOR, 'a[href*="last"]')).click()
        sleep(3)
        self.driver.execute_script("window.scrollTo(0,700)")
        sleep(5)
        text = self.find_element_until_visibility((By.CSS_SELECTOR,'.sidebar-count')).text
        # text = self.find_element_until_visibility((By.CSS_SELECTOR, 'div[class="sidebar-count"]')).text
        # text = self.find_element_until_visibility((By.XPATH,'//div[@class="media-right"]/div')).text
        logging.info(text)
        assert "25 篇" == text, "Test Failed!!!"

    # TODO  左滑删除操作
    @pytest.mark.skip(reason="此用例暂时有问题,没有找到很好的frame例子")
    def test_work07(self):
        self.driver.execute_script('mobile:dragFromToForDuration', {'duration': 0, 'fromX': 180, 'fromY': 75, 'toX': 0, 'toY': 75})
        sleep(2)
