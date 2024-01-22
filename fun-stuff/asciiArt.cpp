// Puzzle on CodinGame.com
// https://www.codingame.com/training/easy/ascii-art

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
  int letterWidth, letterHeight;
  std::string inputText;
  std::string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  std::vector<std::vector<std::string>> letterTable;

  std::cin >> letterWidth;
  std::cin >> letterHeight;
  std::cin.ignore();
  getline(std::cin, inputText);

  std::transform(inputText.begin(), inputText.end(), inputText.begin(), ::toupper);

  letterTable.resize(letterHeight, std::vector<std::string>(27));

  for (int i = 0; i < letterHeight; i++) {
    int letterOffset = 0;
    std::string row;
    getline(std::cin, row);

    for (int j = 0; j < 27; j++) {
      letterTable[i][j] = row.substr(letterOffset, letterWidth);
      letterOffset += letterWidth;
    }
  }
  
  for (int i = 0; i < letterHeight; i++) {
    for (int j = 0; j < inputText.length(); j++) {
      if (alphabet.find(inputText[j]) != std::string::npos) {
        int letterIndex;
        letterIndex = alphabet.find(inputText[j]);
        std::cout << letterTable[i][letterIndex];
      } else {
        std::cout << letterTable[i][26];
      }
    }
    std::cout << std::endl;
  }

  return 0;
}