import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def debug_ui_environment():
    """调试UI测试环境"""
    print("UI测试环境调试")
    print("=" * 50)

    # 检查Chrome Driver
    project_root = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(project_root, 'chromedriver.exe')

    if os.path.exists(chromedriver_path):
        print(f"✓ Chrome Driver路径: {chromedriver_path}")
        print(f"✓ 文件大小: {os.path.getsize(chromedriver_path) / (1024 * 1024):.2f} MB")
    else:
        print("✗ 未找到chromedriver.exe")
        return False

    # 测试Chrome Driver连接
    try:
        service = Service(chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无头模式测试
        options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.baidu.com")
        title = driver.title
        driver.quit()

        print(f"✓ Chrome Driver工作正常，测试页面标题: {title}")
        return True

    except Exception as e:
        print(f"✗ Chrome Driver测试失败: {e}")
        return False


def test_frontend_connectivity():
    """测试前端服务连通性"""
    print("\n前端服务连通性测试")
    print("=" * 50)

    from utils.config import Config
    import requests

    try:
        response = requests.get(Config.FRONTEND_BASE_URL, timeout=10)
        if response.status_code == 200:
            print(f"✓ 前端服务可访问: {Config.FRONTEND_BASE_URL}")
            return True
        else:
            print(f"✗ 前端服务返回状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ 前端服务无法访问: {e}")
        return False


if __name__ == "__main__":
    chrome_ok = debug_ui_environment()
    frontend_ok = test_frontend_connectivity()

    print("\n" + "=" * 50)
    if chrome_ok and frontend_ok:
        print("🎉 UI测试环境就绪！")
        print("可以运行: pytest tests/test_frontend_flows.py -v")
    else:
        print("❌ UI测试环境存在问题，请检查上述错误")

        if not chrome_ok:
            print("\nChrome Driver问题解决方案:")
            print("1. 确保chromedriver.exe在项目根目录")
            print("2. 检查Chrome浏览器版本与Chrome Driver版本匹配")
            print("3. 从 https://chromedriver.chromium.org/ 下载正确版本")

        if not frontend_ok:
            print("\n前端服务问题解决方案:")
            print("1. 确保前端服务正在运行: npm run serve")
            print("2. 检查 .env 文件中的 FRONTEND_BASE_URL 配置")
            print("3. 确认端口没有被占用")