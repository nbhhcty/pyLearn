#coding=utf-8
import requests
import urllib
from lxml import etree
import re

# 获取梨视频视频地址
#1 获取视频id
#2 拼接完整URL
#3 获取视频播放地址
#4 下载视频

def download(url):
    # url='http://www.pearvideo.com/category_9'
    #获取页面源代码
    html = requests.get(url).text
    #把文本文件处理成可解析的对象
    html = etree.HTML(html)
    video_id = html.xpath('//div[@class="vervideo-bd"]/a/@href')

    # 获取页面中所有的div//
    starturl = 'http://www.pearvideo.com'
    #列表
    video_url=[]
    # 拼接完整url
    for id in video_id:
        newurl=starturl+'/'+id
        video_url.append(newurl)

    # 获取视频播放地址
    for playurl in video_url:
        # 一：获取页面源代码
        html=requests.get(playurl).text

        # 二：获取视频名称
        req='<h1 class="video-tt">(.*?)</h1>'
        pname=re.findall(req,html)
        print("视频名字:%s"%pname[0].encode('utf-8'))

        # 三：视频真正的播放url
        # 正则匹配 .*?匹配所有
        req = 'srcUrl="(.*?)"'
        # 增加效率的
        # req=re.compile(req)
        purl = re.findall(req, html)
        print("视频URL:%s" % purl[0].encode('utf-8'))

def downloadmore():
    n=12    
    while True:
        if n>48:
            # 跳出循环的
            return
        url = "http://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=9&start=%d"%n
        n+=12
        download(url)
downloadmore()