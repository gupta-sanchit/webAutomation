from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class CloudFlareReport:
    def __init__(self, inputParams):
        self.URL = 'https://www.cloudflare.com/abuse/form'
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(self.URL)

        self.xpathDropDown = '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div/div[1]'
        self.xpathPhishing = '/html/body/div[5]/ul/li[7]/a/span'
        self.xpathName = '//*[@id="Name"]'
        self.xpathEmail = '//*[@id="Email"]'
        self.xpathConfirmEmail = '//*[@id="EmailConfirm"]'
        self.xpathTitle = '//*[@id="Title"]'
        self.xpathCompanyName = '//*[@id="Company"]'
        self.xpathTelephone = '//*[@id="Tele"]'
        self.xpathEvidenceURL = '//*[@id="URLs"]'
        self.xpathLogs = '//*[@id="Infringement"]'
        self.xpathVideoID = '//*[@id="VideoIDs"]'
        self.xpathComments = '//*[@id="Comments"]'
        self.xpathSubmit = '//*[@id="abuse-submit"]'

        self.name = inputParams['name']
        self.email = inputParams['email']
        self.title = inputParams['title']
        self.companyName = inputParams['company-name']
        self.telephone = inputParams['telephone']
        self.evidenceURL = inputParams['evidence-url']
        self.logs = inputParams['logs']
        self.videoID = inputParams['videoID']
        self.comments = inputParams['comments']

    def formSubmit(self):
        self.browser.find_element_by_xpath(self.xpathDropDown).click()
        self.browser.find_element_by_xpath(self.xpathPhishing).click()

        # Filling Form Details
        self.browser.find_element_by_xpath(self.xpathName).send_keys(self.name)
        self.browser.find_element_by_xpath(self.xpathEmail).send_keys(self.email)
        self.browser.find_element_by_xpath(self.xpathConfirmEmail).send_keys(self.email)
        self.browser.find_element_by_xpath(self.xpathTitle).send_keys(self.title)
        self.browser.find_element_by_xpath(self.xpathCompanyName).send_keys(self.companyName)
        self.browser.find_element_by_xpath(self.xpathTelephone).send_keys(self.telephone)
        self.browser.find_element_by_xpath(self.xpathEvidenceURL).send_keys(self.evidenceURL)
        self.browser.find_element_by_xpath(self.xpathLogs).send_keys(self.logs)
        self.browser.find_element_by_xpath(self.xpathVideoID).send_keys(self.videoID)
        self.browser.find_element_by_xpath(self.xpathComments).send_keys(self.comments)

        self.browser.find_element_by_xpath(self.xpathSubmit).click()

        print("Reported !!")


details = {
    'name': 'ABC',
    'email': 'abc@example.com',
    'title': 'title',
    'company-name': 'XYZ',
    'telephone': '12345',
    'evidence-url': 'http://cloudflare.com',
    'logs': 'malware',
    'videoID': '',
    'comments': 'This is a report'

}

c = CloudFlareReport(inputParams=details)
c.formSubmit()
