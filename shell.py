#Imports
import sys

# Wil return 0 for no command found 1 for initlize shell 2 run shell 3 help
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

def InitlizeShellInDir():
    pass

def RunShellInDir():
    pass

def main():
    StartCmd = ParseCMDArguments()

    if StartCmd == 0:
        print(f"No command found!\nrun 'python3 {sys.argv[0]} --help'\nto see all posible commands! ")
    elif StartCmd == 1:
        InitlizeShellInDir()
    elif StartCmd == 2:
        RunShellInDir()
    elif StartCmd == 3:
        print(
            f"All possible commands:\n"
            f"\t- --help  show all possible commands\n"
            f"\t- init    initialize shell in this directory\n"
            f"\t- run     run the shell that is initilized in this directory"
        )

if __name__ == "__main__":
    main()



