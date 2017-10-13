# 情報科学実験 対数線形モデルとHMMの半教師付き学習
05-175511 中林

## 演習問題1 $V(k,v)$の初期値

$V(0,v)=Z$ (if $v$ == START), $0$ (else)
ただし$Z$は与えられた分配関数である。

## 演習問題2 HMMの対数線形モデル表現
対数線形モデルは$p(y|x; w) = \frac{\exp \sum_{j=1}^{J} w_j F_j (x,y)}{Z(x,w)}$
マルコフモデル $$\log p(x,y) = \sum_{t=1}^T \log p(y_t | y_{t-1}) + \log p(x_t | y_t) = \sum_{i=1}^m \sum_{j=1}^m N^a_{i,j} (y) \log a_{i,j} + \sum_{i=1}^m \sum_{d=1}^D N^e_{i,d} (x,y) \log e_{i,d}$$
を、$p(y|x)$の形に表して、$F_j$の線形和でかけることを示せば良い。

$$p(y|x) = \frac{p(x,y)}{p(x)} = \frac{\exp(\log p(x,y))}{\sum_{y} p(x,y)} = \frac{\exp(\log \sum_{i=1}^m \sum_{j=1}^m N^a_{i,j} (y) \log a_{i,j} + \sum_{i=1}^m \sum_{d=1}^D N^e_{i,d} (x,y) \log e_{i,d}) }{\sum_{y} p(x,y)}$$ 

最右辺の分母の$\exp$の中身は線形和になっているから、対数線形の形になっている


## 演習問題3 式(38)をHMMの場合に直す
HMMの場合の式(演習問題2の式)を、式(38)に代入する。

$p(x,y) = \prod_{t=1}^T a_{y_t, y_{t-1}} e_{x_t, y_t}$
$p(y|x) = \frac{\prod_{t=1}^T a_{y_t, y_{t-1}} e_{x_t, y_t}}{p(x)}$

$$R(y|x) = \frac{ \prod_i p_i^D(y|x;\lambda_i)^{\gamma_i} \prod_i p_j^G(x,y;\lambda_j)^{\gamma_j} }{\sum_y \prod_i p_i^D(y|x;\lambda_i)^{\gamma_i} \prod_i p_j^G(x,y;\lambda_j)^{\gamma_j} }  = \frac{ \prod_i (\frac{\prod_{t=1}^T a_{y_t, y_{t-1}} e_{x_t, y_t}}{p(x)})^{\gamma_i}   \prod_i (\prod_{t=1}^T a'_{y_t, y_{t-1}} e'_{x_t, y_t})^{\gamma_j}  }{  \sum_y \prod_i (\frac{\prod_{t=1}^T a_{y_t, y_{t-1}} e_{x_t, y_t}}{p(x)})^{\gamma_i}   \prod_i (\prod_{t=1}^T a'_{y_t, y_{t-1}} e'_{x_t, y_t})^{\gamma_j}}$$
より
$$ = \frac{ \prod_i (\prod_{t=1}^T a(i)_{y_t, y_{t-1}} e(i)_{x_t, y_t})^{\gamma_i}   \prod_i (\prod_{t=1}^T a'(i)_{y_t, y_{t-1}} e'(i)_{x_t, y_t})^{\gamma_j}  }{  \sum_y \prod_i (\prod_{t=1}^T a(i)_{y_t, y_{t-1}} e(i)_{x_t, y_t})^{\gamma_i}   \prod_i (\prod_{t=1}^T a'(i)_{y_t, y_{t-1}} e'(i)_{x_t, y_t})^{\gamma_j}}$$


