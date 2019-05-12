# -*- coding: utf-8 -*-
import scrapy
from ..model.login import LoginForm


class VietcombankSpider(scrapy.Spider):
    name = 'vietcombank'
    allowed_domains = ['vietcombank.com.vn']
    root_url = 'https://www.vietcombank.com.vn'
    start_urls = ['https://www.vietcombank.com.vn/IBanking2015/']

    def parse(self, response):
        req_url_splitted = response.request.url.split("/")
        session_id = req_url_splitted[4]
        captcha = response.xpath('//*[@id="captchaImage"]/@src')
        captcha_guid = response.xpath('//*[@id="LoginForm"]/div[3]/div[2]/input/@value').extract_first()
        captcha_image = self.root_url + captcha.extract_first()
        yield LoginForm(session_id=session_id, captcha_guid=captcha_guid, file_urls=[captcha_image])
        # print(captcha_image)
        # yield scrapy.Request(captcha_image)
        pass

