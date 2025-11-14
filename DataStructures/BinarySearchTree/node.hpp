#ifndef NODE_H
#define NODE_H

#include <stdlib.h>
#include <string>

class Node {
private:
    int value;
    Node* left, * right;
    int count;
    bool is_deleted;
public:
    Node(int value, Node* l_child = nullptr, Node* r_child = nullptr);
    ~Node();

    Node* getLeft();
    Node* getRight();
    int getValue();

    void setLeft(Node* newNode);
    void setRight(Node* newNode);
    void setValue(int newValue);
    void increaseCount();
    void decreaseCount();
    std::string getValueString();
    void setIsDeleted(bool value);
    bool getIsDeleted();
};

#endif