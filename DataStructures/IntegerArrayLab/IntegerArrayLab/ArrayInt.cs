using System;
using System.IO;

namespace ArrayIntDriver
{
    public class ArrayInt
    {
        private int[] _IntArray;
        private int _index = 0;
        private int _size = 0;
        public ArrayInt(int n)
        {
            if (n < 1)
            {
                _IntArray = new int[10];
                _size = 10;
            }
            else
            {
                _IntArray = new int[n];
                _size = n;
            }
        }

        public ArrayInt()
        {
            _IntArray = new int[10];
            _size = 10;
        }

        public int GetSize()
        {
            return _size;
        }

        public void Append(int value)
        {
            // Create new int array to expand _IntArray
            if (_index >= _size)
            {
                Resize(_size * 2);
            }

            _IntArray[_index] = value;
            _index += 1;
        }

        public int GetLast()
        {
            if (_index == 0)
            {
                throw new IndexOutOfRangeException("Array is empty!");
            }

            return _IntArray[_index - 1];
        }

        public void DeleteLast()
        {
            if (_index == 0)
            {
                throw new IndexOutOfRangeException("Array is empty!");
            }

            _index -= 1;
        }

        public void Resize(int newSize)
        {
            // Do nothing if _size is less than/equal to cur _size
            if (newSize <= _size) return;

            int[] newIntArray = new int[newSize];

            for (int i = 0; i < _size; i++)
            {
                newIntArray[i] = _IntArray[i];
            }

            _IntArray = newIntArray;
            _size = newSize;
        }

        public string ListElements()
        {
            if (_index == 0) return "Empty Array";

            string list = "";
            for (int i = 0; i < _index; i++)
            {
                list += $" {_IntArray[i]}";
            }

            return list;
        }

        public bool Find(int value)
        {
            for (int i = 0; i < _index; i++)
            {
                if (_IntArray[i] == value) return true;
            }

            return false;
        }

        public bool RemoveVal(int value)
        {
            bool isInArray = false;
            int valueLocation = 0;

            // Check if num is in array
            for (int i = 0; i < _index; i++)
            {
                if (_IntArray[i] == value)
                {
                    isInArray = true;
                    valueLocation = i;
                    break;
                }
            }

            if (isInArray == false) return false;

            // Do actual removal
            for (int i = valueLocation; i < _index - 1; i++)
            {
                // Console.WriteLine($"i = {i}");
                _IntArray[i] = _IntArray[i + 1];
            }

            _index--;

            return true;
        }

        public int FindLargest()
        {
            if (_index == 0)
            {
                throw new IndexOutOfRangeException("Attempt to read from empty array.");
            }
            int largest = _IntArray[0];

            for (int i = 0; i < _index; i++)
            {
                if (_IntArray[i] > largest)
                {
                    largest = _IntArray[i];
                }
            }

            return largest;
        }

        public void RemoveLargest()
        {
            if (_index == 0)
            {
                throw new IndexOutOfRangeException("Attempt to remove from empty array.");
            }

            int largest = FindLargest();

            for (int i = 0; i < _index; i++)
            {
                if (_IntArray[i] == largest)
                {
                    bool didItWork = RemoveVal(largest);
                    return;
                }
            }
        }

        public void InsertAt(int index, int value)
        {
            if (index < 0 || index > _index || index > _size) throw new IndexOutOfRangeException("Attempt to write at invalid location.");

            if (_index >= _size) Resize(_size * 2);

            for (int i = _index; i > index; i--)
            {
                _IntArray[i] = _IntArray[i - 1];
            }

            _index++;
            _IntArray[index] = value;
        }

        public int RemoveAt(int index)
        {
            if (_index == 0) throw new IndexOutOfRangeException("Attempt to remove from empty array.");
            if (index < 0 || index > _index) throw new IndexOutOfRangeException("Attempt to remove from invalid location");

            int savedValue = _IntArray[index];

            for (int i = index; i < _index; i++)
            {
                _IntArray[i] = _IntArray[i + 1];
            }
            
            _index--;
            return savedValue;
        }

        public void SolveThink(int[] integers, int newSize)
        {
            int[] orderedArray = new int[newSize];
            ArrayInt uoArray = new(newSize);
            // Populate unordered array
            for (int i = 0; i < newSize; i++)
            {
                uoArray.Append(integers[i]);
            }

            for (int i = 0; i < newSize; i++)
            {
                orderedArray[i] = uoArray.FindLargest();
                uoArray.RemoveLargest();
            }

            _IntArray = orderedArray;
            _index = newSize;
            return;
        }

        private void WriteLineInColor(string message, ConsoleColor color)
        {

            ConsoleColor previous = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ForegroundColor = previous;
        }
    }
}