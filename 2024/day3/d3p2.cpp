#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#define INPUT_FILE "input.txt"
using namespace std;

unordered_map<int, unordered_map<char, int> > transition_map;

void init_transition_map() { 
    transition_map[0]['m'] = 1;
    transition_map[1]['u'] = 2;
    transition_map[2]['l'] = 3;
    transition_map[3]['('] = 4;
    transition_map[4]['0'] = 5;
    transition_map[4]['1'] = 5;
    transition_map[4]['2'] = 5;
    transition_map[4]['3'] = 5;
    transition_map[4]['4'] = 5;
    transition_map[4]['5'] = 5;
    transition_map[4]['6'] = 5;
    transition_map[4]['7'] = 5;
    transition_map[4]['8'] = 5;
    transition_map[4]['9'] = 5;
    transition_map[5]['0'] = 5;
    transition_map[5]['1'] = 5;
    transition_map[5]['2'] = 5;
    transition_map[5]['3'] = 5;
    transition_map[5]['4'] = 5;
    transition_map[5]['5'] = 5;
    transition_map[5]['6'] = 5;
    transition_map[5]['7'] = 5;
    transition_map[5]['8'] = 5;
    transition_map[5]['9'] = 5;
    transition_map[5][','] = 6;
    transition_map[6]['0'] = 7;
    transition_map[6]['1'] = 7;
    transition_map[6]['2'] = 7;
    transition_map[6]['3'] = 7;
    transition_map[6]['4'] = 7;
    transition_map[6]['5'] = 7;
    transition_map[6]['6'] = 7;
    transition_map[6]['7'] = 7;
    transition_map[6]['8'] = 7;
    transition_map[6]['9'] = 7;
    transition_map[7]['0'] = 7;
    transition_map[7]['1'] = 7;
    transition_map[7]['2'] = 7;
    transition_map[7]['3'] = 7;
    transition_map[7]['4'] = 7;
    transition_map[7]['5'] = 7;
    transition_map[7]['6'] = 7;
    transition_map[7]['7'] = 7;
    transition_map[7]['8'] = 7;
    transition_map[7]['9'] = 7;
    transition_map[7][')'] = 8;
    transition_map[0]['d'] = 9;
    transition_map[9]['o'] = 10;
    transition_map[10]['n'] = 11;
    transition_map[11]['\''] = 12;
    transition_map[12]['t'] = 13;
    transition_map[13]['('] = 14;
    transition_map[14][')'] = 15;
    transition_map[10]['('] = 16;
    transition_map[16][')'] = 17;
}

int process_mul(string mul) { 
    string stripped_mul = mul.substr(4, mul.size() - 5);
    string num1 = "";
    string num2 = "";
    bool comma_found = false;
    for (int i = 0; i < stripped_mul.size(); i++) { 
        if (stripped_mul[i] == ',') { 
            comma_found = true;
            continue;
        }
        if (!comma_found) {
            num1 += stripped_mul[i];
        } else { 
            num2 += stripped_mul[i];
        }
    }

    return stoi(num1) * stoi(num2);
}

int main() {
    ifstream input(INPUT_FILE);
    
    if (!input.is_open()) {
        cerr << "unable to open file" << endl;
        return -1;
    }

    init_transition_map();

    char c;
    int state = 0;
    string mul = "";
    int sol = 0;
    bool enabled = true;
    while (input.get(c)) { 
        // get the transition state
        // if it's not in the map
        if (transition_map[state].find(c) == transition_map[state].end()) { 
            mul = "";
            state = 0;
        } else { 
            mul += c;
            state = transition_map[state][c];
        }
        // base case we reach one of the finished operations
        if (state == 8 && enabled) { 
            sol += process_mul(mul);
            mul = "";
            state = 0;
        } else if (state == 15) {
            enabled = false;
            mul = "";
            state = 0;
        } else if (state == 17) { 
            enabled = true;
            mul = "";
            state = 0;
        } else if (state == 8) { 
            mul = "";
            state = 0;
        }

        
    }
    cout << sol << endl;
    return 0;
}   
