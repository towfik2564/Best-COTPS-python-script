import time
from helpers.scraper import Scraper
from helpers.notification import send_notifications
from helpers.functions import countdown, formatted_time, validate_machine

if __name__ == '__main__':
    try:
        registered = validate_machine()
        if registered:
            print('This machine is licensed')
            trade_count = 0
            waiting_for_next_trade = 7200  #2hr
            waiting_for_trade = 0  #2mins
            
            while True:
                scraper = Scraper('https://cotps.com/#/pages/login/login?originSource=userCenter')
                scraper.cotps_login()
                scraper.element_force_click_by_xpath('//*[contains(text(), "Transaction hall")]')
                time.sleep(3)
                trade_waiting_loop = 0

                while True:
                    if trade_waiting_loop != 0:
                        scraper.driver.refresh()

                    tBalance = scraper.get_balance('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]')
                    wBalance = scraper.get_balance('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]')  
                    print(f'Transaction: {tBalance} || Wallet: {wBalance}')        
                
                    if wBalance >= 5:
                        if tBalance < 1:
                            send_notifications("WALLET_ARRIVED")
                            while wBalance >= 5:
                                print(f'${wBalance} available to trade')
                                scraper.element_force_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-button')
                                scraper.element_force_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-view/uni-view/uni-view[6]/uni-button[2]')
                                scraper.element_force_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
                                wBalance = scraper.get_balance('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]')
                                print('Trade completed')
                            trade_count += 1
                            waiting_for_trade = 120
                            trade_waiting_loop = 0
                            send_notifications("TRADE_CYCLED")
                            print(f'Total trade done: {trade_count}times')
                            break
                        else: 
                            trade_waiting_loop += 1
                            if waiting_for_trade == 0:
                                waiting_for_trade = 120
                            time_str = formatted_time(waiting_for_trade)
                            print(f'Waiting {time_str} for remaining balance arrival')
                            countdown(waiting_for_trade)
                    else:
                        trade_waiting_loop += 1
                        if waiting_for_trade == 0:
                            waiting_for_trade = 120
                        time_str = formatted_time(waiting_for_trade)
                        print(f'Waiting {time_str} for expected balance arrival')
                        countdown(waiting_for_trade)
                
                time_str = formatted_time(waiting_for_next_trade, True)
                print('Closing browser')
                scraper.driver.quit()
                print(f'Waiting {time_str} for next trade')
                countdown(waiting_for_next_trade)
        else:
            print('This machine is not licensed')
            print("Contact it's developer at fiverr: https://www.fiverr.com/share/p956eo")
    except: 
        send_notifications("SCRIPT_STOPPED")
         