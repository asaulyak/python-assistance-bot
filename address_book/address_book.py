from collections import UserDict
from datetime import datetime, timedelta

from .record import Record
from display import StylizedElements,ColorsConstants


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


    def find(self, name, default = None) -> Record | None:
        return self.data.get(name.value, default)


    def find_by_name(self, name) -> list[Record]:
        return [record for record in self.data.values() if name.value.lower() in record.name.value.lower()]


    def find_by_phone(self, phone) -> list[Record]:
        return [record for record in self.data.values() if record.find_phone(phone)]


    def find_by_email(self, email) -> list[Record]:
        return [record for record in self.data.values() if record.find_email(email.value)]
    
    def find_by_query(self, query) -> list[Record]:
        return [record for record in self.data.values() if any(query in data for data in record.table_data())]

    def delete(self, name):
        del self.data[name.value]


    def is_empty(self):
        return len(self.data) == 0


    def to_list(self):
        return sorted(self.data.values(), key=lambda v: str(v.name))


    def get_upcoming_birthdays(self, days_to_birthday: int = 7):
        if days_to_birthday < 0:
            raise ValueError('Provide positive number of days to teh birthday')

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

            if 0 <= diff_days < days_to_birthday:
                congratulation_date = today + timedelta(days=diff_days)
                congratulation_date_week_day = congratulation_date.isoweekday()

                if congratulation_date_week_day in [6, 7]:
                    congratulation_date_shift = 8 - congratulation_date_week_day
                    congratulation_date += timedelta(days=congratulation_date_shift)

                upcoming_birthdays_this_week.append((congratulation_date.strftime("%d.%m.%Y"),congratulation_date.strftime("%A"),record.name.value))
        if len(upcoming_birthdays_this_week) > 0:
            return upcoming_birthdays_this_week

        else:
            StylizedElements.stylized_print(f'No upcoming birthdays in the next {days_to_birthday} day(s)', ColorsConstants.WARNING_COLOR.value)
        return []


    def __str__(self):
        if self.is_empty():
            return 'Addressbook is empty'
        return f'Addressbook:\n {'\n '.join(str(record) for record in self.to_list())}'
    
    def table_data(self):
        return [(record.name.value, '\n'.join(email.value for email in record.emails), '\n'.join(str(phone) for phone in record.phones), str(record.birthday) if record.birthday else '', str(record.address) if record.address else '') for record in self.to_list()]
     