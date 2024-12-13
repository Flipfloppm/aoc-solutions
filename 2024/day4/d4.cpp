#include <fstream>
#include <iostream>
#include <vector>
#define INPUT_FILE "input.txt"
using namespace std;

int checkDirection(vector< vector<char> > matrix, int i, int j, int dr, int dc) { 
    vector<char> mas;
    mas.push_back('S');
    mas.push_back('A');
    mas.push_back('M');
    for (int k = 1; k < 4; k++) { 
        int offsetX = (dc * k) + i;
        if (offsetX < 0 || offsetX >= matrix.size()) { 
            return 0;
        }

        int offsetY = (dr * k) + j;
        if (offsetY < 0 || offsetY >= matrix[0].size()) { 
            return 0;
        }

        if (matrix[offsetX][offsetY] != mas[mas.size() - k]) { 
            return 0;
        }
    }

    return 1;
}

int checkForXmas(vector< vector<char> > matrix,int i, int j) { 
    int instances = 0;
    instances += checkDirection(matrix, i, j, 1, 1);
    instances += checkDirection(matrix, i, j, 0, 1);
    instances += checkDirection(matrix, i, j, 1, 0);
    instances += checkDirection(matrix, i, j, -1, -1);
    instances += checkDirection(matrix, i, j, 0, -1);
    instances += checkDirection(matrix, i, j, -1, 0);
    instances += checkDirection(matrix, i, j, -1, 1);
    instances += checkDirection(matrix, i, j, 1, -1);
    return instances;
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
            if (v[i][j] == 'X') { 
                sol += checkForXmas(v, i, j);
            }
        }
    }

    cout << sol << endl;
}
