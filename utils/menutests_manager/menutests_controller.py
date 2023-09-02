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
            choice = menuview.main_menu_choices()
            index = choice.index(answer)

            match index:

                case 5:
                    running = False

                case 0:
                    # exit_code = pytest.main(["-qq"], plugins=[MyPlugin()])
                    args = ['tests/unit']
                    args.append('-vvv')
                    pytest.main(args)

                case 1:
                    args = ['tests/integration']
                    # args.append('-s')
                    args.append('-v')
                    pytest.main(list(args))

                case 2:
                    args = ['tests/fonctionnal/test_stories_edge.py']
                    pytest.main(args)

                case 3:
                    args = ['--cov=./gudlft --cov-report html']
                    pytest.main(args)
