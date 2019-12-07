# -*- coding:utf-8 -*-
import json

import requests
import chardet

url = "http://54.180.120.132:5000/"
#url = "http://127.0.0.1:5000/"


def get_final_cmd(stt, voice):
    data = {"stt": stt, "voice": voice}

    try:
        response = requests.post(url + "cmd", data=data)

        print("url : ", url + "cmd")
        print("data : ", data)
        print("status code :", response.status_code)
        return response.text

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


import  wave
def test():
    #byte_array = array.array('B')
    audio_file = wave.open("../data/sample_sound.wav", 'rb')

    byt_depth = audio_file.getsampwidth()  # Byte depth of the file in BYTES
    frame_rate = audio_file.getframerate()
    buf_size = 512

    print(byt_depth, frame_rate)

    #byte_array.frombytes(audio_file.read())
    bytes_data = audio_file.readframes(buf_size)
    print(type(bytes_data))
    body = bytes_data
    audio_file.close()

    stt = input("stt ")

    try:
        data = {"stt":stt, "voice" : body}
        response = requests.post(url + "device", data=data)

        print("url : ", url + "device")
        print("file len : ", len(body))
        print("status code :", response.status_code)
        return response.text

    except Exception as e:
        print("ERROR! ", str(e))


def main():
#  test()

    stt = input("stt: ")

    try:
        resp = get_final_cmd(stt, "TEST")
        cmd = json.loads(resp)
        print(cmd)

        if "command" in cmd:
            cmd = cmd["command"]
            print(cmd)

    except Exception as e:
        print("ERROR! ", str(e))




if __name__ == "__main__":
    main()
