#include <stdio.h>
#include <types.h>

const int T = MAX_INT/2;

// パラメータたち
const int d = 7;
const int e = 1;
const int MATCH = 1;
const int MISMATCH = -1;

// データ
char A[] = "GGAGTGAGGGGAGCAGTTGGGCTGAAGATGGTCAACGCCGAGGGAACGGTAAAGGCGACGGAGCTGTGGCAGACCTGGCTTCCTAACCACGTCCCGTGTTTTGCGGCTCCGCGAGGACTG";
char B[] = "CGCATGCGGAGTGAGGGGAGCAGTTGGGAACAGATGGTCCCGCCGAGGGACCGGTGGGCAGACGGGGCCAGCTGTGGCAGACACTGGCTTCTAACCACCGAACGTTCTTTCCGCTCCGGG";

// コスト関数
int c(x, y) {
  if(x == y) return MATCH;
  else return MISMATCH;
}

// Match
int M(i, j) {
  if(M[i][j] != T)
    return m[i][j];
  if(i < 0 || j < 0)
    return ;

  M[i][j] = max( M(i-1,j-1), Ix(i-1,j-1), Iy(i-1,j-1) ) + c(A[i], B[j]);
  return M[i][j];
}

int Ix(i, j) {
  if(Ix[i][j] != T) return Ix[i][j];
  if(i < 0 || j < 0) return ; //TODO

  Ix[i][j] = max( 
      M (i-1, j) - d,
      Ix(i-1, j) - e,
      Iy(i-1, j) - d
      );
  return Ix[i][j];
}

int Iy(i, j) {
  if(Iy[i][j] != T) return Iy[i][j];
  if(i < 0 || j < 0) return ;

  Iy[i][j] = max(
      M (i, j-1) - d,
      Iy(i, j-1) - d
      );
  return Iy[i][j];
}


int main(int argc, char *argv[]) {
  
  return 0;
}
