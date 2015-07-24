#include "mih.h"

int main(int argc, const char *argv[]) {
    clock_t _1_, _2_, _3_, _4_;
    string target = "0001100110000000010011111001110111001000011010011011101010001111";
    //string target = "0010100001011001101001000001100110000111010011101000001100010111";
    _1_ = clock();
    readData("B.txt");
    MIH x = MIH(HASHTABLENUMBER);
    _2_ = clock();
    bitset<BITWIDTH> t(target);
    set<int> temp = x.searchCandidates(t, RADIUS);
    _3_ = clock();
    set<int> result = x.selectGoal(temp, t, RADIUS);
    _4_ = clock();
    cout << "result : " << result.size() << endl;
    cout << "Bulid time           : " << (float)(_2_ - _1_)/CLOCKS_PER_SEC << endl;
    cout << "Find Candidate  time : " << (float)(_3_ - _2_)/CLOCKS_PER_SEC << endl;
    cout << "Find Goal time       : " << (float)(_4_ - _3_)/CLOCKS_PER_SEC << endl;
    cout << "Total time           : " << (float)(_4_ - _1_)/CLOCKS_PER_SEC << endl;
    cout << "finish\n";
    return 0;
}
