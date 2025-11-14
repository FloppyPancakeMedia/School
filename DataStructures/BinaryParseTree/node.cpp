#include "node.hpp"
#include <stdlib.h>
#include <iostream>

Node::Node(char value, Node* lchild, Node* rchild) : value(value), left(lchild), right(rchild) {
    // std::cout << "Value = " << value << std::endl;
}

Node::~Node() {
    // left = nullptr;
    // right = nullptr;
    delete left, right;
}

Node* Node::getLeft() {
    return left;
}

Node* Node::getRight() {
    return right;
}

char Node::getValue() {
    return value;
}

void Node::setLeft(Node* newNode) {
    left = newNode;
}

void Node::setRight(Node* newNode) {
    right = newNode;
}

void Node::setChar(char newValue) {
    value = newValue;
}