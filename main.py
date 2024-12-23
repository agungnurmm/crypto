from libs import welcome, exit_program
from tools import buatkunci
from tools import encrypt
from tools import decrypt
from tools import pesan

def menu():
    user_option = int(input(f"\nMenu Program :\n 1. Buat Kunci\n 2. Buat Pesan\n 3. Encrypt Pesan (AES)\n 4. Decrypt Pesan (AES)\n 5. Exit Program\n Silahkan Pilih: "))
    
    if user_option == 1:
        buatkunci.start()
        print('\nkunci telah dibuat, silahkan cek di direktori\n')
    elif user_option == 2:
        pesan.start()
        print('\nPesan encrypted telah dibuat, silahkan cek di direktori\n')
    elif user_option == 3:
        encrypt.start()
        print('\nPesan encrypted telah dibuat, silahkan cek di direktori\n')
    elif user_option == 4:
        decrypt.start()
        print('\nPesan decrypted telah dibuat, silahkan cek di direktori\n')

     
    if user_option == 5:
        exit_program()  
        
    
def main():
    welcome("Kriptografi dan Steganografi Project Enkipsi Crypto")
    menu()

if __name__ == '__main__':
    main()
   