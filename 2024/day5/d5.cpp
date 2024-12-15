#include <fstream>
#include <iostream>
#include <unordered_map>
#include <set>
#define INPUT_PRECEDENCE "input_precedence.txt"
#define INPUT_UPDATES "input.txt"
using namespace std;
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
        if (valid) { 
            double idx = v.size() / 2;
            double truncated = trunc(idx);
            cout << v[truncated] << endl;
            sol += stoi(v[truncated]);
        }
    }
    cout << sol << endl;

    return 0;
}
