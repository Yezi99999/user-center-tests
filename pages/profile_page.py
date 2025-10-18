from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    """个人资料页面 - 根据你的前端实际元素调整定位器"""

    def __init__(self, driver):
        super().__init__(driver)
        # 根据你的前端实际元素调整这些定位器
        self.email_input = (By.ID, "email")
        self.phone_input = (By.ID, "phone")
        self.first_name_input = (By.ID, "first_name")
        self.last_name_input = (By.ID, "last_name")
        self.update_button = (By.XPATH, "//button[contains(text(), '更新') or contains(text(), 'Update')]")
        self.logout_button = (By.XPATH, "//button[contains(text(), '退出') or contains(text(), 'Logout')]")
        self.success_message = (By.CLASS_NAME, "success")  # 根据实际调整

    def open_profile_page(self, base_url):
        """打开个人资料页面"""
        self.driver.get(f"{base_url}/profile")

    def update_profile(self, email=None, phone=None, first_name=None, last_name=None):
        """更新个人资料"""
        if email:
            self.input_text(*self.email_input, email)
        if phone:
            self.input_text(*self.phone_input, phone)
        if first_name:
            self.input_text(*self.first_name_input, first_name)
        if last_name:
            self.input_text(*self.last_name_input, last_name)

        self.click_element(*self.update_button)

    def logout(self):
        """退出登录"""
        self.click_element(*self.logout_button)

    def get_success_message(self):
        """获取成功消息"""
        try:
            return self.get_element_text(*self.success_message)
        except:
            return None

    def is_logout_successful(self, base_url):
        """检查是否退出成功"""
        try:
            # 假设退出后跳转到登录页面
            self.wait_for_url_contains("/login", timeout=10)
            return True
        except:
            return False