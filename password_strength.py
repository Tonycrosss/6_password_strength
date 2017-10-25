import sys
import re


def get_password_strength(password):
    strength_points = 0
    password_blacklist = open('./pass.txt', 'r').read().split('\n')
    if re.search(r"\d", password):
        strength_points += 2
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        strength_points += 4
    if re.search(r"[@,#,$]", password):
        strength_points += 2
    if password in password_blacklist:
        strength_points = 1
        print('Your password is in password blacklist')
    else:
        strength_points += 2

    if strength_points == 1:
        print('Very weak password')
    elif 1 < strength_points < 5:
        print('Weak password')
    elif 5 < strength_points < 10:
        print('Strong password')
    elif strength_points == 10:
        print('Very cool password')


if __name__ == '__main__':
    password = sys.argv[1]
    get_password_strength(password)
