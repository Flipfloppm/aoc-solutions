#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

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
        cout << "===" << endl;
        istringstream iss(line);
        vector<int> currLine;
        int num;
        while (iss >> num) { 
            currLine.push_back(num);
        }
        bool removed = false;
        bool valid = true;
        bool increasing;
        if (currLine.size() > 1) { 
            if ((currLine[currLine.size() - 1] - currLine[0]) > 0) { 
                increasing = true;
            } else {
                increasing = false;
            }
        } 

        cout << idx << ": ";
        for (int i = 1; i < currLine.size(); i++) {
            cout << currLine[i] << ' ';
            int diff = currLine[i] - currLine[i - 1];
            if ((diff > 0 && !increasing) || (diff < 0 && increasing)) {
                if (removed) {
                    valid = false;
                    break;
                } else {
                    cout << "removing " << currLine[i] << ' ';
                    currLine.erase(currLine.begin() + i);
                    removed = true;
                    // dec idx because we remove one
                    i -= 1;
                }
            } 

            if (abs(diff) == 0 || abs(diff) > 3) {
                if (removed) {
                    valid = false;
                    break;
                } else {
                    cout << "removing " << currLine[i] << ' ';
                    currLine.erase(currLine.begin() + i);
                    removed = true;
                    // dec idx because we remove one
                    i -= 1;
                }
            }
        }

        if (valid) { 
            sol += 1;
        } else {
            cout << "INVALID" << endl;
        }
        idx += 1;
        cout << endl;
    }

    cout << sol << endl;
    
    return 0;
}
