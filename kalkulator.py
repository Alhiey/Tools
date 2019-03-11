
#!usr/bin/env python
# © Copyright by Al
#Author:Al gans
print('''.        +--------++---------+--------+
         |.                           |
         |.K A L K  U  L  A  T   O  R |
         |.                           |
         +----------++-------------+--+
''')
print ('Author:Al gans')
print ('\n')
def add(num1,num2):
   return num1 + num2

def subtract(num1,num2):
   return num1 - num2
   
def multiply(num1,num2):
   return num1 * num2
   
def divide(num1,num2):
    return num1 / num2
    
print(' \033[95m Masukan Nomermu cok!\n'
	     '1.tambah\n'
	     '2.kurang\n'
	     '3.kali\n'
	     '4.bagi\n')
	     
select = input ('\033[92m pilih operator dari 1,2,3,4: ')
siji = int(input('\033[93m pilih angka pertama cok=>: '))
loro = int(input('pilih angka ke dua cok=>: '))

if select == '1':
   print(siji,'+',loro,'=',
               add(siji,loro))

elif select == '2':
     print(siji,'-',loro,'\033[91m jumlah =',
           subtract(siji,loro))

elif select == '3' :
     print(siji,'*',loro,'=',
          multiply(siji,loro))

elif select == '4':
     print(siji,'/',loro,'=',
          divide(siji,loro))
else:
    print('Kurang crott cok')
    
