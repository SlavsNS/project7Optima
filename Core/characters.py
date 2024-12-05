import random

class Character:
    def __init__(self, name, description=None, rarity=None):
        """Ініціалізація персонажа з ім’ям, описом, і рідкістю."""
        self.name = name
        self.description = description
        self.rarity = rarity if rarity is not None else random.randint(1, 5)
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
        """Представлення персонажа у вигляді рядка."""
        attributes = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        return f"Character(name={self.name}, attributes={{{attributes}}})"

class CharacterManager:
    def __init__(self):
        self.characters = {}

    def create_character(self, name, description=None, rarity=None):
        if name not in self.characters:
            self.characters[name] = Character(name, description, rarity)
        return self.characters[name]

    def add_attribute(self, name, key, value):
        if name in self.characters:
            self.characters[name].add_attribute(key, value)
        else:
            raise ValueError(f"Character '{name}' not found in the manager.")

    def get_character(self, name):
        return self.characters.get(name, None)

    def show_characters(self):
        for name, character in self.characters.items():
            print(character)
