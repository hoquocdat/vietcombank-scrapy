import scrapy


class LoginForm(scrapy.Item):
    captcha_guid = scrapy.Field()
    session_id = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()