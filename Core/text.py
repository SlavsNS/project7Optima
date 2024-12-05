class TextElement:
    def render(self):
        raise NotImplementedError("Subclasses should implement this!")

class Heading(TextElement):
    def __init__(self, text, level):
        self.text = text
        self.level = level

    def render(self):
        return f"<h{self.level}>{self.text}</h{self.level}>"

class Paragraph(TextElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        return f"<p>{self.text}</p>"

class List(TextElement):
    def __init__(self, items):
        self.items = items

    def render(self):
        list_items = "".join(f"<li>{item}</li>" for item in self.items)
        return f"<ul>{list_items}</ul>"
