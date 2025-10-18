#!/usr/bin/env python3
"""
验证Chrome Driver配置
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def test_chrome_driver():
    """测试Chrome Driver是否正常工作"""
    print("测试Chrome Driver配置...")

    try:
        # 查找chromedriver.exe
        project_root = os.path.dirname(os.path.abspath(__file__))
        chromedriver_path = os.path.join(project_root, 'chromedriver.exe')

        if os.path.exists(chromedriver_path):
            print(f"✓ 找到Chrome Driver: {chromedriver_path}")
            service = Service(chromedriver_path)
        else:
            print("ℹ 使用系统PATH中的Chrome Driver")
            service = Service()  # 依赖系统PATH

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=service, options=options)

        # 测试基本功能
        driver.get("https://www.baidu.com")
        title = driver.title
        driver.quit()

        print("✓ Chrome Driver 工作正常")
        print(f"✓ 页面标题: {title}")
        return True

    except Exception as e:
        print(f"✗ Chrome Driver 配置失败: {e}")
        return False


if __name__ == "__main__":
    success = test_chrome_driver()
    if success:
        print("\n🎉 Chrome Driver 配置成功！")
    else:
        print("\n❌ Chrome Driver 配置失败，请手动下载。")
        print("\n手动下载步骤:")
        print("1. 查看Chrome版本: 在浏览器地址栏输入 chrome://version/")
        print("2. 访问: https://npm.taobao.org/mirrors/chromedriver/")
        print("3. 下载对应版本的 chromedriver_win32.zip")
        print("4. 解压后将 chromedriver.exe 放在项目根目录")