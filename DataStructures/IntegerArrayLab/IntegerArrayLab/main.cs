/*
 * Directly transpiled from Jim Bailey's C++ driver for this assignment 
 */

using System;
using System.IO;

namespace ArrayIntDriver
{
    class Driver
    {
        static void Main(string[] args)
        {
            // Uncomment test functions to run

            // TestConstructor();
            // TestAppend();
            // TestMakeRoom();
            // TestFind();
            // TestFindLargest();

            // TestInsertRemove();
            // TestMixed();

            TestThink();
        }

        static void TestConstructor()
        {
            const int DEFAULT = 10;
            const int OVERLOAD = 15;
            Console.Write("TESTING default and overloaded constructors.\n\n");

            ArrayInt defaultSize = new ArrayInt();
            ArrayInt defineSize = new ArrayInt(OVERLOAD);

            Console.Write("Default size should be " + DEFAULT + " and is " + defaultSize.GetSize() + "\n");
            Console.Write("Overload size should be " + OVERLOAD + " and is " + defineSize.GetSize() + "\n\n");

            Console.Write("Done with constructor test\n\n\n");
        }

        static void TestAppend()
        {
            Console.Write("TESTING Append, GetLast, and DeleteLast\n\n");

            ArrayInt appends = new ArrayInt();
            const int NUM_APPENDS = 5;
            int[] appendVals = new int[NUM_APPENDS];
            ReadInVals(appendVals, NUM_APPENDS, 0);

            for (int i = 0; i < NUM_APPENDS; i++)
            {
                appends.Append(appendVals[i]);
            }

            Console.Write("After APPEND array should be:");
            for (int i=NUM_APPENDS-1; i>=0; i--) Console.Write(" " + appendVals[i]);
            Console.Write("\n             array really is:");
            try
            {
                for (int i=0; i<NUM_APPENDS; i++)
                {
                    Console.Write(" " + appends.GetLast());
                    appends.DeleteLast();
                }
                Console.Write("\n");
            }
            catch (Exception)
            {
                Console.Write("Problem with appending and deleting\n");
            }

            Console.Write("Trying GetLast on empty array, should throw exception\n");
            try
            {
                Console.Write(appends.GetLast() + "\n");
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }

            Console.Write("Trying to delete from empty array, should throw exception\n");
            try
            {
                appends.DeleteLast();
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }

            Console.Write("\n\n");
        }

        static void TestMakeRoom()
        {
            const int START = 7;
            const int UPDATE = 12;
            int[] roomVals = new int[UPDATE];
            ReadInVals(roomVals, UPDATE, 1);

            Console.Write("TESTING Resize, auto expansion on appends, and ListElements\n\n");

            ArrayInt room = new ArrayInt(START);
            Console.Write("Starting size should be " + START + " and is " + room.GetSize() + "\n");
            room.Resize(UPDATE);
            Console.Write("After SetSize, size should be " + UPDATE + " and is " + room.GetSize() + "\n");

            Console.Write("\nNow going to fill array and see if it expands\n");
            for (int i = 0; i < UPDATE; i++) {
                room.Append(roomVals[i]);
            }
            Console.Write("Filled with 12 values, no problem\n");
            Console.Write("Size should still be " + UPDATE + " and is " + room.GetSize() + "\n");
            Console.WriteLine(room.ListElements());
            Console.Write("\nAdding one more\n");
            room.Append(88);
            Console.Write("Size should now be " + 2 * UPDATE + " and is " + room.GetSize() + "\n");

            Console.Write("\nAfter MAKE ROOM should be:");
            for (int i=0; i<UPDATE; i++) Console.Write(" " + roomVals[i]);
            Console.Write(" 88\n");
            Console.Write("                really is:" + room.ListElements());

            Console.Write("\n\n");
        }


