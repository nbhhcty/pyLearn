#coding=utf-8
# from BaiduSearch.BaiduImageSearch import  BaiduImageSearch import BaiduImage
from BaiduImageSearch import BaiduImage
import sys

keyword = " ".join(sys.argv[1:])
save_path = "_".join(sys.argv[1:])

# testKeyWord = u'呵呵'
# bytes_out = testKeyWord.encode('utf-8')
# keyword = " ".join(bytes_out)
# save_path = "_".join(bytes_out)

if not keyword:
    print "亲，你忘记带搜索内容了哦~  搜索内容关键字可多个，使用空格分开"
    print "例如：python run.py 男生 头像"
else:
    print("保存路径 = " + save_path)
    search = BaiduImage(keyword, save_path=save_path)
    search.search()