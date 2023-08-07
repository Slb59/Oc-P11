import sys
import pytest

from .menutests_view import MenuTestView


class MenuTestManager:

    def __init__(self):
        ...

    def __str__(self) -> str:
        return "Gestion des tests pour l'application Gudlft"

    def run(self):

        menuview = MenuTestView(self)
        menuview.display_welcome()
        running = True

        while running:
            answer = menuview.display_main_menu()

            # quit
            if answer == menuview.main_menu_choices()[5]:
                running = False

            elif answer == menuview.main_menu_choices()[0]:
                # exit_code = pytest.main(["-qq"], plugins=[MyPlugin()])
                args = ['tests/unit']
                pytest.main(args)                 

            elif answer == menuview.main_menu_choices()[1]:
                args = ['tests/integration']
                pytest.main(args)                

            elif answer == menuview.main_menu_choices()[2]:
                args = ['tests/fonctionnal_edge']
                pytest.main(args)

            elif answer == menuview.main_menu_choices()[3]:
                args = ['--cov=gudlft --cov-report html']
                pytest.main(args)    