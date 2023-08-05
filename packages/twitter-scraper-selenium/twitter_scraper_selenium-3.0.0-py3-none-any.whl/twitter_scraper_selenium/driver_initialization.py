#!/usr/bin/env python3

from seleniumwire import webdriver
# to add capabilities for chrome and firefox, import their Options with different aliases
from selenium.webdriver.chrome.options import Options as CustomChromeOptions
from selenium.webdriver.firefox.options import Options as CustomFireFoxOptions
# import webdriver for downloading respective driver for the browser
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from fake_headers import Headers
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import logging

logging.getLogger().setLevel(logging.INFO)


class Initializer:

    def __init__(self, browser_name, headless, proxy=None, profile=None):
        self.browser_name = browser_name
        self.proxy = proxy
        self.headless = headless
        self.profile = profile

    def set_properties(self, browser_option):
        """adds capabilities to the driver"""
        header = Headers().generate()['User-Agent']
        if self.headless:
            browser_option.add_argument(
                '--headless')  # runs browser in headless mode
        if self.profile and self.browser_name.lower() == 'chrome':
            browser_option.add_argument(
                'user-data-dir={}'.format(self.profile))
        browser_option.add_argument('--no-sandbox')
        browser_option.add_argument("--disable-dev-shm-usage")
        browser_option.add_argument('--ignore-certificate-errors')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        browser_option.add_argument('--user-agent={}'.format(header))
        return browser_option

    def set_driver_for_browser(self, browser_name):
        """expects browser name and returns a driver instance"""
        # if browser is suppose to be chrome
        if browser_name.lower() == "chrome":
            browser_option = CustomChromeOptions()
            # automatically installs chromedriver and initialize it and returns the instance
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                logging.info("Using Proxy: {}".format(self.proxy))

                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                        options=self.set_properties(browser_option), seleniumwire_options=options)

            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.set_properties(browser_option))
        elif browser_name.lower() == "firefox":
            browser_option = CustomFireFoxOptions()
            if self.profile:
                logging.info('Loading Profile from {}'.format(self.profile))
                profile_path = webdriver.FirefoxProfile(self.profile)
                browser_option.profile = profile_path
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                logging.info("Using Proxy: {}".format(self.proxy))
                return webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()),
                                         options=self.set_properties(browser_option), seleniumwire_options=options)

            # automatically installs geckodriver and initialize it and returns the instance
            return webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), options=self.set_properties(browser_option))
        else:
            # if browser_name is not chrome neither firefox than raise an exception
            raise Exception("Browser not supported!")

    def init(self):
        """returns driver instance"""
        driver = self.set_driver_for_browser(self.browser_name)
        return driver
