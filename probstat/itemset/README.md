# Itemset Mining
## 目次
まず最初にFrequent Itemset Mining
でも結果として出てくるパターンの数が増えがちなので，
その代替として Closedset Mining

## Frequent Itemset Mining
ある頻度以上起きてるパターンを探したい

- Itemset(商品の集合) $I = \{ 1, ..., M \}$
- Transaction(ある人が一回の会計で買ったもののリスト) $t \subset I$
- Transaction DB(トランザクションを集めたもの．この中からパターンを発見したい) $T=\{ t_1, ..., t_N\}$
- Pattern(パターン これもいくつかの商品の集合) $P \subset I$
- Occurrence(パターンを含むような，つまりパターンが出現しているトランザクションの集合) $Occ(P, T) = T(P) = \{ t \in T: P \subseteq t \}$
- Frequency(そのパターンが何回生じているか) $n_T(P) = | T(P) |$


Pattern$P$がfrequentであるとは，$n_T(P) \geq \sigma$．ここでMinimum Support$\sigma, 0\leq \sigma \leq |T|$．ある一定回数以上出ている


上の問題は，Itemsetの部分集合からなるHasse図(DAG)上を探索して，Frequent sets $S = \{ P \subseteq I : | T(P) | \geq \sigma \}$ という集合を求めるのと同じ．


注意するべき点は
- Hasse図上で下に行く時，Frequencyは単調減少する．なので，$\sigma$より低くなったノードより先は調べなくていい
    - $P \subset P'$ならば，$n_T(P) > n_T(P')$
    - $P'$を含むようなトランザクションは，当然$P$を含んでいる
- DAGなので探索時にduplicaitonが生じる．lexicographical orderで調べる.
    - $P$に要素を追加して$P' = P \cup \{i\}$を作る時，$i$は自分の含む要素より後ろの要素からとる．
    - 例えばI = 1,2,3,4, P = 1,3ならば, P' = 1,3,4のみ
- Occurenceはメモリ上に確保しておく必要がある


## Closed Itemset Mining
Frequentの中で，さらに絞った答えをだす
### 言葉
- closed set
    itemset $X$がclosedであるとは，$X$のスーパーセットで，同じfrequencyをもつものが存在しないもの
    $\forall e \in I, Freq(X \cup \{e\}) < Freq(X)$
    同じoccurrence(そのpatternを部分集合にもつtransactionの集合)をもつpatternの集合$[X] = \{ Y | Occ(X) = Occ(Y) \}$の最大元

これを見つける問題

### reduction map
Hasse図で子供から親にいく(下から上に行く)ことをまず考える

- shrink
    - pattern$X$から適当に要素を落とせば，frequencyが高いpattern$X'$が得られる
- closure
    - non-closed setからclosed setに飛ぶ関数
    - pattern$X$を含むtransaction全体でANDをとると，closed setにいける
    - $closure(x) = \cap \{ t \in T: X \subseteq t \}$
組み合わせると，closed set$X$から，その上のclosed set$Y$に飛べる

### children generation
reduction mapの逆関数．親から子供に行く関数．これを使えば，空集合から探索できる

### closure extension と prefix preserving closure extension
- closed set $X$
- $Y = X \cup \{i\}$ で extend
- $Z = closure ( X \cup \{i\})$ でclosed setを得る

DAGを探索する時に，duplicationを防ぐためのordering

- closure tail of P
    $\min \{j | closure(P \cup \{1, ..., j\} ) = P \}$
- $H = closure(P\cup \{i\})$ is ppc-extension of P
    $i > closure tail , H\cap \{1, ..., i-1\} = P\cap \{1, ..., i-1\}$


