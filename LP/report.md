# 情報科学基礎実験 Integer Linear Programming
## 演習問題1
simplex methodでLinear Programmingの問題を解く。

### (1)
$\max 3x_1 + x_2 + x_3$, subject to constraints: $x_1 + x_2 + 3x_3 \leq 30, 2x_1 + 2x_2 + 5x_3 \leq 24, 4x_1 + x_2 + 2x_3 \leq 36, x_1, x_2, x_3 \geq 0$をとく。

まず、slack variable $x4,x5,x6$を導入して等式条件に直す。目的関数の値を$z$とおく。暗黙の条件として、$x_1, x_2, x_3, x_4, x_5 \geq 0$がある。

\begin{align}
\begin{cases}
    z &=      3 x_1 +  x_2 +  x_3 \\
    x_4 &= 30 -  x_1 -  x_2 -3 x_3 \\
    x_5 &= 24 -2 x_1 -2 x_2 -5 x_3 \\
    x_6 &= 36 -4 x_1 -  x_2 -2 x_3 
\end{cases}
\end{align}

この時のbasic solutionは等式の右辺を全て$0$とした時の解で、$z=0$。これにsimplex methodを実行する。
1. $z$の式の中で係数が正の変数を選ぶ。(その変数の値を増やすことで、$z$の値を増やせる。)上の場合では$x_1$を選んだ。
2. $x_1$の値を増やした時に、制約条件を一番最初に破る条件(つまり、一番最初に$0$になるslack variable)を探す。つまり$\min b_i / a_{1,i}$。上の場合だと$x_6$で、$x_1=9$で$0$になる。
3. $x_1$と$x_6$の役割を入れ替える。$x_1 = 9 - 1/4 x_2 - 1/2 x_3 - 1/4 x_6$だから、これを他の式に代入する。

以上の手順を実行した後には、次のようになる:

\begin{align}
\begin{cases}
    z   &= 27 + 1/4 x_2 - 1/2 x_3 -3/4 x_6 \\
    x_1 &= 9  - 1/4 x_2 - 1/2 x_3 -1/4 x_6 \\
    x_4 &= 21 - 3/4 x_2 - 5/2 x_3 +1/4 x_6\\
    x_5 &= 6  - 3/2 x_2 - 4   x_3 +1/2 x_6
\end{cases}
\end{align}

この時のbasic solutionは$z=27$。$x_2$と$x_5$を入れ替えることによって、下が得られる。

\begin{align}
\begin{cases}
    z   &= 28 - 7/6 x_3 - 1/6 x_5 -2/3 x_6 \\
    x_1 &= 8  - 5/6 x_3 + 1/6 x_5 -1/3 x_6 \\
    x_4 &= 4  - 8/3 x_3 - 2/3 x_5 +1/3 x_6 \\
    x_5 &= 18 - 1/2 x_3 + 1/2 x_5 
\end{cases}
\end{align}

この時のbasic solutionは$z=28$。また$z$の式の係数が全て負であるから、これ以上$z$の値を上げることはできない。よって、$(x_1, x_2, x_3) = (8, 4, 0)$の時の$z=28$がoptimal solutionである。

### (2)
$\max 2x_1 + x_2$, subject to constraints: $-x_1 + x_2 \leq 1, x_1 - 2x_2 \leq 2, x_1, x_2 \geq 0$をとく。
問題をslack variableを使った等式の形で表す。

\begin{align}
\begin{cases}
    z   &=  2x_1 + x_2\\
    x_3 &= 1 + x_1 - x_2 \\
    x_4 &= 2 - x_1 + 2x_2
\end{cases}
\end{align}

$x_1$を選び、$x_4$と入れ替える。

\begin{align}
\begin{cases}
    z   &=  4 + 5x_2 - x_4 \\
    x_1 &=  2 + 2x_2 - x_4 \\
    x_3 &=  3 +  x_2 - x_4 
\end{cases}
\end{align}

