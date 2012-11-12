from random import choice
import sys

ROLES = ["Support", "Heavy", "Assault", "Sniper"]


def nickname2string(gender, nickname, role, number):

    nstring = "m_arr%s%sNicknames[%s]=%s\n" % (gender.upper(), role,
                                             str(number), nickname)
    return nstring


def read_nicknames(in_file):
    nicknames = {"m": [], "f": []}
    with open(in_file) as in_handle:
        for line in in_handle:
            gender = line[0]
            nicknames[gender].append(line.split("=")[1].strip())
    return nicknames


def output_nicknames(nicknames):
    for role in ROLES:
        for gender in nicknames.keys():
            count = 0
            for nickname in nicknames[gender]:
                sys.stdout.write(nickname2string(gender, nickname,
                                                 role, count))
                count += 1


def main(in_file):
    nicknames = read_nicknames(in_file)
    output_nicknames(nicknames)

if __name__ == "__main__":
    main(sys.argv[1])
