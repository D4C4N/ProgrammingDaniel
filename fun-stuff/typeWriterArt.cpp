// Puzzle on CodinGame.com
// https://www.codingame.com/training/easy/retro-typewriter-art

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

int main() {
  // Declaring a string variable and getting user input
  std::string userInput;
  getline(std::cin, userInput);
  
  // Creating a string stream from the user input string
  std::istringstream iss(userInput);
  
  // Creating a vector to store the substrings
  std::vector<std::string> substrings;

  // Iterate through each word in the stringstream and add it to the vector
  std::string word;
  while (iss >> word) {
    substrings.push_back(word);
  }

  // Looping through each element in the vector
  for (const auto& substring : substrings) {
    // Variable to check if the substring contains a letter or numbers only
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

        // Convert the numeric part to an integer
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