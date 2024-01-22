// Puzzle on CodinGame.com
// https://www.codingame.com/training/easy/retro-typewriter-art

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

int main() {
  std::string userInput;
  getline(std::cin, userInput);
  
  std::istringstream iss(userInput);
  
  std::vector<std::string> substrings;

  std::string word;
  while (iss >> word) {
    substrings.push_back(word);
  }

  for (const auto& substring : substrings) {
    bool containsLetter = false;
    for (char c : substring) {
      if (std::isalpha(c)) {
        containsLetter = true;
        break;
      }
    }
    if (containsLetter == true) {
      if (substring == "nl") {
        std::cout << std::endl;
      } else {
        auto pos = std::find_if(substring.begin(), substring.end(), [](char c) {
          return !std::isdigit(c);
        });

        std::string numericPart = substring.substr(0, pos - substring.begin());
        std::string nonNumericPart = substring.substr(pos - substring.begin());

        int intValue = std::stoi(numericPart);

        for (int i = 0; i < intValue; i++) {
          if (nonNumericPart == "sp") {
            std::cout << " ";
          } else if (nonNumericPart == "bS") {
            std::cout << "\\";
          } else if (nonNumericPart == "sQ") {
            std::cout << "'";
          } else {
            std::cout << nonNumericPart;
          }
        }
      }
    } else {
      std::string numbers = substring.substr(0, substring.length() - 1);
      int intValue = std::stoi(numbers);
      char printChar = substring.back();

      for (int i = 0; i< intValue; i++) {
        std::cout << printChar;
      }
    }
  }
  
  return 0;
}