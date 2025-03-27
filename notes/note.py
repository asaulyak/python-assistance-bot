from notes import Tag
from notes.text import Text
from notes.title import Title


class Note:
    def __init__(self, title:Title, text: Text | None = None, tags:list[Tag] = []):
        self.title = title
        self.text = text
        self.tags = tags


    def set_title(self, title: Title):
        self.title = title


    def set_text(self, text: Text | None):
        self.text = text


    def add_tag(self, tag: Tag):
        self.tags.append(tag)


    def remove_tag(self, tag: Tag):
        self.tags.remove(tag)


    def __str__(self):
        return self.title.value
