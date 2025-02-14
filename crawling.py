from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from fake_useragent import UserAgent


ua = UserAgent(platforms='pc')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument(f'user-agent={ua.random}')
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://youtu.be/S7Bj0F88Iys?si=XlXDMlO8NQlx7K4W')
driver.maximize_window()
driver.implicitly_wait(12)

# try:
#     a = driver.find_element(By.CSS_SELECTOR, value='#content-text > span')
#     driver.execute_script("arguments[0].scrollIntoView();", a)
#     print(a.text)
# except NoSuchElementException:
#     b = driver.find_element(By.XPATH, value='//*[@id="dismiss-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
#     b.click()
#     time.sleep(7)
# finally:
#     pause = driver.find_element(By.XPATH, value='//*[@id="movie_player"]/div[31]/div[2]/div[1]/button')
#     pause.click()
#     time.sleep(4)
    # driver.execute_script("window.scrollBy(0, 500);")
# last_height = driver.execute_script("return document.body.scrollHeight")
# print(last_height)

while True:
    current_scroll_position = driver.execute_script("return window.scrollY")
    print(current_scroll_position)
    driver.execute_script("window.scrollBy(0, 500);")

    time.sleep(1)

    new_scroll_position = driver.execute_script("return window.scrollY")
    print(new_scroll_position)

    if new_scroll_position == current_scroll_position:
        print("Sudah mencapai bagian bawah halaman.")
        break

authors = driver.find_elements(By.CSS_SELECTOR, value='#author-text > span')
comments = driver.find_elements(By.CSS_SELECTOR, value='#content-text > span')

authors = [author.text for author in authors]
comments = [comment.text for comment in comments]

df = pd.DataFrame({
    'user_id': authors,
    'comment': comments
})

df.to_csv('raw/Volix.csv', index=False)
