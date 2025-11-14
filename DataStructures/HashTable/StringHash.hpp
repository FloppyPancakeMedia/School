#include<stdlib.h>
#include<iostream>
#include<string>
#include<vector>


#ifndef STRINGHASH_H
#define STRINGHASH_H

class StringHash {
private:
    const std::string EMPTY_STRING = "_empty_";
    const std::string DELETED_STRING = "_deleted_";
    int _size;
    int _count;
    std::string *_array;

    void resize();
    

public:
    StringHash(int size = 11);
    ~StringHash();
    void addItem(std::string value);
    bool findItem(std::string value);
    void removeItem(std::string value);
    std::string displayTable();
};

#endif