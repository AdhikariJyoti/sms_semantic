import requests
import json

from config import localIp, hostedIp

api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzMjVmYWFmMjc0ZDE5YjA0ZDc0ZGFjNyIsImlhdCI6MTY2MzQzNTI1MSwiZXhwIjoxNjY2MDI3MjUxfQ.NHW2_-lMyrg6Sn8haxx-MEu6V4TI7-uAsae63BYFkOM"
api_url_base = hostedIp
# api_url = localIp + "/api/v1/transactions"
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def get_sms_from_db():
    api_url = '{0}transactions'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    try:
        sms_json = requests.get(api_url, headers=headers).json()
        sms_list = sms_json['data']
        for i in sms_list:
            with open("sample.json", "w") as outfile:
                json.dump(i["message"], outfile)
            print(i["message"])
    except None:
        print("Exception Occurred")


# if response.status_code == 200:
#     return json.loads(response.content.decode('utf-8'))
# else:
#     return None


sms_info = get_sms_from_db()
if sms_info is not None:
    print("Here is your messages: ")
    for k, v in sms_info["data"]:
        print('{0}:{1}'.format(k, v))
else:
    print('[!] Request Failed')

# print(response.json())
