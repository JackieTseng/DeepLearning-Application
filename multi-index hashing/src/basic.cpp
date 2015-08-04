#include "basic.h"

vector<bitset<SPLITWIDTH> > front_ones, last_ones;
vector<int> hash_number;

// Read binary code from file
void readData(string fileName) {
    fstream file;
    file.open(fileName.c_str());
    string line;
    while (getline(file, line)) {
        data.push_back(bitset<BITWIDTH>(line));
    }
    return;
}

void readDataAndChange(string fileName) {
    data.clear();
    fstream file;
    file.open(fileName.c_str());
    string line;
    while (getline(file, line)) {
        bitset<BITWIDTH> temp = bitset<BITWIDTH>(line);
        bit_transform(temp);
        data.push_back(temp);
    }
    return;
}

// Calculate the variance of each dimension's attribute
// in order to resort the binary code
void calculateVariance() {
    int dataSize = data.size();
    vector<int> varianceNumber = vector<int>(BITWIDTH, 0);
    vector<VAR> variance = vector<VAR>(BITWIDTH);
    for (int i = 0; i < BITWIDTH; ++i) {
        for (int j = 0; j < dataSize; ++j) {
            if (data[j].test(i)) {
                ++varianceNumber[i];
            }
        }
        variance[i].value = (float)varianceNumber[i] / dataSize;
        variance[i].value *= (1 - variance[i].value);
        variance[i].number = i;
    }
    sort(variance.begin(), variance.end());
    vector<HTN> hash_table = vector<HTN>(HASHTABLENUMBER);
    int iteration = BITWIDTH / HASHTABLENUMBER; 
    vector<VAR>::iterator it = variance.begin();
    for (int i = 0; i < iteration; i++) {
        for (int j = 0; j < HASHTABLENUMBER; ++j, ++it) {
            hash_table[j].number.push_back((*it).number);
            hash_table[j].sum += (*it).value;    
        }
        sort(hash_table.begin(), hash_table.end());
    }
    int temp = 0;
    for (int i = 0; i < HASHTABLENUMBER; i++) {
        //cout << i << " -> ";
        temp = hash_table[i].number.size();
        for (int j = 0; j < temp; j++) {
            //cout << hash_table[i].number[j] << " ";
            hash_number.push_back(hash_table[i].number[j]);
        }
        //cout << " = " << hash_table[i].sum << endl;
    }
}
