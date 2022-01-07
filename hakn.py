import threading
import time
import random
print('''
\033[2;31m███╗░░██╗░█████╗░████████╗
\033[2;32m████╗░██║██╔══██╗╚══██╔══╝
██╔██╗██║██║░░██║░░░██║░░░
\033[2;31m██║╚████║██║░░██║░░░██║░░░
\033[2;32m██║░╚███║╚█████╔╝░░░██║░░░
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░
\033[2;33m PANNER √ !
''')
g ='\033[2;31m' """	
							  	516   ALmalki	711
 ————﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉———
		 {tiktok \033[2;32m @l_711_i}
		 [\033[2;31mHA\033[2;32mcked\033[2;31m EM\033[2;32mail]
		 										
"""
print(g)
o = input( '\033[2;31m' 'PAssword:'' \033[2;32m')
if o == '711':
	time.sleep(1)
	print('.')
	time.sleep(1)
	print('..')
	time.sleep(1)
	print('...')
	time.sleep(2)
	gj = '''

[ 1 ] = \033[2;31mEM\033[2;32mail
[ 2 ] = \033[2;31mPA\033[2;32mssword
[ 3 ] = \033[2;31mEM\033[2;32mail \033[1;33m+ \033[2;31mPA\033[2;32mssword
'''
	print(gj)
	g = input('NUmber :' '\033[1;31m')
else:
	time.sleep(1.20)
	print('.')
	time.sleep(1.20)
	print('..')
	time.sleep(1.20)
	print('...')
	time.sleep(3)
	print( ' \033[2;31m' 'NOt PAss')

if g == '1':
	def Ant(data):
		nax = 10
		password = ' '
		while len (password)!=nax:
			gop=random.choice(data)
			password += gop
		return password
	data= '1234567890ASDadgxfyrinMPOIUchcgxkTREWQ'
	h=time.sleep(2)
	for i in range(1,21):
		time.sleep(1)
		print ('			',i)
		print ('\n \033[2;32m',Ant(data)+'\033[2;33m' '@gmali.com', '\033[2;31m' '\n ____516___711___')


#data = '1234567890ASDadgxfyrinMPOIUchcgxkTREWQ'
#h=time.sleep(2)
#for i in range(1,20):
#	time.sleep(1)
	#print ('			',i)
#	print ('\n \033[2;32m',bnt(data)+'\033[2;33m' '@gmali.com', '\033[2;31m' '\n ____516___711___')

if g== '2':
	def Ant(data):
		nax = 8
		password = ' '
		while len (password)!=nax:
			gop=random.choice(data)
			password += gop
		return password
	data= '1234567890zxcvbnmlkjhgfdsaqwertyuiop'
	h=time.sleep(2)
	for i in range(1,21):
		time.sleep(1)
		print ('			',i)
		print ('\n \033[2;32m',Ant(data)+'\033[2;33m', '\033[2;31m' '\n ____516___711___')
if g=='3':
	def unt(data):
		nax = 10
		password = ' '
		while len (password)!=nax:
			gop=random.choice(data)
			password += gop
		return password
		
	data= '1234567890ASDadgxfyrinMPOIUchcgxkTREWQ'
	h=time.sleep(2)
	for i in range(1,21):
		time.sleep(1)
		print ('			',i)
		print ('\n \033[2;32m',unt(data)+'\033[2;33m' '@gmali.com', '\033[2;31m' '\n ____516___711___')

	def knt(data):
		nax = 9
		password = ' '
		while len (password)!=nax:
			gop=random.choice(data)
			password += gop
		return password
	data= '1234567890zxcvbnmlkjhgfdsaqwertyuiop'
	h=time.sleep(2)
	for i in range(1,21):
		time.sleep(1)
		print ('			',i)
		print ('\n \033[2;32m',knt(data)+'\033[2;33m', '\033[2;31m' '\n ____516___711___')

		threading.Thread(target=unt,args=(data))
		threading.Thread(target=knt,args=(data))
