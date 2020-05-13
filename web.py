import os
import  webbrowser


def open_facebook():
    webbrowser.open("https://facebook.com")

def open_google():
    webbrowser.open("https://google.com")

def close_browser():
    browserexe = "chrome.exe"
    os.system("taskkill /f /im " + browserexe)

