import time
from selenium import webdriver
import smtplib

#todo 1: selenium setup
driver_path = '/Users/kyle/Developer/python/chromedriver' #PUT YOUR WEBDRIVER ADDRESS
EMAIL = "YOUR EMAIL"
PASSWORD = 'YOUR PASSWORD'
PROMISED_UP = 0
PROMISED_DOWN = 0
sel = webdriver.Chrome(driver_path)


#todo 2: Create the Bot Class
class InternetSpeedTwitterBot:
    def __init__(self, driver, **kw):
        self.driver = driver
        self.down = 0
        self.up = 0
        self.from_email = kw.get('from_email')
        self.password = kw.get('password')
        self.up_lim = float(kw.get('up_lim'))
        self.down_lim = float(kw.get('down_lim'))

    def get_speed(self):
        self.driver.get('https://www.speedtest.net/')
        go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(80)
        down_spd = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = float(down_spd.text)
        up_spd = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = float(up_spd.text)
        if self.up < self.up_lim or self.down < self.down_lim:
            print(f'Expected Upload: {self.up_lim}, actual: {self.up}')
            print(f"Expected Download: {self.down_lim} actual: {self.down}")
            self.send_email()

    def send_email(self):
        #assuming it's gmail
        handler = smtplib.SMTP('smtp.google.com')
            #Need to authenticate in gmail itself to allow proxy
        handler.login(self.from_email, self.password)
        handler.starttls()
        handler.sendmail(
            from_addr=self.from_email,
            to_addrs=self.to_email,
            msg='Subject: Internet Usage Problem\n\n'
                'Dear service provider, I would like to report that the internet service provided is not consistent with the '
                'speeds that were established in my contract.'
        )
        handler.quit()

#todo 3: Instantiate the class
bot = InternetSpeedTwitterBot(driver=sel,
                              from_email=EMAIL,
                              password = PASSWORD,
                              up_lim = PROMISED_UP,
                              down_lim = PROMISED_DOWN)
bot.get_speed()
