from art import text2art
import qrcode
import speedtest
import os
import shutil
from colorama import Fore, Back, Style, init
import time
import hashlib
import os
import platform
import subprocess
import statistics
os.system("clear")
print (Fore.GREEN + Style.BRIGHT + "👤USER STATUS")
print ("="*20)
target = "google.com"

if platform.system() == "Windows":
    cmd = f"ping -n 1 {target} > nul"
else:
    cmd = f"ping -c 1 {target} > /dev/null 2>&1"

status = os.system(cmd)

print("online : ✔" if status == 0 else "offline : ❌")
print ("="*20)
init(autoreset=True)
                                                                                        #login page logo!
def logo5():
    print (Fore.GREEN + """⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⣴⣿⣿⡿⣿⢿⣟⣿⣻⣟⡿⣟⣿⣟⡿⣟⣿⣻⣟⣿⣻⢿⣻⡿⣿⢿⣷⣆⠄⠄⠄
   ⠄⠄⠄⢘⣿⢯⣷⡿⡿⡿⢿⢿⣷⣯⡿⣽⣞⣷⣻⢯⣷⣻⣾⡿⡿⢿⢿⢿⢯⣟⣞⡮⡀⠄⠄
   ⠄⠄⠄⢸⢞⠟⠃⣉⢉⠉⠉⠓⠫⢿⣿⣷⢷⣻⣞⣿⣾⡟⠽⠚⠊⠉⠉⠉⠙⠻⣞⢵⠂⠄⠄
   ⠄⠄⠄⢜⢯⣺⢿⣻⣿⣿⣷⣔⡄⠄⠈⠛⣿⣿⡾⠋⠁⠄⠄⣄⣶⣾⣿⡿⣿⡳⡌⡗⡅⠄⠄
   ⠄⠄⠄⢽⢱⢳⢹⡪⡞⠮⠯⢯⡻⡬⡐⢨⢿⣿⣿⢀⠐⡥⣻⡻⠯⡳⢳⢹⢜⢜⢜⢎⠆⠄⠄
   ⠄⠄⠠⣻⢌⠘⠌⡂⠈⠁⠉⠁⠘⠑⢧⣕⣿⣿⣿⢤⡪⠚⠂⠈⠁⠁⠁⠂⡑⠡⡈⢮⠅⠄⠄
   ⠄⠄⠠⣳⣿⣿⣽⣭⣶⣶⣶⣶⣶⣺⣟⣾⣻⣿⣯⢯⢿⣳⣶⣶⣶⣖⣶⣮⣭⣷⣽⣗⠍⠄⠄
   ⠄⠄⢀⢻⡿⡿⣟⣿⣻⣽⣟⣿⢯⣟⣞⡷⣿⣿⣯⢿⢽⢯⣿⣻⣟⣿⣻⣟⣿⣻⢿⣿⢀⠄⠄
   ⠄⠄⠄⡑⡏⠯⡯⡳⡯⣗⢯⢟⡽⣗⣯⣟⣿⣿⣾⣫⢿⣽⠾⡽⣺⢳⡫⡞⡗⡝⢕⠕⠄⠄⠄
   ⠄⠄⠄⢂⡎⠅⡃⢇⠇⠇⣃⣧⡺⡻⡳⡫⣿⡿⣟⠞⠽⠯⢧⣅⣃⠣⠱⡑⡑⠨⢐⢌⠂⠄⠄
   ⠄⠄⠄⠐⠼⣦⢀⠄⣶⣿⢿⣿⣧⣄⡌⠂⠢⠩⠂⠑⣁⣅⣾⢿⣟⣷⠦⠄⠄⡤⡇⡪⠄⠄⠄
   ⠄⠄⠄⠄⠨⢻⣧⡅⡈⠛⠿⠿⠿⠛⠁⠄⢀⡀⠄⠄⠘⠻⠿⠿⠯⠓⠁⢠⣱⡿⢑⠄⠄⠄⠄
   ⠄⠄⠄⠄⠈⢌⢿⣷⡐⠤⣀⣀⣂⣀⢀⢀⡓⠝⡂⡀⢀⢀⢀⣀⣀⠤⢊⣼⡟⡡⡁⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠈⢢⠚⣿⣄⠈⠉⠛⠛⠟⠿⠿⠟⠿⠻⠻⠛⠛⠉⠄⣠⠾⢑⠰⠈⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠑⢌⠿⣦⡡⣱⣸⣸⣆⠄⠄⠄⣰⣕⢔⢔⠡⣼⠞⡡⠁⠁⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠑⢝⢷⣕⡷⣿⡿⠄⠄⠠⣿⣯⣯⡳⡽⡋⠌⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢮⣿⣽⣯⠄⠄⢨⣿⣿⡷⡫⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
   ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠙⠝⠂⠄⢘⠋⠃⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄""") #ASCI ART
