import requests
import random
import string
import threading
from itertools import cycle
from colorama import Fore
import os
os.system('color')

length = 5


with open('proxies.txt', 'r+', encoding='utf-8') as f:
    proxy = cycle(f.read().splitlines())

print("""
version - 1.0.0

[1] Strawpoll Vote Bot
[2] Strawpoll Vote Bot (Proxies)

""")
choice = input('>>>> ')





def Strawpollvotetool():
    global amount
    amount = 0
    while True:
        try:
            sendvote = requests.post(f'https://www.strawpoll.me/{strawpollid}', data={f'options': option})
            if sendvote.status_code == 200:
                amount += 1
                print(f'{Fore.GREEN}[ + ] Vote sent: {amount}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def Strawpollvotetool_PROXY():
    global amount
    amount = 0
    while True:
        try:
            proxies = {
                'https': 'https://' + next(proxy)
            }
            sendvote = requests.post(f'https://www.strawpoll.me/{strawpollid}', data={f'options': option}, proxies=proxies)
            if sendvote.status_code == 200:
                amount += 1
                print(f'{Fore.GREEN}[ + ] Votes sent: {amount}{Fore.RESET}')
        except Exception as err:
           x = 'test'
def StrawpollPollGeneration():
    global amount
    amount = 0
    while True:
        try:
            data = {
                'poll-title': title,
                'options-option-1': opt1,
                'options-option-2': opt2,
                'poll-submit': 'create',
                'f13e793ed742636f71173c7a052cf429c': '1'
            }
            amount += 1
            createpoll = requests.post('https://www.strawpoll.me/', data=data)
            print(createpoll.status_code)
            if createpoll.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Poll Created: {amount}{Fore.RESET}')
            else:
                print('')
        except Exception as err:
            print("err")
if choice == '1':
    strawpollid = input('Enter a strawpoll ID: ')
    option = input('Enter an option ID: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=Strawpollvotetool).start()
if choice == '2':
    strawpollid = input('Enter a strawpoll ID: ')
    option = input('Enter an option ID: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=Strawpollvotetool_PROXY).start()
if choice == '3':
    title = input('Enter a Title: ')
    opt1 = input('Enter an Option: ')
    opt2 = input('Enter an Option: ')
    threads = int(input('Threads: '))
    for i in range(threads):
        t1 = threading.Thread(target=StrawpollPollGeneration).start()
