from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """登录页面 - 根据你的前端实际元素调整定位器"""

    def __init__(self, driver):
        super().__init__(driver)
        # 根据你的前端实际元素调整这些定位器
        self.username_input = (By.ID, "username")  # 或者 (By.NAME, "username")
        self.password_input = (By.ID, "password")  # 或者 (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[contains(text(), '登录') or contains(text(), 'Login')]")
        self.error_message = (By.CLASS_NAME, "error")  # 根据实际调整

    def open_login_page(self, base_url):
        """打开登录页面"""
        self.driver.get(f"{base_url}/login")

    def login(self, username, password):
        """执行登录操作"""
        self.input_text(*self.username_input, username)
        self.input_text(*self.password_input, password)
        self.click_element(*self.login_button)

    def get_error_message(self):
        """获取错误消息"""
        try:
            return self.get_element_text(*self.error_message)
        except:
            return None

    def is_login_successful(self, base_url):
        """检查是否登录成功"""
        try:
            # 假设登录成功后跳转到个人资料页面
            self.wait_for_url_contains("/profile", timeout=10)
            return True
        except:
            return False