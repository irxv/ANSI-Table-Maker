# ASCII Table Maker
# made by @irxv

import os, sys

BANNER = '''
\033[0;97mANSI Table Maker
By: @\033[0;34mirxv\033[0;97m
================='''
def main():
    # CLEAR SCREEN
    os.system("cls")
    
    # PRINTS BANNER
    print(BANNER)

    # INPUT NUMBER OF '═'
    NUMBEROFASCII = int(input("Long> "))

    # INPUT NUMBER OF ROWS
    NUMBEROFROWS = int(input("Number of Rows> "))

    # PRINTS ASCII CHARACTER x AMOUNT OF TIMES
    ASCII = "═" * NUMBEROFASCII
    FILLINSPACE = " " * NUMBEROFASCII

    print("╔"+ASCII+"╗")
    for x in range(NUMBEROFROWS):
        '''
        NUMBEROFROWS = amount of lines

        printing table line x amount of times.
        '''
        print("║"+FILLINSPACE+"║")
    print("╚"+ASCII+"╝")

if __name__ == "__main__":
    main()
