from Core.document import Document
from CLI.commands import CommandInterface
from Core.display import Display

def main():
    document = Document()
    interface = CommandInterface(document)

    while True:
        mode = Display.input("Choose mode (text/chars/exit): ").lower()
        if mode == "exit":
            Display.output("Exiting program.")
            break
        elif mode in ["text", "chars"]:
            interface.set_mode(mode)
        else:
            Display.output("Unknown mode.")
            continue

        while True:
            command = Display.input("> ").strip()
            if command.lower() in ["back", "exit"]:
                Display.output("Returning to mode selection.")
                break
            interface.execute_command(command)

if __name__ == "__main__":
    main()
