import unittest
from CLI.commands import CommandInterface
from Core.document import Document

class TestCommandInterface(unittest.TestCase):
    def setUp(self):
        self.document = Document()
        self.interface = CommandInterface(self.document)
        self.interface.set_mode("text")

    def test_add_heading(self):
        self.interface.execute_command("add heading 1 Hello")
        self.assertEqual(len(self.document.elements), 1)
        self.assertEqual(self.document.elements[0].render(), "<h1>Hello</h1>")

    def test_add_paragraph(self):
        self.interface.execute_command("add paragraph This is a test paragraph.")
        self.assertEqual(len(self.document.elements), 1)
        self.assertEqual(self.document.elements[0].render(), "<p>This is a test paragraph.</p>")

    def test_remove_element(self):
        # Додаємо елемент перед видаленням
        self.interface.execute_command("add paragraph Test")
        self.assertEqual(len(self.document.elements), 1)
        self.interface.execute_command("rm 0")
        self.assertEqual(len(self.document.elements), 0)

    def test_remove_nonexistent_element(self):
        # Спроба видалити елемент з порожнього списку
        self.interface.execute_command("rm 0")
        self.assertEqual(len(self.document.elements), 0)

    def test_invalid_command(self):
        with self.assertLogs() as log:
            self.interface.execute_command("unknown command")
            self.assertIn("Unknown text command.", log.output[0])

if __name__ == "__main__":
    unittest.main()
