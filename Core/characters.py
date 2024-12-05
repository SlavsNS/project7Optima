class Character:
    def __init__(self, name):
        self.name = name
        self.attributes = {}

    def add_attribute(self, key, value):
        self.attributes[key] = value

    def __str__(self):
        attributes = ", ".join(f"{k}: {v}" for k, v in self.attributes.items())
        return f"Character(name={self.name}, attributes={{{attributes}}})"


class CharacterManager:
    def __init__(self):
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
