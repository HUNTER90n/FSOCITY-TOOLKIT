import os 
import webbrowser

webbrowser.open('https://aboutus-seven.vercel.app/')
url = "https://aboutus-seven.vercel.app/"
os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
