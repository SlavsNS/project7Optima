<<<<<<< HEAD
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
        self.interface.execute_command("add paragraph Test")
        self.assertEqual(len(self.document.elements), 1)
        self.interface.execute_command("rm 0")
        self.assertEqual(len(self.document.elements), 0)

    def test_remove_nonexistent_element(self):
        self.interface.execute_command("rm 0")
        self.assertEqual(len(self.document.elements), 0)

    def test_invalid_command(self):
        with self.assertLogs() as log:
            self.interface.execute_command("unknown command")
            self.assertIn("Unknown text command.", log.output[0])

if __name__ == "__main__":
    unittest.main()
=======
from Core.characters import CharacterManager
from Infra.api import GenshinAPI
from Core.text import CharacterTextRenderer
class CommandInterface:
    def __init__(self, document):
        self.document = document
        self.character_manager = CharacterManager()
        self.mode = None

    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode set to: {self.mode}")

    def execute_command(self, command):
        parts = command.split()
        if not parts:
            print("No command entered.")
            return

        if self.mode == "text":
            self.handle_text_commands(parts)
        elif self.mode == "chars":
            self.handle_char_commands(parts)
        else:
            print("Unknown mode. Please set mode to 'text' or 'chars'.")

    def handle_text_commands(self, parts):
        from Core.text import Heading, Paragraph, List  # Локальний імпорт
        if parts[0] == "print":
            print(self.document.render())
        elif parts[0] == "add":
            self.add_text_element(parts)
        elif parts[0] == "rm":
            self.remove_text_element(parts)
        else:
            print("Unknown text command.")

    def handle_char_commands(self, parts):
        if parts[0] == "create":
            if len(parts) > 1:
                self.character_manager.create_character(parts[1])
            else:
                print("Usage: create <name>")
        elif parts[0] == "add":
            if len(parts) > 3:
                self.character_manager.add_attribute(parts[1], parts[2], parts[3])
            else:
                print("Usage: add <name> <attribute> <value>")
        elif parts[0] == "show":
            self.character_manager.show_characters()
        else:
            print("Unknown character command.")

    def add_text_element(self, parts):
        from Core.text import Heading, Paragraph, List  # Локальний імпорт
        if len(parts) < 3:
            print("Usage: add <type> <args>")
            return

        element_type = parts[1]
        if element_type == "heading":
            if len(parts) < 4:
                print("Usage: add heading <level> <text>")
                return
            try:
                level = int(parts[2])
                text = " ".join(parts[3:])
                self.document.add_element(Heading(text, level))
                print("Heading added.")
            except ValueError:
                print("Level must be an integer.")
        elif element_type == "paragraph":
            text = " ".join(parts[2:])
            self.document.add_element(Paragraph(text))
            print("Paragraph added.")
        elif element_type == "list":
            items = parts[2:]
            self.document.add_element(List(items))
            print("List added.")
        else:
            print("Unknown element type.")

    def remove_text_element(self, parts):
        if len(parts) < 2 or not parts[1].isdigit():
            print("Usage: rm <index>")
            return
        index = int(parts[1])
        if 0 <= index < len(self.document.elements):
            self.document.elements.pop(index)
            print(f"Element at index {index} removed.")
        else:
            print("Invalid index.")

    def fetch_characters(self):
        data = GenshinAPI.fetch_characters()
        self.character_manager.load_from_api(data)
        print("Characters loaded from API.")

    def show_weapons(self):
        data = GenshinAPI.fetch_weapons()
        print("Weapons:")
        for weapon in data:
            print(f"- {weapon['name']} ({weapon.get('type', 'Unknown')})")

    def equip(self, char_name, weapon_name):
        char = self.character_manager.characters.get(char_name)
        if not char:
            print(f"Character {char_name} not found.")
            return
        char.add_attribute("Weapon", weapon_name)
        print(f"{char_name} equipped with {weapon_name}.")


        class CommandInterface:
            def __init__(self):
                self.character_manager = CharacterManager()

            def fetch_characters(self):
                """Завантажити персонажів з API."""
                data = GenshinAPI.fetch_characters()
                self.character_manager.load_from_api(data)
                print("Characters loaded from API.")

            def show_characters(self):
                """Виввести всіх персонажів."""
                for char in self.character_manager.characters.values():
                    print(CharacterTextRenderer.render_character(char))

            def fetch_weapons(self):
                """Завантажити та показати зброю."""
                data = GenshinAPI.fetch_weapons()
                print("Weapons:")
                for weapon in data:
                    print(f"- {weapon['name']} ({weapon.get('type', 'Unknown')})")
>>>>>>> cd50c83 (Initial commit)
