import string
import random
import argparse

if __name__ == '__main__':
    def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
        pool = ''
        if upper:
            pool += string.ascii_uppercase

        if lower:
            pool += string.ascii_lowercase

        if digit:
            pool += string.digits

        if pun:
            pool += string.punctuation

        if pool == '':
            pool += string.ascii_lowercase

        return ''.join(random.choices(pool, k=length))


    parser = argparse.ArgumentParser()
    parser.add_argument('-len', help='your password length', type=int)
    parser.add_argument('-u', help='your password is upper', action='store_true')
    parser.add_argument('-l', help='your password is lower', action='store_true')
    parser.add_argument('-d', help='your password is digit', action='store_true')
    parser.add_argument('-p', help='your password is pun', action='store_true')
    args = parser.parse_args()

    if args.len or args.u or args.l or args.d or args.p:
        print(create_password(args.len, args.u, args.l, args.d, args.p))
    else:
        print(create_password(10))
