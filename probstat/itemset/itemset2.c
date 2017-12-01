#include <stdio.h>
#include <stdlib.h>

#define MASK (1 << 0)

// 集合に関係する関数
typedef struct _set {
  int length;
  int* member;
} bitset;

// 集合を作る
// 空集合を返す
bitset empty_set(int length) {
  // length is number of bits the set is using
  // 必要なintの個数は，int 1つあたり32個だから，ceil(length/32)
  bitset A;
  int pageNum = (length/32) + 1;
  /* printf("size: %lu(%lu)\n",  sizeof(int) * ((length/32)+1), sizeof(int) ); */
  A.member = (int*)malloc( sizeof(int) * pageNum );
  // 初期化
  for(int i=0; i<pageNum; i++) {
    A.member[i] = 0;
  } 
  A.length = length;
  return A;
}

bitset intersection_set(bitset A, bitset B) {
  bitset C = empty_set(A.length);
  for(int i=0; i<(A.length/32)+1; i++) {
    C.member[i] = A.member[i] & B.member[i];
  }
  return C;
}

bitset union_set(bitset A, bitset B) {
  bitset C = empty_set(A.length);
  for(int i=0; i<(A.length/32)+1; i++) {
    C.member[i] = A.member[i] | B.member[i];
  }
  return C;
}
// index [0..M] がsetに含まれるかどうか
int contains_set(bitset A, int index) {
  if (index >= A.length) {
    printf("error: index out of range\n");
    return -1;
  }
  return (A.member[index / 32] >> (index % 32)) & (1 << 0); 
}

void add_set(bitset A, int index) {
  int pageId = index / 32;
  int i = index % 32;
  A.member[pageId] = A.member[pageId] | (1 << i); 
}

int equal_set(bitset A, bitset B) {
  for(int i=0; i<(A.length/32)+1; i++) {
    if(A.member[i] != B.member[i]) {
      return 0;
    }
  }
  return 1;
}

int equal_empty_set(bitset A) {
  for(int i=0; i<(A.length/32)+1; i++) {
    if(A.member[i] != 0) return 0;
  }
  return 1;
}

// 適当に表示する方 ちゃんとビットで表示したければ，print_setを使ってください．
void print_set_default(bitset x) {
  printf("length: %d\n", x.length);
  for(int i=0; i<((x.length/32) +1); i++) {
    printf("pageid: %d, contents: %d\n", i, x.member[i]);
  }
}

int getDigitsBin(int x, int i) {
  return (x >> i) & (1 << 0);
}

void print_binary(int x) {
  for(int i=0; i<32; i++) {
    printf("%d", getDigitsBin(x, i));
  }
  printf("\n");
}

void print_set(bitset x) {
  printf("length: %d\n", x.length);

  for(int i=0; i<((x.length/32) +1); i++) {
    printf("pageid: %d, contents: ", i);
    print_binary(x.member[i]);
  }
}

// 010001001101 の文字列から， setを作る
// 文字列自体は，プログラムで生成使用
bitset generate_set_from_string(int length, char* string) {
  bitset A = empty_set(length);
  A.length = length;
  for(int i=0; i<length; i++) {
    // 文字列を順番に走査
    if(string[i] == '1') {
      add_set(A, i);
    }
  }
  return A;
}


int computeSupport(bitset C, bitset T[], int L) {
  int n = 0;
  for(int i=0; i<L; i++) {
    if(equal_set(intersection_set(C, T[i]), C)) 
      n++;
  }
  return n;
}
/*
bitset computeClosure(bitset C, bitset T[]) {

}
int is_ppc(bitset C, bitset C2, int i) {
}
void backtrack(bitset C, int i, bitset T[]) {

}
*/




int main(int argc, char *argv[]) {
  int a = 0b101101;

  printf("a = %d, %ld\n", 10/3, sizeof(bitset));

  print_binary(10);

  bitset A = empty_set(40);
  print_set(A);

  bitset B = empty_set(40);
  B.member[0] = 235;
  B.member[1] = 122;
  print_set(B);

  print_set(intersection_set(A, B));
  print_set(union_set(A, B));

  printf("empty\n");
  bitset X = empty_set(40);
  print_set(X);
  printf("add 20\n");
  add_set(X, 5);
  print_set(X);
  printf("contains %d\n", contains_set(X, 0));

  printf("empty %d\n", equal_empty_set(X));
  printf("empty %d\n", equal_empty_set(A));
  printf("empty %d\n", equal_empty_set(B));

  bitset AA = generate_set_from_string(10, "1011001010");
  printf("1011001010\n");
  print_set(AA);

  // データベースファイルを読み込む
  // 各行が1トランザクション，1セットに対応． 0100101011010\n で一行
  FILE *fp = fopen("db.txt", "r");
  // まず1行の行数を測る．他の行も文字数は全て同じはず．
  int N = 0; // 最初の行の文字数
  char c;
  while((c = fgetc(fp)) != '\n') {
    N++;
  }
  printf("N=%d\n", N);
  rewind(fp);

  int L = 0; // 行数
  char* buf = (char*)malloc(sizeof(char)*N+10);
  while(fgets(buf, N+10, fp) != NULL) {
    L++;
  }
  printf("L=%d\n", L);

  // データベース
  bitset* T = (bitset*)malloc(sizeof(bitset)*L);

  char* str = (char*)malloc(sizeof(char)*(N+1));
  // 読み込む
  int i = 0;
  rewind(fp);
  while(fscanf(fp, "%s", str) != EOF) {
    printf("read [%s]\n", str); 
    T[i] = generate_set_from_string(N, str);
    i++;
  }
  printf("loaded %d %d\n", i, N);
  fclose(fp);

  print_set(T[0]);
  print_set(T[1]);
  print_set(T[2]);
  printf("%d\n", computeSupport(T[0], T, L));
  
  return 0;
}
