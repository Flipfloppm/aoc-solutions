#include <algorithm>
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <set>
#define INPUT_PRECEDENCE "input_precedence.txt"
#define INPUT_UPDATES "input.txt"
using namespace std;

int validUpdate(vector<string> invalid, unordered_map<string, set<string> >& m) { 
    vector<string> valid;
    for (int i = 0; i < invalid.size(); i++) { 
        string numToAdd = invalid[i];

        // go forwards to find the earliest
        int earliest = 0;
        for (int j = 0; j < invalid.size(); j++) {
            if (m[invalid[j]].find(numToAdd) != m[invalid[j]].end()) { 
                earliest = j + 1;
            }
        }

        // go backwards to find the latest
        int latest = valid.size();
        for (int j = valid.size() - 1; j > -1; j--) { 
            if (m[numToAdd].find(valid[j]) != m[numToAdd].end()) { 
                latest = j;
            }
        }
        int insertIdx = min(latest, earliest);
        valid.insert(valid.begin() + insertIdx, numToAdd);
    }
    double idx = valid.size() / 2.0;
    int truncated = trunc(idx);

    return stoi(valid[truncated]);
}

int main() { 
    ifstream inputPrecedence(INPUT_PRECEDENCE);

    if (!inputPrecedence.is_open()) { 
        cerr << "could not open file" << endl;
        return -1;
    }

    // first create our precedence map
    // map page -> set of numbers that it must precede
    unordered_map<string, set<string> > m;
    string line;
    while (getline(inputPrecedence, line)) { 
        string num1 = "";
        string num2 = "";
        bool found = false;
        for (int i = 0; i < line.size(); i++) { 
            if (line[i] == '|') { 
                found = true;
                continue;
            }
            if (found) { 
                num2 += line[i];
            } else {
                num1 += line[i];
            }
        }
        m[num1].insert(num2);
    }

    inputPrecedence.close();

    // now iterate through the updates 
    ifstream inputUpdates(INPUT_UPDATES);

    if (!inputUpdates.is_open()) { 
        cerr << "could not open file" << endl;
        return -1;
    }

    int sol = 0;
    while (getline(inputUpdates, line)) { 
        vector<string> v;
        string num = "";
        for (int i = 0; i < line.size(); i++) { 
            if (line[i] == ',') { 
                v.push_back(num);
                num = "";
            } else { 
                num += line[i];
            }
        }
        v.push_back(num);
        vector<string> encountered;
        bool valid = true;
        for (int i = 0; i < v.size(); i++) { 
            set<string> s = m[v[i]];
            for (int j = 0; j < encountered.size(); j++) { 
                if (s.find(encountered[j]) != s.end()) { 
                    valid = false;
                    break;
                }
            }
            if (!valid) { 
                break;
            }
            encountered.push_back(v[i]);
        }
        if (!valid) { 
            sol += validUpdate(v, m);
        }
    }
    cout << sol << endl;

    return 0;
}
