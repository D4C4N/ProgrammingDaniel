# Puzzle on CodinGame.com
# https://www.codingame.com/training/easy/ascii-art

# Variable declaration
letter_width = int(input())
letter_height = int(input())
input_text = input().upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Declaring a two-dimensional list that will contain all the ASCII-Art-letters
letter_table = [['' for _ in range(27)] for _ in range(letter_height)]

# Loop for storing the ASCII characters in the list
for i in range(letter_height):
    letter_offset = 0
    row = input()
    for j in range(27):
        letter_table[i][j] = row[letter_offset: letter_offset + letter_width]
        letter_offset += letter_width

# Loop for printing the final ASCII Art
for i in range(letter_height):
    for j in range(len(input_text)):
        if input_text[j] in alphabet:
            letter_index = alphabet.index(input_text[j])
            print(letter_table[i][letter_index], end='')
        else:
            print(letter_table[i][26], end='')
    print()
