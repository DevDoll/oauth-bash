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
    print(r.text)

    print('account updated successfully...')

def passwordup(sval, bval):
    fcookie = {'S': '%s' % sval, 'B': '%s' % bval}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
               'X-Requested-With': 'XMLHttpRequest'}
    try:

        # Update Password
        print('Launching the API Part...')
        print('Updating Password...')
        furl = 'https://secure.hi5.com/api/?application_id=user&format=JSON'
        passcon = {'method': 'tagged.account.setPassword', 'oldPass': 'NewPassword456', 'newPass': 'NewPassword456',
                   'confPass': 'NewPassword456'}
        upass = requests.post(furl, data=passcon, cookies=fcookie, headers=headers)
        passresult = json.loads(upass.text)
        print(passresult)
    except Exception as e:
        print(e)

def picup(sess):
    fcookie = {'S': '%s' % sess}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0', 'X-Requested-With': 'XMLHttpRequest'}

    try:
        # Upload Pictures
        picurls = open('piclinks.txt', 'r').read().splitlines()
        picurl = random.choice(picurls)
        print(picurl)
        purl = 'https://www.hi5.com/api/?application_id=user&format=JSON'
        print('Uploading Picture from url')
        odara = {'method': 'tagged.photo.urlUpload', 'url': '%s' % picurl, 'make_large_thumb': 'true',
                 'full_path_size': 'p', 'image_type': 'P', 'album_id': '0'}
        upic = requests.post(purl, data=odara, cookies=fcookie, headers=headers)
        resu = json.loads(upic.text)
        print(resu)
        results = resu['result']
        picid = results['id']
        print('Photo id is %s, Making it primary' % picid)
        time.sleep(2)
        pdara = {'method': 'tagged.photo.setPrimary', 'photo_id': '%s' % picid}
        sepic = requests.post(purl, data=pdara, cookies=fcookie, headers=headers)
        print(sepic)

    except Exception as e: print(e)

def getinfo():
        with open('sessions.txt', 'r+') as source:
            thesess = source.readlines()

        with open("acc.txt") as file:
            for line in file:
                email, password, recovmail = line.split(':')

        return thesess email

#COde:
#email = input('Email Address:  ')
#stsess = input('Enter First Session:  ')
email, stsess = getinfo()
print('Updating Profile...')
fixaccount(stsess)
time.sleep(10)
#second Phaze
sval = input('Enter S value:  ')
bval = input('enter B value:  ')
print('Adding Password and uploading Profile Picture...')
time.sleep(2)
passwordup(sval, bval)
print('Uploading Profile Picture...')
time.sleep(2)
picup(sval)
print('Account is done...')
