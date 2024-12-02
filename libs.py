from time import sleep

def welcome(title):
    style = '#' *(len(title)+6)

    print(style)
    print(f"## {title} ##")
    print(style)

def exit_program():
    print('program akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('program berhasil dihentikan')

if __name__ == '__main__':
    welcome()
    exit_program()