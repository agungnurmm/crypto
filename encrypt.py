from cryptography.fernet import Fernet 

def start():
    file = open("kunci.txt", "rb")
    key = file.read()
    file.close()

    with open("pesan.txt", "rb") as f:
        data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

    with open("pesanencrypted.txt", "wb") as f:
        f.write(encrypted)

if __name__ == '__main__':
    start()  