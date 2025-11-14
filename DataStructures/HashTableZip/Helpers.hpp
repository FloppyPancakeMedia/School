#include <stdlib.h>
#include <string>
#include <vector>

#ifndef HELPERS_H
#define HELPERS_H

class Helpers
{
private:
    static bool isPrime(int value);
public:
    static std::vector<int> primes;
    static int hashFunc(std::string key, int modulus);
    static int getNextPrime(int size);
};

#endif