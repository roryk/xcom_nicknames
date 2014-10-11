from random import choice
import sys

ROLES = ["Support", "Heavy", "Assault", "Sniper"]
COUNTRIES = ["Am", "Rs", "Ch", "In", "Af", "Mx", "Ab",
             "En", "Fr", "Gm", "Au", "It", "Jp",
             "Is", "Es", "Gr", "Nw", "Ir", "Sk",
             "Du", "Sc", "Bg"]


def name2string(gender, nickname, country, firstname=False):
    if firstname:
        firstname = "m_arr%s%sFirstNames=%s\n" % (
	    country, gender.upper(), nickname)
        lastname = "m_arr%sLastNames=\n" % (country)
    else:
        firstname = "m_arr%s%sFirstNames=\n" % (country, gender.upper())
        lastname = "m_arr%sLastNames=%s\n" % (country, nickname)
    return (firstname, lastname)


# This one is ungenedered. Gives a firstname, lastname pair, with only
# lastname filled with the nickname supplied.
def name2string_lastname(gender, nickname, country):
    return name2string(gender, nickname, country)


# This one is gendered. Gives a firstname, lastname pair, with only
# firstname filled with the nickname supplied.
def name2string_firstname(gender, nickname, country):
    return name2string(gender, nickname, country, firstname=True)


# This one is gendered. Gives an XCOM nickname field, filled with the
# nickname supplied.
def name2string_nickname(gender, nickname, role, number):
    nstring = "m_arr%s%sNicknames[%s]=%s\n" % (
	gender.upper(), role, str(number), nickname)
    return nstring


def read_nicknames(in_file):
    nicknames = {"m": [], "f": []}
    with open(in_file) as in_handle:
        for line in in_handle:
            gender = line[0]
            nicknames[gender].append(line.split("=")[1].strip())
    return nicknames


def output_names(in_file, name2string_function=name2string_lastname):
    with open(in_file) as in_handle:
        for line in in_handle:
            for country in COUNTRIES:
                names = name2string_function(line[0], line.split("=")[1].strip(), country)
                map(sys.stdout.write, names)

def output_nicknames(nicknames):
    for role in ROLES:
        for gender in nicknames.keys():
            count = 0
            for nickname in nicknames[gender]:
                sys.stdout.write(name2string_nickname(gender, nickname,
                                                      role, count))
                count += 1


def main(in_file, to_generate):
    if to_generate == "nickname":
        nicknames = read_nicknames(in_file)
        output_nicknames(nicknames)
    elif to_generate == "last":
        output_names(in_file, name2string_lastname)
    elif to_generate == "first":
        output_names(in_file, name2string_firstname)
    else:
        print usage
        exit(1)

if __name__ == "__main__":
    usage ="""
usage: python xcom_nicknames.py nicknames_file {nickname,first,last}

	'nickname' outputs XCOM nicknames for all countries and classes.
	'first' outputs gendered first names without last names.
	'last' outputs last names without first names, ignoring gender.

If you want to have the names show up like on Beaglerush's videos use
'last'.
    """
    if len(sys.argv) < 3:
        print usage
        exit(1)

    main(sys.argv[1], sys.argv[2])
