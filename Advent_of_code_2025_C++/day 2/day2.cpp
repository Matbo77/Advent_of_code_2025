
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>

// Function to load data from a text file
std::vector<std::string> load_data(const std::string& file_name) {
    std::ifstream file(file_name);
    std::string line;
    std::getline(file, line);
    std::vector<std::string> data;
    std::stringstream ss(line);
    std::string pair;
    while (std::getline(ss, pair, ',')) {
        data.push_back(pair);
    }
    return data;
}

// Function to check if an ID is invalid (Part 1)
bool is_invalid_ID(long long x) {
    std::string s = std::to_string(x);
    if (s.length() % 2 != 0) {
        return false;
    }
    return s.substr(0, s.length() / 2) == s.substr(s.length() / 2);
}

// Function to check if an ID is invalid (Part 2)
bool is_invalid_ID_new_rules(long long x) {
    std::string s = std::to_string(x);
    bool ok = false;
    int i_mult = 1;
    int k = 1;
    while (i_mult <= s.length() / 2 && k < s.length()) {
        if (s.substr(0, i_mult) == s.substr(k, i_mult)) {
            ok = true;
            k += i_mult;
        } else {
            ok = false;
            i_mult = k + 1;
            k = i_mult;
        }
    }
    return ok;
}

// Part 1 solution
long long part1_solution(const std::string& data_file_name) {
    std::vector<std::string> data = load_data(data_file_name);
    long long total = 0;
    for (const auto& pair : data) {
        size_t dash_pos = pair.find('-');
	
	// Paramount to use the type long long given the size of the numbers in the data files
	long long begin_id = std::stoll(pair.substr(0, dash_pos));
	long long end_id = std::stoll(pair.substr(dash_pos + 1));
	
	// std::cout << "Converting: " << begin_id << "-" << end_id << std::endl;
	
        for (long long num = begin_id; num <= end_id; ++num) {
            if (is_invalid_ID(num)) {
            	//std::cout << "Invalid_ID: " << num << std::endl;
                total += num;
            }
        }
    }
    return total;
}

// Part 2 solution
long long part2_solution(const std::string& data_file_name) {
    std::vector<std::string> data = load_data(data_file_name);
    long long total = 0;
    for (const auto& pair : data) {
        size_t dash_pos = pair.find('-');
        
        // Paramount to use the type long long given the size of the numbers in the data files
        //std::cout << "Converting: " << pair.substr(0, dash_pos) << std::endl;
	long long begin_id = std::stoll(pair.substr(0, dash_pos));
	long long end_id = std::stoll(pair.substr(dash_pos + 1));
        for (long long num = begin_id; num <= end_id; ++num) {
            if (is_invalid_ID_new_rules(num)) {
                total += num;
            }
        }
    }
    return total;
}

int main() {
	long long part_1_solution_test = part1_solution("day2_input_test.txt") ;
    	std::cout << "Part 1 test: " << part_1_solution_test << std::endl;
    	//long long part_1_solution_test2 = part1_solution("day2_input_test2.txt");
    	//std::cout << "Part 1 test2: " << part_1_solution_test2 << std::endl;
    	long long part_1_solution = part1_solution("day2_input.txt");
    	std::cout << "Part 1 solution: " << part_1_solution << std::endl;
    	std::cout << "---" << std::endl;
    	long long part_2_solution_test = part2_solution("day2_input_test.txt");
    	std::cout << "Part 2 test: " << part_2_solution_test  << std::endl;
    	long long part_2_solution = part2_solution("day2_input.txt"); 
    	std::cout << "Part 2 solution: " << part_2_solution << std::endl; 
    return 0;
}

