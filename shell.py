#Imports
import sys
import os

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

def InitlizeOsDevelEnv():
    print("OS env chosen")
def InitlizeWebDevelEnv():
    print("web env chosen")

def InitlizeShellInDir():
    def getchoice():
        choice = input(">")
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        else:
            return 0
    

    os.system("clear")
    print("""
          \rChoose one of the options:\n\r
          \t 1. OS Developement environment\n\r
          \t 2. Website Development evironment\n\r""")
    choice = getchoice()
    if choice == 0:
        print("Not a actual option chosen")
        choice = getchoice()
        if choice == 0:
            print("Not a actual options was chosen exiting..")
            sys.exit(1)
    
    if choice == 1: 
        InitlizeOsDevelEnv()
    elif choice == 2:
        InitlizeWebDevelEnv()

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



