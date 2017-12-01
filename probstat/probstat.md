## 1. 基本法則
$E(g(X)) = \sum_{i\in Z} g(i) P_X(\{i\}) = \sum_{i\in Z} g(i) P(X=i)$
$Var(X) = E((X-E(X))^2) = E(X^2) - E(X)^2$

$E(XY)$って，$f_X$とかでかくとどうなるの？

1. $E(XY) - E(X)E(Y) = E((X-\mu_X)(Y-\mu_Y)) = Cov(X,Y)$

2. $X,Y$:independent，つまり$P(X=a, Y=b) = P(X=a) P(Y=b)$．この時$E(XY) = E(X)E(Y)$
より，
$Cov(X, Y) = E(XY) - E(X)E(Y) = E(X)E(Y) - E(X)E(Y) = 0$．

3. $Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$
	$Cov(X,Y) = E[(X-E[X]) (Y-E[Y])] = E[XY] - E[X][Y]$と期待値の線型性から， 
	$V[X+Y] = E[((X+Y)-E[X+Y])^2] = E[(X+Y)^2] - (E[X+Y])^2 = E[X^2 + Y^2 + 2XY] - (E[X] + E[Y])^2 =  E[X^2] + E[Y^2] + 2E[XY] - ( (E[X]^2 + E[Y]^2 + 2E[X]E[Y] ) = (E[X^2]-E[X]^2 ) + (E[Y^2]-E[Y]^2) + 2(E[XY] - E[X]E[Y]) =  V[X] + V[Y] + 2Cov(X,Y)$である．
4. $Cov(X,Y)^2 \leq Var(X) Var(Y)$
	$P_{zw} = Prob(X-\mu_X = z, Y-\mu_Y = w)$とすると
	$Cov(X,Y) = E((X-\mu_X)(Y-\mu_Y)) = \sum_{z,w} zw P_{zw}$
	$Var(X) = E((X-\mu_X)^2) = \sum_{z} z^2 P_z = \sum_{zw} z^2 P_{zw}$．$P_z = \sum_w P_{zw}$より．
	これを使うと，$Cov(X,Y)^2 = \sum_{z,w} zw P_{zw} \sum_{z',w'} z'w' P_{z'w'} = \sum_{z,w,z',w'} zw z' w' P_{zw} P_{z'w'}$.
	$Var(X)Var(Y) = \sum_{zw} z^2 P_{zw} \sum_{z'w'} w'^2 P_{z'w'} = \sum_{zw z'w'} z^2 P_{zw} w'^2 P_{z'w'}$．これを$\sum_{zw z'w'} z^2 P_{zw} w'^2 P_{z'w'} = \sum_{zw z'w'} z'^2 P_{zw} w^2 P_{z'w'}$を使って器用に分解する と$= \frac{1}{2} \sum_{zw z'w'} z^2 w'^2 P_{zw} P_{z'w'} + \frac{1}{2} \sum_{zw z'w'} z'^2 w^2 P_{zw} P_{z'w'}$．
	$Var(X)Var(Y)-Cov(X,Y)^2 = \frac{1}{2} \sum_{zw z'w'} z^2 w'^2 P_{zw} P_{z'w'} + \frac{1}{2} \sum_{zw z'w'} z'^2 w^2 P_{zw} P_{z'w'} -\sum_{z,w,z',w'} zw z' w' P_{zw} P_{z'w'} = \sum_{zw z'w'} (\frac{1}{2}z^2 w'^2 + \frac{1}{2} z'^2 w^2 - zwz'w') P_{zw} P_{z'w'}$．ここで$\frac{1}{2}z^2 w'^2 + \frac{1}{2} z'^2 w^2 - zwz'w' = \frac{1}{2}(zw' - z'w)^2 \geq 0$．よって$Var(X)Var(Y) - Cov(X,Y)^2 \geq 0$．

$X-Y$，$X+Y$の分散を調べてもできる


## 2. 特性関数(Characteristic function)
一回確率変数を特性関数に変換したら，あとは解析の問題
$\Phi_X(t) = E(e^{itX}) = E(1 + itX + \frac{(it)^2}{2!} X^2 + \frac{(it)^3}{3!} X^3 ...) = 1 + it E(X) + \frac{(it)^2}{2!} E(X^2) + ...$を確率変数$X$の特性関数という．
$f_X(x)$のフーリエ変換になっている．フーリエ変換だから，$\Phi_X(t) = \Phi_Y(t)$ならば$f_X = f_Y$(確率分布として等しい)(なぜなら逆変換できる)

1. $\Phi_X(0) = 1$
    $\Phi_X(0) = E(e^{0}) = E(1) = 1$
2. $\frac{1}{i^m} \frac{d^m \Phi_X}{dt^m} = \frac{1}{i^m} \frac{d^m}{dt^m} ( \sum_{n=0}^\infty \frac{(it)^n}{n!} E(X^n) ) = \sum_{n=0}^\infty \frac{t^n}{n!} E(X^{n+m})$
    これは$t=0$の時，$E(X^m)$
3. Poisson分布の特性関数
    $X \sim Poisson(\lambda)$の時，$\Phi_X(t) = \sum_{k=0}^\infty e^{itk} \frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda} \sum_{k=0}^\infty \frac{(e^{it}\lambda)^k}{k!} = e^{-\lambda} e^{e^{it} \lambda} = e^{\lambda (e^{it}-1)}$．$e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$を使った．
