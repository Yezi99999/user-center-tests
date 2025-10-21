# 用户管理中心 (SUT) 自动化测试项目

基于用户管理中心项目的完整自动化测试框架，包含API测试和UI测试。

## 项目结构
user-center-tests/

├── api/ # API封装类

├── tests/ # 测试用例

├── pages/ # 页面对象模型

├── utils/ # 工具类

├── data/ # 测试数据

└── reports/ # 测试报告

text

## 功能覆盖

### API测试
- ✅ 用户注册功能测试
- ✅ 用户登录功能测试  
- ✅ 用户资料管理测试
- ✅ 权限控制测试
- ✅ 异常场景测试

### UI测试
- ✅ 用户注册流程测试
- ✅ 用户登录流程测试
- ✅ 个人资料管理测试
- ✅ 退出登录功能测试
- ✅ 权限控制测试

## 快速开始

### 1. 环境准备
```bash
# 克隆项目
git clone https://github.com/Yezi99999/user-center-tests
cd user-center-tests

# 安装依赖
pip install -r requirements.txt
```
2. 环境配置
复制环境变量文件并配置：

```bash
cp .env.example .env
# 编辑.env文件，配置你的后端和前端URL
```
3. 运行测试
```bash
# 运行所有测试
pytest

# 运行API测试
pytest -m api

# 运行UI测试  
pytest -m ui

# 运行冒烟测试
pytest -m smoke

# 生成Allure报告
pytest --alluredir=./allure-results
allure serve allure-results
```
4. 测试报告
测试完成后会生成：

HTML报告: reports/report.html

Allure报告: allure-results/

测试用例对应关系
```
测试类	对应功能用例	覆盖场景
test_auth.py	TC-01, TC-02, TC-04, TC-07, TC-08	用户认证相关
test_user_profile.py	TC-03	用户资料管理
test_frontend_flows.py	TC-01 to TC-05	前端完整流程
```
