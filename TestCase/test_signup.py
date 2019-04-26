from Common import Request, Assert,Tools
import allure
import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
# excel_list = read_excel.read_excel_list('./document/订单.xlsx')
# length = len(excel_list)
# for i in range(length):
#     idsList.append(excel_list[i].pop())
phone_num = Tools.phone_num()
pwd = Tools.random_123(3)+Tools.random_str_abc(3)
rePwd=pwd
userName = Tools.random_str_abc(3)+Tools.random_123(2)

url="http://192.168.1.137:1811/"
head={}
item_id=0
@allure.feature('用户注册模块')
class Test_signup:
    @allure.story('用户注册')
    def test_signup(self):
        get_signup_resp = request.post_request(url=url + '/user/signup',
                                               json={"phone": phone_num,"pwd":pwd ,"rePwd":rePwd ,"userName": userName})
        resp_json = get_signup_resp.json()
        assertion.assert_code(get_signup_resp.status_code,200)
        assertion.assert_in_text(resp_json['respBase'], '成功')

@allure.feature('用户登录模块')
class Test_login:
    @allure.story('登录')
    def test_login(self):
        get_login_resp = request.post_request(url=url + '/user/login',json={"pwd": pwd,"userName": userName})
        resp_json = get_login_resp.json()
        assertion.assert_code(get_login_resp.status_code, 200)
        assertion.assert_in_text(resp_json['respDesc'], '成功')











       


