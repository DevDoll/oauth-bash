import random
import requests
import json
import time



def fixaccount(stsess):
    names = open('mnames.txt', 'r', encoding='utf8', errors='ignore').read().splitlines()
    disname = random.choice(names)

    print('Creating an account with %s which will be Named %s '% (email, disname))
    url = 'https://secure.hi5.com/register.html?src=index_email&page=register&loc=fr_FR'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'Referer': 'https://secure.hi5.com/register.html?err=1020'}
    coockies = {'S': '%s'% stsess}
    obj = {'displayName': '%s'% disname, 'email': '%s'% email, 'password': 'NewPassword456', 'passwordStr': '1607268001%3ARCGYBM03Sg', 'city': 'Ville', 'gender': 'M', 'birthMonth': '9', 'birthDay': '21', 'birthYear': '1998', 'zipCode': '10006', 'country': 'US'}
    r = requests.post(url, data=obj, headers=headers, cookies=coockies)
    #print(r.text)

def getinfo():
    with open('sessions.txt', 'r+') as source:
        thesess = source.readlines()
        print(thesess)

    with open("acc.txt") as file:
        for line in file:
            email, password, recovmail = line.split(':')
            emails.append(email)
    return thesess

#COde
#email = input('Email Address:  ')
#stsess = input('Enter First Session:  ')
emails = list()
stsessions = getinfo()
email = ''.join(emails)
stsess = ''.join(stsessions)

print(email)
print(stsess)

print('Updating Profile...')
fixaccount(stsess)
time.sleep(10)
print('Account Verified')
