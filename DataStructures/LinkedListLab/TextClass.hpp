#ifndef TEXTCLASS

#define TEXTCLASS
#include "Node.hpp"
#include<stdlib.h>
#include<string>
#include<iostream>

class TextClass{
    private:
        Node *head;
        Node *tail;
        int _count = 0;
        Node *_curFindNext = nullptr;

    public:
        TextClass();
        ~TextClass();
        void addHead(char value);
        void addTail(char value);
        char getHead();
        char getTail();
        void removeHead();
        void removeTail();
        bool find(char value);
        bool findRemove(char value);
        std::string displayList();
        void append(const TextClass &otherList);
        bool findNext(char value);
        void removeLast();
        void insertLast(char value);
        void thinkSolve(TextClass& s1);
};

#endif