4. 線形性 $X,Y$独立の時，$\Phi_{aX+bY}(t) = \Phi_X(at) \Phi_Y(bt)$
    $\Phi_{aX+bY}(t) = E(e^{it(aX+bY)}) = E(e^{i(at)X} e^{i(bt)Y})$．独立性より，$E(e^{i(at)X}) E(e^{i(bt)Y}) = \Phi_{X}(at) \Phi_{Y}(bt)$

## 3. Law of Large Numbers 
$Z: Z \sim Const(\mu), f_Z(z|\mu) = \delta (z-\mu)$
$\bar{X}_n: \bar{X}_n = \frac{X_1 + ... + X_n}{n}, E(X_i) = \mu, Var(X_i) = \sigma^2$

$\varphi_Z(t) = E[ e^{itZ} ] = \int f_Z(z|\mu) e^{itz} dz = \int \delta (z-\mu) e^{itz} dz = e^{it\mu}$
として，$\varphi_{\bar{X}_n}(t) \to \varphi_Z(t) (n\to \infty)$を示す．
$\varphi_{\bar{X}_n} = \prod_i \varphi_{X_i} (\frac{t}{n}) = \varphi_{X_h}(\frac{t}{n})^n = \exp(n \log (\varphi_{X_h}(\frac{t}{n}) )) = \exp (n \log ( 1+ E(X_h)(\frac{it}{n}^1) + o(\frac{1}{n^2}))) = \exp(n \log(1+\frac{it\mu}{n} + o(\frac{1}{n^2}))) = \exp(n ( \frac{it\mu}{n} + o(\frac{1}{n^2}) )) = \exp(it\mu + o(\frac{1}{n})) \to \exp(it \mu) (n \to \infty) = \varphi_Z$.
$\varphi_X(t)^n = \exp( n \log (\varphi_X(t)))$を使った．

中心極限定理を同様の議論で示せる
正規分布の特性関数は……
任意の分布について，2次以降が消える
**TODO**

## 4. Exponential Distribution
$X \sim Exp(\lambda): X\in R_{>0}, f_X(x) = \lambda e^{-\lambda x}$の時，

