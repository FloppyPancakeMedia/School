#ifndef NODE_H
#define NODE_H

class Node {
private:
    char value;
    Node* left, * right;
public:
    Node(char value, Node* l_child = nullptr, Node* r_child = nullptr);
    ~Node();

    Node* getLeft();
    Node* getRight();
    char getValue();

    void setLeft(Node* newNode);
    void setRight(Node* newNode);
    void setChar(char newValue);
};

#endif