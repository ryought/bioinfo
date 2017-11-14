## 3. Law of Large Numbers 
$Z: Z \sim Const(\mu), f_Z(z|\mu) = \delta (z-\mu)$
$\bar{X}_n: \bar{X}_n = \frac{X_1 + ... + X_n}{n}, E(X_i) = \mu, Var(X_i) = \sigma^2$

$\varphi_Z(t) = E[ e^{itZ} ] = \int f_Z(z|\mu) e^{itz} dz = \int \delta (z-\mu) e^{itz} dz = e^{it\mu}$
として，$\varphi_{\bar{X}_n}(t) \to \varphi_Z(t) (n\to \infty)$を示す．
$\varphi_{\bar{X}_n} = \prod_i \varphi_{X_i} (\frac{t}{n}) = \varphi_{X_h}(\frac{t}{n})^n = \exp(n \log (\varphi_{X_h}(\frac{t}{n}) )) = \exp (n \log ( 1+ E(X_h)(\frac{it}{n}^1) + o(\frac{1}{n^2}))) = \exp(n \log(1+\frac{it\mu}{n} + o(\frac{1}{n^2}))) = \exp(n ( \frac{it\mu}{n} + o(\frac{1}{n^2}) )) = \exp(\frac{it\mu}{n} + o(\frac{1}{n^2})) \to \exp(it \mu) (n \to \infty) = \varphi_Z$.
$\varphi_X(t)^n = \exp( n \log (\varphi_X(t)))$を使った．

## 4. Exponential Distribution


## 7. Posivite Definite Symmetrix Matrix (半正定値行列)
実対称行列$A$が半正定値行列であるとは，
(1) $\forall v \in R^m, v^T Av \geq 0$
また下とも同値:
(2) 固有値が非負 $\lambda_k \geq 0$
(3) $\exists U: 実正方行列, A=U^T U$



実対称行列は，実直交行列$O$で対角化できる．$A=O \Lambda O^{\top}, \Lambda = diag(\lambda_i)$\footnote{PRML Appendix}
- $A$が対称行列であるとは,$A^\top = A$であること
    $A_{ij} = A_{ji}$
- $A$:対称行列, $A^{-1}$も対称行列
    $I = A^{-1} A$の転置をとって$I = A^\top (A^{-1})^\top = A (A^{-1})^\top$．両辺に$A^{-1}$を左からかけて，$A^{-1} = A^{-1} A (A^{-1})^\top = (A^{-1})^\top$．
- $A$:対称行列ならば，その固有値は実数．
    $A u_i = \lambda_i u_i$の両辺に$(u_i^*)^\top$をかけて，$(u_i^*)^\top A u_i = \lambda_i (u_i^*)^\top u_i$．
    また複素共役をとって$u_i^\top$をかけて，$u_i^\top A u_i^* = \lambda_i^* u_i^\top u_i^*$
- eigenvectors $u_i$をorthonormalityを満たすように選べる．$U^\top U = I$．
- $A u_i = \lambda_i u_i$は，$A U = U \Lambda$と書けて，両辺に$U^\top$を右からかけると，$A = U\Lambda U^\top$と分解できることがわかる
- $\det A$は固有値の積. $\det A = \prod_{i=1}^M \lambda_i$. $tr A = \sum_{i=1}^M \lambda_i$


二次形式とは$A$に対して$v^T A v$のこと．


(1)$\to$(2): $v$として固有ベクトル$v_i$を選ぶと，対応する固有値$\lambda_i$について$A v_i = \lambda_i v_i$だから，$v_i^T A v_i = v_i^T \lambda_i v_i = \lambda_i v_i^T v_i = \lambda_i > 0$ ($|O| = 1$を使った)

(2)$\to$(1): $\lambda_i > 0$ならば，二次形式$v^T A v = v^T O^T \Lambda O v = (Ov)^T \Lambda Ov = \sum_i \lambda_i (Ov)_i^2 \geq 0$である．

(3)$\to$(1): $A=U^T U$の時，$v^T Av = (Uv)^T (Uv) = || Uv ||^2 \geq 0$
(2)$\to$(3): $A=O^T \Lambda O$で，$\Lambda = diag(\lambda_1, ...)$の対角成分が全て非負だから，$\Lambda^{1/2} = diag(\sqrt{\lambda_1}, ...), \Lambda^{1/2} \Lambda^{1/2} = \Lambda$が作れる．これを使うと$A=(\Lambda^{\frac{1}{2}} O)^T \Lambda^{\frac{1}{2}} O$とできる.

