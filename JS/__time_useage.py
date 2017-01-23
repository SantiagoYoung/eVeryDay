# coding=utf-8
import time
# %a 英文星期的简写
# %A 英文星期的完整拼写
# %b 英文月份的简写
# %B 英文月份的完整拼写
# %c 本地当前的日期与时间
# %d 日期数,1-31之间
# %H 小时数,00-23之间
# %I 小时数,01-12之间
# %m 月份,01-12之间
# %M 分钟数,01-59之间
# %j 本年从第1天开始计数到当天的天数
# %w 星期数,0-6之间(0是周日)
# %W 当天属于本年的第几周,周一作为一周的第一天进行计算
# %x 本地的当天日期
# %X 本地的当前时间
# %y 年份,0-99之间
# %Y 年份的完整拼写

print time.localtime()
str = time.strftime('%Y-%m-%d %X', time.localtime())
print str

str = '2014/12/30'
str = time.strptime(str, '%Y/%m/%d')
print str





















