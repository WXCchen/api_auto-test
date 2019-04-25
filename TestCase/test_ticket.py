
from Common import Request, Assert,read_excel,login
import allure
import pytest

request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url='http://192.168.1.137:8080/'
head={}
item_id=0

@allure.feature('优惠券模块')
class Test_ticket:
    @allure.story('查询优惠券列表')
    def test_get_ticket_list(self):
        global head
        head = login.Login().get_token()
        param = {'PageNum': '1', 'pageSize': '10'}
        get_ticket_list_resp = request.get_request(url=url + 'coupon/list', params=param, headers=head)
        resp_json = get_ticket_list_resp.json()
        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global item_id
        item_id = item['id']
        assertion.assert_code(get_ticket_list_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story('删除优惠券')
    def test_del_ticket(self):
        del_resp = request.post_request(url=url + 'coupon/delete/' + str(item_id), headers=head)
        resp_json = del_resp.json()
        assertion.assert_code(del_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')


    @allure.story('添加优惠券')
    @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg',excel_list,ids=idsList)
    def test_add_ticket_list(self,name,amount,minPoint,publishCount,msg):
        json={"type":0,"name":name,"platform":0,amount:10,"perLimit":1,"minPoint":minPoint,
              "startTime":'',"endTime":'',"useType":0,"note":'',"publishCount":publishCount,
              "productRelationList":[],"productCategoryRelationList":[]}
        add_resp = request.post_request(url=url + 'coupon/create', json=json, headers=head)
        resp_json = add_resp.json()
        assertion.assert_code(add_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], msg)









