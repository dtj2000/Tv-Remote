from remote import create_remote

from tv import Television

def main():
    # Television 1

    tv_1 = Television()
    create_remote(tv_1)
    tv_1.power()
    print(tv_1)             # TV status: Power = True, Channel = 0, Volume = 0


if __name__ == '__main__':
    main()