from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_py

def wordle_solver(word_to_guess):
    driver = webdriver.Chrome()

    try:
        driver.get("https://wordleunlimited.org/")
        time.sleep(2)
        input_field = driver.find_element("id", "guess")
        input_field.send_keys((word_to_guess))
        input_field.send_keys(Keys.RETURN)
        time.sleep(3)
        result = driver.find_element("id", "result").text
        return result
    finally:
        driver.quit()

if __name__ == "__main__":
    word_to_guess = "crane"

    result = wordle_solver(word_to_guess)

    print(f"Result: {result}")

