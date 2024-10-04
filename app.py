from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from sendemail import send_email
import threading


# sadasdas

app = Flask(__name__)

cookies = {
    'argus_session': 'ck0uaujk7c6s0dbjicv6qmlera',
    'cf_clearance': 'HOUq.GZFglU.zwbLVtLlFAJfokW0fYKp8h0hrv5HcC8-1727271938-1.2.1.1-zjc6Z81Bsv7iiG2yqMHAwhobXt5oMNQt0UrOtqc8MJgzrns1JZS5.UCKIBZgZ8TbIjOOi896Bt_A9VMO8NCtzXXX5PJaBYJYFPogFMKqUhoU52QW1z7OihqzvkA1iRnZon8KIwLZDB1rfyyuS1YTdFSHrxO9Ci0Nckml9hebJCmv2IANXESXW8V2qCHCCKtJLR8LmpQpiLOc4i_SoHG5yRci1A_jrCtAP43ksxjd6.DGPS6kbI8PhuyaqrUHZu62QET7oCzJEZJ7r5NV0eSuIngi4cljraRlngWPiJhIdc6TUsYmhDUIq75OJ0jjmREbzhhxlhKAOPe0u7hfImsrNKzaT8QL8NwqpPcih9J1FiKzsv0ewQGBGuanlddvEmsd4i5KdpUrIXO5oI.Ngx7y4Y1rAwCvhP05X4B40z_EV34'
}
gadarchevisUrl = 'https://classroom.btu.edu.ge/ge/student/me/rechoose/9082'
archevisUrl = 'https://classroom.btu.edu.ge/ge/student/me/choose/8950'

# Global flag to control the background task
registration_active = False

def registration_loop():
    global registration_active
    while registration_active:
        response2 = requests.get(archevisUrl, cookies=cookies)
        if response2.status_code == 200:
            soup = BeautifulSoup(response2.text, 'html.parser')
            isRechoose = soup.find('div', class_='rechoose')
            if not isRechoose:
                requests.get(gadarchevisUrl, cookies=cookies)
                continue
            error_message = soup.find('div', class_='alert system-error alert-danger')
            if not error_message:
                send_email('BTU Manager', "Subject was choosen.", 'anzor.gachechiladze.1@btu.edu.ge')
                registration_active = False
                break

def start_registration_thread():
    global registration_active
    if not registration_active:
        registration_active = True
        thread = threading.Thread(target=registration_loop)
        thread.start()

@app.route('/start', methods=['GET'])
def start_registration():
    start_registration_thread()
    return jsonify({"message": "Registration process started"}), 200

@app.route('/stop', methods=['GET'])
def stop_registration():
    global registration_active
    registration_active = False
    return jsonify({"message": "Registration process stopped"}), 200

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"active": registration_active}), 200

if __name__ == "__main__":
    app.run(debug=True)