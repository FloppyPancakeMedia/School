#include "ChainHash.hpp"
#include "Helpers.hpp"

ChainHash::ChainHash(int size) : _size(size), _curElements(0)
{
    // Initialize empty array and empty link pointers
    _array = new ChainLink * [size];
    for (int i = 0; i < size; i++)
    {
        _array[i] = nullptr;
    }
}

ChainHash::~ChainHash()
{
    // Delete all links in array
    for (int i = 0; i < _size; i++)
    {
        ChainLink* current = _array[i];
        while (current != nullptr)
        {
            ChainLink* next = current->getNext();
            delete current;
            current = next;
        }
    }

    delete[] _array;
}

void ChainHash::addItem(std::string value)
{
    // Check size to see if need resizing
    if (_curElements > _size * 2) {
        resize();
    }

    int index = Helpers::hashFunc(value, _size);

    ChainLink* newLink = new ChainLink(value);
    // No start link at index. Add this one.
    if (_array[index] == nullptr)
    {
        _array[index] = newLink;
    }
    // Link already exists at index. Loop through links in array[index] and add to end
    else
    {
        ChainLink* curLink = _array[index];
        while (curLink->getNext() != nullptr)
        {
            curLink = curLink->getNext();
        }

        curLink->setNext(newLink);
    }
    _curElements++;
}

bool ChainHash::findItem(std::string value)
{
    int index = Helpers::hashFunc(value, _size);
    ChainLink* curLink = _array[index];
    // std::cout << "curLink = " << curLink << std::endl;
    // Nothing at this index
    if (curLink == nullptr)
    {
        return false;
    }
    // Check first link
    else if (curLink->getValue() == value)
    {
        return true;
    }
    // If not first link, loop through links in array[index]
    else
    {
        while (curLink != nullptr)
        {
            if (curLink->getValue() == value)
            {
                return true;
            }
            else
            {
                curLink = curLink->getNext();
            }
        }
    }

    // Couldn't find it
    return false;
}

void ChainHash::removeItem(std::string value)
{
    int index = Helpers::hashFunc(value, _size);
    ChainLink* curLink = _array[index];

    // Check if valid object at index
    if (curLink == nullptr)
    {
        std::cout << "Couldn't find " << value << ". Returning..." << std::endl;
    }
    else
    {
        // First object holds value
        if (curLink->getValue() == value)
        {
            _array[index] = curLink->getNext();
            delete curLink;
        }
        // Still need to find proper object
        else
        {
            // Loop through links to find proper object
            while (curLink != nullptr)
            {
                if (curLink->getValue() == value)
                {
                    break;
                }
                else
                {
                    curLink = curLink->getNext();
                    if (curLink == nullptr)
                    {
                        std::cout << "Couldn't find " << value << ". Returning..." << std::endl;
                        return;
                    }
                }
            }

            // Check for previous link
            ChainLink* previousLink = _array[index];
            while (true)
            {
                if (previousLink->getNext() == curLink)
                {
                    break;
                }
                // Shouldn't trigger
                else if (previousLink->getNext() == nullptr)
                {
                    std::cout << "Something weird happened when determining previous link.... " << std::endl;
                    return;
                }
                else
                {
                    previousLink = previousLink->getNext();
                }
            }

            // Found previous link. Set it's _next to curLink's _next
            previousLink->setNext(curLink->getNext());

            previousLink = nullptr;
            delete curLink, previousLink;
        }
    }

    _curElements--;
}

std::string ChainHash::displayTable()
{
    std::string buffer = "";
    for (int i = 0; i < _size; i++)
    {
        ChainLink* curLink = _array[i];
        // No value found. Skip.
        if (curLink == nullptr)
        {
            buffer += "_empty_";
        }
        // Loop through all links in index
        else
        {
            while (true)
            {
                if (curLink == nullptr)
                {
                    break;
                }
                else
                {
                    buffer += curLink->getValue();
                    buffer += ' ';
                    curLink = curLink->getNext();
                }
            }
        }
        buffer += "\n";
    }

    return buffer;
}

void ChainHash::resize()
{
    // Create new array with new size
    int newSize = Helpers::getNextPrime(_size);
    // std::cout << "new size = " << newSize << ". Changed from " << _size << std::endl;
    ChainLink** newArray = new ChainLink * [newSize];

    // Populate vector with all available ChainLinks
    std::vector<ChainLink*> links;
    for (int i = 0; i < _size; i++) {
        if (_array[i] == nullptr) {
            continue;
        }
        else {
            ChainLink* curLink = _array[i];
            while (true) {
                if (curLink == nullptr) {
                    break;
                }
                else {
                    links.push_back(curLink);
                    curLink = curLink->getNext();
                }
            }
        }
    }

    delete _array;

    // Get hash for all chain links and add to new array
    for (int i = 0; i < links.size(); i++) {
        // Reset curLink
        ChainLink* curLink = links[i];
        curLink->setNext(nullptr);

        std::string value = links[i]->getValue();
        int index = Helpers::hashFunc(value, newSize);

        if (newArray[index] == nullptr) {
            newArray[index] = curLink;
        }
        else {
            // Find last link in chain
            ChainLink* indexedLink = newArray[index];
            while (true) {
                if (indexedLink->getNext() == nullptr) {
                    indexedLink->setNext(curLink);
                    break;
                }
                else {
                    indexedLink = indexedLink->getNext();
                }
            }
        }
    }

    _size = newSize;
    _array = newArray;
}