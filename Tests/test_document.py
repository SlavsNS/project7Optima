import unittest
from Core.document import Document
from Core.text import Heading, Paragraph

class TestDocument(unittest.TestCase):
    def setUp(self):
        self.document = Document()

    def test_add_element(self):
        heading = Heading("Title", 1)
        self.document.add_element(heading)
        self.assertEqual(len(self.document.elements), 1)

    def test_render_document(self):
        self.document.add_element(Heading("Title", 1))
        self.document.add_element(Paragraph("This is a paragraph."))
        expected_html = "<h1>Title</h1>\n<p>This is a paragraph.</p>"
        self.assertEqual(self.document.render(), expected_html)

if __name__ == "__main__":
    unittest.main()
