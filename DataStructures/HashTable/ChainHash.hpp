#include <stdlib.h>
#include <string>
#include <iostream>
#include "ChainLink.hpp"

class ChainHash
{
private:
    int _size;
    int _curElements;
    ChainLink** _array;

public:
    ChainHash(int size = 7);
    ~ChainHash();

    void addItem(std::string value);
    bool findItem(std::string value);
    void removeItem(std::string value);
    std::string displayTable();
    void resize();
};