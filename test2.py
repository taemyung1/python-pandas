import webbrowser
from selenium import webdriver
import threading
count = 0


def web1():
    url = "https://smartstore.naver.com/dhkdldoswpdl/products/4609248541"
    webbrowser.open(url, new = 0)
    timer = threading.Timer(10, web1)
    timer.start()
    count += 1

    if count == 5:
        timer.cancel()
        print('stop')