        static void TestFind()
        {
            const int FIND_COUNT = 10;
            int[] findRemVals = new int[FIND_COUNT];
            ReadInVals(findRemVals, FIND_COUNT, 1);

            Console.Write("TESTING Find and RemoveVal \n\n");

            ArrayInt findRemove = new ArrayInt();
            for (int i = 0; i < FIND_COUNT; i++) {
                findRemove.Append(findRemVals[i]);
            }
            int lastEl = findRemVals[FIND_COUNT-1];

            Console.Write("Array contains " + findRemove.ListElements() + "\n");

            Console.Write("Testing Find on 4 and 7.\n");
            Console.Write("  4" + (findRemove.Find(4) ? " was " : " was not ") + "found\n");
            Console.Write("  7" + (findRemove.Find(7) ? " was " : " was not ") + "found\n");

            Console.Write("Testing RemoveVal on 4 and 7.\n");
            Console.Write("  4" + (findRemove.RemoveVal(4) ? " was " : " was not ") + "removed\n");
            Console.Write("  7" + (findRemove.RemoveVal(7) ? " was " : " was not ") + "removed\n");

            Console.Write("After REMOVE expected:");
            for (int i=0; i<FIND_COUNT; i++) 
                if ((findRemVals[i]!=4) && (findRemVals[i]!=7)) Console.Write(" " + findRemVals[i]);
            Console.Write("\n             actually:" + findRemove.ListElements() + "\n\n");

            Console.Write("Using RemoveVal on final element, " + lastEl + "\n");
            Console.Write(lastEl + (findRemove.RemoveVal(lastEl) ? " was " : " was not ") + "removed\n");

            Console.Write("Using find to look for " + lastEl + " after removal.  Should not find\n");
            Console.Write(lastEl + (findRemove.Find(lastEl) ? " was " : " was not ") + "found\n\n\n");
        }

        static void TestFindLargest()
        {
            const int LARGE_COUNT = 8;
            Console.Write("TESTING FindLargest and RemoveLargest \n\n");

            ArrayInt findLarge = new ArrayInt();
            int[] largeVals = new int[LARGE_COUNT] { 3, 11, 19, 7, 5, 2, 13, 23 };
            for (int i = 0; i < LARGE_COUNT; i++)
            {
                findLarge.Append(largeVals[i]);
            }

            Console.Write("Array contains " + findLarge.ListElements() + "\n");

            Console.Write("Largest should be 23 and is " + findLarge.FindLargest() + "\n");

            findLarge.RemoveLargest();
            findLarge.RemoveLargest();
            Console.Write("After removing two largest should be: 3 11 7 5 2 13\n");
            Console.Write("                         actually is:" + findLarge.ListElements() + "\n");

            Console.Write("Emptying array\n");
            for (int i = 0; i < LARGE_COUNT - 2; i++)
            {
                findLarge.DeleteLast();
            }

            Console.Write("\nNow testing FindLargest on empty array\n");
            try
            {
                findLarge.FindLargest();
                Console.Write("Should have thrown an exception\n");
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }

            Console.Write("Now testing RemoveLargest on empty array\n");
            try
            {
                findLarge.RemoveLargest();
                Console.Write("Should have thrown an exception\n");
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }

            Console.Write("\n\n");
        }


