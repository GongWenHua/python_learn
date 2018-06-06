import chardet

data1 = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data1))

data2 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data2))

data3 = 'Just do it'.encode('utf-8')
print(chardet.detect(data3))
