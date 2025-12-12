#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdexcept>

using namespace std;

// Function to load data from a text file
vector<string> load_data(const string& file_name) {
    ifstream file(file_name);
    vector<string> lines;
    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }
    return lines;
}

// Part 1 solution
long long part1_solution(const string& data_file_name) {
    vector<string> lines = load_data(data_file_name);

    bool space = false;
    vector<long long> available_ingredients;
    vector<pair<long long, long long>> min_max_ranges;

    for (const string& line : lines) {
        if (line.empty()) {
            space = true;
        } else if (!space) {
            size_t dash_pos = line.find('-');
            if (dash_pos == string::npos) {
                continue;
            }
            try {
                long long min_val = stoll(line.substr(0, dash_pos));
                long long max_val = stoll(line.substr(dash_pos + 1));
                min_max_ranges.emplace_back(min_val, max_val);
            } catch (const out_of_range& e) {
                continue;
            } catch (const invalid_argument& e) {
                continue;
            }
        } else {
            try {
                long long ingredient = stoll(line);
                available_ingredients.push_back(ingredient);
            } catch (const out_of_range& e) {
                continue;
            } catch (const invalid_argument& e) {
                continue;
            }
        }
    }

    long long fresh_available_ingredient = 0;

    for (long long x : available_ingredients) {
        bool fresh_ingredient = false;
        for (size_t i = 0; i < min_max_ranges.size() && !fresh_ingredient; ++i) {
            if (min_max_ranges[i].first <= x && x <= min_max_ranges[i].second) {
                fresh_available_ingredient++;
                fresh_ingredient = true;
            }
        }
    }

    return fresh_available_ingredient;
}

// Part 2 solution
long long part2_solution(const string& data_file_name) {
    vector<string> lines = load_data(data_file_name);

    vector<pair<long long, long long>> min_max_ranges;

    for (const string& line : lines) {
        if (line.empty()) {
            break;
        } else {
            size_t dash_pos = line.find('-');
            if (dash_pos == string::npos) {
                continue;
            }
            try {
                long long min_val = stoll(line.substr(0, dash_pos));
                long long max_val = stoll(line.substr(dash_pos + 1));
                min_max_ranges.emplace_back(min_val, max_val);
            } catch (const out_of_range& e) {
                continue;
            } catch (const invalid_argument& e) {
                continue;
            }
        }
    }

    sort(min_max_ranges.begin(), min_max_ranges.end());

    long long fresh_ingredient = 0;
    size_t i = 0;

    while (i < min_max_ranges.size()) {
        size_t j = 1;
        while (i + j < min_max_ranges.size() && min_max_ranges[i].second >= min_max_ranges[i + j].first) {
            min_max_ranges[i + j].first = min_max_ranges[i].second + 1;

            if (min_max_ranges[i].second >= min_max_ranges[i + j].second) {
                min_max_ranges.erase(min_max_ranges.begin() + i + j);
                j--;
            }
            j++;
        }

        fresh_ingredient += min_max_ranges[i].second - min_max_ranges[i].first + 1;
        i++;
    }

    return fresh_ingredient;
}

int main() {
    cout << "Part 1 test: " << part1_solution("day5_input_test.txt") << endl;
    cout << "Part 1 solution: " << part1_solution("day5_input.txt") << endl;
    cout << "---" << endl;
    cout << "Part 2 test: " << part2_solution("day5_input_test.txt") << endl;
    cout << "Part 2 solution: " << part2_solution("day5_input.txt") << endl;
    return 0;
}

