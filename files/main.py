import time
from helpers.scraper import Scraper
from helpers.functions import countdown, formatted_time, validate_machine
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    registered = validate_machine()
    if registered:
        print('This machine is licensed')
        trade_count = 0
        waiting_for_next_trade = 7800  #2hr15mins
        waiting_for_trade = 0  #5mins

        while True:
            scraper = Scraper('https://cotps.com/#/pages/login/login?originSource=userCenter')
            scraper.cotps_login()
            scraper.element_click_by_xpath('//*[contains(text(), "Transaction hall")]')
            time.sleep(2)
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
            print('Closing browser')
            scraper.driver.quit()
            print(f'Waiting {time_str} for next trade')
            countdown(waiting_for_next_trade)
    else:
        print('This machine is not licensed')
        print("Contact it's developer at fiverr: https://www.fiverr.com/share/p956eo")