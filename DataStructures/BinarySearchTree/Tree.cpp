#include "Tree.hpp"
#include <stdlib.h>
#include <iostream>

Tree::Tree() {
    _root = nullptr;
}


Tree::~Tree() {
    delete _root;
}


void Tree::insertValue(int value) {
    Node* newNode = new Node(value);

    // Add to root if null
    if (_root == nullptr) {
        Node* newNode = new Node(value);
        _root = newNode;
        newNode = nullptr;
        delete newNode;
        return;
    }

    // Start at root node and decide where to go
    Node* curNode = _root;
    while (true) {
        int curVal = curNode->getValue();

        if (curVal == value) {
            curNode->increaseCount();
            break;
        }
        else if (value > curVal) {
            if (curNode->getRight() == nullptr) {
                // Empty spot found. Add node.
                curNode->setRight(newNode);
                break;
            }
            else {
                // Spot occupied. Need to run again.
                curNode = curNode->getRight();
            }
        }
        else {
            if (curNode->getLeft() == nullptr) {
                curNode->setLeft(newNode);
                break;
            }
            else {
                curNode = curNode->getLeft();
            }
        }
    }
    curNode = nullptr;
    newNode = nullptr;
    delete curNode, newNode;
}


bool Tree::findValue(int value) {
    Node* curNode = _root;

    while (curNode != nullptr) {
        int curValue = curNode->getValue();
        if (curNode->getIsDeleted()) {
            return false;
        }

        if (value == curValue) {
            return true;
        }
        else if (value > curValue) {
            curNode = curNode->getRight();
        }
        else {
            curNode = curNode->getLeft();
        }
    }

    return false;
}


bool Tree::removeValue(int value) {
    Node* curNode = _root;

    while (curNode != nullptr) {
        int curValue = curNode->getValue();
        if (curValue == value && !curNode->getIsDeleted()) {
            curNode->decreaseCount();
            return true;
        }
        else if (value > curValue) {
            curNode = curNode->getRight();
        }
        else {
            curNode = curNode->getLeft();
        }
    }

    return false;
}


std::string Tree::preOrder() {
    if (_root == nullptr) {
        std::cout << "Tried preOrder from root but root is null\n";
        return "";
    }

    return recPreOrder(_root);
}

std::string Tree::recPreOrder(Node* node) {
    std::string buffer = "";
    if (node == nullptr) {
        return buffer;
    }

    if (node->getIsDeleted()) {
        buffer += node->getValueString() + "D ";
    }
    else {
        buffer += node->getValueString() + " ";
    }

    buffer += recPreOrder(node->getLeft());
    buffer += recPreOrder(node->getRight());
    return buffer;
}


std::string Tree::inOrder() {
    return recInOrder(_root);
}

std::string Tree::recInOrder(Node* node) {
    std::string buffer = "";

    if (node == nullptr) {
        return buffer;
    }

    buffer += recInOrder(node->getLeft());
    if (node->getIsDeleted()) {
        buffer += node->getValueString() + "D ";
    }
    else {
        buffer += node->getValueString() + " ";
    }
    buffer += recInOrder(node->getRight());

    return buffer;
}


std::string Tree::postOrder() {
    return recPostOrder(_root);
}

std::string Tree::recPostOrder(Node* node) {
    std::string buffer = "";

    if (node == nullptr) {
        return buffer;
    }

    buffer += recPostOrder(node->getLeft());
    buffer += recPostOrder(node->getRight());
    if (node->getIsDeleted()) {
        buffer += node->getValueString() + "D ";
    }
    else {
        buffer += node->getValueString() + " ";
    }


    return buffer;
}


int Tree::findLarger(int value) {
    return recFindLarger(_root, value);
}

int Tree::recFindLarger(Node* node, int value) {
    if (node == nullptr) return -1;

    int curValue = node->getValue();

    if (curValue == value && !node->getIsDeleted()) return value;

    if (value > curValue) {
        return recFindLarger(node->getRight(), value);
    }
    else {
        int leftResult = recFindLarger(node->getLeft(), value);
        if (leftResult != -1) return leftResult;
        else {
            if (!node->getIsDeleted()) return curValue;
            else return -1;
        }
    }

    
}


int Tree::removeLarger(int value) {
    return recRemoveLarger(_root, value);

}

int Tree::recRemoveLarger(Node* node, int value) {
    if (node == nullptr) return -1;

    int curValue = node->getValue();

    if (curValue == value && !node->getIsDeleted()) {
        node->decreaseCount();
        return value;
    }

    if (value > curValue) {
        return recRemoveLarger(node->getRight(), value);
    }
    else {
        int leftResult = recRemoveLarger(node->getLeft(), value);
        if (leftResult != -1) {
            return leftResult;
        }
        else {
            if (!node->getIsDeleted()) {
                node->decreaseCount();
                return curValue;
            }
            else return -1;
        }
    }
}