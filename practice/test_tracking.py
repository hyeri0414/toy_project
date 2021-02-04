from get_companylist import Get_Companylist
import requests

# URL
base_url: str = 'http://info.sweettracker.co.kr'
tracking_api: str = '/api/v1/trackingInfo' # 운송장 번호 조회

# Parameters (t_key: 발급받은 key), (t_code: 운송장 코드), (t_invoice: 운송장 번호)
params: dict = {'t_key':'MUwk2l0qX3mP47ZeL2lNUA', 't_code':'06', 't_invoice':'98996271544'}

# 운송장 번호 조회
# response = requests.get(base_url+tracking_api, params=params)
# result = response.json()
# print(result)

# 슬라이싱하기
info = {'result': 'Y', 'senderName': '', 'receiverName': '', 'itemName': 'P101 SILENT PC케이스 :1EA', 'invoiceNo': '98996271544', 'receiverAddr': '', 'orderNumber': None, 'adUrl': None, 'estimate': '당일배송', 'level': 6, 'complete': True, 'recipient': '', 'itemImage': '', 'trackingDetails': [{'time': 1612186500000, 'timeString': '2021-02-01 22:35:00', 'code': None, 'where': '원주센터', 'kind': '터미널입고', 'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, {'time': 1612186560000, 'timeString': '2021-02-01 22:36:00', 'code': None, 'where': '원주센터', 'kind': '터미널출고', 'telno': '', 'telno2': '', 'remark': None, 
'level': 3, 'manName': '', 'manPic': ''}, {'time': 1612201080000, 'timeString': '2021-02-02 02:38:00', 'code': None, 'where': '이천센터', 'kind': '터미널출고', 'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, {'time': 1612211460000, 'timeString': '2021-02-02 05:31:00', 'code': None, 'where': '이천센터', 'kind': '터미널입고', 'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, {'time': 1612223820000, 'timeString': '2021-02-02 08:57:00', 'code': None, 'where': '동평택', 'kind': '배송입고', 'telno': '0505-278-8310', 'telno2': '', 'remark': None, 'level': 4, 'manName': '', 'manPic': ''}, {'time': 1612223940000, 'timeString': '2021-02-02 08:59:00', 'code': None, 'where': '동평택', 'kind': '배송출고(당일배송)', 'telno': '010-3476-9122', 'telno2': '', 'remark': None, 'level': 5, 'manName': '', 'manPic': ''}, {'time': 1612244580000, 'timeString': '2021-02-02 14:43:00', 'code': None, 'where': '동평택', 'kind': '배송완료', 'telno': '010-3476-9122', 'telno2': '', 'remark': None, 'level': 6, 'manName': '', 'manPic': ''}], 'productInfo': None, 'zipCode': None, 'firstDetail': {'time': 1612186500000, 'timeString': '2021-02-01 22:35:00', 'code': None, 'where': '원주센터', 'kind': '터미널입고', 'telno': '', 'telno2': '', 'remark': None, 'level': 3, 'manName': '', 'manPic': ''}, 'completeYN': 'Y', 'lastDetail': {'time': 1612244580000, 'timeString': '2021-02-02 14:43:00', 'code': None, 'where': '동평택', 'kind': '배송완료', 'telno': '010-3476-9122', 'telno2': '', 'remark': None, 'level': 6, 'manName': '', 'manPic': ''}, 'lastStateDetail': {'time': 1612244580000, 'timeString': '2021-02-02 14:43:00', 'code': None, 'where': '동평택', 'kind': '배송완료', 'telno': '010-3476-9122', 'telno2': '', 'remark': None, 'level': 6, 'manName': '', 'manPic': ''}}

# print(info['trackingDetails'])
# print(type(info['trackingDetails'])) # <class 'list'>
# print(len(info['trackingDetails'])) # len은 7

details = info['trackingDetails']

where = []

for i in range(0, len(info['trackingDetails'])):
    print(details[i])
    where.append(details[i]['where'])

# 리스트에서 unique값만 갖게하기
'''where = list(set(where))
print(where)'''



