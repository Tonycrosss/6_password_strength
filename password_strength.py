import sys
import re
from string import punctuation


def load_passwords_black_list(filepath='./pass.txt'):
    with open(filepath, 'r') as black_list_passwords:
        return black_list_passwords.read().split('\n')


def password_strength_check(password):
    password_blacklist = load_passwords_black_list()
    strength_points = 0

    if re.search(r"\d", password):
        strength_points += 2
    if re.search(r"[a-z]",password) and re.search(r"[A-Z]", password):
        strength_points += 2
    if re.search(r"[{}]".format(punctuation), password):
        strength_points += 4
    if password in password_blacklist:
        strength_points = 1
    else:
        strength_points += 2
    return strength_points


def get_password_strength(strength_points):
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
    strength_points = password_strength_check(password)
    get_password_strength(strength_points)
