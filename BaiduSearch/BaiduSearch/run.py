#coding=utf-8
from BaiduSearch.BaiduImageSearch import BaiduImage

# keyword = " ".join(sys.argv[1:])
# save_path = "_".join(sys.argv[1:])

keyword = " ".join("1234")
save_path = "_".join("1234")

if not keyword:
    print "亲，你忘记带搜索内容了哦~  搜索内容关键字可多个，使用空格分开"
    print "例如：python run.py 男生 头像"
else:
    search = BaiduImage(keyword, save_path=save_path)
    search.search()