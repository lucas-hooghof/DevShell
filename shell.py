import sys
import os


class Shell:
    def __init__(self):
        pass  # no env tracking for now

    def initialize(self):
        os.system("clear")
        print("""
              \rChoose one of the options:\n\r
              \t 1. OS Development environment\n\r
              \t 2. Website Development environment\n\r""")
        choice = self._get_choice()
        
        if choice == 1:
            print("OS environment chosen")
        elif choice == 2:
            print("Web environment chosen")
        else:
            print("Not a valid option chosen. Exiting..")
            sys.exit(1)

    def _get_choice(self):
        choice = input(">")
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        else:
            return 0


def ParseCMDArguments() -> int:
    args = sys.argv
    argc = len(args)

    if argc < 2:
        return 0
    elif args[1] == "--help":
        return 3
    elif args[1] == "init":
        return 1
    elif args[1] == "run":
        return 2
    else:
        return 0


def main():
    shell = Shell()
    StartCmd = ParseCMDArguments()

    if StartCmd == 0:
        print(f"No command found!\nrun 'python3 {sys.argv[0]} --help'\nto see all possible commands! ")
    elif StartCmd == 1:
        shell.initialize()
    elif StartCmd == 2:
        print("Run functionality not yet implemented.")
    elif StartCmd == 3:
        print(
            f"All possible commands:\n"
            f"\t- --help  show all possible commands\n"
            f"\t- init    initialize shell in this directory\n"
            f"\t- run     run the shell that is initialized in this directory"
        )


if __name__ == "__main__":
    main()
