import sys

def main():
    print(sys.argv, file=sys.stderr)

    if len(sys.argv) < 5:
        print("Usage: python app.py --name <bot_name> --author <author_name>", file=sys.stderr)
        exit(1)

    __name_arg = sys.argv[1]

    if __name_arg != '--name':
        print("Usage: python app.py --name <bot_name> --author <author_name>", file=sys.stderr)
        exit(1)

    bot_name = sys.argv[2]

    __author_arg = sys.argv[3]

    if __author_arg != '--author':
        print("Usage: python app.py --name <bot_name> --author <author_name>", file=sys.stderr)
        exit(1)
        
    author_name = sys.argv[4]

if __name__ == '__main__':
    main()