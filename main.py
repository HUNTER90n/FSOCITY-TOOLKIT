import os
import sys
import pyfiglet
from colorama import Fore, Style
import Vulnerability_Scanning
import FPC

# ---- Banner ----
banner = pyfiglet.figlet_format("FSOCITY")
print(Fore.CYAN + banner + Style.RESET_ALL)
print(Fore.GREEN + "FSOCITY IS CREATED BY @HUNTER90n" + Style.RESET_ALL)
print(Fore.YELLOW + "Welcome to FSOCITY ULTIMATE HACKING TOOLKIT!" + Style.RESET_ALL)

while True:
    print(Fore.MAGENTA + "\nMain Menu:" + Style.RESET_ALL)
    print(Fore.RED + "1. File Password Cracker" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Vulnerability Scanning" + Style.RESET_ALL)
    print(Fore.BLUE + "3. About Us" + Style.RESET_ALL)
    print(Fore.WHITE + "4. Exit" + Style.RESET_ALL)

    choice = input("Select an option (1-4): ")

    if choice == '1':
        FPC.FPC_cracker()
        input("\nPress Enter to return...")

    elif choice == '2':
        Vulnerability_Scanning.real_scanner()
        input("\nPress Enter to return...")

    elif choice == '3':
        os.system(f'"{sys.executable}" about.py')
        input("\nPress Enter to return...")

    elif choice == '4':
        print(Fore.RED + "Exiting FSOCITY. Goodbye!" + Style.RESET_ALL)
        break

    else:
        print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

