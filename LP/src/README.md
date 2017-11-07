# Linear Programming Report プログラミング課題

## 1. `cplex.c`(and `Makefile`)
glpkのAPIを使って、CPLEX formatをロードしてsimplex法で解くプログラム。Cで実装した。
### コンパイル
`make`

### 実行
CPLEX LP Formatの問題ファイル`data.txt`を解くとすると、`./cplex data.txt`を実行する。


## 2. `branchAndBound.py`
branch and boundを使って、cplexフォーマットで書かれた問題をbinary integerの制約をつけた上での最適解を求めるプログラム。
package`swiglpk`(https://github.com/biosustain/swiglpk)を使って、pythonからglpkの関数を呼び出した。ライブラリのインストールは
```
$ pip install swiglpk
```

CPLEX LPフォーマットのファイル`data.txt`をbinary integer programmingで解くときは、
```
$ python branchAndBound.py data.txt
```
として実行する。

実行後、一番末尾に表示される
```
('solution: ', (943077.0, [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]))
('call', 1)
```
のメッセージの1行目は解を、2行目はsimplex法の呼び出し回数を表している。

## 3. `combinatorial_auction.py`
オークションの問題を、与えられた問題形式からCPLEX LPフォーマットに変換する。
pythonで実装した。

```
$ python combinatorial_auction.py
```
で、`ca-data/*.txt`に入っている問題ファイルを全て変換し、`lp-datas/data_out_*.txt`に保存する。
これを課題2のプログラムで解くには、
```
$ python branchAndBound.py lp-datas/data_out_*.txt
```
とする。
