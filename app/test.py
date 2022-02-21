import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def main(driver, wait, n):
    abc = "abcdefghijklmnopqrstuvwxyz"
    names = [""] * (n * 2)
    while (len(set(names)) < 2*n):
        for i in range(2*n):
            name = ""
            for j in range(4):
                name = name + abc[random.randint(0, 25)]
            names[i] = name


    driver.get("https://miiitomi.github.io/matching/")

    numbers = driver.find_elements(By.TAG_NAME, "input")
    for e in numbers:
        e.clear()
        e.send_keys(f"{n}")

    button = driver.find_element(By.XPATH, "//div[@id='number']/button[1]")
    button.click()

    time.sleep(3)

    for i in range(2 * n):
        name = driver.find_element(By.XPATH, f"//div[@id='man_name']/div[{i+1}]/input[1]")
        name.send_keys(names[i])

    button = driver.find_element(By.XPATH, "//div[@id='man_name']/button[1]")
    button.click()

    time.sleep(3)

    button = driver.find_element(By.XPATH, "//div[@id='app']/button[1]")
    button.click()

    time.sleep(3)



if __name__ == '__main__':
    # Selenium サーバーへ接続する。
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        options=webdriver.ChromeOptions()
    )
    # 任意のHTMLの要素が特定の状態になるまで待つ
    # ドライバとタイムアウト値を指定
    wait = WebDriverWait(driver, 10)

    # Googleにアクセス
    # driver.get("https://google.com")
    # "selenium"で検索
    # driver.find_element(By.NAME, "q").send_keys("selenium" + Keys.RETURN)
    # 1件目の検索結果を取得(描画されるまで待機)
    # first_result = wait.until(
    #     presence_of_element_located((By.CSS_SELECTOR, "h3")))
    # print(first_result.get_attribute("textContent"))

    try:
        main(driver, wait, n=5)
    except Exception as e:
        print(e)

    time.sleep(3)

    driver.quit()
