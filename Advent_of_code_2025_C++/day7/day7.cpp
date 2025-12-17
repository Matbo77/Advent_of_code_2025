#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_set>

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
int part1_solution(const string& data_file_name) {
    vector<string> lines = load_data(data_file_name);

    int n_c = lines[0].size();
    int n_l = lines.size();

    int sum_beam_splitted = 0;

    // Initialize list_beam
    vector<vector<int>> list_beam(n_l);

    // Detect tachyon beam enters (S)
    for (int j = 0; j < n_c; ++j) {
        if (lines[0][j] == 'S') {
            list_beam[0].push_back(j);
        }
    }

    for (int i = 1; i < n_l; ++i) {
        unordered_set<int> unique_beams;
        for (int elt : list_beam[i-1]) {
            if (lines[i][elt] == '^') { // beam splitting
                sum_beam_splitted += 1;
                if (elt >= 1) {
                    unique_beams.insert(elt - 1);
                }
                if (elt < n_c - 1) {
                    unique_beams.insert(elt + 1);
                }
            } else { // vertical beam propagation
                unique_beams.insert(elt);
            }
        }
        // Convert unordered_set to vector
        list_beam[i].assign(unique_beams.begin(), unique_beams.end());
    }

    return sum_beam_splitted;
}

// Part 2 solution
long long part2_solution(const string& data_file_name) {
    vector<string> lines = load_data(data_file_name);

    int n_c = lines[0].size();
    int n_l = lines.size();

    // Initialize list_number_beams
    vector<vector<long long>> list_number_beams(n_l, vector<long long>(n_c, 0));

    // Detect tachyon beam enters (S)
    for (int j = 0; j < n_c; ++j) {
        if (lines[0][j] == 'S') {
            list_number_beams[0][j] += 1;
        }
    }

    for (int i = 1; i < n_l; ++i) {
        for (int elt = 0; elt < n_c; ++elt) {
            if (list_number_beams[i-1][elt] > 0) {
                if (lines[i][elt] == '^') { // beam splitting
                    if (elt >= 1) {
                        list_number_beams[i][elt-1] += list_number_beams[i-1][elt];
                    }
                    if (elt < n_c - 1) {
                        list_number_beams[i][elt+1] += list_number_beams[i-1][elt];
                    }
                } else { // vertical beam propagation
                    list_number_beams[i][elt] += list_number_beams[i-1][elt];
                }
            }
        }
    }

    long long number_timelines = 0;
    for (long long num : list_number_beams[n_l-1]) {
        number_timelines += num;
    }

    return number_timelines;
}

int main() {
    cout << "Part 1 test: " << part1_solution("day7_input_test.txt") << endl;   // 21
    cout << "Part 1 solution: " << part1_solution("day7_input.txt") << endl;   // 1594
    cout << "---" << endl;
    cout << "Part 2 test: " << part2_solution("day7_input_test.txt") << endl;  // 40
    cout << "Part 2 solution: " << part2_solution("day7_input.txt") << endl; // 15650261281478
    return 0;
}

