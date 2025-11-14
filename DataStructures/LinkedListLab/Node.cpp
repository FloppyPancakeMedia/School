#include "Node.hpp"
#include <stdlib.h>
#include <iostream>

Node::Node(char value, Node *next, Node *prev){
    _value = value;
    this->next = next;
    this->prev = prev;
}

Node::~Node(){
    next = nullptr;
    prev = nullptr;
    delete next;
    delete prev;
}

char Node::getValue(){
    return _value;
}

Node* Node::getNext(){
    return this->next;
}

Node* Node::getPrev(){
    return this->prev;
}

void Node::setNext(Node *next){
    this->next = next;
}

void Node::setPrev(Node *prev){
    this->prev = prev;
}