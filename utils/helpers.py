import random
import string
from faker import Faker

fake = Faker()

def generate_random_username(prefix="testuser"):
    """生成随机用户名"""
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"{prefix}_{random_suffix}"

def generate_random_email():
    """生成随机邮箱"""
    return generate_random_username() + "@example.com"

def generate_random_password(length=10):
    """生成随机密码"""
    characters = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choices(characters, k=length))

def validate_response(response, expected_status=200):
    """验证响应状态码"""
    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, but got {response.status_code}. Response: {response.text}"
    return response