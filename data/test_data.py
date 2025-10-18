from utils.helpers import generate_random_username, generate_random_email, generate_random_password


class TestData:
    """测试数据管理 - 根据用户管理中心项目调整"""

    # 有效测试数据
    @staticmethod
    def get_valid_user_data():
        return {
            "username": generate_random_username(),
            "email": generate_random_email(),
            "password": "TestPass123!",
            "password_confirm": "TestPass123!",
            "phone": "13800138000"
        }

    # 无效测试数据
    INVALID_REGISTRATION_DATA = [
        # 密码不匹配
        {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123",
            "password_confirm": "differentpassword",
            "description": "密码不匹配"
        },
        # 用户名过短
        {
            "username": "ab",
            "email": "test@example.com",
            "password": "password123",
            "password_confirm": "password123",
            "description": "用户名过短"
        },
        # 无效邮箱
        {
            "username": "testuser",
            "email": "invalid-email",
            "password": "password123",
            "password_confirm": "password123",
            "description": "无效邮箱格式"
        }
    ]

    # 登录测试数据
    LOGIN_CASES = [
        # (username, password, expected_status, description)
        ("valid_user", "valid_password", 200, "有效凭证"),
        ("invalid_user", "password", 401, "无效用户名"),
        ("valid_user", "wrong_password", 401, "错误密码"),
    ]

    # 资料更新测试数据
    @staticmethod
    def get_profile_update_data():
        return {
            "email": "updated@example.com",
            "phone": "13900139000",
            "first_name": "张",
            "last_name": "三"
        }