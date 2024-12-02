from cryptography.fernet import Fernet 

def start():
    file = open("kunci.txt", "rb")
    key = file.read()
    file.close()

    with open("pesanencrypted.txt", "rb") as f:
        data = f.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

    with open("pesandecrypted.txt", "wb") as f:
        f.write(decrypted)

if __name__ == '__main__':
    start()  