実対称行列$A$が正定値であるとは，
(1) $\forall v \in R^m, v^T Av > 0$

(2) $A_{kk} > 0$: $v$として$e_i = (0, 0, ..., 0, 1, 0, ..., 0)$を考える．$0 < e_i^T A e_i = e_i^T A_i = A_{ii}$．

(3) $| A_{kl} | < \sqrt{A_{kk} A_{ll}}$: $v$として$e_{ij}$: 第$i,j$要素が1，それ以外は0のベクトルを考えると，


## 8. 多変数ガウス分布


## 9. Kullback-Leibler Divergence
(1)  $g(x) = x-1$, $h(x)=\log(x)$は$x=1$で接する
$f(x) = x-1-\log x$とすると$\frac{d}{dx}f(x) = 1-\frac{1}{x} = \frac{x-1}{x}$
$f'(x) < 0(0\leq x \leq 1), f'(x) > 0(x\geq 1)$より$f(x)\geq 0$，$x-1 \geq \log x$. $x=1$で接する．

(3) $KL(p||q) = \sum_{k=1}^m p_k \log(\frac{p_k}{q_k})$とする．
$KL(p||q) \geq 0, KL(p||q) = 0 (if \forall k , p_k= q_k)$．

なぜなら，$\log x \leq x-1$と$\log\frac{p}{q} = - \log \frac{q}{p}$より
$KL(p||q) = \sum_k p_k \log\frac{p_k}{q_k} = \sum_k p_k (- \log \frac{q_k}{p_k} ) \geq \sum_k p_k (-\frac{q_k}{p_k} + 1) = \sum_k (-q_k + p_k) = \sum_k p_k - \sum_k q_k = 0$


## 10. EM
PRML 9章の内容

$p(X,Z | \theta) = p(Z|X, \theta) p(X|\theta)$より$\log p(X,Z | \theta) = \log p(Z | X, \theta) + \log p(X | \theta)$．

$L(q, \theta) = \sum_Z q(Z) \log \frac{p(X,Z|\theta)}{q(Z)}$
$KL(q||p) = - \sum_Z q(Z) \log \frac{p(Z|X, \theta)}{q(Z)}$

$q(Z) = p(Z|X, \theta^{old}$


$L(q, \theta) = \sum_Z q(Z) \log p(X, Z|\theta) - \sum_Z q(Z) \log q(Z) = \sum_Z p(Z|X, \theta^{old} \log p(X, Z|\theta) - \sum_Z p(Z|X, \theta^{old}) \log p(Z|X, \theta^{old}) = Q(\theta, \theta^{old} + H(\theta^{old})$．


## 12. Order Statistics
$X_h \sim Unif(0, 1), h=1,...,n: iid$ この確率密度関数は$f(x) = 1 (0 \leq x \leq 1), 0(otherwise)$(図を書くとわかる)

1. $F_{X_h} (x) := P(X_h \leq x) = \int_{-\infty}^x f(t) dt = \int_0^x 1 dt = x$
2. $F_{X_{\max}} (x) = P(X_{\max} \leq x) = \prod_{n=1}^n P(X_h \leq x) = x^n$
3. $f_X(x) = \frac{dF_X}{dx} (x)$, $f_X(x)$:確率密度関数, $F_X(x)$:累積密度関数より，$f_{X_{\max}} (x) = \frac{d}{dx} x^n = n x^{n-1}$
4. $E[X_{\max}] = \int_{-\infty}^{\infty} x f_{X_{\max}} (x) dx = \int_0^1 x n x^{n-1} dx = [ \frac{n}{n-1} x^{n+1} ]_0^1 = \frac{n}{n+1}$
これは，一様分布からサンプルしたデータ列の最大値が従う分布と，最大値の期待値を示す．
5. $F_{X_{\min}}(x) = P(X_{\min} \leq x) = 1 - \prod_h ( P( X_h \geq x ) )$ なぜなら，最小値が$x$以下という事象は全てが$x$以上であることの否定だから
$P(X_h \geq x) = \int_x^{+\infty} f(t) dt = \int_x^1 dt = 1-x$なので，$F_{X_{\min}} (x) = 1-\prod_{h=1}^n (1-x) = 1-(1-x)^n$

6. 同様に$E[X_{\min}]$も計算すると...



