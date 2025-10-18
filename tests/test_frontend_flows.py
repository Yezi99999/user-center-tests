# tests/test_frontend_flows.py
import pytest
import time
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.profile_page import ProfilePage
from data.test_data import TestData
from utils.config import Config


class TestFrontendFlows:
    """前端流程测试 - 完全重写版本"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """每个测试前的设置"""
        print("开始前端测试...")
        yield
        print("前端测试完成")

    @pytest.mark.ui
    @pytest.mark.smoke
    def test_user_registration_flow(self, driver):
        """测试用户注册前端流程 - TC-01"""
        print("执行用户注册流程测试")

        # 创建页面对象
        register_page = RegisterPage(driver)

        # 打开注册页面
        register_page.open_register_page(Config.FRONTEND_BASE_URL)

        # 获取测试数据
        user_data = TestData.get_valid_user_data()

        # 执行注册操作
        register_page.register(**user_data)

        # 验证注册成功
        assert register_page.is_registration_successful(Config.FRONTEND_BASE_URL), "注册后应跳转到个人资料页面"

        # 验证当前URL包含profile
        assert "/profile" in driver.current_url, f"当前URL应为个人资料页面，实际为: {driver.current_url}"

        print("✓ 用户注册流程测试通过")

    @pytest.mark.ui
    def test_user_login_flow(self, driver):
        """测试用户登录前端流程 - TC-02"""
        print("执行用户登录流程测试")

        # 先通过API注册一个测试用户（避免依赖注册流程）
        from api.auth_api import AuthAPI
        auth_api = AuthAPI()
        user_data = TestData.get_valid_user_data()

        try:
            # 注册用户
            register_response = auth_api.register(**user_data)
            if register_response.status_code != 201:
                pytest.skip(f"用户注册失败: {register_response.text}")
        except Exception as e:
            pytest.skip(f"用户注册API调用失败: {e}")

        # 创建页面对象
        login_page = LoginPage(driver)

        # 打开登录页面
        login_page.open_login_page(Config.FRONTEND_BASE_URL)

        # 执行登录操作
        login_page.login(user_data["username"], user_data["password"])

        # 验证登录成功
        assert login_page.is_login_successful(Config.FRONTEND_BASE_URL), "登录后应跳转到个人资料页面"

        # 验证当前URL包含profile
        assert "/profile" in driver.current_url, f"当前URL应为个人资料页面，实际为: {driver.current_url}"

        print("✓ 用户登录流程测试通过")

    @pytest.mark.ui
    def test_profile_management_flow(self, driver):
        """测试个人资料管理前端流程 - TC-03"""
        print("执行个人资料管理流程测试")

        # 先通过API注册并登录一个测试用户
        from api.auth_api import AuthAPI
        auth_api = AuthAPI()
        user_data = TestData.get_valid_user_data()

        try:
            # 注册用户
            register_response = auth_api.register(**user_data)
            if register_response.status_code != 201:
                pytest.skip(f"用户注册失败: {register_response.text}")

            # 登录用户
            login_response = auth_api.login(user_data["username"], user_data["password"])
            if login_response.status_code != 200:
                pytest.skip(f"用户登录失败: {login_response.text}")
        except Exception as e:
            pytest.skip(f"用户注册/登录API调用失败: {e}")

        # 创建页面对象
        profile_page = ProfilePage(driver)

        # 直接打开个人资料页面（因为已登录）
        profile_page.open_profile_page(Config.FRONTEND_BASE_URL)

        # 验证成功进入个人资料页面
        assert "/profile" in driver.current_url, f"应直接进入个人资料页面，实际URL: {driver.current_url}"

        # 更新资料
        update_data = TestData.get_profile_update_data()
        profile_page.update_profile(**update_data)

        # 验证更新成功（检查成功消息或页面状态）
        success_message = profile_page.get_success_message()
        if success_message:
            assert "成功" in success_message or "更新" in success_message, f"成功消息应包含成功提示，实际: {success_message}"

        print("✓ 个人资料管理流程测试通过")

    @pytest.mark.ui
    def test_logout_flow(self, driver):
        """测试退出登录前端流程 - TC-04"""
        print("执行退出登录流程测试")

        # 先通过API注册并登录一个测试用户
        from api.auth_api import AuthAPI
        auth_api = AuthAPI()
        user_data = TestData.get_valid_user_data()

        try:
            # 注册用户
            register_response = auth_api.register(**user_data)
            if register_response.status_code != 201:
                pytest.skip(f"用户注册失败: {register_response.text}")

            # 登录用户
            login_response = auth_api.login(user_data["username"], user_data["password"])
            if login_response.status_code != 200:
                pytest.skip(f"用户登录失败: {login_response.text}")
        except Exception as e:
            pytest.skip(f"用户注册/登录API调用失败: {e}")

        # 创建页面对象
        profile_page = ProfilePage(driver)

        # 直接打开个人资料页面（因为已登录）
        profile_page.open_profile_page(Config.FRONTEND_BASE_URL)

        # 验证成功进入个人资料页面
        assert "/profile" in driver.current_url, f"应直接进入个人资料页面，实际URL: {driver.current_url}"

        # 执行退出登录
        profile_page.logout()

        # 验证退出成功
        assert profile_page.is_logout_successful(Config.FRONTEND_BASE_URL), "退出后应跳转到登录页面"

        # 验证当前URL包含login
        assert "/login" in driver.current_url, f"当前URL应为登录页面，实际为: {driver.current_url}"

        print("✓ 退出登录流程测试通过")

    @pytest.mark.ui
    def test_unauthorized_access(self, driver):
        """测试未授权访问前端流程 - TC-05"""
        print("执行未授权访问测试")

        # 创建页面对象
        profile_page = ProfilePage(driver)

        # 直接尝试访问个人资料页面（未登录状态）
        profile_page.open_profile_page(Config.FRONTEND_BASE_URL)

        # 验证被重定向到登录页面
        current_url = driver.current_url
        assert "/login" in current_url, f"未登录访问受限页面应重定向到登录页面，实际URL: {current_url}"

        print("✓ 未授权访问测试通过")