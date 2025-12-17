#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

// Function to load data from a text file
vector<vector<int>> load_data(const string& file_name) {
    ifstream file(file_name);
    vector<vector<int>> list_of_digit_lists;
    string line;
    while (getline(file, line)) {
        vector<int> digits;
        for (char digit_char : line) {
            digits.push_back(digit_char - '0'); // Convert char to int
        }
        list_of_digit_lists.push_back(digits);
    }
    return list_of_digit_lists;
}

// Part 1 solution
long long part1_solution(const string& data_file_name) {
    vector<vector<int>> data = load_data(data_file_name);
    long long total_output_joltage = 0;

    for (size_t i = 0; i < data.size(); ++i) {
        const vector<int>& line_digits = data[i];

        // Find indices of the max digit (excluding the last digit)
        vector<size_t> max_list;
        int max_digit = *max_element(line_digits.begin(), line_digits.end() - 1);
        for (size_t k = 0; k < line_digits.size() - 1; ++k) {
            if (line_digits[k] == max_digit) {
                max_list.push_back(k);
            }
        }

        // Generate candidates and find the maximum
        vector<long long> list_candidate;
        for (size_t k : max_list) {
            int next_max = *max_element(line_digits.begin() + k + 1, line_digits.end());
            long long candidate = line_digits[k] * 10 + next_max;
            list_candidate.push_back(candidate);
        }

        long long max_output_joltage = *max_element(list_candidate.begin(), list_candidate.end());
        total_output_joltage += max_output_joltage;
    }

    return total_output_joltage;
}

// Part 2 solution
long long part2_solution(const string& data_file_name) {
    vector<vector<int>> data = load_data(data_file_name);
    long long total_output_joltage = 0;
    const int number_digits_joltage = 12;

    for (size_t i = 0; i < data.size(); ++i) {
        const vector<int>& line_digits = data[i];
        int remaining_number_digits = number_digits_joltage;
        vector<int> dynamic_line_digits(line_digits.begin(), line_digits.end() - remaining_number_digits + 1);

        // Find the first max digit
        auto max_it = max_element(dynamic_line_digits.begin(), dynamic_line_digits.end());
        size_t max_index = distance(dynamic_line_digits.begin(), max_it);
        long long candidate = dynamic_line_digits[max_index];
        size_t last_max_index = max_index;
        remaining_number_digits--;

        // Iteratively find the next max digits
        while (remaining_number_digits > 0) {
            dynamic_line_digits.assign(
                line_digits.begin() + last_max_index + 1,
                line_digits.end() - remaining_number_digits + 1
            );
            max_it = max_element(dynamic_line_digits.begin(), dynamic_line_digits.end());
            max_index = distance(dynamic_line_digits.begin(), max_it);
            candidate = candidate * 10 + dynamic_line_digits[max_index];
            last_max_index += max_index + 1;
            remaining_number_digits--;
        }

        total_output_joltage += candidate;
    }

    return total_output_joltage;
}

int main() {
    cout << "Part 1 test: " << part1_solution("day3_input_test.txt") << endl;   // 357
    cout << "Part 1 solution: " << part1_solution("day3_input.txt") << endl;   // 17074
    cout << "---" << endl;
    cout << "Part 2 test: " << part2_solution("day3_input_test.txt") << endl;  // 3121910778619
    cout << "Part 2 solution: " << part2_solution("day3_input.txt") << endl; // 169512729575727
    return 0;
}

