#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

std::string readFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Не вдалося відкрити файл: " << filename << std::endl;
        exit(EXIT_FAILURE);
    }
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    return content;
}

void writeFile(const std::string& filename, const std::string& content) {
    std::ofstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Не вдалося відкрити файл: " << filename << std::endl;
        exit(EXIT_FAILURE);
    }
    file << content;
    file.close();
}

bool matchesPattern(const std::string& word, const std::string& pattern) {
    size_t wordIndex = 0;
    size_t patternIndex = 0;

    while (wordIndex < word.length() && patternIndex < pattern.length()) {
        if (pattern[patternIndex] == '[') {
            if (patternIndex + 4 >= pattern.length()) return false; // Перевіряємо, чи довжина маски не перевищує 5 символів
            std::string range = pattern.substr(patternIndex + 1, 3); // Отримуємо діапазон символів метасимвола
            char startRange = range[0];
            char endRange = range[2];
            if (wordIndex >= word.length() || (word[wordIndex] < startRange || word[wordIndex] > endRange)) return false;
            wordIndex++;
            patternIndex += 5;
        } else if (wordIndex >= word.length() || pattern[patternIndex] != word[wordIndex]) {
            return false;
        } else {
            wordIndex++;
            patternIndex++;
        }
    }

    return wordIndex == word.length() && patternIndex == pattern.length();
}


int main() {
    std::string inputFilename = "input.txt";
    std::string outputFilename = "output.txt";
    std::string inputContent = readFile(inputFilename);
    std::cout << "Вміст вхідного файлу:\n" << inputContent << std::endl;

    std::string mask;
    std::cout << "Введіть маску: ";
    std::cin >> mask;

    std::vector<std::string> words;
    std::istringstream iss(inputContent);
    std::string word;
    while (iss >> word) {
        if (matchesPattern(word, mask)) {
            words.push_back(word);
        }
    }

    std::sort(words.begin(), words.end());

    std::cout << "Слова, що підходять під маску:\n";
    for (const std::string& w : words) {
        std::cout << w << std::endl;
    }

    // Формування вихідного контенту
std::string outputContent;
for (const std::string& w : words) {
    outputContent += w + " ";
}

// Запис у вихідний файл лише слів, які відповідають масці
writeFile(outputFilename, outputContent);


    std::cout << "Вміст результуючого файлу:\n" << outputContent << std::endl;

    return 0;
}
