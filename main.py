import time
from helpers.scraper import Scraper
from selenium.webdriver.common.by import By

def formatted_time(t, hours = False):
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    if hours:
        return '{:d}:{:02d}:{:02d}'.format(h, m, s)
    else: 
        return '{:02d}:{:02d}'.format(m, s)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60) 
        hours, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    print('Waiting is over')

def cotps_login(scraper):
    with open('credential.txt') as f:
        code = f.readline().strip()
        phone = f.readline().strip()
        password = f.readline().strip()
    code = code
    phone = phone
    password = password
    print('Opening browser')
    scraper.element_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text')
    scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-input/div/input', code)
    scraper.element_click_by_xpath("//uni-button[contains(text(), 'Confirm')]")
    scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input', phone)
    scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input', password)
    scraper.element_click_by_xpath('//uni-button[contains(text(), "Log in")]')
    print('Logged in your account')

if __name__ == '__main__':
    trade_count = 0
    waiting_for_next_trade = 7800  #2hr15mins
    waiting_for_trade = 0  #5mins

    while True:
        scraper = Scraper('https://cotps.com/#/pages/login/login?originSource=userCenter')
        cotps_login(scraper)
        scraper.element_click_by_xpath('//*[contains(text(), "Transaction hall")]')
        time.sleep(1)
        trade_waiting_loop = 0

        while True:
            if trade_waiting_loop != 0:
                scraper.driver.refresh()

            tBalance = scraper.driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]').text
            wBalance = scraper.driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]').text  
            print(f'Transaction: {tBalance} || Wallet: {wBalance}')

            if float(wBalance) > 5:
                while float(wBalance) > 5:
                    print(f'${wBalance} available to trade')
                    scraper.element_click_by_xpath('//uni-button[contains(text(), "Immediate competition for orders")]')
                    scraper.element_click_by_xpath('//uni-button[contains(text(), "Sell")]')
                    scraper.element_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
                    wBalance = scraper.driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]').text  
                    print('Trade completed')
                trade_count += 1
                waiting_for_trade = 300
                trade_waiting_loop = 0
                print(f'Total trade done: {trade_count}times')
                break
            else:
                trade_waiting_loop += 1
                if waiting_for_trade == 0:
                    waiting_for_trade = 300
                time_str = formatted_time(waiting_for_trade)
                print(f'Insufficient balance \nWaiting {time_str} for expected balance')
                countdown(waiting_for_trade)
        
        time_str = formatted_time(waiting_for_next_trade, True)
        print(f'Waiting {time_str} for next trade')
        countdown(waiting_for_next_trade)