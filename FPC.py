import os
import webbrowser
import time

def FPC_cracker():
    print("FPC Activated.")
    time.sleep(1)

    print("Opening Telegram Bot for File Password Cracking...")
    url = "https://t.me/Dx_hack69_bot"

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
    FPC_cracker()
