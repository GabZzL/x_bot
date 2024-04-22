from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# options to don't close the windows
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# your X information account
EMAIL = "example@gmail.com"
PASSWORD = "example"


# A class to get your current internet speed and post on X
class InternetSpeedTwitterBot:
    def __init__(self):
        # your promised down speed
        self.PROMISED_DOWN = 50
        # your promised up speed
        self.PROMISED_UP = 5
        self.USER_DOWN = ""
        self.USER_UP = ""
        # speedtest url
        self.SPEED_URL = "https://www.speedtest.net/es"
        # X url
        self.X_URL = "https://twitter.com"
        self.TEXT = ""

    # method to get your speed information
    def speed_test(self):
        # open the speedtest window
        driver.get(url=self.SPEED_URL)
        speed_button = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                           '/div[1]/a')
        speed_button.click()
        # set the time to wait for the speedtest to complete the test
        sleep(60)
        # get the values and convert into a float
        up_result = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div'
                                                        '[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.USER_DOWN = float(up_result.text)
        down_result = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                          'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]'
                                                          '/span')
        self.USER_UP = float(down_result.text)
        print(f"User speed down: {self.USER_DOWN}, type: {type(self.USER_DOWN)}")
        print(f"User speed up: {self.USER_UP} type: {type(self.USER_UP)}")
        # send a message depending if your speed was like your internet provider promised you
        if self.USER_DOWN < self.PROMISED_DOWN or self.USER_UP < self.PROMISED_UP:
            self.TEXT = (f"Dear internet company, why my internet only have {self.USER_DOWN}down/{self.USER_UP}up,"
                         f" but i'm paying for a service of {self.PROMISED_DOWN}down/{self.PROMISED_UP}up")
        else:
            self.TEXT = "Thanks internet company, my service is working fine"

    # method to post on X
    def post_x(self, email, password):
        # open the X window
        driver.get(url=self.X_URL)
        sleep(10)
        # process to log on X
        session_button = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]'
                                                             '/div[1]/div/div[3]/div[5]/a')
        session_button.click()
        sleep(10)
        email_input = driver.find_element(By.XPATH,
                                          value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                                'div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(email, Keys.ENTER)
        sleep(10)
        password_input = driver.find_element(By.XPATH,
                                             value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/'
                                                   'div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/'
                                                   'div[2]/div[1]/input')
        password_input.send_keys(password, Keys.ENTER)
        sleep(10)
        text_input = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
                                                         '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/'
                                                         'div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/'
                                                         'div/div/div[2]/div/div/div/div')
        # write the text to post, the text come from the previous method
        text_input.send_keys(self.TEXT)
        sleep(5)
        # click the post button
        post_button = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
                                                          '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div'
                                                          '[2]/div/div/div/div[3]')
        post_button.click()


# Create a new object to use both classes
speed = InternetSpeedTwitterBot()
speed.speed_test()
speed.post_x(EMAIL, PASSWORD)

