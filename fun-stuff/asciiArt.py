# Puzzle on CodinGame.com
# https://www.codingame.com/training/easy/ascii-art

letter_width = int(input())
letter_height = int(input())
input_text = input().upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_table = [['' for _ in range(27)] for _ in range(letter_height)]

for i in range(letter_height):
    letter_offset = 0
    row = input()
    for j in range(27):
        letter_table[i][j] = row[letter_offset: letter_offset + letter_width]
        letter_offset += letter_width

for i in range(letter_height):
    for j in range(len(input_text)):
        if input_text[j] in alphabet:
            letter_index = alphabet.index(input_text[j])
            print(letter_table[i][letter_index], end='')
        else:
            print(letter_table[i][26], end='')
    print()
