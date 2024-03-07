import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

sites = {
    "Google":"https://www.google.com",
}

timeout = 10

def main():
    c = input()
    if c == "1":
        load_page(input(), init())
    else:
        google_search(init())

def load_page(url, d: webdriver.Firefox):
    d.get(url)
    time.sleep(timeout)
    save_page("", d.title, d.get_full_page_screenshot_as_png())

def google_search(d: webdriver.Firefox):
    t = str(time.time())
    print("Awaiting input...")
    d.get(sites["Google"])
    search(get_query(), d)
    time.sleep(timeout) # wait for page load
    save_page(d.page_source, d.title, d.get_full_page_screenshot_as_png())
    d.quit()

def search(query: str, d: webdriver.Firefox):
    elem = d.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)

def get_query():
    s = input()
    for _ in range(50):
        print("")
    return s

def save_page(src, t: str, img: bytes):
    if src != "":
        save(src)
    save_png("pages/"+t, img)

def save_png(title, data):
    with open(title+".png", "wb") as f:
        f.write(data)

def save(txt):
    txt = txt + "\n"
    with open("dump.html", "+w") as f:
        f.write(txt)

def debug(d: webdriver.Firefox):
    save_page(d.page_source, d.title, d.get_full_page_screenshot_as_png())

def init():
    op = webdriver.FirefoxOptions()
    op.add_argument("-headless")
    op.page_load_strategy = "eager"
    op.set_preference("javascript.enabled", True)
    driver = webdriver.Firefox(options=op)
    driver.implicitly_wait(timeout)
    driver.set_page_load_timeout(timeout)
    return driver

if __name__ == "__main__":
    main()
