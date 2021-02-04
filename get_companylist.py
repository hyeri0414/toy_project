import requests

def Get_Companylist()-> list:
    url: str = 'http://info.sweettracker.co.kr/api/v1/companylist'
    params: dict = {'t_key':'MUwk2l0qX3mP47ZeL2lNUA'}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        company_list: dict = response.json()
        return company_list['Company']
    else:
        print('오류 발생')

if __name__ =="__main__":
    company_list: dict = Get_Companylist()
    print(company_list)