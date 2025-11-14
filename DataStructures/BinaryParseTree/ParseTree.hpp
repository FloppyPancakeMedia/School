#include <stdlib.h>
#include <string>
#include <stack>
#include "node.hpp"

#ifndef PARSETREE_H
#define PARSETREE_H

class ParseTree {
private:
    Node* _root;
    std::string getPreOrder(Node* node);
    std::string getInOrder(Node* node, char parentOp = ' ', bool isRightChild = false);
    std::string getPostOrder(Node* node);

public:
    ParseTree(std::string expression);
    ~ParseTree();

    static bool isOperator(char c);
    std::string preOrder();
    std::string inOrder();
    std::string postOrder();
    std::string display();
    void parseInOrder(std::string infix);
    static bool isPrecedent(char a, char b);
    static bool isOperand(char c);
    static int getPrec(char op);

};

#endif