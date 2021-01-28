from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/kyle/Developer/python/chromedriver")
print("DO NOT CLOSE THE CHROME WINDOW")
link = input("Please paste TikTok link:\n")
while "tiktok.com" not in link:
    link = input("Please ensure TikTok is in your link:\n")

driver.get(link)

time.sleep(2)
install_tiktok = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[2]/span')
install_tiktok.click()


def share():
    share_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div/div[1]/div/div[3]/div/div/div[2]/div/div[3]/strong')
    time.sleep(1)
    driver.execute_script("arguments[0].click();", share_button)
    # share_button.click()

    copy_link = driver.find_element_by_xpath('//*[@id="tiktok-share"]/div/div/div[2]/div/div/div[1]/div')
    time.sleep(1)
    driver.execute_script("arguments[0].click();", copy_link)
    # copy_link.click()


for i in range(100000):
    print("Click", i+1)  # because it starts at 0
    share()
