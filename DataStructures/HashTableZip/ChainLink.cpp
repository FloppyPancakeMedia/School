#include "ChainLink.hpp"

ChainLink::ChainLink(std::string value, ChainLink *next) : _value(value), _next(next){}

ChainLink::~ChainLink(){
    _next = nullptr;
    delete _next;
}

ChainLink* ChainLink::getNext(){
    return _next;
}

std::string ChainLink::getValue(){
    return _value;
}

void ChainLink::setNext(ChainLink *newNext){
    _next = newNext;
}