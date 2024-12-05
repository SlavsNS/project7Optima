import requests

class GenshinAPI:
    BASE_URL = "https://genshin.jmp.blue"

    @staticmethod
    def fetch_characters():
        """Отримаємо список персонажів з API."""
        try:
            response = requests.get(f"{GenshinAPI.BASE_URL}/characters/all?lang=en")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка під час отримання персонажів: {e}")
            return []

    @staticmethod
    def fetch_weapons():
        """Отримуємо список зброї з API."""
        try:
            response = requests.get(f"{GenshinAPI.BASE_URL}/weapons/all?lang=en")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка під час отримання зброї: {e}")
            return []
