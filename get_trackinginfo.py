from get_companylist import Get_Companylist
import requests

def Get_Trackinginfo(t_invoice: str, t_code: str)-> list:
    url: str = 'http://info.sweettracker.co.kr/api/v1/trackingInfo'
    params: dict = {'t_key':'MUwk2l0qX3mP47ZeL2lNUA'}
    params['t_invoice'] = t_invoice
    
    company_list = Get_Companylist()
    for com in company_list:
        if com['Code'] == t_code:
            params['t_code'] = com['Code']

    response = requests.get(url, params=params)

    if response.status_code == 200:
        tracking_info: dict = response.json()
        return tracking_info['trackingDetails']
    else:
        print('오류 발생')

if __name__ =="__main__":
    t_invoice: str = input('운송장 번호: ')
    t_code: str = input('택배사 코드: ')

    tracking_details: list = Get_Trackinginfo(t_invoice, t_code)
    print(tracking_details)