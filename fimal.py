import requests
from get_trackinginfo import Get_Trackinginfo
from get_location import Get_Location

if __name__ =="__main__":
    t_invoice: str = input('운송장 번호: ')
    t_code: str = input('택배사 코드: ')

    tracking_details: list = Get_Trackinginfo(t_invoice, t_code)

    