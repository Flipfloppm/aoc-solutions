#include <unordered_map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cstdlib>
using namespace std;


int main(int argc, char *argv[]) {
    ifstream input(argv[1]);
    vector<int> leftColumn;
    vector<int> rightColumn;
    
    if (input.is_open()) { 
        std::string line;
        while (getline(input, line)) { 
            istringstream iss(line);
            int left, right;

            if (iss >> left >> right) { 
                leftColumn.push_back(left);
                rightColumn.push_back(right);
            }
        }
    }

    sort (leftColumn.begin(), leftColumn.end());
    sort (rightColumn.begin(), rightColumn.end());

    int sol = 0;
    for (int i = 0; i < leftColumn.size(); i++) { 
        sol += abs(leftColumn[i] - rightColumn[i]);
    }
    // part 1 sol
    cout << sol << '\n';

    unordered_map<int, int> rightFreq;
    for (int i = 0; i < rightColumn.size(); i++) {
        rightFreq[rightColumn[i]]++;
    }

    int freq;
    int sol2 = 0;
    for (int i = 0; i < leftColumn.size(); i++) { 
        if (rightFreq.find(leftColumn[i]) != rightFreq.end()) { 
            sol2 += leftColumn[i] * rightFreq[leftColumn[i]];
        }  
    }
    // part 2 sol
    cout << sol2 << '\n';
    return 0;
}
