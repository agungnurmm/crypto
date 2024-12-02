def start():
    data = input(f"\nMasukan Pesan yang akan di Enkripsi :")
    file = open('pesan.txt', 'w')
    file.write(data)
    file.close()

if __name__ == '__main__':
    start()