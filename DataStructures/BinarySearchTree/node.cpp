#include "node.hpp"
#include <stdlib.h>
#include <iostream>

Node::Node(int value, Node* lchild, Node* rchild) : value(value), left(lchild), right(rchild) {
    is_deleted = false;
    count = 1;
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

int Node::getValue() {
    return value;
}

void Node::setLeft(Node* newNode) {
    left = newNode;
}

void Node::setRight(Node* newNode) {
    right = newNode;
}

void Node::setValue(int newValue) {
    value = newValue;
}
std::string Node::getValueString() {
    return std::to_string(value);
}

void Node::increaseCount() {
    if (count <= 0 && is_deleted) {
        is_deleted = false;
    }
    count++;
}

void Node::decreaseCount() {
    count--;
    if (count <= 0) {
        is_deleted = true;
        count = 0;
    }
}

void Node::setIsDeleted(bool value) {
    is_deleted = value;
}

bool Node::getIsDeleted() {
    return is_deleted;
}