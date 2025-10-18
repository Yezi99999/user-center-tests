from .base_api import BaseAPI
from utils.helpers import validate_response


class AuthAPI(BaseAPI):
    """认证相关API - 根据用户管理中心API调整"""

    def register(self, username, email, password, password_confirm, phone=None, **kwargs):
        """用户注册 - 根据项目文档调整参数"""
        data = {
            "username": username,
            "email": email,
            "password": password,
            "password_confirm": password_confirm,
            **kwargs
        }
        if phone:
            data["phone"] = phone

        response = self.post("/api/register/", json=data)
        return validate_response(response, 201)  # 注册成功返回201

    def login(self, username, password):
        """用户登录"""
        data = {
            "username": username,
            "password": password
        }
        response = self.post("/api/login/", json=data)
        response = validate_response(response, 200)

        # 保存token - 根据实际API响应结构调整
        if response.status_code == 200:
            token_data = response.json()
            # 假设token在响应体的'token'字段中，根据实际调整
            if 'token' in token_data:
                self.set_token(token_data['token'])
            elif 'access' in token_data:  # 如果是JWT格式
                self.set_token(token_data['access'])
        return response

    def logout(self):
        """用户登出"""
        response = self.post("/api/logout/")
        self.set_token(None)  # 清除token
        return validate_response(response, 200)