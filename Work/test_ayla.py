from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAyla:
    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9999"

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://aylasunsea.sunseaiot.com/proreail")

    def teardown_method(self):
        self.driver.quit()

    def test_one(self):
        self.driver.find_element(By.XPATH,
                                 "//*[@id='app']/div[1]/div[2]/div/div[2]/div[2]/ul/li[4]/div[2]/div[1]").click()
        button = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div/div[1]/div/ul/li[1]")
        print(button.text)
        button.click()
        # self.driver.execute_script(
        #     'document.getElementsByClassName("inputSize")[0].value="/Users/parson/Documents/02_Code/PyDemo/images/0.png"')

        upload_btn = self.driver.find_elements(By.XPATH, '//input[@class="inputSize"]')
        upload_btn[2].send_keys("/Users/parson/Documents/02_Code/PyDemo/images/1.png")