1. $\int_0^\infty \lambda e^{-\lambda x} dx = [ - e^{-\lambda x} ]_0^\infty = 1$
2. $E(X) = \int_0^\infty x \lambda e^{-\lambda x} = \lambda \int_0^\infty x e^{-\lambda x} = \lambda \frac{d}{d\lambda} ( - \int_0^\infty e^{-\lambda x} dx) = \lambda \frac{d}{d\lambda} (-\frac{1}{\lambda}) = \lambda \frac{1}{\lambda^2} = \frac{1}{\lambda}$
3. $Var(X) = E(X^2) - E(X)$．ここで$E(X^2) = \int_0^\infty x^2 \lambda x^{-\lambda x} = \lambda \int_0^\infty x^2 e^{-\lambda x} dx = \lambda (\frac{d}{d\lambda})^2 ( \int_0^\infty e^{-\lambda x} dx) = \lambda (\frac{d}{d\lambda})^2 (\frac{1}{\lambda}) = \lambda \frac{2}{\lambda^3} = \frac{2}{\lambda^2}$なので，$Var(X) = \frac{1}{\lambda^2}$.


## 5. Categorical Distribution
$X \sim Cat(\{q_k\}): X\in \{ 1, ..., m \}, P(X=k) = q_k, \sum_{k=1}^m q_k = 1$の時，

1. $E(1) = \sum_{k=1}^m 1 q_k = 1$
2. $E(X) = \sum_{x} x P(X=x) = \sum_{k=1}^m k q_k$

$Y_k = I(X=k)$:確率変数とする．
3. $E(Y_k) = \sum_{x} I(x=k) P(X=x) = P(X=k) = q_k$
4. $Cov(Y_k, Y_l) = E( (Y_k - E(Y_k)) (Y_l - E(Y_l)) ) = E(Y_k Y_l) - q_k q_l$．
    ここで$k\neq l$の時，$E(Y_k Y_l) = \sum_{x} I(x=k) I(x=l) P(X=x) = 0$．また$k=l$の時，$E(Y_k Y_l) = \sum_x I(x=k)^2 P(X=x) = q_k$．したがってまとめて，$Cov(Y_k, Y_l) = \delta_{kl}q_k - q_k q_l$．

## 6. Multinominal Distribution

1. $E(N_k) = \sum_{n=1}^\infty E(Y_k^{(h)}) = n_0 q_k$
2. $Cov(N_k, N_l)$

Covは双線形性を持つ

**TODO**

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
- $O$が直交行列であるとは，$O^\top O = O O^\top = I$で，$O^\top = O^{-1}$．この行列式は$1, -1$．
- $diag(\lambda_1, ..., \lambda_n)^{-1} = diag( (\lambda_1)^{-1}, ..., (\lambda_n)^{-1} )$．


二次形式とは$A$に対して$v^T A v$のこと．


(1)$\to$(2): $v$として固有ベクトル$v_i$を選ぶと，対応する固有値$\lambda_i$について$A v_i = \lambda_i v_i$だから，$v_i^T A v_i = v_i^T \lambda_i v_i = \lambda_i v_i^T v_i = \lambda_i > 0$ ($|O| = 1$を使った)

(2)$\to$(1): $\lambda_i > 0$ならば，二次形式$v^T A v = v^T O^T \Lambda O v = (Ov)^T \Lambda Ov = \sum_i \lambda_i (Ov)_i^2 \geq 0$である．

(3)$\to$(1): $A=U^T U$の時，$v^T Av = (Uv)^T (Uv) = || Uv ||^2 \geq 0$
(2)$\to$(3): $A=O^T \Lambda O$で，$\Lambda = diag(\lambda_1, ...)$の対角成分が全て非負だから，$\Lambda^{1/2} = diag(\sqrt{\lambda_1}, ...), \Lambda^{1/2} \Lambda^{1/2} = \Lambda$が作れる．これを使うと$A=(\Lambda^{\frac{1}{2}} O)^T \Lambda^{\frac{1}{2}} O$とできる.

