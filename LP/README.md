# Linear Programming Report プログラミング課題

## 1. `cplex.c`(and `Makefile`)
CPLEX formatをロードしてsimplex法で解く
### コンパイル
`make`

### 実行
CPLEX LP Formatの問題ファイル`data.txt`を解くとすると、`./cplex data.txt`を実行。


## 2. `branchAndBound.py`
branch and boundを使って、cplexフォーマットで書かれた問題をbinary integerの制約をつけた上での最適解を求めるプログラム。
package`swiglpk`(https://github.com/biosustain/swiglpk)を使って、pythonからglpkの関数を呼び出した。インストールは
```
$ pip install swiglpk
```

CPLEX LPフォーマットのファイル`data.txt`をbinary integer programmingで解くときは、
```
$ python branchAndBound.py data.txt
```
として実行します。

## 3. `combinatorial_auction.py`
オークションの問題を、与えられた問題形式からCPLEX LPフォーマットに変換する。
pythonで実装しました。
