#include "mih.h"

int main(int argc, const char *argv[]) {
    readData("B.txt");
    HashTable a = HashTable(4);
    a.makeTable();
    //calculateVariance();
    return 0;
}
