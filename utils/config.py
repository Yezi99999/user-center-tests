import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """配置管理类 - 根据用户管理中心项目调整"""

    # 后端配置
    BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "http://127.0.0.1:8000")

    # 前端配置
    FRONTEND_BASE_URL = os.getenv("FRONTEND_BASE_URL", "http://localhost:8080")

    # API端点 - 根据你的项目文档调整
    REGISTER_URL = f"{BACKEND_BASE_URL}/api/register/"
    LOGIN_URL = f"{BACKEND_BASE_URL}/api/login/"
    PROFILE_URL = f"{BACKEND_BASE_URL}/api/profile/"
    LOGOUT_URL = f"{BACKEND_BASE_URL}/api/logout/"

    # 前端页面路径
    LOGIN_PAGE_URL = f"{FRONTEND_BASE_URL}/login"
    REGISTER_PAGE_URL = f"{FRONTEND_BASE_URL}/register"
    PROFILE_PAGE_URL = f"{FRONTEND_BASE_URL}/profile"

    # 测试数据
    TEST_USERNAME = os.getenv("TEST_USERNAME", "testuser")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD", "testpass123")
    TEST_EMAIL = os.getenv("TEST_EMAIL", "test@example.com")

    # 超时设置
    WAIT_TIMEOUT = 10
    API_TIMEOUT = 30