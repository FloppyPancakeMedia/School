#ifndef NODE

#define NODE
#include <stdlib.h>

class Node{
private:
    char _value;
    Node *next;
    Node *prev;

public:
    Node(char value, Node *next = nullptr, Node *prev = nullptr);
    ~Node();
    char getValue();
    Node* getNext();
    Node* getPrev();
    void setNext(Node *next);
    void setPrev(Node *prev);
};

#endif