class Paginator:
    def __init__(self, items: list):
        self.__records_cursor = 0
        self.items = items

    @property
    def records_cursor(self):
        return self.__records_cursor


    def show(self, reset_cursor = False, max_records = 5):
        if reset_cursor:
            self.__records_cursor = 0

        start = self.__records_cursor
        end = start + max_records

        for i, item in enumerate(self.items[start:end]):
            print(f'[{i + start}] {str(item)}')


        self.__records_cursor = end