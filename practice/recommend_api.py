import requests

# URL
base_url: str = 'http://info.sweettracker.co.kr'
recommend_api: str = '/api/v1/recommend' # 추천 택배사 정보 가져오기

# Parameters (t_key: 발급받은 key), (t_invoice: 운송장 번호)
params: dict = {'t_key':'MUwk2l0qX3mP47ZeL2lNUA', 't_invoice':'385504122525'}

# 운송장 번호 조회
response = requests.get(base_url+recommend_api, params=params)
print(response.status_code)
print(response.text)