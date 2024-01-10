// Puzzle on CodinGame.com
// https://www.codingame.com/training/easy/ascii-art

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
  // Variable declaration
  int letterWidth, letterHeight;
  std::string inputText;
  std::string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // This alphabet string will help us to determine if a letter can be printed in ASCII

  // Declaring a two-dimensional vector table that will contain all the ASCII-Art-letters
  std::vector<std::vector<std::string>> letterTable;

  // Getting user input for the letter width, height and the text that needs to be printed
  std::cin >> letterWidth;
  std::cin >> letterHeight;
  std::cin.ignore();
  getline(std::cin, inputText);

  // Transforming the text input to be all uppercase
  std::transform(inputText.begin(), inputText.end(), inputText.begin(), ::toupper);

  // Resizing the two-dimensional vector-table to have "letterHeight" rows and 27 columns (as there are 27 ASCII-characters)
  letterTable.resize(letterHeight, std::vector<std::string>(27));

  // Loop for storing the ASCII characters in the vector-table
  for (int i = 0; i < letterHeight; i++) {  // The loop will run once for each row of the ASCII-characters
    int letterOffset = 0; // This variable will help us to store the substrings of each row in the correct index of our table.
    std::string row;
    getline(std::cin, row);

    for (int j = 0; j < 27; j++) {  // This loop will run 27 times as there are 27 characters which need to be stored. 
      letterTable[i][j] = row.substr(letterOffset, letterWidth);  // We are storing substrings that are "letterWidth" long
      letterOffset += letterWidth;  // The offset gets increased each time the loop runs.
    }
  }
  
  // Loop for printing the final ASCII Art
  for (int i = 0; i < letterHeight; i++) {  // The loop will run for each row of the ASCII-characters
    for (int j = 0; j < inputText.length(); j++) { // The nested loop will run for each character that needs to be printed 
      if (alphabet.find(inputText[j]) != std::string::npos) { // We are checking if the current char is part of the alphabet
        int letterIndex;
        letterIndex = alphabet.find(inputText[j]);  // Finding the index of the char
        std::cout << letterTable[i][letterIndex]; // Printing the corresponding index of the table
      } else {
        std::cout << letterTable[i][26]; // If the current char is not part of the alphabet, print a placeholder ASCII-art
      }
    }
    std::cout << std::endl;
  }

  return 0;
}