import requests

searching = '한양대'
url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
headers = {"Authorization": "KakaoAK 8a17c4c710d86b2c7e6704d7411b2ff4"}

# location의 좌표값 얻기
#location = requests.get(url, headers = headers).json()['documents']
#print(location[0]['y'],',', location[0]['x'])

response = requests.get(url, headers = headers)
location_info = response.json()
print(location_info['documents'][0])
