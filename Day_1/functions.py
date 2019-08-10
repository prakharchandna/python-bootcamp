import sys

def main():
    print('main')
    print(sys.argv, type(sys.argv))
    print(len(sys.argv))
    print(sys.argv[0])
    print(sys.argv[1])




if __name__ == '__main__':
    main()