from selenium import webdriver
import requests


def check_status(url):
    response = requests.get(url)
    status = response.status_code
    if status in range(200, 400):
        print('Available URL!')
        new_browser = open_browser(url)
        return new_browser
    else:
        print('URL Not Found!')


pass


def open_browser(url):
    browser_type = 'wrong'
    while browser_type.lower() not in ['chrome', 'edge']:
        print('Make a preference: ')
        browser_type = input('Edge or Chrome: ')
        if browser_type.lower() == 'edge':
            driver_edge = webdriver.Edge(executable_path='./drivers/msedgedriver.exe')
            driver_edge.get(url)
            return driver_edge
        elif browser_type.lower() == 'chrome':
            driver_chrome = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
            driver_chrome.get(url)
            return driver_chrome
        else:
            print('Unknown Value')


pass

my_url = input('Enter a url: ')
new_status = check_status(my_url)
