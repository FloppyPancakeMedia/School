#include <stdlib.h>
#include <string>


#ifndef CHAINLINK_H
#define CHAINLINK_H
class ChainLink
{
private:
    std::string _value;
    ChainLink *_next;

public:
    ChainLink(std::string value, ChainLink *next = nullptr);
    ~ChainLink();

    ChainLink* getNext();
    std::string getValue();
    void setNext(ChainLink *newNext);
};

#endif