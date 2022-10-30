from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    birthday = input('Date of Birth: ')
    try:
        year, month, day = check_date(birthday)
    except:
        sys.exit('Invalid Date')
    date_birth = date(int(year), int(month), int(day))
    date_today = date.today()
    diff = date_today - date_birth
    total_minutes = diff.days * 24 * 60
    output = p.number_to_words(total_minutes, andword='')
    print(output.capitalize() + ' minutes')


def check_date(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split('-')
        return year, month, day


if __name__ == "__main__":
    main()
