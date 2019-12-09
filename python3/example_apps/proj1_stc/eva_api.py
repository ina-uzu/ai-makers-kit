# -*- coding:utf-8 -*-
import json
import array
import requests

url = "http://163.239.28.22:5000/"
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


def test():

    '''
    audio_file = wave.open("../data/sample_sound.wav", 'rb')
    byt_depth = audio_file.getsampwidth()  # Byte depth of the file in BYTES
    frame_rate = audio_file.getframerate()
    buf_size = 512
    
    print(byt_depth, frame_rate)
    
    bytes_data = audio_file.readframes(buf_size)
    body = bytes_data
    audio_file.close()
    
    #audio_file = open("../data/sample_sound.wav",'rb')
    audio_file = wave.open("../data/sample_sound.wav", 'rb')
    euc_bytes = audio_file.readframes(1024)
    byte_data = euc_bytes

    #byte_data = audio_file.readlines()
    print(type(byte_data), byte_data)
    '''

    byte_array = array.array('B')
    audio_file = open("../data/minwoo.wav", 'rb')
    byte_array.frombytes(audio_file.read())
    body = byte_array.tobytes()
    stt = '카스'
    print(type(stt))

    try:

        stt_data = stt.encode() + b'!'
        body = stt_data + body

        print(body)
        response = requests.post(url + "cmd/", data=body, headers={'Content-Type': 'application/octet-stream'})

        print("url : ", url + "cmd")
        print("file len : ", len(body))
        print("status code :", response.status_code)
        return response.text

    except Exception as e:
        print("ERROR! ", str(e))


def main():
    resp = test()
    cmd = json.loads(resp)
    print(cmd)


if __name__ == "__main__":
    main()
