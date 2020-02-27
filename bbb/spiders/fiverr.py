# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from selenium import webdriver

class FiverrSpider(scrapy.Spider):
    name = 'fiverr'
    start_urls = ['https://www.example.com/']

    def parse(self, response):
        self.driver = webdriver.Chrome("C:\Users\Danial Taimoor\Desktop\chromedriver")
        self.driver2 = webdriver.Chrome("C:\Users\Danial Taimoor\Desktop\chromedriver")
        self.driver.get("https://www.bbb.org/us/category/aids-clinic")
        self.driver2.get("https://www.bbb.org/us/category/aids-clinic")
        self.logger.info("Sleeping for 3 seconds....")
        sleep(3)
        self.driver.find_element_by_xpath('//figcaption').click()
        self.driver2.find_element_by_xpath('//figcaption').click()

        all_links=self.driver.find_elements_by_xpath('//h3/a')
        for link in all_links:
            dic={}
            self.driver2.get(link.get_attribute('href'))
            phone=''
            company=''
            address=self.driver2.find_elements_by_xpath('//*[@class="dtm-address styles__DivLayoutWithIcon-sc-47rb2e-0 eRLStY"]/p')
            c_address = ''
            webaddress=''
            if len(address)>0:
                company = self.driver2.find_element_by_xpath('//h4').text
                for i in address:
                    c_address+=i.text
                w_address=self.driver2.find_elements_by_xpath('//*[@class="dtm-url styles__LinkStyled-sc-1yozr49-0 eyfwAI"]')
                if len(w_address)>0:
                    webaddress=w_address.pop().text
                phone=self.driver2.find_element_by_xpath('//*[@class="dtm-phone"]').text
                dic['Company Name']=company
                dic['Phone']=phone
                dic['Address']=c_address
                dic['Website']=webaddress
                for i in self.driver2.find_elements_by_xpath('//tr'):
                    header=i.find_element_by_xpath('./th').text
                    data=i.find_element_by_xpath('./td').text
                    dic[header]=data

            else:
                company=self.driver2.find_element_by_xpath('//*[@class="business-title"]').text
                phone=self.driver2.find_element_by_xpath('//*[@class="phone"]').text
                c_address=self.driver2.find_element_by_xpath('//*[@class="address"]').text
                webaddress=self.driver2.find_element_by_xpath('//*[@class="webaddress"]').text

                dic['Company Name'] = company
                dic['Phone'] = phone
                dic['Address'] = c_address
                dic['Website'] = webaddress
            print dic



