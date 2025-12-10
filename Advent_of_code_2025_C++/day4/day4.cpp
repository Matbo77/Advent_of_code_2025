#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

// Function to load data from a text file
vector<vector<int>> load_data(const string& file_name) {
    ifstream file(file_name);
    vector<vector<int>> list_of_digit_lists;
    string line;
    while (getline(file, line)) {
        vector<int> row;
        for (char c : line) {
            row.push_back(c == '@' ? 1 : 0);
        }
        list_of_digit_lists.push_back(row);
    }
    return list_of_digit_lists;
}

// Part 1 solution
int part1_solution(const string& data_file_name) {
    vector<vector<int>> data = load_data(data_file_name);
    int n_l = data.size();
    if (n_l == 0) return 0;
    int n_c = data[0].size();
    int max_neighbor_rolls = 3;
    int paper_rolls_accessed = 0;

    for (int l = 0; l < n_l; ++l) {
        vector<int> rolls_of_papers;
        for (int c = 0; c < n_c; ++c) {
            if (data[l][c] == 1) {
                rolls_of_papers.push_back(c);
            }
        }

        for (int c : rolls_of_papers) {
            int neighbor_rolls = -1;
            for (int j_l = -1; j_l < 2 && neighbor_rolls <= max_neighbor_rolls; ++j_l) {
                for (int j_c = -1; j_c < 2 && neighbor_rolls <= max_neighbor_rolls; ++j_c) {
                    int new_l = l + j_l;
                    int new_c = c + j_c;
                    if (new_l >= 0 && new_l < n_l && new_c >= 0 && new_c < n_c) {
                        if (data[new_l][new_c] == 1) {
                            neighbor_rolls++;
                        }
                    }
                }
            }
            if (neighbor_rolls <= max_neighbor_rolls) {
                paper_rolls_accessed++;
            }
        }
    }

    return paper_rolls_accessed;
}

// Function to check if a roll is accessible
bool is_accessible(const vector<vector<int>>& data, int l, int c, int max_neighbor_rolls) {
    int n_l = data.size();
    if (n_l == 0) return false;
    int n_c = data[0].size();
    int neighbor_rolls = -1;

    for (int j_l = -1; j_l < 2 && neighbor_rolls <= max_neighbor_rolls; ++j_l) {
        for (int j_c = -1; j_c < 2 && neighbor_rolls <= max_neighbor_rolls; ++j_c) {
            int new_l = l + j_l;
            int new_c = c + j_c;
            if (new_l >= 0 && new_l < n_l && new_c >= 0 && new_c < n_c) {
                if (data[new_l][new_c] == 1) {
                    neighbor_rolls++;
                }
            }
        }
    }
    return neighbor_rolls <= max_neighbor_rolls;
}

// Part 2 solution
int part2_solution(const string& data_file_name) {
    vector<vector<int>> data = load_data(data_file_name);
    int n_l = data.size();
    if (n_l == 0) return 0;
    int n_c = data[0].size();
    int max_neighbor_rolls = 3;
    int paper_rolls_accessed = 0;

    int l = 0;
    while (l < n_l) {
        vector<int> rolls_of_papers;
        for (int c = 0; c < n_c; ++c) {
            if (data[l][c] == 1) {
                rolls_of_papers.push_back(c);
            }
        }

        bool accessible_roll_removed = false;
        for (int c : rolls_of_papers) {
            if (is_accessible(data, l, c, max_neighbor_rolls)) {
                data[l][c] = 0;
                paper_rolls_accessed++;
                accessible_roll_removed = true;
            }
        }

        if (accessible_roll_removed) {
            l = -1; // Restart from the beginning
        }
        l++;
    }

    return paper_rolls_accessed;
}

int main() {
    cout << "Part 1 test: " << part1_solution("day4_input_test.txt") << endl;   // 13
    cout << "Part 1 solution: " << part1_solution("day4_input.txt") << endl;   // 1428
    cout << "---" << endl;
    cout << "Part 2 test: " << part2_solution("day4_input_test.txt") << endl;  // 43
    cout << "Part 2 solution: " << part2_solution("day4_input.txt") << endl; // 8936
    return 0;
}

