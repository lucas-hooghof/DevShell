import sys
import os
import zlib
import struct
import shutil

def templib():
    return zlib.Z_BEST_COMPRESSION


class Shell:
    def __init__(self):
        #All env data needed for initlization of the shell
        self.env_data: dict[str,str] = {}

    def clear(self):
        os.system("clear")
    def exit(self):
        sys.exit(1)

    #pack env data into a bytes 
    def packos(self) -> bytes:
        #make this pack all the env_data
        return struct.pack("10s20s20s10s10s30s", self.env_data["boot_type"].encode(), self.env_data["arch"].encode(), self.env_data["bootloader"].encode(), self.env_data["assembler"].encode(),self.env_data["cross_compilers"].encode(),self.env_data["compiler"].encode())

    #unpack bytes to env data
    def unpackos(self,envbytes: bytes) -> dict[str,str]:
        boot_type, arch, bootloader, assembler,cross_compilers, compiler = struct.unpack("10s20s20s10s10s30s", envbytes)
        return {
            "boot_type": boot_type.decode().strip('\x00'),
            "arch": arch.decode().strip('\x00'),
            "bootloader": bootloader.decode().strip('\x00'),
            "assembler": assembler.decode().strip('\x00'),
            "cross_compilers": cross_compilers.decode().strip('\x00'),
            "compiler": compiler.decode().strip('\x00')
        }


    def _OsDevEnvGen(self):
        self.clear()
        print("OS environment chosen")
        print("""
              \rBoot type:\n\r
              \t 1. Legacy (16-bit x86 x64)\n\r
              \t 2. UEFI   (Expecting x64)\n\r
              \t 3. Hybrid (Expecting x64 and From scratch bootloader)\n\r""")
        choice = int(input(">"))
        if choice == 1:
            self.clear()
            print("Legacy")
            self.env_data["boot_type"] = "legacy"
            print("""
              \rArchitecture:\n\r
              \t 1. 16-bit\n\r
              \t 2. 32-bit\n\r
              \t 3. 64-bit\n\r""")
            choice = int(input(">"))
            if choice == 1:
                print("Legacy 16-bit")
                self.env_data["arch"] = "16-bit"
            elif choice == 2:
                print("Do you also want to support 64-bit? (y/n)")
                choice = input(">")
                if choice == "y":
                    print("Legacy 32-bit and 64-bit")
                    self.env_data["arch"] = "32-bit, 64-bit"
                else:
                    print("Legacy 32-bit only")
                    self.env_data["arch"] = "32-bit"
            elif choice == 3:
                print("Do you also want to support 32-bit? (y/n)")
                choice = input(">")
                if choice == "y":
                    print("Legacy 32-bit and 64-bit")
                    self.env_data["arch"] = "32-bit, 64-bit"
                else:
                    print("Legacy 64-bit only")
                    self.env_data["arch"] = "64-bit"

            # Ask for bootloader Choice
            print("""
              \rBootloader:\n\r
              \t 1. GRUB2\n\r
              \t 2. From scratch\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["bootloader"] = "grub2"
            elif choice == 2:
                self.env_data["bootloader"] = "from_scratch"

            # Ask for assembler choice
            print("""
              \rAssembler:\n\r
              \t 1. NASM\n\r
              \t 2. FASM\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["assembler"] = "nasm"
            elif choice == 2:
                self.env_data["assembler"] = "fasm"

            #Ask if the shell should compile the cross compilers
            print("Should the shell compile the cross compilers for after bootloader? will take up storage and time depending on system using cores/2 for make -j (y/n)")
            choice = input(">")
            if choice == "y":
                self.env_data["cross_compilers"] = "y"
            else:
                self.env_data["cross_compilers"] = "n"
        elif choice == 2:
            #UEFI ask which compiler
            self.env_data["boot_type"] = "uefi"
            self.env_data["arch"] = "64-bit"

            print("""
              \rBootloader:\n\r
              \t 1. Limine\n\r
              \t 2. From scratch\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["bootloader"] = "Limine"
            elif choice == 2:
                self.env_data["bootloader"] = "from_scratch"
            self.clear()
            print("""
              \rAssembler:\n\r
              \t 1. NASM\n\r
              \t 2. FASM\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["assembler"] = "nasm"
            elif choice == 2:
                self.env_data["assembler"] = "fasm"

            print("Should the shell compile the cross compilers for after bootloader? will take up storage and time depending on system using cores/2 for make -j (y/n)")
            choice = input(">")
            if choice == "y":
                self.env_data["cross_compilers"] = "y"
            else:
                self.env_data["cross_compilers"] = "n"

            print("""
              \rCompiler:\n\r
              \t 1. Clang\n\r
              \t 2. x86_64-w64-mingw32-gcc\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["compiler"] = "clang"
            elif choice == 2:
                self.env_data["compiler"] = "x86_64-w64-mingw32-gcc"
        elif choice == 3:
            #UEFI and BIOS ask which compiler and asmbler
            self.env_data["boot_type"] = "hybrid"
            self.env_data["arch"] = "64-bit"
            self.env_data["bootloader"] = "from_scratch"
            # Ask for assembler choice
            print("""
              \rAssembler:\n\r
              \t 1. NASM\n\r
              \t 2. FASM\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["assembler"] = "nasm"
            elif choice == 2:
                self.env_data["assembler"] = "fasm"

            #Ask if the shell should compile the cross compilers
            print("Should the shell compile the cross compilers for after bootloader? will take up storage and time depending on system using cores/2 for make -j (y/n)")
            choice = input(">")
            if choice == "y":
                self.env_data["cross_compilers"] = "y"
            else:
                self.env_data["cross_compilers"] = "n"

            #Ask if clang or x86_64-w64-mingw32-gcc for UEFI bootloader using the same as the asmbler print question
            print("""
              \rCompiler:\n\r
              \t 1. Clang\n\r
              \t 2. x86_64-w64-mingw32-gcc\n\r""")
            choice = int(input(">"))
            if choice == 1:
                self.env_data["compiler"] = "clang"
            elif choice == 2:
                self.env_data["compiler"] = "x86_64-w64-mingw32-gcc"
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
              \t 1. OS Development environment (linux only)\n\r
              \t 2. Website Development environment\n\r""")
        choice = self._get_choice()
        
        if choice == 1:
            self._OsDevEnvGen()
            if self.env_data["cross_compilers"] == "y":
                self.env_data["cross_compilers"] = "y"
        elif choice == 2:
            self._WebDevEnvGen()
        else:
            print("Not a valid option chosen. Exiting..")
            sys.exit(1)

        print("Building Shell....")
        if os.path.exists("./shell"):
            shutil.rmtree("./shell")
        os.mkdir("./shell")
        with open("./shell/conf.bin","wb") as conf:
            # Maybe later when done conf.write(zlib.compress(self.packos()))
            conf.write(self.packos())

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
