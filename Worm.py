import os
import webbrowser
import time
from colorama import Fore, Style

def W_GPT():
    print(Fore.CYAN + "WGPT Activating..." + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.YELLOW + "We are not responsible for any misuse of this tool." + Style.RESET_ALL)
    time.sleep(3)
    agree = input(Fore.RED + "Do you agree to use this tool responsibly? (y/n): " + Style.RESET_ALL).lower()

    if agree != 'y':
        print(Fore.RED + "You must agree to use this tool responsibly. Exiting..." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "Opening WGPT Telegram Bot..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.BLUE + "Opening in 5s..." + Style.RESET_ALL)
    
    for i in range(5, 0, -1):
        print(Fore.BLUE + f"[+] Countdown: {i}" + Style.RESET_ALL)
        time.sleep(1)
    print(Fore.BLUE + "Launching now..." + Style.RESET_ALL)
    time.sleep(1)
    url = "https://t.me/Fsocity_gpt_bot"

    # Desktop Browsers
    try:
        webbrowser.open(url)
    except:
        pass

    # Android / Termux
    try:
        os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
    except:
        pass


# ------------ IMPORTANT ------------
# THIS MAKES SURE IT DOESN'T AUTO‑RUN
# ----------------------------------
if __name__ == "__main__":
    W_GPT()