logo5()

print (Fore.BLUE + Style.BRIGHT + "[ ✔️ ] Loadin In 10 second")

time.sleep(10)
print ("\n" * 100)
def banner2():
    print (Style.BRIGHT + Fore.RED + """

░▒▓█▓▒░       ░▒▓██████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓████████▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░
                https://github.com/serviceloser-gif
    Version : 2.0                                              """) #banner
banner2()

print ("\n"*1)
print (Style.BRIGHT + "========= | RIGESTER  |==========")
username = "localhost@user1"
password = "YouRcool1"
print (Style.BRIGHT + "=================================")
print (Style.BRIGHT +(f"User is :{username}"))
print (Style.BRIGHT + "Type |Yes| To continue")
LOGIN = input(Style.BRIGHT + "ARE YOU SURE TO CONTINUE :")
#countdown
print ("\n" * 100)
print (Style.BRIGHT + Fore.BLUE + "=" * 50)
print (Style.BRIGHT + Fore.RED + "  . . . . . . . . . LOADING PAGE. . . . . . . . .")
print (Style.BRIGHT + Fore.BLUE + "=" * 50)
print ("\n" * 2)
print (Style.BRIGHT + "10%[#         ]")
time.sleep(0.5)
print (Style.BRIGHT + "20%[##        ]")
time.sleep(0.5)
print (Style.BRIGHT + "30%[###       ]")
time.sleep(0.5)
print (Style.BRIGHT + "40%[####      ]")
time.sleep(0.5)
print (Style.BRIGHT + "50%[#####     ]")
time.sleep(0.5)
print (Style.BRIGHT + "60%[######    ]")
time.sleep(0.5)
print (Style.BRIGHT + "70%[#######   ]")
time.sleep(0.5)
print (Style.BRIGHT + "80%[########  ]")
time.sleep(0.5)
print (Style.BRIGHT + "90%[######### ]")
time.sleep(0.5)
print (Style.BRIGHT + "100%[#########]")
time.sleep(0.5)
print (Fore.YELLOW + "LOADING COMPLETED")
print (f"hello {username}  thank you for using Our script!")
print (Style.BRIGHT + Fore.BLUE + "=" * 50)
time.sleep(2)
print ("\n" * 100)

def banner():
    print (Back.RED + """
▄▄▄        ▄▄▄▄   ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄
███      ▄██▀▀██▄ ▀▀▀███▀▀▀ ▄███████▄ ███▀▀███▄
███      ███  ███    ███    ███   ███ ███▄▄███▀
███      ███▀▀███    ███    ███▄▄▄███ ███▀▀██▄
████████ ███  ███    ███     ▀█████▀  ███  ▀███
   version :  2.0
https://github.com/serviceloser-gif """) #banner2

banner()

print ("\n" * 1)

text = ("Hello,WORLD" + "\n")

for ch in text:
    print(ch, end="", flush=True)
    time.sleep(0.10)

print (Style.BRIGHT + Fore.RED + f"logged as : {username}")
def sign():
   print (Style.BRIGHT + Fore.YELLOW + "="*25)
   print (Fore.YELLOW + "[👑] created by : ADRIAN🔐")
   print (Fore.YELLOW + "[✏️] Signature : **AdsUk_")
   print (Fore.YELLOW + "[✨]Version : 1.0")
   print (Fore.GREEN +"[✨] contribute : github")
   print (Fore.YELLOW + "[📨] email : serviceloser@gmail.com")
   print (Fore.YELLOW +"[🏪] discord : Adrianxpro_53803")
   print (Style.BRIGHT + Fore.YELLOW + "========= | EXIT | ===========")
