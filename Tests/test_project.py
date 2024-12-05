from Core.text import Heading, Paragraph, List
from Core.characters import Character, CharacterManager
from Core.document import Document


# Test for Heading class
def test_heading_render():
    heading = Heading("Test Heading", 1)
    assert heading.render() == "<h1>Test Heading</h1>"

# Test for Paragraph class
def test_paragraph_render():
    paragraph = Paragraph("Test Paragraph")
    assert paragraph.render() == "<p>Test Paragraph</p>"

# Test for List class
def test_list_render():
    list_element = List(["item1", "item2", "item3"])
    assert list_element.render() == "<ul><li>item1</li><li>item2</li><li>item3</li></ul>"

# Test for Document class
def test_document_add_and_render():
    document = Document()
    heading = Heading("Title", 1)
    paragraph = Paragraph("Content")
    document.add_element(heading)
    document.add_element(paragraph)
    assert document.render() == "<h1>Title</h1>\n<p>Content</p>"

# Test for Character class
def test_character_attributes():
    character = Character("Hero")
    character.add_attribute("strength", "10")
    assert character.attributes["strength"] == "10"
    assert str(character) == "Character(name=Hero, attributes={strength: 10})"

# Test for CharacterManager class
def test_character_creation_and_attribute_assignment():
    manager = CharacterManager()
    hero = manager.create_character("Hero")
    manager.add_attribute("Hero", "strength", "10")

    assert "Hero" in manager.characters
    assert manager.characters["Hero"].attributes["strength"] == "10"