                static void TestInsertRemove()
        {
            const int BEGIN = 10;
            Console.Write("TESTING InsertAt and RemoveAt \n\n");
            
            int[] insRemVals = new int[BEGIN];
            ReadInVals(insRemVals, BEGIN, 3);
            ArrayInt insertRemove = new ArrayInt();
            for (int i = 0; i < BEGIN; i++) {
                insertRemove.Append(insRemVals[i]);
            }

            Console.Write("Array starting with: " + insertRemove.ListElements());

            Console.Write("\nSize should be " + BEGIN + " and is " + insertRemove.GetSize() + "\n");

            Console.Write("\nNow inserting 5 at index 2\n");
            insertRemove.InsertAt(2, 5);
            Console.Write("Size should be " + 2 * BEGIN + " and is " + insertRemove.GetSize() + "\n");
            Console.Write("  After INSERT AT expected:");
            for (int i=0; i<2; i++) Console.Write(" " + insRemVals[i]);
            Console.Write(" 5");
            for (int i=2; i<BEGIN; i++) Console.Write(" " + insRemVals[i]);
            Console.Write("\n  After INSERT AT actually:");
            Console.Write(insertRemove.ListElements());

            Console.Write("\n\nTrying to remove values at indices: 8 2 0\n");
            Console.Write("                           Removed: ");
            Console.Write(insertRemove.RemoveAt(8) + " "
                        + insertRemove.RemoveAt(2) + " "
                        + insertRemove.RemoveAt(0) + "\n");

            Console.Write("  After REMOVE AT expected:");
            for (int i=1; i<7; i++) Console.Write(" " + insRemVals[i]);
            for (int i=8; i<BEGIN; i++) Console.Write(" " + insRemVals[i]);
            Console.Write("\n  After REMOVE AT actually:");
            Console.Write(insertRemove.ListElements());

            Console.Write("\n\nNow testing illegal inserts and removes \n");
            Console.Write("Testing invalid InsertAt at index larger than array size\n");
            try
            {
                insertRemove.InsertAt(BEGIN * 3, -1);
                Console.Write("Should have thrown an exception inserting at " + BEGIN * 3 + "\n");
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }

            Console.Write("Testing invalid InsertAt at negative index\n");
            try
            {
                insertRemove.InsertAt(-1, 500);
                Console.Write("Should have thrown an exception inserting at -1\n");
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }

            Console.Write("\nEmptying the array, expecting:");
            for (int i=BEGIN-1; i>7; i--) Console.Write(" " + insRemVals[i]); 
            for (int i=6; i>0; i--) Console.Write(" " + insRemVals[i]);
            Console.Write("\n  Actually removed the values:");
            for (int i = 0; i < BEGIN-2; i++)
            {
                Console.Write(" " + insertRemove.GetLast());
                insertRemove.DeleteLast();
            }
            Console.WriteLine();

            Console.Write("\nNow testing RemoveAt on empty array\n");
            try
            {
                insertRemove.RemoveAt(0);
                Console.Write("Should have thrown an exception\n");
            }
            catch (IndexOutOfRangeException e)
            {
                Console.Write("Caught out of range with message: " + e.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something weird \n");
            }
            Console.Write("\n\n");

        }

        static void TestMixed()
        {
            Console.Write("TESTING a mixture of Appends, InsertAts, and RemoveAts\n");

            ArrayInt mixed = new ArrayInt();

            mixed.Append(2);
            mixed.Append(4);
            mixed.Append(6);
            mixed.DeleteLast();
            mixed.Append(50000);
            mixed.InsertAt(0, 16);
            mixed.Append(32);
            mixed.InsertAt(2, 19);
            mixed.Append(256);
            mixed.RemoveLargest();
            mixed.Append(64);
            mixed.RemoveAt(4);

            Console.Write("Displaying the results\n");
            Console.Write("  After MIX expected: 16 2 19 4 256 64\n");
            Console.Write("  After MIX actually:" + mixed.ListElements());

            Console.Write("\nDone testing mixed\n\n\n");
        }

        static void TestThink()
        {
            Console.Write("TESTING the thinking problem\n");

            ArrayInt think = new ArrayInt();
            const int NUM_THINK = 10;
            int[] thinkVals = new int[NUM_THINK];
            ReadInVals(thinkVals, NUM_THINK, 3);

            Array.Sort(thinkVals, (x, y) => y.CompareTo(x));
            Console.Write("  After THINK expected:");
            for (int i=0; i<NUM_THINK; i++) Console.Write(" " + thinkVals[i]);

            think.SolveThink(thinkVals, NUM_THINK);
            Console.Write($"\n  After THINK actually:{think.ListElements()}");
            Console.Write("\nDone with thinking test\n\n");


        }

        static void ReadInVals(int[] arr, int numElems, int skipLines)
        {
            string path = Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "input");

            try
            {
                using (StreamReader inputFile = new StreamReader(path))
                {   
                    string line;

                    for (int i = 0; i < skipLines; i++)
                    {
                        if (inputFile.ReadLine() == null)
                        {
                            Console.Error.WriteLine("Error: Reached end of file while skipping lines!");
                            return;
                        }
                    }

                    line = inputFile.ReadLine();
                    string[] parts = line.Split(' ');
                    //Console.WriteLine(line); 

                    for (int i = 0; i < numElems; i++)
                    {
                        if (!(i < parts.Length && int.TryParse(parts[i], out arr[i])))
                        // {
                        //     // Successfully parsed the value into the array
                        //     Console.WriteLine($"arr[{i}] = {arr[i]}");
                        // }
                        // else
                        {
                            // Error reading value from the file
                            Console.Error.WriteLine($"Error reading values from file at index {i}!");
                            return;
                        }
                    }

                }
            }
            catch (Exception ex)
            {
                Console.Error.WriteLine($"Error reading values from file: {ex.Message}");
                Environment.Exit(1);
            }
        }

    }
}

