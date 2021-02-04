import requests

# URL
base_url: str = 'http://info.sweettracker.co.kr'
company_api: str = '/api/v1/companylist' # 택배사 목록 가져오기

# Parameters (t_key: 발급받은 key)
params: dict = {'t_key':'MUwk2l0qX3mP47ZeL2lNUA'}

# 운송장 번호 조회
response = requests.get(base_url+company_api, params=params)
print(response.status_code)
print(response.text)