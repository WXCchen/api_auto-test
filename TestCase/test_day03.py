import os
import time
import pytest


from selenium import webdriver

from Common import baseui
from Common.read_excel import *




class TestMall():
    @pytest.mark.s
    def test_login(self,driver):
        #确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../vinson/chromedriver.exe")
        # #打开浏览器
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.set_page_load_timeout(10)  # 网页加载超时为10s
        # driver.set_script_timeout(10)  # js脚本运行超时10s
        # driver.implicitly_wait(10)  # 元素查找超时时间10s
        base = baseui.baseUI(driver)
        #打开网址
        driver.get('http://192.168.1.137/#/login')
        base.click("点击登录按钮","//span[contains(text(),'登录')]")
        #定位并处理异常弹框

        #定位用户名输入框

        #输入用户名
        #定位密码输入框
        #输入密码
        #定位登录按钮，并点击登录按钮
        # driver.find_element_by_xpath('//span[contains(text(),"登录")]').click()
        #定位并处理异常弹框
        # try:
        #     driver.find_element_by_xpath("//span[contains(text(),'残忍拒绝')]").click()
        # except:
        #     pass
        try:
            base.click("点击残忍拒绝","//span[contains(text(),'残忍拒绝')]")
        except:
            pass
        time.sleep(2)
        #点击登录按钮
        # driver.find_element_by_xpath('//span[contains(text(),"登录")]').click()
        base.click("点击登录按钮", "//span[contains(text(),'登录')]")
        time.sleep(2)
        #断言页面是否跳转到首页
        print(driver.page_source)
        assert"首页"in driver.page_source
        pass

        def test_order_1(self, driver):

            print("查询订单")

            pass

        l_name = read_excel_list("C:\\name.xlsx")

        @pytest.fixture(params=l_name)
        def name(self, request):
            return request.param

        def test_order_2(self, name):
            print(name[0])

