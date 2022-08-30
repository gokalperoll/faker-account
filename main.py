from faker import Faker
import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()
fake = Faker()
import signal
import readchar


def handler(signum, frame):
    msg = "\nCtrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y' or res == 'Y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)  # clear the printed line
        print("    ", end="\r", flush=True)


signal.signal(signal.SIGINT, handler)
class Account():
    def __init__(self):
        self.clear()

        self.status=True

    def clear(self):
        if os.name == 'nt':
            _ = os.system('cls')
        elif os.name == 'mac':
            _ = os.system('clear')
        elif os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('clear')

    def menu(self):
        try:

            banner="""
      █████▒▄▄▄       ██ ▄█▀▓█████                                    
    ▓██   ▒▒████▄     ██▄█▒ ▓█   ▀                                    
    ▒████ ░▒██  ▀█▄  ▓███▄░ ▒███                                      
    ░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄                                    
    ░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒                                   
     ▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░                                   
     ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░                                   
     ░ ░     ░   ▒   ░ ░░ ░    ░                                      
                 ░  ░░  ░      ░  ░                                   
                                                                      
     ▄▄▄       ▄████▄   ▄████▄   ▒█████   █    ██  ███▄    █ ▄▄▄█████▓
    ▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
    ▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░
    ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
     ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ 
     ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   
      ▒   ▒▒ ░  ░  ▒     ░  ▒     ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░    
      ░   ▒   ░        ░        ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░      
          ░  ░░ ░      ░ ░          ░ ░     ░              ░          
              ░        ░                                              
                                                                
            """
            print(Fore.YELLOW+banner+Style.RESET_ALL)
            print(f"{Fore.GREEN}[{Style.RESET_ALL}1{Style.RESET_ALL}{Fore.GREEN}]{Style.RESET_ALL}{Fore.BLUE}Random Name{Style.RESET_ALL}\n{Fore.GREEN}[{Style.RESET_ALL}2{Style.RESET_ALL}{Fore.GREEN}]{Style.RESET_ALL}{Fore.BLUE}Register Account{Style.RESET_ALL}\n{Fore.GREEN}[{Style.RESET_ALL}0{Style.RESET_ALL}{Fore.GREEN}]{Style.RESET_ALL}{Fore.BLUE}Exit{Style.RESET_ALL}\n")

            while self.status:
                choose = int(input(f"{Fore.GREEN}Select : "))
                if choose==00:
                    self.func_exit()
                elif choose==1:
                    self.random_name()

                elif choose==2:
                    self.register_account()
                else:
                    print("Correct choice!!")
        except ValueError:
            self.clear()
            self.menu()
    def random_name(self):
        create=int(input("How many create (1-50): "))

        if create>50 or create<1:
            self.clear()
            print("The limit cannot be exceeded.")
            self.menu()
        else:
            save = input("Do you want to save? (Y/N) : ")
            if save == "Y" or save=="y":
                with open("random_name", "w") as file:
                    sayac = 1
                    for i in range(1, create + 1):
                        file.write(f"\n{sayac}-{fake.name()}")
                        sayac += 1
                    print("random_name.txt file saved.")
            elif save == "N" or save == "n":

                sayac = 1
                for i in range(1, create + 1):
                    print(f"\n{sayac}-{fake.name()}")
                    sayac += 1

            else:
                print("Error!")
    def register_account(self):
        username = fake.user_name()
        password = fake.password()
        adress = fake.address()
        name = fake.name()
        phone_number = fake.phone_number()
        email=fake.email()
        print(f"""
Username : {username}\n
Password : {password}\n
Name Surname : {name}\n
Email : {email}\n
Adress : {adress}\n
Phone Number : {phone_number}\n
        """)


    def func_exit(self):
        self.status=False
account= Account()
account.menu()
