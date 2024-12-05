<<<<<<< HEAD
class Character:
    def __init__(self, name):
        self.name = name
        self.attributes = {}

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def __str__(self):
        attributes = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        return f"Character(name={self.name}, attributes={{{attributes}}})"
=======
import random

class Character:
    def __init__(self, name, description=None, rarity=None):
        # Ініціалізація персонажа з ім’ям, описом і рідкістю.
        self.name = name
        self.description = description
        self.rarity = rarity or random.randint(1, 5)
        self.attributes = {}

    @staticmethod
    def from_api_data(data):
        """Створюємо персонажа з даних API."""
        return Character(
            name=data.get("name", "Unknown"),
            description=data.get("description", "No description available"),
            rarity=data.get("rarity")
        )

    def add_attribute(self, key, value):
        """Додаємо атрибут персонажу."""
        self.attributes[key] = value

    def __str__(self):
        """ Представлення персонажа у вигляді рядка."""
        attributes = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        return f"Character(name={self.name}, rarity={self.rarity}, attributes={{ {attributes} }})"
>>>>>>> cd50c83 (Initial commit)


class CharacterManager:
    def __init__(self):
<<<<<<< HEAD
        self.characters = {}

    def create_character(self, name):
        if name in self.characters:
            print(f"Character with name '{name}' already exists.")
        else:
            self.characters[name] = Character(name)
            print(f"Character '{name}' created.")

    def add_attribute(self, name, key, value):
        if name not in self.characters:
            print(f"Character '{name}' does not exist.")
        else:
            self.characters[name].add_attribute(key, value)
            print(f"Added attribute '{key}: {value}' to character '{name}'.")

    def show_characters(self):
        if not self.characters:
            print("No characters available.")
        else:
            for char in self.characters.values():
                print(char)
=======
        """ Ініціалізація менеджера персонажів."""
        self.characters = {}

    def load_from_api(self, api_data):
        """Завантажуємо персонажів з API."""
        for char_data in api_data:
            char = Character.from_api_data(char_data)
            self.characters[char.name] = char

    def show_characters(self):
        """Вивводимо список персонажів."""
        for char in self.characters.values():
            print(char)
>>>>>>> cd50c83 (Initial commit)
