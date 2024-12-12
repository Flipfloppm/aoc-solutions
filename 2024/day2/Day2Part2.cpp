#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

/*
 *  Found a few edge cases:
 *  Case where we remove the one at idx 0
 *  Case where we can't extrapolate increase/decrease from just two numbers
 */
int main(int argc, char *argv[]) { 
    ifstream input(argv[1]);

    if (!input.is_open()) {
        cerr << "Error opening file" << endl;
        return -1;
    }

    string line;
    int sol = 0;
    int idx = 1;

    while (getline(input, line)) { 
        istringstream iss(line);
        vector<int> currLine;
        int num;
        while (iss >> num) { 
            currLine.push_back(num);
        }
        bool valid = true;
        bool increasing = false;
        if (currLine.size() > 1) { 
            int numIncreasing = 0;
            for (int i = 1; i < currLine.size(); i++) { 
                int diff = currLine[i] - currLine[i - 1];
                if (diff > 0) { 
                    numIncreasing += 1;
                } 
            }
            // if we have more than 1 increasing pair, then either it is wrong
            // or it is increasing, both cases accounted for
            if (numIncreasing > 1) { 
                increasing = true;
            }
        } 
        // first we check if the array without modification is safe
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
            idx += 1;
            continue;
        }
        // brute force and remove each index and check if they are safec
        bool valid2 = true;
        for (int j = 0; j < currLine.size(); j++) {
            valid2 = true;
            vector<int> currLine2 (currLine);
            currLine2.erase(currLine2.begin() + j);
            for (int i = 1; i < currLine2.size(); i++) {
                int diff = currLine2[i] - currLine2[i - 1];
                if ((diff > 0 && !increasing) || (diff < 0 && increasing)) {
                        valid2 = false;
                        break;
                } 

                if (abs(diff) == 0 || abs(diff) > 3) {
                        valid2 = false;
                        break;
                }
            }
            
            if (valid2) { 
                break;
            }
        }

        if (valid2) { 
            sol += 1;
        } 
        idx += 1;
    }

    cout << sol << endl;
    
    return 0;
}
