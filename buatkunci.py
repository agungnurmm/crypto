from cryptography.fernet import Fernet

def start():
    key = Fernet.generate_key()
    file = open('kunci.txt', 'wb')
    file.write(key)
    file.close()

if __name__ == '__main__':
    start()
