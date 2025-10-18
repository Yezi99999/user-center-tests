from .base_api import BaseAPI
from utils.helpers import validate_response


class UserAPI(BaseAPI):
    """用户管理相关API - 根据用户管理中心API调整"""

    def get_profile(self):
        """获取用户资料"""
        response = self.get("/api/profile/")
        return validate_response(response, 200)

    def update_profile(self, email=None, phone=None, first_name=None, last_name=None, **kwargs):
        """更新用户资料 - 根据项目文档调整参数"""
        update_data = {}
        if email is not None:
            update_data["email"] = email
        if phone is not None:
            update_data["phone"] = phone
        if first_name is not None:
            update_data["first_name"] = first_name
        if last_name is not None:
            update_data["last_name"] = last_name
        update_data.update(kwargs)

        response = self.put("/api/profile/", json=update_data)
        return validate_response(response, 200)