from get_trackinginfo import Get_Trackinginfo
import requests

def Get_Location(keyword: str)-> tuple:
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(keyword)
    headers = {"Authorization": ""}

    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        location_info: dict = response.json()
        if location_info['meta']['total_count'] > 0:
            location = location_info['documents'][0]
            return (location['y'], ',', location['x'])
        else:
            print('검색 결과 없음')
    else:
        print('오류 발생')

if __name__ =="__main__":
    keyword = '한양대'  # 값은 trackinginfo에서 받아서 넣어야함
    location: tuple = Get_Location(keyword)
    print(location)
