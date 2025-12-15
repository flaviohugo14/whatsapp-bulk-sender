import os
import random
import time
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

driver = webdriver.Chrome(options=chrome_options)

driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    },
)

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

delay = 40  # espera máxima
min_between_messages = 10
max_between_messages = 25


def human_sleep(min_sec=0.3, max_sec=0.9):
    time.sleep(random.uniform(min_sec, max_sec))


def human_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    human_sleep(0.2, 0.6)
    actions.click()
    actions.perform()


class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("****************  WHATSAPP BULK SENDER  ******************")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

print(style.YELLOW + "\nThis is your message-")
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number = len(numbers)
print(
    style.RED + "We found " + str(total_number) + " numbers in the file" + style.RESET
)

print("Once your browser opens up sign in to web whatsapp")
driver.get("https://web.whatsapp.com")
input(
    style.MAGENTA
    + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..."
    + style.RESET
)

for idx, number in enumerate(numbers, start=1):
    if not number:
        continue

    print(
        style.YELLOW
        + f"{idx}/{total_number} => Sending message to {number}."
        + style.RESET
    )

    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    sent = False

    for attempt in range(1, 4):
        try:
            driver.get(url)
            human_sleep(3, 6)

            send_btn = WebDriverWait(driver, delay).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar']"))
            )

            human_sleep(1, 2)
            human_click(driver, send_btn)

            sent = True
            print(style.GREEN + f"Message sent to: {number}" + style.RESET)
            break

        except Exception:
            print(
                style.RED
                + f"Failed ({attempt}/3) to send message to {number}"
                + style.RESET
            )
            human_sleep(1, 2)

    if sent:
        human_sleep(min_between_messages, max_between_messages)
