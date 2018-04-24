# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]

    UserAgent = {"User-Agent:":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2050.400 QQBrowser/9.5.10169.400"}

    def start_requests(self):
        return [Request("https://accounts.douban.com/login",callback=self.Login,meta={"cookiejar":1})]

    def Login(self, response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        url = "https://accounts.douban.com/login"
        print("正在保存验证码图片")
        captchapicfile = "F:/20_Python/2000_PythonData/SelfStudy/douban/douban/captcha.png"
        urllib.request.urlretrieve(captcha[0],filename = captchapicfile)
        print("打开图片文件，查看验证码，输入单词......")
        captcha_value = input()

        data = {
            "form_email":"XXXX",
            "form_password":"XXXX",
            "captcha-solution":captcha_value,
        }
        print("正在登陆中……")
        return [FormRequest.from_response(response,
                                          meta={"cookiejar":response.meta["cookiejar"]},
                                          headers = self.UserAgent,
                                          formdata = data,
                                          callback=self.crawlerdata,
                                         )]

    def crawlerdata(self,response):
        print("完成登录.........")
        title = response.xpath("/html/head/title/text()").extract()
        content2 = response.xpath("//meta[@name='description']/@content").extract()
        print(title[0])
        print(content2[0])
