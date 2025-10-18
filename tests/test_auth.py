import pytest
import time
from api.auth_api import AuthAPI
from data.test_data import TestData
from utils.helpers import generate_random_username, generate_random_email


class TestAuthentication:
    """认证功能API测试"""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.auth_api = AuthAPI()
        yield
        # 测试后清理
        if self.auth_api.token:
            self.auth_api.logout()

    @pytest.mark.smoke
    @pytest.mark.api
    def test_user_registration_success(self):
        """测试用户注册成功 - TC-01"""
        user_data = TestData.get_valid_user_data()

        response = self.auth_api.register(**user_data)

        assert response.status_code == 201
        response_data = response.json()
        assert "username" in response_data
        assert response_data["username"] == user_data["username"]
        assert response_data["email"] == user_data["email"]
        # 确保密码没有返回
        assert "password" not in response_data

    @pytest.mark.api
    def test_user_login_success(self):
        """测试用户登录成功 - TC-02"""
        # 先注册用户
        user_data = TestData.get_valid_user_data()
        self.auth_api.register(**user_data)

        # 测试登录
        response = self.auth_api.login(user_data["username"], user_data["password"])

        assert response.status_code == 200
        response_data = response.json()
        # 根据实际API响应结构调整断言
        assert "token" in response_data or "access" in response_data

    @pytest.mark.parametrize("username,password,expected_status,description", [
        ("nonexistent_user", "password", 401, "用户不存在"),
        ("test_user", "wrong_password", 401, "密码错误"),
    ])
    def test_user_login_failure(self, username, password, expected_status, description):
        """测试用户登录失败场景 - TC-08"""
        response = self.auth_api.login(username, password)
        assert response.status_code == expected_status, f"Failed case: {description}"

    @pytest.mark.api
    def test_user_logout_success(self):
        """测试用户退出登录 - TC-04"""
        # 先注册并登录用户
        user_data = TestData.get_valid_user_data()
        self.auth_api.register(**user_data)
        self.auth_api.login(user_data["username"], user_data["password"])

        # 测试退出
        response = self.auth_api.logout()
        assert response.status_code == 200

        # 验证token已清除
        assert self.auth_api.token is None

    @pytest.mark.api
    def test_registration_duplicate_username(self):
        """测试重复用户名注册 - TC-07"""
        user_data = TestData.get_valid_user_data()

        # 第一次注册
        self.auth_api.register(**user_data)

        # 第二次注册相同用户名
        duplicate_data = user_data.copy()
        duplicate_data["email"] = generate_random_email()  # 不同邮箱

        response = self.auth_api.register(**duplicate_data)
        assert response.status_code == 400
        # 根据实际API返回验证错误信息