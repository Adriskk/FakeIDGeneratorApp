from random import randrange
from random import choice
from faker import Faker
import datetime
# - FILES
from random_identity.data.data import *

fake = Faker()

minimum_age = 19
now = datetime.datetime.now()
current_year = now.year - minimum_age

years = []
year = 1940
for i in range(0, (current_year - 1940)):
    years.append(year)
    year += 1

# born_year = choice(years)


# age = now.year - born_year

# print(age)
# print(years)


def full_name():
    global fullname
    fullname = choice(first_names) + ' ' + choice(surnames)
    return fullname


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        if year % 400 == 0:
            return True
    elif year % 4 != 0:
        return False


def birthday():
    global born_year, born_month, born_day
    birthday_date = ''
    rand_month = choice(months)
    rand_year = choice(years)
    born_year = rand_year
    born_month = rand_month

    if rand_month != 'February':
        x = 29
        while len(days) < 30:
            days.append(str(x))
            x += 1
    else:
        if not leap_year(rand_year):
            days.remove('29')

    rand_day = choice(days)
    born_day = rand_day

    return rand_day + ' ' + rand_month + ' ' + str(rand_year)


def age():
    year_age = now.year - born_year

    if now.month > months.index(born_month):
        return year_age
    elif now.month <= months.index(born_month):
        if now.day > days.index(born_day):
            return year_age
        else:
            return year_age - 1


def phone_number():
    phone_num = ''
    for num in range(0, 10):
        number = choice(numbers)
        if num == 3 or num == 6:
            phone_num += '-'

        phone_num += number

    return phone_num


def email_address():
    email = ''

    chars = [
        '-',
        '_',
        '.',
        ''
    ]

    email_page = [
        '@gmail.com',
        '@yahoo.com',
        '@hotmail.com',
        '@aol.com'
    ]

    fullname_list = fullname.split()
    [name.lower() for name in fullname_list]

    email += fullname_list[0].lower() + choice(chars) + fullname_list[1].lower() + choice(chars) + choice(email_page)
    return email


def phone_nr():
    return "+ " + str(country_code) + " " + phone_number()


def address():
    return fake.address()


def identity():
    print("Full name: {}".format(full_name()))
    print("Birthday: {}".format(birthday()))
    print("Age: {}".format(age()))

    print("Phone number: {}".format('+' + str(country_code) + ' ' + phone_number()))
    print("Nationality: {}".format(nationality))
    print("Address: ")
    
    print(fake.address())
    print("Workplace: {}".format(choice(workers)))
    print("E-mail: {}".format(email_address()))


# identity()

