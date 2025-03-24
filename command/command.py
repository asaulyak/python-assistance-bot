class Command:
    def __init__(self):
        pass


    @property
    def name(self):
        return 'empty'


    @property
    def aliases(self):
        return []


    def run(self, *args):
        pass
