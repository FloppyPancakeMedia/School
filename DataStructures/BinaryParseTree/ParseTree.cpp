#include "ParseTree.hpp"
#include <iostream>
#include <set>
#include <queue>
#include <sstream>
#include <iomanip>

ParseTree::ParseTree(std::string expression) {
    if (expression == "") {
        _root = nullptr;
    }
    else {
        std::stack<Node*> theStack;
        for (int i = 0; i < expression.size(); i++) {
            char letter = expression[i];

            // Skip if isSpace
            if (letter == ' ') {
                continue;
            }

            bool isThing = isOperator(letter);
            if (isThing) {
                // Is an operator; push to stack
                Node* temp = new Node(letter);
                if (theStack.top() != nullptr) {
                    temp->setRight(theStack.top());
                    theStack.pop();
                    temp->setLeft(theStack.top());
                    theStack.pop();
                }

                theStack.push(temp);
            }
            else {
                // Is letter; 
                theStack.push(new Node(letter));

            }
        }
        _root = theStack.top();
    }
}

ParseTree::~ParseTree() {
    delete _root;
}

std::string ParseTree::preOrder() {
    return getPreOrder(_root);
}

std::string ParseTree::getPreOrder(Node* node) {
    std::string buffer = "";
    if (node == nullptr) {
        return buffer;
    }
    buffer += node->getValue();
    buffer += getPreOrder(node->getLeft());
    buffer += getPreOrder(node->getRight());

    return buffer;
}

std::string ParseTree::inOrder() {
    return getInOrder(_root);
}

std::string ParseTree::getInOrder(Node* node, char parentOp, bool isRightChild) {
    std::string buffer = "";

    if (node == nullptr) {
        return buffer;
    }

    // Check precedence for parentheses
    bool isParent = node->getLeft() || node->getRight();
    bool hasPrecedence = false;
    if (isParent) {
        char value = node->getValue();
        hasPrecedence = isPrecedent(parentOp, value);
        if (hasPrecedence) {
            buffer += "(";
        }
    }

    buffer += getInOrder(node->getLeft(), node->getValue());
    buffer += node->getValue();
    buffer += getInOrder(node->getRight(), node->getValue(), true);

    if (hasPrecedence) {
        buffer += ")";
    }
    return buffer;
}

std::string ParseTree::postOrder() {
    return getPostOrder(_root);
}

std::string ParseTree::getPostOrder(Node* node) {
    std::string buffer = "";
    if (node == nullptr) {
        return buffer;
    }

    buffer += getPostOrder(node->getLeft());
    buffer += getPostOrder(node->getRight());
    buffer += node->getValue();

    return buffer;
}


void ParseTree::parseInOrder(std::string infix) {
    delete _root;

    // convert "A/(B+C)*(D+E)" to ABC+/DE+*
    std::stack<char> theStack;
    std::string buffer = "";

    for (int i = 0; i < infix.length(); i++) {
        char value = infix[i];
        if (isOperand(value)) {
            buffer += value;
        }

        else if (value == '(') {
            theStack.push(value);
        }
        else if (value == ')') {
            bool isPopping = true;
            while (!theStack.empty() && isPopping) {
                char newValue = theStack.top();
                theStack.pop();

                if (newValue == '(') {
                    isPopping = false;
                }
                else {
                    buffer += newValue;
                }
            }
        }

        else if (isOperator(value)) {
            bool isPopping = true;

            while (!theStack.empty() && isPopping) {
                char next = theStack.top();
                theStack.pop();

                if (next == '(') {
                    theStack.push(next);
                    isPopping = false;
                }
                else {
                    // std::cout << "Checking precedence of " << value << " vs " << next << " which is " << isPrecedent(value, next) << std::endl;
                    if (isPrecedent(value, next)) {
                        theStack.push(next);
                        isPopping = false;
                    }
                    else {
                        buffer += next;
                    }

                }

            }
            theStack.push(value);
        }
    }
    // Get remaining operators on stack
    while (!theStack.empty()) {
        buffer += theStack.top();
        theStack.pop();
    }


    ParseTree* newTree = new ParseTree(buffer);
    this->_root = newTree->_root;
}

bool ParseTree::isOperand(char c) {

    static const std::set<char> operators = {
        '+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '~', '(', ')'
    };

    bool isIt = operators.count(c) == 0;
    return isIt;
}

bool ParseTree::isOperator(char c) {
    static const std::set<char> operators = {
        '+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '~'
    };

    bool isIt = operators.count(c) > 0;

    return operators.count(c) > 0;
}

bool ParseTree::isPrecedent(char parentOp, char childOp) {
    short parentPrec = getPrec(parentOp);
    short childPrec = getPrec(childOp);
    if (parentPrec == childPrec) {
        if (parentOp == '/' || parentOp == '-') {
            return true;
        }
        else {
            return false;
        }
    }

        return parentPrec > childPrec;
}

int ParseTree::getPrec(char op) {
    switch (op) {
        case '/': case '*': return 2;
        case '+': case '-': return 1;
        default: return 0;
    }
}

std::string ParseTree::display() {
    // arbitrary width of the display
    const int PAGE_WIDE = 64;
    // dummy placeholder for null leaves
    Node* dummy = nullptr;
    // empty node output
    std::string emptyNode = ".";
    // define buffer to collect output
    std::stringstream buffer;
    // define queue (FIFO) to hold next layer's nodes
    std::queue<Node*> theQueue;
    // boolean to keep track of when no nodes in layer
    bool more = true;
    // start with the root
    theQueue.push(_root);

    // first layer has one node
    int curNodes = 1;
    // while there are nodes in the queue
    while (more)
    {
        more = false;
        // calculate the base offset
        int offset = PAGE_WIDE / (curNodes * 2);
        // process the nodes in the layer
        for (int i = 0; i < curNodes; i++)
        {
            // get and remove front node
            Node* ptr = theQueue.front();
            theQueue.pop();
            // all offsets after the first are doubled
            if (i == 1)
            {
                offset *= 2;
            }
            // if not a dummy node process it
            if (ptr != dummy)
            {
                // add contents to buffer
                buffer << std::setw(offset) << ptr->getValue();
                // if there is a left child, add to fifo
                if (ptr->getLeft())
                {
                    more = true;
                    theQueue.push(ptr->getLeft());
                }
                // no left child, add dummy in its place
                else
                {
                    theQueue.push(dummy);
                }
                // if right child, add to fifo
                if (ptr->getRight())
                {
                    more = true;
                    theQueue.push(ptr->getRight());
                }
                // no right child, add dummy in its place
                else
                {

                    theQueue.push(dummy);
                }
            }
            // this node was a dummy
            // output the emptyNode symbol
            // add two dummies to FIFO for children placeholders
            else
            {
                buffer << std::setw(offset) << emptyNode;
                theQueue.push(dummy);
                theQueue.push(dummy);
            }
        }
        curNodes *= 2;
        buffer << std::endl;
    }
    return buffer.str();
}
