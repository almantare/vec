import termcolor
import os


class Menu:

    def __init__(self) -> None:
        self.all_commands = []

    def add_command(self, command):
        if command.get_point() in map(lambda x: x.get_point(), self.all_commands):
            raise Exception(termcolor.colored('Пункты меню должны быть разными!', 'red'))
        self.all_commands.append(command)

    def run_command(self, point, with_clear=False):
        for command in self.all_commands:
            if command.get_point() == point:
                if with_clear:
                    os.system('clear')
                command.run()
                if with_clear:
                    os.system('clear')

    def print_menu_points(self):
        s1 = termcolor.colored('      [', 'red')
        s2 = termcolor.colored(']', 'red')
        print(s1 + termcolor.colored('1', 'blue') + s2, termcolor.colored('показать меню', 'green'))
        for command in self.all_commands:
            print(s1 + termcolor.colored(command.get_point(), 'blue') + s2, termcolor.colored(command.menu_name(), 'green'))
        print()