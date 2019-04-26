
from Common import Request, Assert,read_excel,login
import allure
import pytest

request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('./document/订单.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url='http://192.168.1.137:8080/'
head={}
item_id=0

@allure.feature('订单模块')
class Test_order:
    @allure.story('查询退货原因订单列表')
    def test_get_order_list(self):
        global head
        head = login.Login().get_token()
        param = {'PageNum': '1', 'pageSize': '5'}
        get_order_list_resp = request.get_request(url=url + 'returnReason/list', params=param, headers=head)
        resp_json = get_order_list_resp.json()
        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global item_id
        item_id = item['id']
        assertion.assert_code(get_order_list_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story('删除退货原因订单')
    def test_del_order(self):
        del_resp = request.post_request(url=url + 'returnReason/delete?ids=' + str(item_id), headers=head)
        resp_json = del_resp.json()
        assertion.assert_code(del_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')

    @allure.story('添加退货原因订单')
    @pytest.mark.parametrize("name,sort,status,msg",excel_list,ids=idsList)
    def test_add_order_list(self,name,sort,status,msg):
        json={"name":name,"sort":sort,"status":status,"createTime":""}
        add_resp = request.post_request(url=url + 'returnReason/create', json=json, headers=head)
        resp_json = add_resp.json()
        assertion.assert_code(add_resp.status_code,200)
        assertion.assert_in_text(resp_json['message'], msg)