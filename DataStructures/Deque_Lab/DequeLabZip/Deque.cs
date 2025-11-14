using System;

namespace DequeDriver;

public class Deque
{
    private int[] _dequeArray;
    private int _validNums = 0;
    private int _head = 0;
    private int _tail = 0;
    private int _size = 0;

    public Deque(int n)
    {
        if (n < 1)
        {
            _dequeArray = new int[20];
            _size = 20;    
        }
        else
        {
            _dequeArray = new int[n];
            _size = n;    
        } 
    }

    public Deque()
    {
        _dequeArray = new int[20];
        _size = 20;
    }

    public void addTail(int value)
    {
        // WriteLineInColor($"validNums = {_validNums}, _size = {_size}, _tail = {_tail}, head = {_head}, value = {value}", ConsoleColor.Red);
        if (_validNums >= _size) resize();

        // Wrap if tail will exceed size
        if (_tail >= _size) _tail = 0;
        _dequeArray[_tail] = value;
        _tail++;
        _validNums++;
    }

    public int removeHead()
    {
        if (isEmpty()) throw new IndexOutOfRangeException("Array is empty in removeHead");
        int value = _dequeArray[_head];

        // Wrap if head will exceed size
        if (_head + 1 >= _size) _head = 0;
        else _head++;
        _validNums--;

        return value;
    }

    public string dumpArray()
    {
        string arrayDump = "";
        for (int i = 0; i < _size; i++)
        {
            arrayDump += $"{_dequeArray[i]} ";
        }

        return arrayDump;
    }

    public void resize()
    {
        // WriteLineInColor($"Resizing: _head = {_head}, _tail = {_tail}, _size = {_size}", ConsoleColor.Red);

        int[] newArray = new int[_size * 2];

        int numberAdded = 0;
        if (_head >= _tail)
        {
            // Add numbers from head to end first
            for (int i = _head; i < _size; i++)
            {
                // WriteLineInColor($"In loop: i = {i}, newArray[i-_head] = {newArray[i - _head]}, dequeArray[i] = {_dequeArray[i]}, i = {i}", ConsoleColor.Red);
                // Subtract _head from i to place at next location from beginning
                // Console.Write($"Head i = {i} | ");
                newArray[i - _head] = _dequeArray[i];
                numberAdded++;
            }
            // Console.WriteLine();

            // Add numbers from tail
            for (int i = 0; i < _tail; i++)
            {
                // Console.Write($"| {i} |");
                // WriteLineInColor($"In next loop: i = {i}, newArray[i + _head] = {newArray[i + _head]}, dequeArray[i] = {_dequeArray[i]}, i = {i}", ConsoleColor.Red);
                newArray[i + _head] = _dequeArray[i];
                numberAdded++;
            }

        }
        else
        {
            for (int i = _head; i < _tail; i++)
            {
                newArray[i - _head] = _dequeArray[i];
                numberAdded++;
                // WriteLineInColor($"newArray[i] = {newArray[i]}, dequeArray[i] = {_dequeArray[i]}, i = {i}", ConsoleColor.Red);
            }


        }

        _tail = numberAdded; // Tail = amount of numbers we just added to new array
        _dequeArray = newArray;
        _head = 0;
        _size *= 2;
        // WriteLineInColor($"After resizing: _head = {_head}, _tail = {_tail}, validNums = {_validNums}, _size = {_size}", ConsoleColor.Red);
    }

    public bool isEmpty()
    {
        if (_validNums <= 0)
        {
            return true;
        }

        return false;
    }

    public string listQueue()
    {
        string dump = "";

        // If wrapping
        if (_tail <= _head)
        {
            // Add numbers from head to end first
            for (int i = _head; i < _size; i++)
            {
                dump += $"{_dequeArray[i]} ";
            }

            // Add numbers from 0 to head last
            for (int i = 0; i < _head - 1; i++)
            {
                dump += $"{_dequeArray[i]} ";
            }
        }
        else
        {
            for (int i = 0; i < _tail; i++)
            {
                dump += $"{_dequeArray[i]} ";
            }
        }
        return dump;
    }

    public void addHead(int value)
    {
        // WriteLineInColor($"In addHead: head = {_head}, tail = {_tail}, validNums = {_validNums}, size = {_size}, value = {value}", ConsoleColor.Red);
        if (_validNums >= _size) resize();

        // Handle wrapping or add normally if not needed
        if (_head - 1 < 0)
        {
            _dequeArray[_size - 1] = value; // Wrap
            _head = _size - 1;
        }
        else
        {
            _dequeArray[_head - 1] = value; // Don't wrap
            _head--;
        }

        _validNums++;
        // WriteLineInColor(dumpArray(), ConsoleColor.Cyan);
        
    }

    public int removeTail()
    {
        // WriteLineInColor($"In removeTail: head = {_head}, tail = {_tail}, validNums = {_validNums}, size = {_size}", ConsoleColor.Red);

        if (isEmpty()) throw new IndexOutOfRangeException("Array is empty in removeTail");

        int value = 0;
        if (_tail - 1 < 0)
        {
            value = _dequeArray[_size - 1];
            _tail = _size - 1;
        }
        else
        {
            value = _dequeArray[_tail - 1];
            _tail--;
        }

        _validNums--;
        return value;
    }

    public void solveThink(int[] numbers, int size)
    {
        // Create and populate new deque
        Deque newDeque = new(size);
        for (int i = 0; i < size; i++)
        {
            newDeque.addTail(numbers[i]);
        }

        for (int i = 0; i < size; i++)
        {
            addHead(newDeque.removeHead());
        }
    }
    
    // private void WriteLineInColor(string line, ConsoleColor color)
    // {
    //     ConsoleColor previous = Console.ForegroundColor;
    //     Console.ForegroundColor = color;
    //     Console.WriteLine(line);
    //     Console.ForegroundColor = previous;
    // }
}
