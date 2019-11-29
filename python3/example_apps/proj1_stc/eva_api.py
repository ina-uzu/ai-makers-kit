import requests

url = "http://15.164.50.174:5000/"


def get_final_cmd(stt, voice):
    params = {"stt": stt, "voice": voice}
    try:
        response = requests.post(url + "cmd", params=params)

        print("url : ", url + "cmd")
        print("params : ", params)
        print("status code :", response.status_code)

    except Exception as e:
        print("ERROR! ", str(e))


def send_stt(stt):
    params = {"stt": stt}
    try:
        response = requests.post(url + "stt", params=params)

        print("url : ", url + "stt")
        print("params : ", params)
        print("status code :", response.status_code)

    except Exception as e:
        print("ERROR! ", str(e))


def get_final_cmd(stt, voice):
    params = {"stt": stt, "voice": voice}

    try:
        response = requests.post(url + "eva", params=params)

        print("url : ", url + "eva")
        print("params : ", params)
        print("status code :", response.status_code)

    except Exception as e:
        print("ERROR! ", str(e))


def main():
    stt = input("stt: ")

    get_final_cmd(stt, None)


if __name__ == "__main__":
    main()
