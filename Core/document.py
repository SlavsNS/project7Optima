class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        if not self.elements:
            return "Document is empty."
<<<<<<< HEAD
        return "\n".join(element.render() for element in self.elements)
=======
        return '\n'.join(element.render() for element in self.elements)
>>>>>>> cd50c83 (Initial commit)
