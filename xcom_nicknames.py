from random import choice
import sys

ROLES = ["Support", "Heavy", "Assault", "Sniper"]
COUNTRIES = ["Am", "Rs", "Ch", "In", "Af", "Mx", "Ab",
             "En", "Fr", "Gm", "Au", "It", "Jp",
             "Is", "Es", "Gr", "Nw", "Ir", "Sk",
             "Du", "Sc", "Bg"]


def name2string(gender, nickname, country):
    firstname = "m_arr%s%sFirstNames=\n" % (country, gender.upper())
    lastname = "m_arr%sLastNames=%s\n" % (country, nickname.capitalize())
    return (firstname, lastname)


def nickname2string(gender, nickname, role, number):
    nstring = "m_arr%s%sNicknames[%s]=%s\n" % (gender.upper(), role,
                                             str(number), nickname.capitalize)
    return nstring


def read_nicknames(in_file):
    nicknames = {"m": [], "f": []}
    with open(in_file) as in_handle:
        for line in in_handle:
            gender = line[0]
            nicknames[gender].append(line.split("=")[1].strip())
    return nicknames

def output_names(in_file):
    with open(in_file) as in_handle:
        for line in in_handle:
            for country in COUNTRIES:
                names = name2string(line[0], line.split("=")[1].strip(), country)
                map(sys.stdout.write, names)

def output_nicknames(nicknames):
    for role in ROLES:
        for gender in nicknames.keys():
            count = 0
            for nickname in nicknames[gender]:
                sys.stdout.write(nickname2string(gender, nickname,
                                                 role, count))
                count += 1


def main(in_file, to_generate):
    if to_generate == "nickname":
        nicknames = read_nicknames(in_file)
        output_nicknames(nicknames)
    elif to_generate == "first":
        output_names(in_file)
    else:
        print usage
        exit(1)

if __name__ == "__main__":
    usage = """usage: python xcom_nicknames.py nicknames_file nickname/last
    adding nickname will output nicknames. last will output as last names.
    gender is not respected for either ATM.
    """
    if len(sys.argv) < 3:
        print usage
        exit(1)

    main(sys.argv[1], sys.argv[2])
