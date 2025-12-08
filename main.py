import os
import sys
import pyfiglet
from colorama import Fore, Style
import Vulnerability_Scanning
import FPC
import Worm
import DDOS

# ---- Banner ----
banner = pyfiglet.figlet_format("FSOCITY")
print(Fore.RED + banner + Style.RESET_ALL)
print(Fore.GREEN + "FSOCITY IS CREATED BY @HUNTER90n" + Style.RESET_ALL)
print(Fore.YELLOW + "Welcome to FSOCITY ULTIMATE HACKING TOOLKIT!" + Style.RESET_ALL)

while True:
    print(Fore.MAGENTA + "\nMain Menu:" + Style.RESET_ALL)
    print(Fore.RED + "1. File Password Cracker (V.FAST)" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Vulnerability Scanning" + Style.RESET_ALL)
    print(Fore.BLUE + "3. Worm GPT" + Style.RESET_ALL)
    print(Fore.CYAN + "4. DDoS Attack" + Style.RESET_ALL)
    print(Fore.MAGENTA + "5. BUG_SCAN (SOON)" + Style.RESET_ALL)
    print(Fore.YELLOW + "6. About Us" + Style.RESET_ALL)
    print(Fore.WHITE + "7. Exit" + Style.RESET_ALL)

    choice = input("Select an option (1-7): ")

    if choice == '1':
        FPC.FPC_cracker()
        input("\nPress Enter to return...")

    elif choice == '2':
        Vulnerability_Scanning.real_scanner()
        input("\nPress Enter to return...")

    elif choice == '3':
        Worm.W_GPT()
        input("\nPress Enter to return...")

    elif choice == '4':
        DDOS.S_DOS()
        input("\nPress Enter to return...")

    elif choice == '5':
        os.system(f'"{sys.executable}" bug_hunter.py')
        input("\nPress Enter to return...")

    elif choice == '6':
        os.system(f'"{sys.executable}" about.py')
        input("\nPress Enter to return...")

    elif choice == '7':
        print(Fore.RED + "Exiting FSOCITY. Goodbye!" + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)


