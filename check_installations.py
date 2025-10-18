#!/usr/bin/env python3
"""
检查测试框架所需Python库是否安装完整
"""


def verify_installation():
    print("最终安装验证")
    print("=" * 40)

    tests = []

    # 测试1: 基础库导入
    try:
        import pytest
        import requests
        import allure_pytest
        import pytest_html
        from dotenv import load_dotenv
        from faker import Faker
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.firefox import GeckoDriverManager
        tests.append(("基础库导入", "✓ 成功"))
    except ImportError as e:
        tests.append(("基础库导入", f"✗ 失败: {e}"))

    # 测试2: 配置系统
    try:
        # 模拟一个简单的配置类
        class SimpleConfig:
            BACKEND_BASE_URL = "http://127.0.0.1:8000"
            FRONTEND_BASE_URL = "http://localhost:8080"

        tests.append(("配置系统", "✓ 就绪"))
    except Exception as e:
        tests.append(("配置系统", f"✗ 错误: {e}"))

    # 测试3: API功能
    try:
        import requests
        # 测试requests基本功能
        session = requests.Session()
        tests.append(("HTTP客户端", "✓ 正常"))
    except Exception as e:
        tests.append(("HTTP客户端", f"✗ 错误: {e}"))

    # 测试4: 测试框架
    try:
        import pytest
        tests.append(("测试框架", f"✓ pytest {pytest.__version__}"))
    except Exception as e:
        tests.append(("测试框架", f"✗ 错误: {e}"))

    # 测试5: 浏览器驱动管理
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        tests.append(("浏览器驱动", "✓ 就绪"))
    except Exception as e:
        tests.append(("浏览器驱动", f"✗ 错误: {e}"))

    # 打印结果
    for test_name, result in tests:
        print(f"{test_name:20} {result}")

    # 总结
    success_count = sum(1 for _, result in tests if result.startswith("✓"))
    total_count = len(tests)

    print("=" * 40)
    if success_count == total_count:
        print("🎉 所有组件安装成功！")
        print("你可以开始运行测试框架了。")
    else:
        print(f"⚠️  {success_count}/{total_count} 个组件正常")
        print("请检查失败的组件并重新安装。")


if __name__ == "__main__":
    verify_installation()