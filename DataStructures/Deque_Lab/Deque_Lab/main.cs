using System;

namespace DequeDriver
{
    class Driver
    {
        static void Main(string[] args)
        {
            // uncomment function to select a given test

            QueueTest();
            ResizeTest();
            ListTest();
            AddHeadTest();
            RemoveTailTest();
            RevQueueTest();
            MixTest();
            ThinkTest();
        }

        static void QueueTest()
        {
            const int NUM_QUEUE = 8;
            int num = 0;
            Deque queue = new Deque();

            Console.Write("Testing basic queue, addTail, removeHead, isEmpty\n\n");

            Console.Write("Adding eight odd integers to FIFO\n");
            for (int i = 0; i < NUM_QUEUE; i++)
            {
                queue.addTail(2 * num + 1);
                num += 1;
            }

            Console.Write("Expected 1 3 5 7 9 11 13 15\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_QUEUE; i++)
            {
                Console.Write(queue.removeHead() + " ");
            }
            Console.WriteLine();

            Console.Write("\nFIFO should be empty\n");
            Console.Write("FIFO " + (queue.isEmpty() ? "is " : "is not ") + "empty\n");

            Console.Write("\nDone with basic test\n\n");
        }

        static void ResizeTest()
        {
            const int NUM_RESIZE = 8;
            const int NUM_RESIZE_EXTRA = 4;
            Deque resize = new Deque(NUM_RESIZE);
            int num = 0;

            Console.Write("Testing resizing queue, addTail, removeHead\n\n");

            Console.Write("Adding eight odd integers to FIFO\n");
            for (int i = 0; i < NUM_RESIZE; i++)
            {
                resize.addTail(2 * num + 1);
                num += 1;
            }
            Console.Write("Removing four to cause wrap\n");
            Console.Write("Expected 1 3 5 7\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_RESIZE_EXTRA; i++)
            {
                Console.Write(resize.removeHead() + " ");
            }
            Console.WriteLine();

            Console.Write("\nAdding four more for wrapping\n");
            for (int i = 0; i < NUM_RESIZE_EXTRA; i++)
            {
                resize.addTail(2 * num + 1);
                num += 1;
            }

            Console.Write("Dumping the array \n");
            Console.Write("Expected 17 19 21 23 9 11 13 15\n");
            Console.Write("Actually " + resize.dumpArray() + "\n");

            Console.Write("\nNow adding eight more\n");
            for (int i = 0; i < NUM_RESIZE; i++)
            {
                resize.addTail(2 * num + 1);
                num += 1;
            }
            Console.Write("Expected 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39\n");
            Console.Write("Actually " + resize.dumpArray() + "\n");

            Console.Write("\nDone with resize test\n\n");
        }

        static void ListTest()
        {
            const int NUM_LIST = 7;
            const int NUM_LIST_EXTRA = 5;
            Deque list = new Deque(NUM_LIST + 1);
            int[] listValues = new int[NUM_LIST + NUM_LIST_EXTRA] { 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78 };
            int num = 0;

            Console.Write("Testing listQueue, addTail, removeHead\n\n");

            Console.Write("Adding seven values to FIFO\n");
            for (int i = 0; i < NUM_LIST; i++)
            {
                list.addTail(listValues[num]);
                num += 1;
            }

            Console.Write("Testing list\n");
            Console.Write("Expected 1 3 6 10 15 21 28\n");
            Console.Write("Actually " + list.listQueue() + "\n");

            Console.Write("\nRemoving five to cause wrap\n");
            Console.Write("Expected 1 3 6 10 15\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_LIST_EXTRA; i++)
            {
                Console.Write(list.removeHead() + " ");
            }
            Console.WriteLine();

            Console.Write("\nAdding five more for wrapping\n");
            for (int i = 0; i < NUM_LIST_EXTRA; i++)
            {
                list.addTail(listValues[num]);
                num += 1;
            }

            Console.Write("Testing list after wrap\n");
            Console.Write("Expected 21 28 36 45 55 66 78\n");
            Console.Write("Actually " + list.listQueue() + "\n");

            Console.Write("\nDone with testing listQueue\n\n");
        }

        static void AddHeadTest()
        {
            const int NUM_HEAD = 7;
            Deque head = new Deque();
            int[] headValues = new int[NUM_HEAD] { 3, 5, 7, 11, 13, 17, 19 };

            Console.Write("Testing addHead\n\n");

            Console.Write("Adding seven values to head\n");
            for (int i = 0; i < NUM_HEAD; i++)
            {
                head.addHead(headValues[i]);
            }

            Console.Write("Now removing from head\n");
            Console.Write("Expected 19 17 13 11 7 5 3\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_HEAD; i++)
            {
                Console.Write(head.removeHead() + " ");
            }
            Console.WriteLine();

            Console.Write("\nDone with testing addHead\n\n");
        }

        static void RemoveTailTest()
        {
            const int NUM_TAIL = 6;
            Deque tail = new Deque();
            int[] tailValues = new int[NUM_TAIL] { 1, 2, 4, 8, 16, 32 };

            Console.Write("Testing removeTail\n\n");

            Console.Write("Adding six values to tail\n");
            for (int i = 0; i < NUM_TAIL; i++)
            {
                tail.addTail(tailValues[i]);
            }

            Console.Write("Now removing from tail\n");
            Console.Write("Expected 32 16 8 4 2 1\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_TAIL; i++)
            {
                Console.Write(tail.removeTail() + " ");
            }
            Console.WriteLine();

            Console.Write("\nDone with testing removeTail\n\n");
        }

        static void RevQueueTest()
        {
            const int NUM_REV_QUEUE = 8;
            const int NUM_REV_ADD = 4;
            Deque revQueue = new Deque(NUM_REV_QUEUE);
            int num = 0;

            Console.Write("Testing reverse FIFO, addHead, removeTail, isEmpty\n\n");

            Console.Write("Adding eight even integers to FIFO\n");
            for (int i = 0; i < NUM_REV_QUEUE; i++)
            {
                revQueue.addHead(2 * num);
                num += 1;
            }

            Console.Write("Removing four before wrapping\n");

            Console.Write("Expected 0 2 4 6\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_REV_ADD; i++)
            {
                Console.Write(revQueue.removeTail() + " ");
            }
            Console.WriteLine();

            Console.Write("\nAdding four more to force wrap\n");
            for (int i = 0; i < NUM_REV_ADD; i++)
            {
                revQueue.addHead(2 * num);
                num += 1;
            }

            Console.Write("Now dumping array\n");
            Console.Write("Expected 14 12 10 8 22 20 18 16\n");
            Console.Write("Actually " + revQueue.dumpArray() + "\n");

            Console.Write("\nNow adding eight more to force resize\n");
            for (int i = 0; i < NUM_REV_QUEUE; i++)
            {
                revQueue.addHead(2 * num);
                num += 1;
            }
            Console.Write("Now dumping array\n");
            Console.Write("Expected 22 20 18 16 14 12 10 8 38 36 34 32 30 28 26 24\n");
            Console.Write("Actually " + revQueue.dumpArray() + "\n");

            Console.Write("\nNow using removeTail to empty array\n");
            Console.Write("Expected 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_REV_QUEUE * 2; i++)
            {
                Console.Write(revQueue.removeTail() + " ");
            }
            Console.WriteLine();

            Console.Write("\nFIFO should be empty\n");
            Console.Write("FIFO " + (revQueue.isEmpty() ? "is " : "is not ") + "empty\n");

            Console.Write("\nDone with reverse FIFO tests\n\n");
        }

        static void MixTest()
        {
            const int NUM_MIX = 3;
            Deque mixQueue = new Deque(NUM_MIX * 2);
            int num = 0;
            Console.Write("Testing reverse mix of adds and removes\n\n");

            Console.Write("Adding three odd integers to tail\n");
            for (int i = 0; i < NUM_MIX; i++)
            {
                mixQueue.addTail(2 * num + 1);
                num += 1;
            }
            Console.Write("Adding three even numbers to head\n");
            for (int i = 0; i < NUM_MIX; i++)
            {
                mixQueue.addHead(2 * num);
                num += 1;
            }
            Console.Write("Dumping array \n");
            Console.Write("Expected 1 3 5 10 8 6\n");
            Console.Write("Actually " + mixQueue.dumpArray() + "\n");

            Console.Write("\nAdding three more to tail to force resize\n");
            for (int i = 0; i < NUM_MIX; i++)
            {
                mixQueue.addTail(2 * num + 1);
                num += 1;
            }
            Console.Write("Adding three more to head to fill array\n");
            for (int i = 0; i < NUM_MIX; i++)
            {
                mixQueue.addHead(2 * num);
                num += 1;
            }
            Console.Write("Dumping array \n");
            Console.Write("Expected 10 8 6 1 3 5 13 15 17 22 20 18\n");
            Console.Write("Actually " + mixQueue.dumpArray() + "\n");

            Console.Write("\nNow removing from Tail \n");
            Console.Write("Expected 17 15 13 5 3 1\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_MIX * 2; i++)
            {
                Console.Write(mixQueue.removeTail() + " ");
            }
            Console.WriteLine();

            Console.Write("\nNow removing from Head \n");
            Console.Write("Expected 22 20 18 10 8 6\n");
            Console.Write("Actually ");
            for (int i = 0; i < NUM_MIX * 2; i++)
            {
                Console.Write(mixQueue.removeHead() + " ");
            }
            Console.WriteLine();

            Console.Write("\nCalling removeHead from empty FIFO\n");
            try
            {
                mixQueue.removeHead();
                Console.Write("Failed to throw exception\n");
            }
            catch (IndexOutOfRangeException ex)
            {
                Console.Write("Caught out_of_range with message " + ex.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something else \n");
            }
            Console.Write("\nCalling removeTail from empty FIFO\n");
            try
            {
                mixQueue.removeTail();
                Console.Write("Failed to throw exception\n");
            }
            catch (IndexOutOfRangeException ex)
            {
                Console.Write("Caught out_of_range with message " + ex.Message + "\n");
            }
            catch (Exception)
            {
                Console.Write("Caught something else \n");
            }

            Console.Write("\nDone with mixed tests\n\n");
        }

        static void ThinkTest()
        {
            Console.Write("Now testing the thinking problem\n");

            const int NUM_THINK = 5;
            int[] thinkValues = new int[NUM_THINK] { 2, 3, 5, 7, 11 };
            Deque think = new Deque(NUM_THINK);


            Console.Write("Values in reverse order should be 11 7 5 3 2\n");
            think.solveThink(thinkValues, NUM_THINK);
            Console.Write("Values are:                       " + think.listQueue() + "\n");

            Console.Write("\nDone with thinking test\n\n");
        }
    }
}
