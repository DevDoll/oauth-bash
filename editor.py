import requests
import json
from fake_useragent import UserAgent
import time
import random
import string



def getinfo():
    with open('sessions.txt', 'r+') as source:
        thesess = source.readlines()

    with open("acc.txt") as file:
        for line in file:
            email, password, recovmail = line.split(':')
            emails.append(email)
    return thesess

def getacc():
    try:
        alphanumiric = string.ascii_lowercase + string.digits
        did = ''.join(random.choice(alphanumiric) for i in range(16))
        aid = "".join([random.choice(alphanumiric) for i in range(8)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(12)])

        print('Using %s as a DeviceID and as AAID: %s' % (did, aid))

        url = 'https://secure.hi5.com/api/?method=tagged.login.login&application_id=user'
        headers = {'User-Agent': '%s'%useragent}
        obj = {'email': '%s'%email, 'password': 'NewPassword456', 'deviceId': '%s'%did, 'aaid': '%s'%aid}
        try:
            r = requests.post(url, data=obj, headers=headers)
            response = json.loads(r.text)
            print('Retrieving Account Info')
            print(response)
            results = response['result']
            working = response['stat']
            if working == 'fail':
                return False
            else:
                accid = results['user_id']
                autotoken = results['auto_token']
                session = results['session']
                mid = str(accid)
                return mid, autotoken, session
        except Exception as e: print(e)
    except:
        print('\nCant Login to the account, moving on\n')
        return False

useragent = 'hi5/9.30.1 (SPA Condor Electronics TFX-708G; Android 4.4.2; Android/TFX-708G/TFX-708G:4.4.2/KOT49H/1445414608:user/release-keys)'
emails = list()
stsessions = getinfo()
email = ''.join(emails)
myid, token, session = getacc()
