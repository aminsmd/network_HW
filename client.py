from requests import get,post
import json
import jsonpickle


def login(username,password):
    response = post("http://127.0.0.1:8000/user/login/", data={'username': username, 'password': password})
    global token
    if(response.text == "<h1> username or password wrong </h1>"):
        print(response.text)
        exit(0)
    token = json.loads(response.text)["token"]
    status = json.loads(response.text)["status"]
    print(status)

def getbalance():
    global token
    response = get('http://127.0.0.1:8000/user/balance', {'token': str(token)})
    print("balance : "+str(json.loads(response.text)["balance"]))

def deposite(m_add):
    global token
    response = get('http://127.0.0.1:8000/user/deposite' , {'token': str(token) , 'add': str(m_add)})
    nb = json.loads(response.text)
    print("new balance : " + str(nb["new balance"]))

def withdraw(amount):
    global token
    response = get('http://127.0.0.1:8000/user/withdraw', {'token': str(token), 'wd': str(amount)})
    nb = json.loads(response.text)
    print("withdraw "+nb["status"]+" , new balance : " + str(nb["new balance"]))

def logout():
    global token
    response = get('http://127.0.0.1:8000/user/logout', {'token': str(token)})
    print(response.text)

login("amin","amin")
getbalance()
deposite(1)
withdraw(0)
logout()
