#include <stdio.h>
#include <fstream>
#include <iostream>
#include <sstream>
using namespace std;

int main(int argc, char *argv[]) { 
    ifstream input(argv[1]);

    if (!input.is_open()) {
        cerr << "Error opening file" << endl;
        return -1;
    }

    string line;
    int sol = 0;

    while (getline(input, line)) { 
        istringstream iss(line);
        vector<int> currLine;
        int num;
        while (iss >> num) { 
            currLine.push_back(num);
        }

        bool valid = true;
        bool increasing;
        if (currLine.size() > 1) { 
            if ((currLine[1] - currLine[0]) > 0) { 
                increasing = true;
            } else {
                increasing = false;
            }
        } 

        for (int i = 1; i < currLine.size(); i++) {
            int diff = currLine[i] - currLine[i - 1];
            if ((diff > 0 && !increasing) || (diff < 0 && increasing)) {
                valid = false;
                break;
            } 

            if (abs(diff) == 0 || abs(diff) > 3) {
                valid = false;
                break;
            }
        }

        if (valid) { 
            sol += 1;
        }
        
    }

    // part 1 solution
    cout << sol << endl;
    
    return 0;
}
