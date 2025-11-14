#include "StringHash.hpp"
#include "Helpers.hpp"

StringHash::StringHash(int size) : _size(size){
    _array = new std::string[_size];
    _count = 0;

    for (int i = 0; i < _size; i++)
    {
        _array[i] = EMPTY_STRING;
    }
}

StringHash::~StringHash(){
    delete[] _array;
}

void StringHash::resize(){
    int newSize = Helpers::getNextPrime(_size);
    if (newSize == -1){
        throw std::logic_error("Invalid new prime...?");
    }

    // Initialize new array
    std::string *newArray = new std::string[newSize];
    for (int i = 0; i < newSize; i++){
        newArray[i] = EMPTY_STRING;
    }
    // std::cout << "_array before resizing \n"
            //   << displayTable() << std::endl;

    // Loop through previous array to rehash value into new array
    for (int i = 0; i < _size; i++){
        if (_array[i] != EMPTY_STRING && _array[i] != DELETED_STRING){
            int index = Helpers::hashFunc(_array[i], newSize);
            // std::cout << _array[i] << " is hashing to " << index << std::endl;
            while (newArray[index] != EMPTY_STRING)
            {
                index++;
                if (index >= newSize){
                    index = 0;
                }
            }
            // std::cout << _array[i] << " ended up at " << index << std::endl;
            newArray[index] = _array[i];
        }
    }

    // Copy newArray into _array and delete unused memory
    delete[] _array;
    _array = newArray;
    newArray = nullptr;
    _size = newSize;
    delete newArray;

    // std::cout << "_array after resizing \n"
            //   << displayTable() << std::endl;
}



void StringHash::addItem(std::string value){
    // Resize if needed
    if (_count >= _size / 2){
        resize();
    }

    // Get index hash. Then loop until empty position found
    int index = Helpers::hashFunc(value, _size);

    while (_array[index] != EMPTY_STRING){
        index += 1;
        if (index >= _size)
            index = 0;
    }

    _count++;
    _array[index] = value;
}

bool StringHash::findItem(std::string value){
    int index = Helpers::hashFunc(value, _size);
    bool found = false;

    // Loop through positions till empty found or value
    while (_array[index] != EMPTY_STRING && !found){
        if (_array[index] == value) {
            found = true;
        }
        else{
            index++;
            if (index >= _size)
                index = 0;
        }
    }

    return found;
}

void StringHash::removeItem(std::string value){
    int index = Helpers::hashFunc(value, _size);
    int numOfIterations = 0;

    while (_array[index] != EMPTY_STRING){
        // Value is not in array. Throw error?
        if (numOfIterations > _size){
            throw std::invalid_argument("Couldn't find value");
        }

        if (_array[index] == value){
            _array[index] = DELETED_STRING;
            break;
        }

        numOfIterations++;
        index++;
        if (index >= _size)
            index = 0;
    }
}

std::string StringHash::displayTable(){
    std::string table = "";

    for (int i = 0; i < _size; i++){
        table += _array[i];
        table += "\n";
    }

    return table;
}

