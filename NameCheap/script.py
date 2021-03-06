from selenium import webdriver
from twocaptcha import TwoCaptcha
from webdriver_manager.chrome import ChromeDriverManager


class Automator:
    def __init__(self, inputParams):
        self.URL = 'https://support.namecheap.com/index.php?/Tickets/Submit/RenderForm'
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(self.URL)

        self.next = '//*[@id="department_13"]'
        self.abuseReports = '//*[@id="department_219"]'
        self.phishing = '//*[@id="department_237"]'
        self.radialButton = '//*[@id="maincorecontent"]/form[2]/div/div[2]/div/input'

        self.xpathFirstLastName = '//*[@id="maincorecontent"]/form[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]/input'
        self.xpathEmail = '//*[@id="maincorecontent"]/form[2]/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/input'
        self.xpathAbusiveDomain = '//*[@id="maincorecontent"]/form[2]/div/div[2]/table[3]/tbody/tr[1]/td[2]/input'
        self.xpathAbusiveURL = '//*[@id="maincorecontent"]/form[2]/div/div[2]/table[3]/tbody/tr[2]/td[2]/textarea'
        self.xpathTargetedWebsite = '//*[@id="maincorecontent"]/form[2]/div/div[2]/table[5]/tbody/tr/td[2]/input'
        self.xpathSubject = '//*[@id="ticketsubject"]'
        self.xpathBody = '//*[@id="ticketmessage"]'
        self.xpathTermsCheck = '// *[ @ id = "maincorecontent"] / form[2] / div / div[2] / label / input'
        self.xpathCaptchaTextArea = '//*[@id="g-recaptcha-response"]'
        self.xpathSubmit = '//*[@id="maincorecontent"]/form[2]/div/div[2]/div[6]/input[1]'

        self.firstLastName = inputParams['first-last-name']
        self.email = inputParams['email']
        self.abusiveDomain = inputParams['abusive-domain']
        self.abusiveURL = inputParams['abusive-url']
        self.targetedWebsite = inputParams['targeted-website']
        self.subject = inputParams['subject']
        self.body = inputParams['body']

    def formSubmit(self):
        # Page ==> 1
        self.browser.find_element_by_xpath(self.next).click()
        self.browser.find_element_by_xpath(self.abuseReports).click()
        self.browser.find_element_by_xpath(self.phishing).click()
        self.browser.find_element_by_xpath(self.radialButton).click()

        # Page ==> 2
        self.browser.find_element_by_xpath(self.xpathFirstLastName).send_keys(self.firstLastName)
        self.browser.find_element_by_xpath(self.xpathEmail).send_keys(self.email)
        self.browser.find_element_by_xpath(self.xpathAbusiveDomain).send_keys(self.abusiveDomain)
        self.browser.find_element_by_xpath(self.xpathAbusiveURL).send_keys(self.abusiveURL)
        self.browser.find_element_by_xpath(self.xpathTargetedWebsite).send_keys(self.targetedWebsite)
        self.browser.find_element_by_xpath(self.xpathSubject).send_keys(self.subject)
        self.browser.find_element_by_xpath(self.xpathBody).send_keys(self.body)
        self.browser.find_element_by_xpath(self.xpathTermsCheck).click()

        self.captchaHandler()

        self.browser.find_element_by_xpath(self.xpathSubmit).click()

        print('Form Submitted !!')

    def captchaHandler(self):
        element = self.browser.find_element_by_class_name("g-recaptcha-response")
        element = self.browser.execute_script("arguments[0].style.display = 'block'; return arguments[0];", element)
        token = self.generateToken()

        element.send_keys(token)
        element = self.browser.execute_script("arguments[0].style.display = 'none'; return arguments[0];", element)

    def generateToken(self):
        print("Generating Token.....")
        captcha = TwoCaptcha('a464e17395843472cfcf29502f14be1f')
        token = captcha.solve_captcha(site_key="6Lc_ilIUAAAAANld5QNB-AiX_HdommM2dxwxku3Q", page_url=self.URL)

        print("Token Generated !!")

        return token


formData = {
    'first-last-name': 'Name',
    'email': 'abc@example.com',
    'abusive-domain': 'domain',
    'abusive-url': 'domain@abc.com',
    'targeted-website': 'website1@example.com',
    'subject': 'This is an important subject !!',
    'body': 'This is Body !!'

}

a = Automator(inputParams=formData)
a.formSubmit()