sign()

#Options List
#home
print (Style.BRIGHT + Fore.YELLOW + "============| OPTIONS | ==========")
print (Fore.RED +Style.BRIGHT + "0.EXIT")
print (Fore.GREEN+Style.BRIGHT + "1.View password")
print (Style.BRIGHT + Fore.GREEN + "2.Math_solving (-)")
print (Style.BRIGHT + Fore.GREEN + "3.( * ) Times_solving")
print (Style.BRIGHT + Fore.GREEN + "4.(+)Addition solving")
print (Style.BRIGHT + Fore.GREEN +"5.Full calculator control✏")
print (Style.BRIGHT + Fore.GREEN +"6.Password hash (haslib)")
print (Style.BRIGHT + Fore.GREEN + "7.Script info")
print (Style.BRIGHT + Fore.GREEN +"8.Hashing Tool (More options)")
print (Style.BRIGHT + Fore.GREEN +"9.Password Checker")
print (Style.BRIGHT + Fore.GREEN +"10.WIfi Speed checker")
print (Style.BRIGHT + Fore.GREEN +"11.View Your Terminal info")
print (Style.BRIGHT + Fore.GREEN + "12.Show fake hacking")
print (Style.BRIGHT + Fore.GREEN + "13.QCODE Generator")
print (Style.BRIGHT + Fore.GREEN + "14.Asci Art generator (New)")
print (Style.BRIGHT + Fore.GREEN + "15.Ping checker (New)")
print (Style.BRIGHT + Fore.GREEN + "16.Nmap (New)")
print (Style.BRIGHT + Fore.GREEN + "17.view top")
print (Style.BRIGHT + Fore.GREEN + "18.view htop ( same as top )")
print (Style.BRIGHT + Fore.GREEN + "19.Password Manager")
print (Style.BRIGHT + Fore.YELLOW + "20.Notepad")
print (Style.BRIGHT + "choose an Option 0-12")
#Input
print (Fore.RED + "==============================")
option = int(input(Style.BRIGHT + "Select 1-10 :"))
print (Fore.RED + "==============================")



#Option 0
if option == 0:
   print ("Goodbye")
#option 1
elif option == 1:
   print (Style.BRIGHT + "[~] : LOADING.. THIS MIGTH TAKE 10 SECONDS")
   time.sleep(10)
   print(Style.BRIGHT + (f"[~] :Your password is: 🔑{password}"))
#option 2
elif option == 2:
     print ("\n" * 100)
     a = int(input("FIRST NUMBER :"))
     b = int(input("SECOND NUMBER :"))
     print (Back.RED + "[~] : Answer :",a - b)
#option 3
elif option == 3:
     print ("\n" * 100)
     a = int(input("FIRST NUMBER :"))
     b = int(input("SECOND NUMBER :"))
     print (Back.RED + "[~] : Answer :",a * b)
#option 4
elif option ==4:
     print ("\n" * 100)
     a = int(input("FIRST NUMBER :"))
     b = int(input("SECOND NUMBER :"))
     print (Back.RED + "[~] : Answrer :",a +b)
#option 5
elif option == 5:
     a = input(Style.BRIGHT + "NUMBERS INPUT :")
     print (eval(a))
     print (Style.BRIGHT + "To run thr script again , :python main.py")
#Option 6
elif option == 6:
   print ("\n" * 100)
   print (Style.BRIGHT + "========= |HASH|=========")
   print (Style.BRIGHT + "====== |SHA-256| =====")
   usrn = input(Style.BRIGHT + "ENTER THE ACCOUNT USER :")
   password = input(Style.BRIGHT + "Enter Your Password :")
   print (Fore.RED + "====== |HASHING STATUS🚥| ======")
   print (Style.BRIGHT + "🚥HASHING...")
   time.sleep(2)
   print (Style.BRIGHT + "💉PROCESSING...")
   time.sleep(2)
   print (Style.BRIGHT + "⌛Generating...")
   time.sleep(2)
   print (Style.BRIGHT + "📖GATHERING INFO...")
   time.sleep(2)
   print (Style.BRIGHT + "💉HASHING Account...")
   time.sleep(2)
   print (Style.BRIGHT + "✔️COMPLETED")
   print ("\n" * 1)
   print (Style.BRIGHT + "====== |HASH RESULT| ======")
   hashed = hashlib.sha256(password.encode()).hexdigest()
   print (Style.BRIGHT + (f"✔️Result : {hashed}"))
   print (Style.BRIGHT + "TO RUN AGAIN :python3 main.py")
   print (Style.BRIGHT + "===========================")
   start = time.time()

   print(Style.BRIGHT + (f"⌛Time taken: {time.time() - start:.3f}s"))
