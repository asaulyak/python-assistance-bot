from display import StylizedElements


class Paginator:
    '''
    Class for pagination
    '''
    def __init__(self, items: list):
        '''
        Constructor
        '''
        self.__records_cursor = 0
        self.items = items

    @property
    def records_cursor(self):
        '''
        Getter property cursor
        '''
        return self.__records_cursor

    @records_cursor.setter
    def records_cursor(self, value):
        '''
        Setter property cursor
        '''
        self.__records_cursor = value


    def show(self, text:str='',max_records = 5,):
        '''
        Method for pagination
        '''
        prev_text = '⬅️  Prev'
        next_text = 'Next ➡️'
        exit_text = '↩️  Exit'

        while True:
            start = self.records_cursor
            end = start + max_records if start + max_records <= len(self.items) else len(self.items)
            
            default_opt = [prev_text if start > 0 else None, next_text if end < len(self.items) \
                            else None, exit_text]

            options =[f"{self.items.index(opt) + 1}. {opt.name.value}"  for opt in self.items[start:end]]\
                    +   [option for option in default_opt if option] # +1 for index because index starts from 0 and in menu index starts from 1

            user_choice = StylizedElements.console_menu(text, options)
            match user_choice:
                case text if text == prev_text :
                    self.__records_cursor = start - max_records
                case text if text == next_text:
                    self.__records_cursor = end
                case text if text == exit_text:
                    return None
                case _:
                    return int(user_choice.split(".")[0]) - 1 # -1 for index because index starts from 0