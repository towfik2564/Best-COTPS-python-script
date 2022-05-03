import time
from helpers.scraper import Scraper
from selenium.webdriver.common.by import By

def cotps_login(scraper):
    with open('credential.txt') as f:
        code = f.readline().strip()
        phone = f.readline().strip()
        password = f.readline().strip()
    code = code
    phone = phone
    password = password

    scraper.element_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text')
    scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-input/div/input', code)
    scraper.element_click_by_xpath("//uni-button[contains(text(), 'Confirm')]")
    scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-input/div/input', phone)
    scraper.element_send_keys_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[7]/uni-input/div/input', password)
    scraper.element_click_by_xpath('//uni-button[contains(text(), "Log in")]')
    
if __name__ == '__main__':
    scraper = Scraper('https://cotps.com/#/pages/login/login?originSource=userCenter')
    cotps_login(scraper)
    scraper.element_click_by_xpath('//*[contains(text(), "Transaction hall")]')

    while True:
        scraper.driver.refresh()
        time.sleep(5)
        tBalance = scraper.driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[1]/uni-view[2]').text
        wBalance = scraper.driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]').text  
        delay = 10
        if float(wBalance) > 5:
            while float(wBalance) > 5:
                print(f'${wBalance} available to trade')
                scraper.element_click_by_xpath('//uni-button[contains(text(), "Immediate competition for orders")]')
                time.sleep(5)
                scraper.element_click_by_xpath('//uni-button[contains(text(), "Sell")]')
                time.sleep(5)
                scraper.element_click_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[8]/uni-view/uni-view/uni-button')
                time.sleep(5)
                print('Trade done')
                wBalance = scraper.driver.find_element(By.XPATH, '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view[2]/uni-view[2]').text  
        else:
            print(f'Insufficient balance \n Waiting {delay}second to refresh')
            time.sleep(delay)