#option 7
elif option == 7:
    print (Style.BRIGHT + "LOADING ...")
    time.sleep(3)
    print ("\n" * 100)
    print (Fore.RED + Style.BRIGHT + """ ___ _   _ _____ ___
|_ _| \ | |  ___/ _ \
 | ||  \| | |_ | | | |
 | || |\  |  _|| |_| |
|___|_| \_|_|   \___/""")
    print (Style.BRIGHT + "===== |Script Info| =====")
    print (Style.BRIGHT + "[📄] SCRIPT EDITOR : nano")
    print (Style.BRIGHT + "[⚡] TERMINAL : TERMUX/TMUX")
    print (Style.BRIGHT + "[🔥] PROJECT NO:4")
    print (Style.BRIGHT + "[👑] OWNER :ADRIAN")
    print (Style.BRIGHT + "[💬] PROGRAMMING LANG : PYTHON")
    print (Style.BRIGHT + "[👥] Tiktok Account : @Rectypy")
    print (Style.BRIGHT + "[👥] Youtube account : @souless")
    print (Style.BRIGHT + "[👥] Discord : adrianxpro_53803")
    print (Style.BRIGHT + "[📧] email : serviceloser@gmail.com")
    print (Style.BRIGHT + "=========================")
#Exit
elif option == 8:

   print (Style.BRIGHT + "======= |HASHING OPTION| ======")

   password = input("Enter Your Password: ").encode()

   print("Available Algorithms:")
   print("1. SHA-256")
   print("2. SHA-512")
   print("3. MD5 (weak)")
   print("4. BLAKE2")
   choice = input("Select: ")

   start = time.time()

   if choice == "1":
      result = hashlib.sha256(password).hexdigest()
   elif choice == "2":
      result = hashlib.sha512(password).hexdigest()
   elif choice == "3":
      result = hashlib.md5(password).hexdigest()
   elif choice == "4":
      result = hashlib.blake2b(password).hexdigest()

   print(f"\nHash: {result}")
   print(f"Time: {time.time() - start:.2f}s")
#password checker
elif option == 9:
   print (Style.BRIGHT + "LOADING...")
   time.sleep(5)
   print ("\n" * 100)

   print (Fore.RED + """
|  _ \ / \  / ___/ ___\ \      / /
| |_) / _ \ \___ \___ \\ \ /\ / /
|  __/ ___ \ ___) |__) |\ V  V /
|_| /_/   \_\____/____/  \_/\_/
      ver 2.0""")
   print ("\n " * 2)
   print (Fore.YELLOW + "👨‍💻CREATED BY:ADRIAN")

   print (Style.BRIGHT + "===================")
   pw = input(Style.BRIGHT + (f"[🔐] Your password :")).encode()
   length = len(pw)
   print (Style.BRIGHT + "🚥Measuring length...")
   time.sleep(1.0)
   print (Style.BRIGHT + "🔐Solving Length Combination...")
   time.sleep(1)
   print (Style.BRIGHT + (f"✔️Measuring : {pw} ..."))
   time.sleep(1)
   print (Style.BRIGHT + "✔️ password measure completed")
   print ("\n" * 2)
   print (Style.BRIGHT + "========= |RESULT| ========")
   print (Style.BRIGHT + (f"Priview of your password is : {pw}"))
   print (Style.BRIGHT + "=============|HASH|===============")
   result =  hashlib.blake2b(pw).hexdigest()
   print (Style.BRIGHT + "========|PASSW STATUS|==========")
   print (result)
   if length < 5:
      print (Style.BRIGHT + (f"🚥Status :Weak 🔑"))
   elif length < 4:
      print (Style.BRIGHT + (f"🚥Status :Weak 🔑"))
   elif length < 7:
      print (Style.BRIGHT + (f"💔Status :weak 🌓"))
   elif length < 8:
      print (Style.BRIGHT + (f"💔Status :weak 🌓"))
   elif length < 10:
      print(Style.BRIGHT + (f"🚥Status : Average😐"))
   elif length < 15:
      print (Style.BRIGHT + (f"📶Status : 🔥 Strong"))
   else:
      print("🚥Status : Strong🔥")
   print ("=" * 15)
