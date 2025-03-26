from .title import Title
from .body import Body

class Note:
    def __init__(self):
        self.title = ''
        self.text = ''
        self.tags: list[str] = []

    def add_title(self, title: Title):
        self.title = title

    def add_body(self, body: Body):
        self.body = body