この時、$z$のうちで係数が正のものは$x_2$のみだが、$x_2$をいくら増やしても制約条件は破られない(なぜなら$x_1, x_3$の式の$x_2$の係数が正だから)。つまり、$z$はいくらでも増やせる。よってこれはunboundedな問題であることがわかる。

これは、上の式を$(x_1, x_2)$を二次元平面上にプロットした時の領域からもわかる。

\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{draw.pdf}
\caption{上のLP問題の制約を図示したもの。}
\end{figure}

## 演習問題2
$\max 8x_1 + 11x_2 + 6x_3 + 4x_4$ such that $6.7x_1 + 10x_2 + 5.5x_3 + 3.4x_4 \leq 19$をバイナリの制約付きで解く。CPLEX-formatで書くと、次のようになる。
```
Maximize
obj : 8 x1 + 11 x2 + 6 x3 + 4 x4

Subject To
q: 6.7x1 + 10x2 + 5.5x3 + 3.4x4 <= 19

Bounds
0 <= x1 <= 1
0 <= x2 <= 1
0 <= x3 <= 1
0 <= x4 <= 1

End
```
各部分問題でのboundを求めるために、`glpsol`を使った。その探索木は次の図のようになった。

\begin{figure}
\centering
\includegraphics[width=0.6\textwidth]{branch_and_bound_tree_diagram.pdf}
\caption{上の問題に対応するsearch tree。各セルの中では、(i)は訪れた順番、数字の組はその制約の元でのsimplex法によるoptimalな解、3行目の数字はその時のobject valueを表す。青いセルはbranchingが行われたことを、赤いセルはその問題における最適解がすでに得られたbinary optimal solutionよりも悪かったためにpruneされたことを、紫色のセルはleaf nodeでないのにbinary solutionがoptimal solutionとして得られたためにそれ以降がpruneされたことを示す。}
\end{figure}

## 演習問題3
### (a) C3, C4の条件の変形
RNAの二次構造安定化問題をILPの形に変形する。
- C3
    - $r_i$を含むペアが多くて1つになればいいから
    $$\forall k \in \{1,...,n\}, \sum_{j=k+1}^n x_{kj} + \sum_{i=1}^{k-1} x_{ik} \leq 1$$
- C4
    $$\forall (i,j,k,l) s.t. i<k<j<l, x_{ij}+x_{kl} \leq 1$$

### (b) 制約条件の数の見積もり
- 変数$x_{i,j}$($1\leq i < j\leq n$)の個数: ${}_n C_2 \simeq O(n^2)$
- 条件C1: $(n-1)+(n-2)+ ... +(n-d) \simeq O(n)$
- 条件C2: RNAの塩基$x_i, x_j \in \{ A,C,G,U \}$が塩基対を作る確率は、おおよそ$\frac{3}{{}_4 C_2}$なので、$\frac{n(n-1)}{2} (1-\frac{3}{{}_4 C_2}) \simeq O(n^2)$
- 条件C3: $\forall k \in \{1,...,n\}$で1つの条件式があるから、$O(n)$
- 条件C4: $(i,j,k,l)$の選び方が${}_n C_4$通りあるので、$O(n^4)$
これらを合わせると、合計では$O(n^4)$程度。

## 演習問題4: Additional constraint to disallow isolated pairs
$y_{i,j} = \frac{1}{2}x_{i,j} + \frac{1}{2}x_{i-1, j+1}, 1\leq j < \leq n-1$ という新しい変数を作る。制約条件を$0 \leq y_{i,j} \leq 1$とし、$y_{i,j} \in \{0,1\}$の元で解くと、$x_{i,j}, x_{i-1,j+1}$とも1もしくは0という条件を作れる。(片方だけが1の時は、$y_{i,j}=\frac{1}{2}$になってしまう。)
新たに加えた変数の数は$O(n^2)$、そして制約条件も各変数につき1つずつあるから、$O(n^2)$。
