import requests
from bs4 import BeautifulSoup
cookies = {
    'argus_session': 'ck0uaujk7c6s0dbjicv6qmlera',
    'cf_clearance':  'HOUq.GZFglU.zwbLVtLlFAJfokW0fYKp8h0hrv5HcC8-1727271938-1.2.1.1-zjc6Z81Bsv7iiG2yqMHAwhobXt5oMNQt0UrOtqc8MJgzrns1JZS5.UCKIBZgZ8TbIjOOi896Bt_A9VMO8NCtzXXX5PJaBYJYFPogFMKqUhoU52QW1z7OihqzvkA1iRnZon8KIwLZDB1rfyyuS1YTdFSHrxO9Ci0Nckml9hebJCmv2IANXESXW8V2qCHCCKtJLR8LmpQpiLOc4i_SoHG5yRci1A_jrCtAP43ksxjd6.DGPS6kbI8PhuyaqrUHZu62QET7oCzJEZJ7r5NV0eSuIngi4cljraRlngWPiJhIdc6TUsYmhDUIq75OJ0jjmREbzhhxlhKAOPe0u7hfImsrNKzaT8QL8NwqpPcih9J1FiKzsv0ewQGBGuanlddvEmsd4i5KdpUrIXO5oI.Ngx7y4Y1rAwCvhP05X4B40z_EV34'
}
gadarchevisUrl = 'https://classroom.btu.edu.ge/ge/student/me/rechoose/9082'
archevisUrl = 'https://classroom.btu.edu.ge/ge/student/me/choose/8950'

print("Sending Request Loop started... ")
while True:
    response2 = requests.get(archevisUrl, cookies=cookies)
    if response2.status_code == 200:
        soup = BeautifulSoup(response2.text, 'html.parser')
        isRechoose = soup.find('div', class_='rechoose')
        if not isRechoose:
            response1 = requests.get(gadarchevisUrl, cookies=cookies)
        error_message = soup.find('div', class_='alert system-error alert-danger')
        if not error_message:
            break
        print(error_message.select_one('span.alert-message').text.strip())
    else:
        print('Failed to retrieve the second URL:', response2.status_code)
print("sagani aircha")