import unittest
from Core.text import Heading, Paragraph, List

class TestTextElements(unittest.TestCase):
    def test_heading_render(self):
        heading = Heading("Hello", 1)
        self.assertEqual(heading.render(), "<h1>Hello</h1>")

    def test_paragraph_render(self):
        paragraph = Paragraph("This is a test.")
        self.assertEqual(paragraph.render(), "<p>This is a test.</p>")

    def test_list_render(self):
        items = ["Item1", "Item2", "Item3"]
        lst = List(items)
        self.assertEqual(lst.render(), "<ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>")

if __name__ == "__main__":
    unittest.main()
