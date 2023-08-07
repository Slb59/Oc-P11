import questionary


class MenuTestView:

    def __init__(self, manager):
        self.manager = manager

    def main_menu_choices(self) -> list:
        return [
                "Tests unitaires",
                "Tests d'intégration",
                "Tests fonctionnels",
                "Couverture de tests",
                "Tests de performances",
                "Quitter l'utilitaire"
            ]

    def display_welcome(self) -> None:
        text = "  Bienvenue dans le gestionnaire "
        text += "de tests pour l'application Gudlft"
        print(len(text) * '-')
        print(text)
        print(len(text) * '-')
        print('')

    def display_main_menu(self) -> str:
        print('')
        print(50 * '-')
        answer = questionary.select(
            "Que souhaitez-vous faire ?",
            choices=self.main_menu_choices()
        ).ask()
        return answer
