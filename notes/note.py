from notes import Tag
from notes.text import Text
from notes.title import Title


class Note:
    def __init__(self, title: Title, text: Text | None = None):
        self.title = title
        self.text = text
        self.tags = set()

    def set_title(self, title: Title):
        self.title = title

    def get_title(self):
        return self.title

    def set_text(self, text: Text | None):
        self.text = text

    def get_text(self):
        return self.text

    def add_tag(self, tag: Tag):
        self.tags.add(tag)

    def remove_tag(self, tag: Tag):
        self.tags.remove(tag)

    def table_data(self):
        return (
            self.title.value,
            self.text.value if self.text else "",
            ", ".join(tag.value for tag in self.tags),
        )

    def __str__(self):
        return self.title.value
