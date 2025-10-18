# test_framework_validation.py
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os


def validate_framework():
    print("测试框架全面验证")
    print("=" * 50)

    tests_passed = 0
    total_tests = 0

    # 测试1: 基础库导入
    total_tests += 1
    try:
        import pytest
        import requests
        import allure_pytest
        import pytest_html
        from dotenv import load_dotenv
        from faker import Faker
        from selenium import webdriver
        print("✓ 基础库导入成功")
        tests_passed += 1
    except ImportError as e:
        print(f"✗ 基础库导入失败: {e}")

    # 测试2: API 类导入
    total_tests += 1
    try:
        from api.base_api import BaseAPI
        from api.auth_api import AuthAPI
        from api.user_api import UserAPI
        print("✓ API 类导入成功")
        tests_passed += 1
    except Exception as e:
        print(f"✗ API 类导入失败: {e}")

    # 测试3: 页面对象导入
    total_tests += 1
    try:
        from pages.base_page import BasePage
        from pages.login_page import LoginPage
        from pages.register_page import RegisterPage
        from pages.profile_page import ProfilePage
        print("✓ 页面对象导入成功")
        tests_passed += 1
    except Exception as e:
        print(f"✗ 页面对象导入失败: {e}")

    # 测试4: Chrome Driver 功能
    total_tests += 1
    try:
        project_root = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(project_root, 'chromedriver.exe')

        if os.path.exists(chromedriver_path):
            service = Service(chromedriver_path)
        else:
            service = Service()

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无头模式，避免弹出浏览器窗口
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://httpbin.org/html")
        title = driver.title
        driver.quit()

        print("✓ Chrome Driver 功能正常")
        tests_passed += 1
    except Exception as e:
        print(f"✗ Chrome Driver 功能测试失败: {e}")

    # 测试5: 配置文件
    total_tests += 1
    try:
        from utils.config import Config
        print(f"✓ 配置加载成功 - 后端URL: {Config.BACKEND_BASE_URL}")
        tests_passed += 1
    except Exception as e:
        print(f"✗ 配置加载失败: {e}")

    print("=" * 50)
    print(f"测试结果: {tests_passed}/{total_tests} 通过")

    if tests_passed == total_tests:
        print("🎉 测试框架完全就绪！")
        return True
    else:
        print("⚠️  部分组件需要检查")
        return False


if __name__ == "__main__":
    validate_framework()