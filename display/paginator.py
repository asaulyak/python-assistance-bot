from user_input import yes_no_question


class Paginator:
    def __init__(self, items: list):
        self.__records_cursor = 0
        self.items = items

    @property
    def records_cursor(self):
        return self.__records_cursor


    def show(self, reset_cursor = False, max_records = 5):
        self.__show(reset_cursor, max_records)

        items_to_show_exist = len(self.items) > self.records_cursor

        while items_to_show_exist:
            show_more = yes_no_question('Show more?')

            if not show_more:
                break

            self.__show(False, max_records)
            items_to_show_exist = len(self.items) > self.records_cursor


    def __show(self, reset_cursor, max_records):
        if reset_cursor:
            self.__records_cursor = 0

        start = self.__records_cursor
        end = start + max_records

        for i, item in enumerate(self.items[start:end]):
            print(f'[{i + start}] {str(item)}')


        self.__records_cursor = end