実対称行列$A$が正定値であるとは，
(1) $\forall v \in R^m, v^T Av > 0$

(2) $A_{kk} > 0$: $v$として$e_i = (0, 0, ..., 0, 1, 0, ..., 0)$を考える．$0 < e_i^T A e_i = e_i^T A_i = A_{ii}$．

(3) $| A_{kl} | < \sqrt{A_{kk} A_{ll}}$: $v$として$e_{ij}$: 第$i,j$要素が$x,y$，それ以外は0のベクトルを考えると，


## 8. 多変数ガウス分布
$\int_{-\infty}^{\infty} dx \exp( -\frac{1}{2a} (x-b)^2 ) = \sqrt{2\pi a}$を使う．
(1) $f_X(x) = \frac{1}{(2\pi)^{m/2}} \exp( -\frac{1}{2} x^\top I^{-1} x)$の時$\int_{R^m} f_X(x) d^mx = 1$を示す．
$f_X(x) = \frac{1}{(2\pi)^{m/2}} \exp (-\frac{1}{2} x^\top x) = \frac{1}{(2\pi)^{m/2}} \exp ( - \frac{1}{2} \sum_{i=0}^n x_i^2 )$で，$\int_{R^m} \exp(-\frac{1}{2} \sum_{i=0}^n x_i^2) d^mx = \int_{R} \exp(-\frac{1}{2} x_1^2) dx_1 \int_{R} \exp(-\frac{1}{2} x_2^2) dx_2 ... = (\sqrt{2\pi})^m$．より，元の関数を積分すると$1$．

(2) $\exp(-\frac{1}{2} (x-\mu)^\top \Sigma^{-1} (x-\mu))$は，$y=x-\mu$,$\Sigma = O \Lambda O^\top$と置くと, $\exp(-\frac{1}{2} (O^\top x)^\top \Lambda^{-1} (O^\top x)), dy = dx$.


$\Delta^2 = (x-\mu)^\top \Sigma^{-1} (x-\mu)$として，$\Sigma = O \Lambda O^\top$と分解すると，$\Delta^2 = (x-\mu)^\top \sum_{i=1}^n \lambda_i u_i u_i^\top (x-\mu) = \sum_{i=1}^n \frac{y_i^2}{\lambda_i}$．ただし$y_i = u_i^\top (x-\mu)$とおいた．
ヤコビアンは$J_{ij} = \frac{\partial x_i}{\partial y_j} = U_{ji}$で，$U U^\top = 1$より$\det U \det U^\top = 1$で$\det U = 1$だから，$dx = dy$．

ここで，$\int f_X (x) dx = \int \frac{1}{(2\pi)^{m/2} |\Sigma|^{1/2}} \exp ( -\frac{1}{2} (x-\mu)^\top \Sigma^{-1} (x-\mu)) = \int \frac{1}{(2\pi)^{m/2} |\Sigma|^{1/2}} \exp ( -\frac{1}{2} \Delta^2) = \int \prod_{i=1}^n \frac{1}{(2\pi \lambda_i)^{1/2}} \exp (-\frac{y_i^2}{2 \lambda_i} ) dy_1 dy_2 ... = 1$

以下$dx = dx_1 dx_2 ... dx_n$の略記．$\int_{R^m} f_X(x) d^mx = \int_{R^m} \frac{1}{(2\pi)^{m/2} |\Lambda|^{1/2}} \exp(-\frac{1}{2} (x-\mu)^\top (O^\top)^{-1} \Lambda^{-1} (O)^{-1} (x-\mu) )d^mx$．$y=O^\top (x-\mu)$とおくと$dx = \det O dy, \det O = 1$なので$=\int_{R^m} \frac{1}{(2\pi)^{m/2} |\Lambda|^{1/2}} \prod_i \exp (-\frac{1}{2} \lambda_i^{-1} y_i^2 ) 1 d^my$．またここで$z_i = \lambda_i^{-1/2} y_i$と置くと，$dy_i = \lambda_i^{1/2} dz_i$．また行列式は固有値の積なので$|\Lambda| = \prod_i \lambda_i$．よって$= \int_{R^m} \frac{1}{(2\pi)^{m/2} \prod_i \lambda_i^{1/2}} \prod_i \sqrt{\lambda_i} \prod_i \exp(-1/2 z_i^2) dz_i = \frac{1}{(2\pi)^{m/2} \prod_i \lambda_i^{1/2}} \prod_i \sqrt{\lambda_i} (\sqrt{2 \pi})^m$


