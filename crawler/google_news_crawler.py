# coding=utf-8

import urllib.request
from optparse import OptionParser
from bs4 import BeautifulSoup
import sys
 
#開始
if __name__ == '__main__':
	url = None
	url = "https://news.google.com.tw/"
 
	if url is not None:
		#設置假的瀏覽器資訊
		headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
		#發送請求
		req = urllib.request.Request(url = url,headers=headers)
		page = urllib.request.urlopen(req)
		contentBytes = page.read()
		type = sys.getfilesystemencoding()	#讀取
		contentBytes = contentBytes.decode(type)#轉換成本地系統編碼
		print(contentBytes)
		
		#進行分割
		soup = BeautifulSoup(str(contentBytes), "html.parser")
		matches = soup.find_all("span", { "class" : "section-name" })
		#將資訊顯示出來
		print("Section Name : "+matches[0].string)
