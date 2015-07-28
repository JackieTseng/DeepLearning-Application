#include "mih.h"

int main(int argc, const char *argv[]) {
    //double _1_, _2_, _3_, _4_;//win
    clock_t _1_, _2_, _3_, _4_;//unix
    string target = "0011101110000010010011111001111110001110001010001110100010001011";//378
    //string target = "0001100110100000010011011011101110001110001010010110101010001011";18873
    //string target = "0001101010100000010011011011100110001110001010011110101010001011";//32214
    //string target = "0001100010000010010011011011110111001110001010011010101010101011";//5374
    //string target = "0001100110000000010011011001111111001110001010000010101010001011";//6100
    _1_ = clock();
    readData("B.txt");
    //calculateVariance();
    MIH x = MIH(HASHTABLENUMBER);
    _2_ = clock();
    bitset<BITWIDTH> t(target);
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