#wifite
elif option == 10:
   print ("\n" * 100)
   print  (Fore.RED + """ ____  ____  _____ _____ ____ _____ _____ ____ _____
/ ___||  _ \| ____| ____|  _ \_   _| ____/ ___|_   _|
\___ \| |_) |  _| |  _| | | | || | |  _| \___ \ | |
 ___) |  __/| |___| |___| |_| || | | |___ ___) || |
|____/|_|   |_____|_____|____/ |_| |_____|____/ |_|
version : 2.0""")
   print ("\n" * 1)
   print (Back.RED +    "Created by : ADRIAN")
   print ("\n" * 2)

   start = time.time()


   st = speedtest.Speedtest()
   print (Style.BRIGHT + "📶Fetching Data...") #ask user
   time.sleep(5)
   print (Style.BRIGHT +"🔥TESTING DOWNLOAD...")
   time.sleep(2)
   print (Style.BRIGHT + "📈TESTING UPLOAD...")
   time.sleep(2)
   print (Style.BRIGHT + "📡Collecting Data...")
   download = st.download() / 1_000_00
   upload = st.upload() / 1_000_000
   print ("\n")
   print (Style.BRIGHT + "============== |SPEED RESULT|=============")
   print (f"🔥Download: {download:.2f} Mbps")
   print (f"📈Upload: {upload:.2f} Mbps")


   print (f"⏳Time: {time.time() - start:.2f}s")
#option 11
elif option == 11:
   print (Style.BRIGHT + "1.Install fastfetch") #auto install fastfetch
   print (Style.BRIGHT + "2.Install neofetch") #auto install neofetch
   print (Style.BRIGHT + "3.Install Screenfetch") #auto install screenfetch
   print (Style.BRIGHT + "4.Exit") #Exit
   section = int(input("Your Option :"))
   if section == 1:
      os.system("pkg install fastfetch")
      os.system("fastfetch")
   elif section == 2:
      os.system("pkg install neofetch")
      os.system("neofetch")
   elif section == 3:
      os.system("pkg install screenfetch")
      os.system("screenfetch")
   elif section == 4:
      print (Style.BRIGHT + "🔴Exitting...")
      time.sleep(3)
   else:
      print (Style.BRIGHT + "Invalid choice") #shows invalid option
elif option == 12:   #Fake hacking
   os.system("apt install hollywood")
   os.system("hollywood")
elif option == 13:
    print ("\n" * 100)
    print (Style.BRIGHT + Fore.RED + """  ___  ____   ____ ___  ____  _____
 / _ \|  _ \ / ___/ _ \|  _ \| ____|
| | | | |_) | |  | | | | | | |  _|
| |_| |  _ <| |__| |_| | |_| | |___
 \__\_\_| \_\\____\___/|____/|_____|
   version : 1.0     """) #ASCII ART BANNER
    print ("\n" * 2)
    print (Back.RED + Style.BRIGHT + "=" * 20)
    print (Style.BRIGHT + Fore.YELLOW + "Created By : ADRIAN")
    print (Back.RED + Style.BRIGHT + "=" * 20)
    print ("\n" * 1)
    data = input(Style.BRIGHT + "Enter link or text: ")
    print (Fore.YELLOW + Style.BRIGHT + "[✔]- Generating..")
    time.sleep(5)
    print (Fore.YELLOW + Style.BRIGHT + "[✔]- completed ")
    time.sleep(2)

    qr = qrcode.QRCode()  #  Capital QRCode
    qr.add_data(data)
    qr.make(fit=True)

    qr.print_ascii(invert=True)
    print (Fore.YELLOW + Style.BRIGHT + "[✔] ~ QRCODE VIRRIFIED")

