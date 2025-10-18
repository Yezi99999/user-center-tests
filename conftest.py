from dotenv import load_dotenv
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 设置环境变量
os.environ['WDM_SSL_VERIFY'] = '0'  # 虽然不用webdriver_manager，但留着以防其他依赖需要
os.environ['WDM_LOG_VERIFY'] = '0'


@pytest.fixture
def driver():
    """浏览器驱动fixture - 使用手动配置的Chrome Driver"""
    driver = None
    try:
        # 方法1: 首先尝试在项目根目录查找chromedriver.exe
        project_root = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(project_root, 'chromedriver.exe')

        if os.path.exists(chromedriver_path):
            print(f"✓ 使用项目中的Chrome Driver: {chromedriver_path}")
            service = Service(chromedriver_path)
        else:
            # 方法2: 如果在项目根目录没找到，尝试使用系统PATH中的chromedriver
            print("ℹ 使用系统PATH中的Chrome Driver")
            service = Service()

        # Chrome 选项配置
        options = webdriver.ChromeOptions()

        # 可选：注释掉headless模式以便观察测试过程
        # options.add_argument('--headless')

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        # 创建驱动实例
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(10)

        # 执行脚本来隐藏webdriver属性
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        yield driver

    except Exception as e:
        pytest.skip(f"浏览器驱动初始化失败: {e}")
    finally:
        if driver:
            driver.quit()


@pytest.fixture
def api_client():
    """API客户端fixture"""
    from api.auth_api import AuthAPI
    return AuthAPI()


@pytest.fixture
def test_user():
    """测试用户fixture"""
    from utils.helpers import generate_random_username, generate_random_email
    return {
        "username": generate_random_username(),
        "email": generate_random_email(),
        "password": "TestPass123!"
    }
@pytest.fixture(scope="session")
def backend_base_url():
    """返回后端基础URL"""
    return os.getenv("BACKEND_BASE_URL", "http://127.0.0.1:8000")

@pytest.fixture(scope="session")
def frontend_base_url():
    """返回前端基础URL"""
    return os.getenv("FRONTEND_BASE_URL", "http://localhost:8080")

@pytest.fixture(autouse=True)
def setup_teardown():
    """每个测试用例前后的设置"""
    # 测试前的设置
    print("Starting test...")
    yield
    # 测试后的清理
    print("Test finished!")

# 添加命令行选项
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="测试环境: local, dev, staging")