(2) (別解) 変数変換をするやつ
$\Sigma = O \Lambda O^\top$として，$\exp(-\frac{1}{2} (x-\mu)^\top \Sigma^{-1} (x-\mu))$について$y=O^{-1}(x-\mu)$とおく．ヤコビアン$J=O^\top$より，$\det J = 1$．すると$\exp(-\frac{1}{2} y^\top \Sigma^{-1} y) = \exp( - \sum_{i=1}^n \frac{1}{2} \frac{1}{\lambda_i} y_i^2 )$

$y'_i = \frac{1}{\sqrt{\lambda_i}} y_i$とすると，$dy'_i = \frac{1}{\sqrt{\lambda_i}} dy_i$．

$\int_{R^m} f_X (x) d^mx$


また$(diag(\lambda_i) x)_j = \lambda_j x_j$で，$x^\top \Lambda x = x^\top (\lambda_i x_i)_i = \sum_{i=0}^n \lambda_i x_i^2$.

$\Lambda^{-1} = diag(\lambda_i^{-1})$より$y^\top \Lambda^{-1} y = \sum_{i} y_i^2 \lambda_i^{-1}$なので，前式は$\exp(-\frac{1}{2} \sum_{i=1}^m (O^\top x)_i^2 \lambda_i^{-1})$である．

## 9. Kullback-Leibler Divergence
$KL(p|q) = \int p(x) \log (\frac{p(x)}{q(x)} )$
確率分布$p,q$の間の距離のようなもの

(1)  $g(x) = x-1$, $h(x)=\log(x)$は$x=1$で接する
$f(x) = x-1-\log x$とすると$\frac{d}{dx}f(x) = 1-\frac{1}{x} = \frac{x-1}{x}$
$f'(x) < 0(0\leq x \leq 1), f'(x) > 0(x\geq 1)$より$f(x)\geq 0$，$x-1 \geq \log x$. $x=1$で接する．
→結論として$\log x \leq x - 1$, 等号成立は$x=1$.(グラフを書いて見てもわかる)

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

データが得られる確率が最大になるパラメータを求めたい．
隠れ変数があると考える．(隠れ変数を使って，確率分布が簡単になる場合が適している)
$\max p(X|\theta) = \max p(X, Z | \theta)$を考える．

- $L(q, \theta) = \sum_z q(z) \log \frac{p(x,z | \theta)}{q(z)}$と置くと，$\log p(X) = L(q,\theta) + KL(q||p)$．
    なぜなら，$\log p(X,Z) = \log p(Z|X) + \log p(X)$を定義に代入して，$L(q, \theta) = \sum_z q(z) (\log p(z|x) + \log p(x) - \log q(z) ) = \sum_z q(z) \log \frac{p(z|x)}{q(z)} + \sum_z q(z) \log p(x) = - KL(q||p) + \log p(x)$．ただし$KL(p||q) = \sum_x p(x) \log \frac{q(x)}{p(x)}$，$\sum_z q(z) = 1$を用いた．
    $\log p(X,Z)$の下界が$L(q,\theta)$である．

