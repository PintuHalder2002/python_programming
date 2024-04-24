'''terminal pyshell code
>>> f=open('mytext.txt','w')
>>> f.write('pintu')
5
>>> f.write('PYTHON IIT MADRAS')
17
>>> f.close()
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> x=open('mytext.txt','r')
>>> s=x.read
>>> print(s)
<built-in method read of _io.TextIOWrapper object at 0x00000253DDAEB920>
>>> s=x.read()
>>> print(s)
pintuPYTHON IIT MADRAS
>>> x.close()
>>> x.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.'''

