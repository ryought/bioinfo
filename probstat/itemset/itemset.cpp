/*
 * itemset mining
 */

#include <iostream>
#include <bitset>


// 集合のクラス
// 任意サイズ
int and_set(int x[], int y[])


// load_data_from_file(path)
// return T: データベース (配列)
//


int main(void) {
  int theta = 1;
  bool a = true;
  int T[2] = { 0b10001011011,
               0b00001000010 };
  int A = 0b100101010010;
  int B = 0b000000011101;

  int C = A & B;

  std::cout << a << std::endl;
  std::cout << static_cast<std::bitset<8> >(T[1]) << std::endl;
  std::cout << static_cast<std::bitset<8> >(C) << std::endl;
  return 0;
}
