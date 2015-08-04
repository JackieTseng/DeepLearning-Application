#include "mih.h"

int main(int argc, const char *argv[]) {
    //double _1_, _2_, _3_, _4_;//win
    clock_t _1_, _2_, _3_, _4_;//unix
    //string target = "1101101000110001000101010010100000101100000111101101001101011110010000001011010011100101111111010011100010101000000001111001100101011010000010000111001001010110110011101000111001110101100101111010011100011000111111011011010001000000110001110110110001110001011010111010010111101111011100001011110011110101001001101000010110101101010011111110011100000101111010111100011111011101001110001110001001110000101111010110110001111111000101010001111100111001101001100000101111111010110011110110101110111010110000111010000010110011101100111011001000110101110111101011000011111000101101101111100010110000010011110000000011110111101110111111001000111001110011001011011011000001010000101101100000000101110110011001101000001001110011000010001101000011001001001011010001101001001100101100010100011101010001001101100111001010000101110100000001010110110111111111010001011000111100001011000110101011001011001001011001110000001010100000111110011101010001111011011000111001001101011111100000000001010001010001011011110110";
    string target = "0011101110000010010011111001111110001110001010001110100010001011";//378
    _1_ = clock();
    //readData("B_1000.txt");
    readData("B_64.txt");
    calculateVariance();
    //readDataAndChange("B_1000.txt");
    readDataAndChange("B_64.txt");
    MIH x = MIH(HASHTABLENUMBER);
    _2_ = clock();
    bitset<BITWIDTH> t(target);
    bit_transform(t);
    set<int> candidates;
    candidates = x.searchCandidates(t, RADIUS, candidates);
    _3_ = clock();
    set<int> result;
    result = x.selectGoal(candidates, t, RADIUS, result);
    _4_ = clock();
    cout << "result : " << candidates.size() << " -> " << result.size() << endl;
    /*win*/
    //cout << "Bulid time           : " << _2_ - _1_ << endl;
    //cout << "Find Candidate  time : " << _3_ - _2_ << endl;
    //cout << "Find Goal time       : " << _4_ - _3_ << endl;
    //cout << "Total time           : " << _4_ - _1_ << endl;
    /*unix*/
    cout << "Bulid time           : " << (float)(_2_ - _1_)/CLOCKS_PER_SEC << endl;
    cout << "Find Candidate  time : " << (float)(_3_ - _2_)/CLOCKS_PER_SEC << endl;
    cout << "Find Goal time       : " << (float)(_4_ - _3_)/CLOCKS_PER_SEC << endl;
    cout << "Total time           : " << (float)(_4_ - _1_)/CLOCKS_PER_SEC << endl;
    cout << "finish\n";
    return 0;
}
