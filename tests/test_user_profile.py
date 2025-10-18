import pytest
from api.auth_api import AuthAPI
from api.user_api import UserAPI
from data.test_data import TestData


class TestUserProfile:
    """用户资料管理API测试"""

    @pytest.fixture
    def authenticated_user(self):
        """创建一个已认证的用户"""
        auth_api = AuthAPI()
        user_api = UserAPI()

        # 注册并登录用户
        user_data = TestData.get_valid_user_data()
        auth_api.register(**user_data)
        login_response = auth_api.login(user_data["username"], user_data["password"])

        # 设置token到user_api
        token_data = login_response.json()
        if 'token' in token_data:
            user_api.set_token(token_data['token'])
        elif 'access' in token_data:
            user_api.set_token(token_data['access'])

        return user_api

    @pytest.mark.smoke
    @pytest.mark.api
    def test_get_user_profile(self, authenticated_user):
        """测试获取用户资料 - TC-03"""
        response = authenticated_user.get_profile()

        assert response.status_code == 200
        profile_data = response.json()
        assert "username" in profile_data
        assert "email" in profile_data

    @pytest.mark.api
    def test_update_user_profile(self, authenticated_user):
        """测试更新用户资料 - TC-03"""
        update_data = TestData.get_profile_update_data()

        response = authenticated_user.update_profile(**update_data)

        assert response.status_code == 200
        updated_data = response.json()

        # 验证更新字段
        for key, value in update_data.items():
            assert updated_data[key] == value

    @pytest.mark.api
    def test_access_profile_without_auth(self):
        """测试未认证访问用户资料 - 权限控制"""
        user_api = UserAPI()  # 未设置token

        response = user_api.get_profile()
        assert response.status_code == 401  # 未授权