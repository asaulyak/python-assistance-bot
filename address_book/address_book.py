from collections import UserDict
from datetime import datetime, timedelta

from .record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


    def find(self, name, default = None) -> Record:
        return self.data.get(name.value, default)


    def delete(self, name):
        del self.data[name.value]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()

        upcoming_birthdays_this_week = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y")
            birthday_this_year = datetime(year=today.year, month=birthday.month, day=birthday.day).date()
            birthday_next_year = datetime(year=today.year + 1, month=birthday.month, day=birthday.day).date()

            diff_days_this_year = abs((birthday_this_year - today).days)
            diff_days_next_year = abs((birthday_next_year - today).days)
            diff_days = min(diff_days_this_year, diff_days_next_year)

            if 0 <= diff_days < 7:
                congratulation_date = today + timedelta(days=diff_days)
                congratulation_date_week_day = congratulation_date.isoweekday()

                if congratulation_date_week_day in [6, 7]:
                    congratulation_date_shift = 8 - congratulation_date_week_day
                    congratulation_date += timedelta(days=congratulation_date_shift)

                upcoming_birthdays_this_week.append(f'Congratulate {record.name.value} on {congratulation_date.strftime("%d.%m.%Y")}')

        return '\n'.join(birthday for birthday in upcoming_birthdays_this_week)


    def __str__(self):
        return f'Address Book:\n {'\n '.join(str(record) for record in self.data.values())}'