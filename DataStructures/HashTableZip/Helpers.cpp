#include <stdlib.h>
#include <iostream>
#include "Helpers.hpp"


int Helpers::hashFunc(std::string key, int modulus){
    int hashValue = 0;

    for (int i = 0; i < key.size(); i++){
        hashValue *= 128;
        hashValue += static_cast<int>(key[i]);
        hashValue %= modulus;
    }

    return hashValue;
}

int Helpers::getNextPrime(int size){
    int newSize = size * 2;
    bool isPrime = false;
    
    while (!Helpers::isPrime(newSize)) {
        newSize++;
    }

    return newSize;
}

bool Helpers::isPrime(int value) {
    int upperLimit = value / 2;
    for (int i = 2; i < upperLimit; i++) {
        if (value % i == 0) {
            return false;
        }
    }

    return true;
}