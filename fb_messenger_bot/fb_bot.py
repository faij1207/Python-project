import os
import time
import random
import undetected_chromedriver as uc # type: ignore
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv # type: ignore

# Load credentials
load_dotenv()
FB_EMAIL = os.getenv("FB_EMAIL")
FB_PASSWORD = os.getenv("FB_PASSWORD")

# Human-like delay
def human_delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))

# Set up stealth driver
options = uc.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 15)

# Anti-detection JavaScript injection
driver.execute_script("""
Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
window.navigator.chrome = { runtime: {} };
Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});
""")

# Go to Facebook and log in
driver.get("https://www.facebook.com/")
human_delay()

email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
pass_field = driver.find_element(By.ID, "pass")
email_field.send_keys(FB_EMAIL)
human_delay()
pass_field.send_keys(FB_PASSWORD)
human_delay()
pass_field.send_keys(Keys.RETURN)

# Wait for homepage to load
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
human_delay(5, 7)

# Go to Messenger
driver.get("https://www.facebook.com/messages")
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
human_delay(3, 5)

# Message details
friends_to_message = ["Faij Alam Ansari", "Rustam Ali"]
message_text = "Hello from my stealth bot!"

for friend in friends_to_message:
    try:
        print(f"Messaging {friend}...")

        # Find and use the Messenger search bar
        search_input = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Search Messenger"]')
        ))
        search_input.clear()
        search_input.send_keys(friend)
        human_delay(2, 3)
        search_input.send_keys(Keys.RETURN)
        human_delay(3, 4)

        # Find the message box
        message_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"]')
        ))
        message_box.click()
        human_delay()
        message_box.send_keys(message_text)
        human_delay()
        message_box.send_keys(Keys.RETURN)
        print(f"Sent message to {friend}")
        human_delay(2, 4)
    except Exception as e:
        print(f"Failed to message {friend}: {e}")
        human_delay(2, 4)

print("All messages sent. Closing browser.")
human_delay(5, 7)
driver.quit()
