import pytest
from api.auth_api import AuthAPI
from api.user_api import UserAPI
from utils.helpers import generate_random_username, generate_random_email


class TestUserManagement:
    """用户管理功能测试"""

    @pytest.fixture
    def authenticated_user(self):
        """创建一个已认证的用户"""
        auth_api = AuthAPI()
        user_api = UserAPI()

        # 注册并登录用户
        user_data = {
            "username": generate_random_username(),
            "email": generate_random_email(),
            "password": "TestPass123!"
        }
        auth_api.register(**user_data)
        login_response = auth_api.login(user_data["username"], user_data["password"])
        token = login_response.json()["access"]

        # 设置token
        user_api.set_token(token)
        return user_api

    @pytest.mark.smoke
    @pytest.mark.api
    def test_get_user_profile(self, authenticated_user):
        """测试获取用户资料"""
        response = authenticated_user.get_profile()

        assert response.status_code == 200
        profile_data = response.json()
        assert "username" in profile_data
        assert "email" in profile_data

    @pytest.mark.api
    def test_update_user_profile(self, authenticated_user):
        """测试更新用户资料"""
        update_data = {
            "first_name": "Test",
            "last_name": "User"
        }

        response = authenticated_user.update_profile(**update_data)

        assert response.status_code == 200
        updated_data = response.json()
        assert updated_data["first_name"] == update_data["first_name"]
        assert updated_data["last_name"] == update_data["last_name"]