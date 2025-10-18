from .base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    """注册页面 - 根据你的前端实际元素调整定位器"""

    def __init__(self, driver):
        super().__init__(driver)
        # 根据你的前端实际元素调整这些定位器
        self.username_input = (By.ID, "username")
        self.email_input = (By.ID, "email")
        self.phone_input = (By.ID, "phone")  # 可选
        self.password_input = (By.ID, "password")
        self.password_confirm_input = (By.ID, "password_confirm")
        self.register_button = (By.XPATH, "//button[contains(text(), '注册') or contains(text(), 'Register')]")

    def open_register_page(self, base_url):
        """打开注册页面"""
        self.driver.get(f"{base_url}/register")

    def register(self, username, email, password, password_confirm, phone=None):
        """执行注册操作"""
        self.input_text(*self.username_input, username)
        self.input_text(*self.email_input, email)
        if phone:
            self.input_text(*self.phone_input, phone)
        self.input_text(*self.password_input, password)
        self.input_text(*self.password_confirm_input, password_confirm)
        self.click_element(*self.register_button)

    def is_registration_successful(self, base_url):
        """检查是否注册成功"""
        try:
            # 假设注册成功后跳转到个人资料页面
            self.wait_for_url_contains("/profile", timeout=10)
            return True
        except:
            return False