elif option == 14:
   print ("\n" * 100)
   print (Style.BRIGHT + Fore.RED + """    _     ____    ____  ___    ____  _____  _   _
   / \   / ___|  / ___||_ _|  / ___|| ____|| \ | |
  / _ \  \___ \ | |     | |  | |  _ |  _|  |  \| |
 / ___ \  ___) || |___  | |  | |_| || |___ | |\  |
/_/   \_\|____/  \____||___|  \____||_____||_| \_|""")
   print (Back.RED + "=" * 20)
   print (Fore.YELLOW + Style.BRIGHT + "Created By: Adrian")
   print (Back.RED + "=" * 20)
   print ("\n" * 2)
   text = input(Style.BRIGHT + "Your Text :")
   art = text2art(text)
   print (Fore.YELLOW + Style.BRIGHT + "Generating...")
   time.sleep(3)
   print (art)
   print (Fore.RED + Style.BRIGHT + "=" * 30)
   end()
#option 15
elif option == 15:
   print (Style.BRIGHT + Fore.RED + "=" * 30)
   print (Style.BRIGHT + Fore.YELLOW + "Ping checker")
   print (Style.BRIGHT + Fore.RED + "=" * 30)
   ping = input(Style.BRIGHT + "Enter a website to ping :")
   print (Fore.YELLOW + Style.BRIGHT + "Starting...")
   time.sleep(3)
   os.system(f"ping {ping}")
   print (Fore.YELLOW +Style.BRIGHT + "[LATOR] ~ Free Open source")
elif option == 16:
   print ("\n" * 100)
   print (Style.BRIGHT + Fore.RED + """ _   _
| \ | |
|  \| |_ __ ___   __ _ _ __
| . ` | '_ ` _ \ / _` | '_ \
| |\  | | | | | | (_| | |_) |
\_| \_/_| |_| |_|\__,_| .__/
                      | |
                      |_|

https://github.com/serviceloser-gif
created by : Adrian""")
   print ("\n" * 1)
   print (Style.BRIGHT + Fore.YELLOW + "🚨- Riminder please dont scan rondom networks without permission")
   print ("\n" * 1)
   print (Style.BRIGHT + Fore.RED + "=" * 30)
   print (Style.BRIGHT + "Created by : ADRIAN")
   print (Style.BRIGHT + Fore.RED + "=" * 30)
   print ("\n" * 1)
   ip = input(Style.BRIGHT + Fore.RED + "Enter Your IP address :")
   time.sleep(5)
   print (Style.BRIGHT + Fore.YELLOW + "[ ✔ ]~ Locating ports...")
   os.system(f"nmap {ip}")
elif option == 17:
   os.system("top") #regular system info
elif option == 18:
   os.system("apt install htop") #Terminal Monitor
   os.system("htop")
elif option == 19:
    print (Fore.RED + "=" * 30)
    print ("Password Manager")
    print (Fore.RED + "=" * 30)
    site = input("Site/App: ")
    username = input("Username: ")
    password = input("Password: ")
    with open("passwords.txt", "a") as f:
       f.write(f"Site: {site} | Username: {username} | Password: {password}\n")
    time.sleep(3)
    print (Style.BRIGHT + Fore.YELLOW + "Succesfully Saved!\n")
    print (Style.BRIGHT + "Type ( cat passwords.txt ) to view the passwords and user")

#Saved Messages
elif option == 20:
    print (Fore.RED + "Saved Messages")
    message = input(Style.BRIGHT + "Enter Your message :")
    with open ("message.txt", "a") as f:
       f.write(f"Saved : {message}\n")
    time.sleep(5)
    print (Fore.YELLOW + Style.BRIGHT + "Succesfully saved!\n")
    print (Fore.YELLOW + Style.BRIGHT + "Script Finnished!")

def end():
    print ("Script Finnished")

#hi if your reading this message pls Respect my code.
#i have spent over Months to make this.
#Im adrian a 15 years old programmer. who wants to code and learn coding
#im still new to python
