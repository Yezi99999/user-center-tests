import requests
from utils.config import Config
from utils.helpers import validate_response


class BaseAPI:
    """API基类 - 适配用户管理中心的Token认证"""

    def __init__(self):
        self.base_url = Config.BACKEND_BASE_URL
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        """设置认证token - 根据项目使用Token认证"""
        self.token = token
        if token:
            self.session.headers.update({"Authorization": f"Token {token}"})
        else:
            self.session.headers.pop("Authorization", None)

    def _request(self, method, endpoint, **kwargs):
        """发送请求的通用方法"""
        url = f"{self.base_url}{endpoint}"

        # 确保Content-Type为application/json
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        if 'json' in kwargs and 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'

        response = self.session.request(method, url, **kwargs)
        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)