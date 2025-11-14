#include "TextClass.hpp"
#include <stdexcept>

TextClass::TextClass(){
    this->head = nullptr;
    this->tail = nullptr;
}

TextClass::~TextClass(){
    while (tail != nullptr){
        Node *nextTail = tail->getPrev();
        delete tail;
        tail = nextTail;
        }
}

void TextClass::addHead(char value){
    Node* newNode = new Node(value, head);
    
    // Handle if first item in list
    if (head != nullptr) 
        head->setPrev(newNode);
    if (tail == nullptr)
        tail = newNode;

    head = newNode;
    _count++;
}

void TextClass::addTail(char value){
    Node *newNode = new Node(value, nullptr, tail);
    if (tail != nullptr) tail->setNext(newNode);
    if (head == nullptr)
        head = newNode;
    tail = newNode;
    _count++;
}

char TextClass::getHead(){
    if (_count == 0) throw std::out_of_range("Empty List");

    return head->getValue();
}

char TextClass::getTail(){
    if (_count == 0) throw std::out_of_range("Empty List");

    return tail->getValue();
}

void TextClass::removeHead(){
    if (_count == 0)
        throw new std::out_of_range("Empty List");

    Node *prevHead = head;
    Node *newHead = head->getNext();
    if (newHead == nullptr){
        head = nullptr;
        tail = nullptr;
    }
    else head = newHead;
    delete prevHead;
    _count--;
}

void TextClass::removeTail(){
    Node *curTail = tail;
    Node *nextTail = tail->getPrev();

    if (nextTail == nullptr){
        tail = nullptr;
        head = nullptr;
    }
    else tail = nextTail;

    delete curTail;
    _count--;
}

std::string TextClass::displayList(){
    Node *curNode = head;
    bool isEqual = false;
    std::string list_to_display = "";
    for (int i = 0; i < _count; i++)
    {
        if (curNode == nullptr) {
            // std::cout << "curNode is null in displayList" << std::endl;
            break;
        }
        list_to_display += curNode->getValue();
        list_to_display += ' ';
        curNode = curNode->getNext();
        
    }
    curNode = nullptr;
    delete curNode;

    return list_to_display;
}

bool TextClass::find(char value){
    Node *curNode = head;
    for (int i = 0; i < _count; i++){
        if (value == curNode->getValue())
        {
            return true;
        }
        curNode = curNode->getNext();
    }
        return false;
}

bool TextClass::findRemove(char value){
    Node *curNode = head;
    Node *prev = curNode->getPrev();
    Node *next = curNode->getNext();
    while (curNode != nullptr)
    {
        char curValue = curNode->getValue();
        if (value == curValue){
            // Handle if removing head or tail
            if (prev == nullptr) {
                head = next;
            }
            else if (next == nullptr){
                tail = prev;
            }

            // Set prev and next to point to each other instead of cur
            else{
                prev->setNext(next);
                next->setPrev(prev);
            }

            // Delete unneeded memory
            prev = nullptr;
            next = nullptr;
            delete next;
            delete prev;
            delete curNode;

            _count--;

            return true;
        }

        // Retrieve next nodes to iterate through
        curNode = curNode->getNext();

        if (curNode != nullptr){
            prev = curNode->getPrev(); // Could possibly set this to curNode before changing curNode
            next = curNode->getNext();
        }
    }

    // Delete unneeded memory
    curNode = nullptr;
    next = nullptr;
    prev = nullptr;
    delete next;
    delete prev;
    delete curNode;

    return false;
}

void TextClass::append(const TextClass &otherList){
    Node *curOtherNode = otherList.head;
    while (true)
    {
        addTail(curOtherNode->getValue());
        curOtherNode = curOtherNode->getNext();
        _count++;

        if (curOtherNode == nullptr)
            break;
    }
}

bool TextClass::findNext(char value){
    // Handle if value not equal to curNode's value
    if (_curFindNext == nullptr || _curFindNext->getValue() != value){
        _curFindNext = head;
        while (_curFindNext != nullptr){
            if (_curFindNext->getValue() == value){
                return true;
            }

            _curFindNext = _curFindNext->getNext();
        }
    }
    // Handle if we're searching for same value as in curFindNext
    else{
        while (true){
            // Set curFindNext to next node since it should already hold the same value
            _curFindNext = _curFindNext->getNext();
            
            // Wrap if reached end
            if (_curFindNext == nullptr){
                _curFindNext = head;
            }

            if (_curFindNext->getValue() == value){
                return true;
            }
        }
    }

    // Couldn't find value
    _curFindNext = nullptr;
    return false;
}

void TextClass::removeLast(){
    if (_curFindNext == nullptr)
        return;

    Node *prev = _curFindNext->getPrev();
    Node *next = _curFindNext->getNext();
    // Handle if at head
    if (prev == nullptr){
        head = _curFindNext->getNext();
        delete _curFindNext;
        _curFindNext = nullptr;
    }
    // Handle if at tail
    else if (next == nullptr){
        tail = _curFindNext->getPrev();
        delete _curFindNext;
        _curFindNext = nullptr;
    }
    else{
        prev->setNext(next);
        next->setPrev(prev);
        delete _curFindNext;
        _curFindNext = nullptr;
    }
    _count--;
}

void TextClass::insertLast(char value){
    if (_curFindNext == nullptr){
        return;
    }

    Node *prev = _curFindNext->getPrev();
    Node *newNode = new Node(value, _curFindNext, prev);
    prev->setNext(newNode);
    _curFindNext->setPrev(newNode);
    _count++;
}

void TextClass::thinkSolve(TextClass& s2){
    Node *s1iter = head;
    Node *s2iter = s2.head;
    while (s1iter == nullptr || s2iter == nullptr || s1iter->getValue() == s2iter->getValue())
    {
        s1iter = s1iter->getNext();
        s2iter = s2iter->getNext();
    }

    TextClass andString = TextClass();
    andString.addTail(' ');
    andString.addTail('a');
    andString.addTail('n');
    andString.addTail('d');
    andString.addTail(' ');

    append(andString);

    while (s2iter != nullptr){
        addTail(s2iter->getValue());
        s2iter = s2iter->getNext();
    }

}