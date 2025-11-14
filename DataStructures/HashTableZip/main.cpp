//
//  main.cpp
//  HashTables
//
//  Created by jim bailey on 4/19/21.
//

#include "ChainHash.hpp"
#include "StringHash.hpp"
#include <iostream>

// #define TEST_BASE_FIND
// #define TEST_BASE_REMOVE
// #define TEST_BASE_DISPLAY
// #define TEST_BASE_GROW

// #define TEST_ADV_FIND
// #define TEST_ADV_REMOVE
// #define TEST_ADV_DISPLAY

#define TEST_THINK // test adv grow

int main() {

  const int BASE_SIZE = 5;
  std::string baseWords[BASE_SIZE] = {"maple", "spruce", "oak", "cedar",
                                      "cherry"};

  const int ADV_SIZE = 10;
  std::string advWords[ADV_SIZE] = {"dog",  "cat",  "ape",  "cow",  "frog",
                                    "fish", "goat", "bear", "deer", "elk"};

#ifdef TEST_BASE_FIND
  std::cout << "Testing base addItem and findItem\n" << std::endl;
  StringHash baseFind;

  for (int i = 0; i < BASE_SIZE; i++) {
    baseFind.addItem(baseWords[i]);
  }
  std::cout << "Should find maple and not apple" << std::endl;
  std::cout << "  maple" << (baseFind.findItem("maple") ? " " : " not ")
            << "found" << std::endl;
  std::cout << "  apple" << (baseFind.findItem("apple") ? " " : " not ")
            << "found" << std::endl;

  std::cout << "\nDone testing base addItem and findItem\n" << std::endl;
#endif // TEST_BASE_FIND

#ifdef TEST_BASE_REMOVE
  std::cout << "Testing base addItem, findItem, and removeItem\n" << std::endl;
  StringHash baseRemove;

  for (int i = 0; i < BASE_SIZE; i++) {
    baseRemove.addItem(baseWords[i]);
  }
  std::cout << "Should find maple and then not find maple" << std::endl;
  std::cout << "  maple" << (baseRemove.findItem("maple") ? " " : " not ")
            << "found" << std::endl;

  baseRemove.removeItem("maple");
  std::cout << "  maple" << (baseRemove.findItem("maple") ? " " : " not ")
            << "found" << std::endl;
  std::cout << "Should find spruce" << std::endl;
  std::cout << "  spruce" << (baseRemove.findItem("spruce") ? " " : " not ")
            << "found" << std::endl;

  std::cout << "\nDone testing base addItem, findItem, and removeItem\n"
            << std::endl;
#endif // TEST_BASE_REMOVE

#ifdef TEST_BASE_DISPLAY
  std::cout << "Testing base addItem, findItem, removeItem, and display\n"
            << std::endl;
  StringHash baseList;

  for (int i = 0; i < BASE_SIZE; i++) {
    baseList.addItem(baseWords[i]);
  }
  baseList.removeItem("maple");
  std::cout << "Should be \ncedar \ncherry \n_deleted_ \nspruce \n_empty_ "
               "\n_empty_ \n_empty_ \n_empty_ \n_empty_ \n_empty_ \noak"
            << std::endl;
  std::cout << "\nActually is \n" << baseList.displayTable();

  std::cout
      << "\nDone testing base addItem, findItem, removeItem, and display\n"
      << std::endl;
#endif // TEST_BASE_DISPLAY

#ifdef TEST_BASE_GROW
  std::cout << "Testing base growing StringHash\n" << std::endl;
  const int BASE_EXTRA = 3;
  std::string baseExtraWords[BASE_EXTRA] = {"bear", "pony", "cow"};

  StringHash baseGrow;

  for (int i = 0; i < BASE_SIZE; i++) {
    baseGrow.addItem(baseWords[i]);
  }

  for (int i = 0; i < BASE_EXTRA; i++) {
    baseGrow.addItem(baseExtraWords[i]);
  }
  std::cout << "After growing the list should be " << std::endl;
  std::cout << "_empty_ \nbear \noak \n_empty_ \nspruce \n_empty_ ";
  std::cout << "\n_empty_ \nmaple \ncow \n_empty_ \n_empty_";
  std::cout << "\npony \n_empty_ \n_empty_ \n_empty_ \ncherry ";
  std::cout << "\n_empty_ \ncedar \n_empty_ \n_empty_ \n_empty_ ";
  std::cout << "\n_empty_ \n_empty_ ";
  std::cout << "\n\nAnd actually is\n" << baseGrow.displayTable() << std::endl;

  std::cout << "Now testing find and remove after growing" << std::endl;
  std::cout << "Should find maple and then not find maple" << std::endl;
  std::cout << " maple" << (baseGrow.findItem("maple") ? " " : " not ")
            << "found" << std::endl;
  baseGrow.removeItem("maple");
  std::cout << " maple" << (baseGrow.findItem("maple") ? " " : " not ")
            << "found" << std::endl;
  std::cout << "Should find spruce" << std::endl;
  std::cout << " spruce" << (baseGrow.findItem("spruce") ? " " : " not ")
            << "found" << std::endl;

  std::cout << "\nDone testing base growing StringHash\n" << std::endl;
#endif // TEST_BASE_GROW

#ifdef TEST_ADV_FIND
  std::cout << "Testing advanced addItem and findItem\n" << std::endl;
  ChainHash advFind;

  for (int i = 0; i < ADV_SIZE; i++) {
    advFind.addItem(advWords[i]);
  }
  std::cout << "Should find goat and not horse" << std::endl;
  std::cout << "  goat" << (advFind.findItem("goat") ? " " : " not ") << "found"
            << std::endl;
  std::cout << "  horse" << (advFind.findItem("horse") ? " " : " not ")
            << "found" << std::endl;

  std::cout << "\nDone testing advanced addItem and findItem\n" << std::endl;
#endif // TEST_ADV_FIND

#ifdef TEST_ADV_REMOVE
  std::cout << "Testing advanced addItem, findItem, and removeItem\n"
            << std::endl;
  ChainHash advRemove;

  for (int i = 0; i < ADV_SIZE; i++) {
    advRemove.addItem(advWords[i]);
  }
  std::cout << "Should find goat and then not find goat" << std::endl;
  std::cout << "  goat" << (advRemove.findItem("goat") ? " " : " not ")
            << "found" << std::endl;
  advRemove.removeItem("goat");
  std::cout << "  goat" << (advRemove.findItem("goat") ? " " : " not ")
            << "found" << std::endl;

  std::cout << "\nDone testing advanced addItem, findItem, and removeItem\n"
            << std::endl;
#endif // TEST_ADV_REMOVE

#ifdef TEST_ADV_DISPLAY
  std::cout << "Testing advanced addItem, findItem, removeItem, and display\n"
            << std::endl;
  ChainHash advList;

  for (int i = 0; i < ADV_SIZE; i++) {
    advList.addItem(advWords[i]);
  }

  advList.removeItem("goat");
  std::cout << "Should be: \n_empty_\nfrog deer\ncow fish\n"
            << "_empty_\ndog\nbear\ncat ape elk" << std::endl;

  std::cout << "\nAnd is\n" << advList.displayTable();

  std::cout
      << "\nDone testing advanced addItem, findItem, removeItem, and display\n"
      << std::endl;
#endif // TEST_ADV_DISPLAY

#ifdef TEST_THINK
  std::cout << "Testing thinking problem (growing ChainHash)\n" << std::endl;
  const int ADV_EXTRA = 6;
  std::string advExtraWords[ADV_EXTRA] = {"apple", "pine",  "fir",
                                          "oak",   "maple", "fig"};

  ChainHash advGrow;

  for (int i = 0; i < ADV_SIZE; i++) {
    advGrow.addItem(advWords[i]);
  }
  for (int i = 0; i < ADV_EXTRA; i++) {
    advGrow.addItem(advExtraWords[i]);
  }
  std::cout << "\nAfter growing the list should have 17 rows ";
  std::cout << "and include \nfrog \n_empty_ \n_empty_ \n_empty_ ";
  std::cout << "\n_empty_ \nfish fir dog pine \n_empty_ ";
  std::cout << "\nape \ncow \noak \n_empty_ \ndeer fig \nelk ";
  std::cout << "\nbear \n_empty_ \napple cat \ngoat maple";
  std::cout << "\n\nAnd is\n" << advGrow.displayTable();

  std::cout << "\nDone testing thinking problem\n" << std::endl;
#endif // TEST_THINK

  return 0;
}
