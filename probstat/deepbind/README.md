# Deepbind
DNAの配列結合モチーフ発見

## requirements
keras \footnote{ \url{ https://keras.io/ja/ } }
numpy
```
$ sudo pip install keras
$ pip install numpy
```

## コード
`simple..py`

## 実行
tensorflow backendで動かした．学習サンプル数は2000，検証サンプル数は200に増やし，batch size 100で100 epoch学習させた．

## 結果

### 各学習についてのばらつき
検証のために学習を数回行ったところ，accuracyが0.9程度まで上がる時と，0.8程度の低い値で止まってしまう時とがあった．epoch数とaccuracyの推移を，条件を変えずに8回試行した時のデータをプロットしたものが以下の図である．8回中3回はよく学習しているが，残りは低い値で止まってしまっている．

\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{figure/compare_dropout1.png}
\caption{}
\end{figure}

以下では，このうち精度の高い方の学習結果について，妥当性をみた．

### 精度
ここで検証した学習では，test dataに対するaccuracyは0.9699999988079071だった．またepoch数に関するaccuracyの推移は，以下のグラフのようだった．trainingデータのaccuracyだけ上がっているのではなく，validationについても同じように上昇しているので，過学習にならずうまく学習できていそうなことがわかる．

\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{figure/training.png}
\caption{epoch数(横軸)に対するaccuracy(縦軸)の推移．学習に使ったデータに対して計算したaccuracy(training)と，学習に使わないtestデータに対するaccuracy(validation)を同時にプロットしている．}
\end{figure}

### Convolution層の重みの分析
学習後に，Convolution層の重み行列は以下のような値を取っていた．
```
[array([[[-1.06869733],
        [ 0.53636855],
        [-1.06798279],
        [-1.0663842 ]],

       [[ 0.17715622],
        [-1.42838645],
        [-1.4269135 ],
        [ 0.1762639 ]],

       [[-1.40744865],
        [ 0.16241203],
        [ 0.16904299],
        [-1.44135761]],

       [[-1.12742162],
        [-1.12841606],
        [ 0.47733912],
        [-1.12644589]],

       [[-0.93403089],
        [-0.93356711],
        [-0.93546027],
        [ 0.67002547]]], dtype=float32)
```

これは配列生成スクリプトのモチーフの重みに対応している．(`motif_finding/generate_motif_dataset.py`)
```
motif    = [[0.0, 1.0, 0.0, 0.0], # C
            [0.5, 0.0, 0.0, 0.5], # A/T
            [0.0, 0.5, 0.5, 0.0], # C/G
            [0.0, 0.0, 1.0, 0.0], # G
            [0.0, 0.0, 0.0, 1.0]] # T
```
符号や絶対値ではなく単純に4つの中での大小を比較すると，下のmotifの生成確率と同じ傾向があることがわかる．Convolution層では，この重み行列でフィルタした値が次の層に出力されるので，今回の例では埋め込まれたモチーフ，例えば`CACGT`という配列に対してフィルタを当てた時に，大きい正の値が出る．続くMaxPooling層で，長さ20の配列の中のフィルタ処理後の最大値を取るので，モチーフが含まれている配列が入力された時は，その結果もモチーフを含まない配列に比べて大きい値を取る．その結果出てくるスカラー量を元に，モチーフを含むか含まないかを判別している．
この結果から，モチーフが埋め込まれた配列のデータを使って正しくモチーフの配列を推定できていると言えそうである．


## Motifサイズへの依存
今回学習に使っているデータセットが，長さ5のモチーフを含めるように作られている．上ではこのモチーフの長さは既知として学習させたが，実際にはモチーフの長さが未知の場合の方が多いはずである．そのためMotifサイズをパラメータに取って，学習を行わせた後の精度がどう変化するかをみた．その結果が下の図である．長さ5というのはここからも推定可能なように思われる．

\begin{figure}
\begin{minipage}{0.45\hsize}
\centering
\includegraphics[width=0.9\textwidth]{figure/motiflength.png}
\caption{横軸を学習時にdeepbindモデル内で仮定したモチーフの長さ，縦軸がtestデータに対するaccuracy．全てモチーフの長さ以外は同一のデータセット，モデル構成を使っている．モチーフの長さが実際の5より短い場合，長い場合共に下がっていく傾向が見える．これはConvolutionの働きから考えても矛盾しない結果である．}
\end{minipage}
\hfill
\begin{minipage}{0.45\hsize}
\centering
\includegraphics[width=0.9\textwidth]{figure/motiflength-time.png}
\caption{epoch数に関して各学習のaccuracyの推移を示したもの．}
\end{minipage}
\end{figure}

## 変更点
- dropout層の追加
- sigmoidの変更


