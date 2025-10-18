from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class BasePage:
    """页面基类 - 增强版本"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # 增加等待时间

    def find_element(self, by, value, timeout=15):
        """查找元素并等待"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_clickable_element(self, by, value, timeout=15):
        """查找可点击元素"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def click_element(self, by, value, timeout=15):
        """点击元素"""
        element = self.find_clickable_element(by, value, timeout)
        element.click()

    def input_text(self, by, value, text, timeout=15):
        """输入文本"""
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, by, value, timeout=15):
        """获取元素文本"""
        element = self.find_element(by, value, timeout)
        return element.text

    def is_element_present(self, by, value, timeout=5):
        """检查元素是否存在"""
        try:
            self.find_element(by, value, timeout)
            return True
        except:
            return False

    def wait_for_url_contains(self, text, timeout=15):
        """等待URL包含特定文本"""
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    def take_screenshot(self, name):
        """截图"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename