from modules.app import app
from modules.window import main_window
def main():
    try:
        main_window.show()
        app.exec()
    except Exception as error:
        print("Error:", error)
if __name__ == "__main__":
    main()
