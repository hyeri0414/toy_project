import requests

# URL
base_url: str = 'http://info.sweettracker.co.kr'
tracking_api: str = '/api/v1/trackingInfo' # 운송장 번호 조회

# Parameters (t_key: 발급받은 key), (t_code: 운송장 코드), (t_invoice: 운송장 번호)
params: dict = {'t_key':'MUwk2l0qX3mP47ZeL2lNUA', 't_code':'04', 't_invoice':'385504122525'}

# 운송장 번호 조회
response = requests.get(base_url+tracking_api, params=params)
print(response.text)