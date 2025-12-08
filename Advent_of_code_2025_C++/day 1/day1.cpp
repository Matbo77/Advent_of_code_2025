#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

// Function to load data from a text file
void load_data(const std::string& file_name, std::vector<char>& rotation_dir_letter, std::vector<int>& rotation_clicks) {
    std::ifstream file(file_name);
    std::string line;
    while (std::getline(file, line)) {
        rotation_dir_letter.push_back(line[0]);
        rotation_clicks.push_back(std::stoi(line.substr(1)));
    }
}

// Part 1 solution
int part1_solution(const std::string& data_file_name) {
    std::vector<char> rotation_dir_letter;
    std::vector<int> rotation_clicks;
    load_data(data_file_name, rotation_dir_letter, rotation_clicks);

    int dial = 50;
    int counter_pointing_0 = 0;

    for (size_t i = 0; i < rotation_dir_letter.size(); ++i) {
        int rotation_dir = (rotation_dir_letter[i] == 'R') ? 0 : 1;
        // Conditional ternary operator ( ? )
        dial += std::pow(-1, rotation_dir) * rotation_clicks[i];

        while (dial > 99 || dial < 0) {
            dial += std::pow(-1, rotation_dir + 1) * 100;
        }

        if (dial == 0) {
            counter_pointing_0++;
        }
    }

    return counter_pointing_0;
}

// Part 2 solution
int part2_solution(const std::string& data_file_name) {
    std::vector<char> rotation_dir_letter;
    std::vector<int> rotation_clicks;
    load_data(data_file_name, rotation_dir_letter, rotation_clicks);

    int dial_previous = 50;
    int counter_pointing_0_during_rotation = 0;
    int counter_pointing_0 = 0;

    for (size_t i = 0; i < rotation_dir_letter.size(); ++i) {
        int rotation_dir = (rotation_dir_letter[i] == 'R') ? 0 : 1;
         
        int dial = dial_previous + std::pow(-1, rotation_dir) * rotation_clicks[i];


        while (dial > 99 || dial < 0) {
            counter_pointing_0_during_rotation++;
            dial += std::pow(-1, rotation_dir + 1) * 100;
        }

        // Correction not to count another time 0 during Left rotation starting from 0
        if (dial_previous == 0 && rotation_dir == 1) {
            counter_pointing_0_during_rotation--;
        }
        // Correction not to count two times 0 during Right rotation
        if (dial == 0 && rotation_dir == 0) {
            counter_pointing_0_during_rotation--;
        }

        if (dial == 0) { // last dial
            counter_pointing_0++;
        }

        dial_previous = dial;
    }

    return counter_pointing_0 + counter_pointing_0_during_rotation;
}

int main() {
    std::cout << "Part 1 test: " << part1_solution("day1_input_test.txt") << std::endl;
    std::cout << "Part 1 solution: " << part1_solution("day1_input.txt") << std::endl;
    std::cout << "---" << std::endl;
    std::cout << "Part 2 test: " << part2_solution("day1_input_test.txt") << std::endl;
    std::cout << "Part 2 solution: " << part2_solution("day1_input.txt") << std::endl;

    return 0;
}

