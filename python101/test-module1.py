Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Gundam'
print(name)
Gundam
type(name)
<class 'str'>
name.lower()
'gundam'
name.upper()
'GUNDAM'
friend = 'สมชาย'
print('สวัสดีสมชาย สบายดีไหม?')
สวัสดีสมชาย สบายดีไหม?
print('สวัสดี' + friend + ' สบายดีไหม?')
สวัสดีสมชาย สบายดีไหม?
money = 10
print('สมชายยืมเงิน 10
      
SyntaxError: incomplete input
print('สมชายยืมเงิน 10 บาท')
      
สมชายยืมเงิน 10 บาท
type(money)
      
<class 'int'>
pirnt(friend + 'ยืมเงิน ' + str(money) + ' บาท')
      
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pirnt(friend + 'ยืมเงิน ' + str(money) + ' บาท')
NameError: name 'pirnt' is not defined. Did you mean: 'print'?
print(friend + 'ยืมเงิน ' + str(money) + ' บาท')
      
สมชายยืมเงิน 10 บาท
print('{ }ยืมเงิน{ } บาท'.format(friend,money))
      
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('{ }ยืมเงิน{ } บาท'.format(friend,money))
KeyError: ' '
>>> print('{ }ยืมเงิน { } บาท'.format(friend,money))
...       
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print('{ }ยืมเงิน { } บาท'.format(friend,money))
KeyError: ' '
>>> print('{}ยืมเงิน {} บาท'.format(friend,money) )
...       
สมชายยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท')
...       
สมชายยืมเงิน 10 บาท
>>> money = 9999999999999999999999999999999999999999999999999999999999999999
...       
>>> print(f'{money:}')
...       
9999999999999999999999999999999999999999999999999999999999999999
>>> print(f'{money:,}')
...       
9,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999,999
>>> print(f'{money:,.2f}')
      
10,000,000,000,000,000,213,204,190,094,543,968,723,012,578,712,679,649,467,743,338,496.00
