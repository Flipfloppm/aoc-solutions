#include <fstream>
#include <iostream>
#include <vector>
#define INPUT_FILE "sample2.txt"
using namespace std;

bool checkBounds(vector< vector<char> > matrix, int i, int j) { 
    if (i < 0 || i >= matrix.size()) { 
        return false;
    }
    
    if (j < 0 || j >= matrix[0].size()) { 
        return false;
    }

    return true;
}

int checkForXmas(vector< vector<char> > matrix,int i, int j) { 
    if (!checkBounds(matrix, i - 1, j - 1) || !checkBounds(matrix, i + 1, j + 1)) {
        return 0;
    }

    if ((matrix[i - 1][j - 1] == 'M' && matrix[i + 1][j + 1] == 'S') || 
            (matrix[i - 1][j - 1] == 'S' && matrix[i + 1][j + 1] == 'M')) { 
        if ((matrix[i - 1][j + 1] == 'M' && matrix[i + 1][j - 1] == 'S') ||
             matrix[i - 1][j + 1] == 'S' && matrix[i + 1][j - 1] == 'M') {
            return 1;
        }
    }
    if ((matrix[i - 1][j + 1] == 'M' && matrix[i + 1][j - 1] == 'S') || 
            (matrix[i - 1][j + 1] == 'S' && matrix[i + 1][j - 1] == 'M')) { 
        if ((matrix[i - 1][j - 1] == 'M' && matrix[i + 1][j + 1] == 'S') || 
            (matrix[i - 1][j - 1] == 'S' && matrix[i + 1][j + 1] == 'M')){
            return 1;
        }
    }
    return 0;
}

int main() { 
    ifstream input(INPUT_FILE);

    if (!input.is_open()) {
        cerr << "could not open file" << endl;
        return -1;
    }
    vector< vector<char> > v;

    string line;
    while (getline(input, line)) { 
        vector<char> charVector;
        for (int i = 0; i < line.size(); i++) { 
            charVector.push_back(line[i]);
        }
        v.push_back(charVector);
    }
    int sol = 0;
    for (int i = 0; i < v.size(); i++) { 
        for (int j = 0; j < v[i].size(); j++) { 
            if (v[i][j] == 'A') { 
                sol += checkForXmas(v, i, j);
            }
        }
    }

    cout << sol << endl;
}
