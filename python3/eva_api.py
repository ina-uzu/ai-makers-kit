import requests

url = "http://15.164.50.174:5000/"


def send_stt(stt):
    params = {"stt": stt}
    response = requests.post(url + "stt", params=params)

    print("url : ", url + "stt")
    print("params : ", params)
    print("status code :", response.status_code)