- $L(q,\theta) = Q_{EM}(\theta, \theta_{old}) + H(q)$
    $q(Z) = p(X,Z|\theta_{old})$と置くと，$L(q,\theta) = \sum_z q(z) \log \frac{p(X,Z|\theta)}{q(Z)} = \sum_z p(Z|X,\theta_{old}) \log p(X, Z| \theta) - \sum_z q(z) \log q(z) = Q_{EM}(\theta, \theta_{old}) + H(q)$．
- ステップ
    - Eステップ：$\theta$を$\theta_{old}$に固定．$L(q, \theta_{old})$を$q$について最大化する
        $KL(q||p)=0, q=p$となるような$q$を探す．$\log p(X,Z)$に接するような分布$q$を作る
    - Mステップ：$q$を固定．$L$を$\theta$について最大化する
        $L$を上昇させる．$p\neq q$になるはずなので，$KL$の上昇分を加味して$\log p(X)$はさらに上がるはず．


(1) $l(\theta | D) = Q_{EM}(\theta| \theta') + H(\theta') + KL(\theta' || \theta)$
(2) $\theta = \theta'$で，上の式は接しているか？


## 11. Data Assimilation
**TODO**
決定性の力学モデルをデータにフィットさせる
初期値とパラメータが決まってしまえば残りの点列は決まってしまう．それをgradient descentで求める

## 12. Order Statistics
平均値の分布，分散の分布は考える．最大値の分布，最小値の分布は？
$X_h \sim Unif(0, 1), h=1,...,n: iid$ この確率密度関数は$f(x) = 1 (0 \leq x \leq 1), 0(otherwise)$(図を書くとわかる)

1. $F_{X_h} (x) := P(X_h \leq x) = \int_{-\infty}^x f(t) dt = \int_0^x 1 dt = x$
2. $F_{X_{\max}} (x) = P(X_{\max} \leq x) = \prod_{n=1}^n P(X_h \leq x) = x^n$
	絵を描いてみると，納得できる
3. $f_X(x) = \frac{dF_X}{dx} (x)$, $f_X(x)$:確率密度関数, $F_X(x)$:累積密度関数より，$f_{X_{\max}} (x) = \frac{d}{dx} x^n = n x^{n-1}$
4. $E[X_{\max}] = \int_{-\infty}^{\infty} x f_{X_{\max}} (x) dx = \int_0^1 x n x^{n-1} dx = [ \frac{n}{n-1} x^{n+1} ]_0^1 = \frac{n}{n+1}$
これは，一様分布からサンプルしたデータ列の最大値が従う分布と，最大値の期待値を示す．
n個の点が等間隔に並ぶ．植木算的に，そのn個目の位置にいることになる
i番目の点が入る期待値を求めて，そのi=nの時と同じ結果になる

5. $F_{X_{\min}}(x) = P(X_{\min} \leq x) = 1 - \prod_h ( P( X_h \geq x ) )$ なぜなら，最小値が$x$以下という事象は全てが$x$以上であることの否定だから
$P(X_h \geq x) = \int_x^{+\infty} f(t) dt = \int_x^1 dt = 1-x$なので，$F_{X_{\min}} (x) = 1-\prod_{h=1}^n (1-x) = 1-(1-x)^n$

グラフ書いてみる

6. 同様に$E[X_{\min}]$も計算すると...

P値の分布

## 13. Sparse Modeling
	


1. 微分するだけ
	$\frac{\partial}{\partial w} w^\top X^\top X w = 2X^\top X w$が使える
2. $\arg\min_z (1/2 ||y-Xw||^2 + \lambda |z| + \alpha^\top (w-z) + \rho/2 ||w-z||^2 )= \arg\min_z (\lambda/\rho |z| + 1/2(z^\top z - w^\top z - z^\top w - 2/\rho \alpha^\top z) = \arg\min_z (\lambda/\rho |z| + 1/2 || (z-(w+\alpha/\rho))||^2)$より


## 14. Brownian Motion
1. 帰納法で$p(x_n | x_0)$を求める
2. 拡散方程式を満たすことを示す

## 15. Neural Network
