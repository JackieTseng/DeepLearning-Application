#ifndef _BASE_H_
#define _BASE_H_

#include <iostream>
#include <fstream>
#include <cstring>
#include <bitset>
#include <vector>
#include <cmath>
#include <ctime>
#include <set>
using namespace std;

#define BITWIDTH 64 // Total binary code's width
#define HASHTABLENUMBER 4
#define SPLITWIDTH (BITWIDTH / HASHTABLENUMBER)
#define RADIUS 4 // The variance for the whole binary code

// codes for calculating hamming weight
const unsigned long m1  = 0x5555555555555555; //binary: 0101...  
const unsigned long m2  = 0x3333333333333333; //binary: 00110011..  
const unsigned long m4  = 0x0f0f0f0f0f0f0f0f; //binary: 4 zeros,  4 ones ...  
const unsigned long h01 = 0x0101010101010101; //the sum of 256 to the power of 0,1,2,3...  

extern vector<bitset<SPLITWIDTH> > front_ones, last_ones; // codes like 0000.., 1000.., 1100.. and ..0111, ..0011, ..0001
extern vector<bitset<BITWIDTH> > data; // dataset
extern vector<int> variance;

void readData(string);
void calculateVariance();
inline vector<bitset<SPLITWIDTH> >& split(bitset<BITWIDTH> B, vector<bitset<SPLITWIDTH> >& result) {
    unsigned long temp;
    int single_length = SPLITWIDTH;
    int whole_length = single_length * (HASHTABLENUMBER - 1);
    for (int i = 0; i < HASHTABLENUMBER; ++i) {
        temp = ((B << (i * single_length)) >> whole_length).to_ulong();
        result.push_back(bitset<SPLITWIDTH>(temp));
    }
    return result;
}
// Hamming weight using merge method form wiki
inline int calculateOnes(unsigned long x) {
    x -= (x >> 1) & m1;             //put count of each 2 bits into those 2 bits  
    x = (x & m2) + ((x >> 2) & m2); //put count of each 4 bits into those 4 bits   
    x = (x + (x >> 4)) & m4;        //put count of each 8 bits into those 8 bits   
    return (x * h01)>>56;
}
#endif
