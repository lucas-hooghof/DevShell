import sys
import os
import zlib

def templib():
    return zlib.Z_BEST_COMPRESSION


class Shell:
    def __init__(self):
        pass

    def clear(self):
        os.system("clear")
    def exit(self):
        sys.exit(1)


    def _OsDevEnvGen(self):
        self.clear()
        print("OS environment chosen")
        print("""
              \rBoot type:\n\r
              \t 1. Legacy (16-bit x86 x64)\n\r
              \t 2. UEFI   (Expecting x64)\n\r
              \t 3. Hybrid (Expecting x64)\n\r""")
        choice = int(input(">"))
        if choice == 1:
            #Legacy ask for arch and asmbler
            print("Legacy")
        elif choice == 2:
            #UEFI ask which compiler
            print("UEFI")
        elif choice == 3:
            #UEFI and BIOS ask which compiler and asmbler
            print("Hybrid")
        else:
            print(f"{choice} unknown choice exiting...")
            self.exit()
            
    def _WebDevEnvGen(self):
        self.clear()
        print("Web environment chosen")
        print("""
              \rChoose one of the options:\n\r
              \t 1. Javascript/Typescript\n\r
              \t 2. Python\n\r
              \t 3. HTML/CSS/js\n\r""")
        

    def initialize(self):
    
        print("""
              \rChoose one of the options:\n\r
              \t 1. OS Development environment\n\r
              \t 2. Website Development environment\n\r""")
        choice = self._get_choice()
        
        if choice == 1:
            self._OsDevEnvGen()
        elif choice == 2:
            self._WebDevEnvGen()
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
