假设第一个字符串是最长公共头串prefix，
然后一个一个字符串去比较，若不符合就prefix= prefix[:-1](python特有的去尾方法)

python 特有的方法
str.startswith(str, beg=0,end=len(string));
