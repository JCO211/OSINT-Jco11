from cli.menu import show_menu
from modes.osint_mode import osint_mode
from modes.stress_mode import stress_mode
from modes.defense_mode import defense_mode


def main():
    while True:
        option = show_menu()

        if option == "1":
            osint_mode()
        elif option == "2":
            stress_mode()
        elif option == "3":
            defense_mode()
        elif option == "4":
            print("Saliendo del toolkit.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
