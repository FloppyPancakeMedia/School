#ifndef TREE_H
#define TREE_H

#include <stdlib.h>
#include <string>
#include "node.hpp"

class Tree {
private:
    Node* _root;
    std::string recPreOrder(Node* node);
    std::string recInOrder(Node* node);
    std::string recPostOrder(Node* node);
    int recFindLarger(Node* node, int value);
    int recRemoveLarger(Node* node, int value);

public:
    Tree();
    ~Tree();

    void insertValue(int value);
    bool findValue(int value);
    bool removeValue(int value);
    std::string preOrder();
    std::string inOrder();
    std::string postOrder();
    int findLarger(int value);
    int removeLarger(int value);
};

#endif