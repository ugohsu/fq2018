# 概要 (2018-01-08)

# base

- `base.txt`
    - 2018-01-08
- `base_stock.txt`
    - 2018-01-13
    - 上場全社 (上場廃止含む) とジャスダック全社 (上場廃止含む) の両方
      を取得し、sort | uniq をおこなう。

# data

## ディレクトリの作成

- データ種のディレクトリの作成
    - `mkdir $(ls directory of 2016)`
- subdirectory の作成
    - `ls | while read x; do mkdir $x/code $x/csv $x/xls; done`

## 取得共通規則

- ダウンロード
    - 行種
        - 会社
        - 単独/連結
        - 有報/短信
        - 決算期
        - 期間
    - 列種
        - 項目
- 業績予想 (会社発表) 
    - サブキー
        - 採用する予想
            - すべての予想履歴
        - 採用する実績
            - すべての実績履歴
        - 予想データの取り扱い
            - 実績および予想データを採用
- 株式 (月次)
    - アイテム指定
        - 株式で検索してヒットする後半すべて
            - 株式コード、発行済株式数、普通株式数
        - 月次株価
        - 月次銘柄別指標

## 期間指定

195001 ～ 202012

## ターゲット指定

- attr
    - 会社属性
- basis
    - 基本項目
- bs
    - 株式コード (検索)
    - 資産 (すべて)
    - 負債 (フラグ以外)
    - 純資産 (フラグ以外)
- pl
    - 損益計算書 (すべて)
    - 包括利益関連項目 (フラグ以外)
- cf
    - キャッシュフロー計算書
- ss
    - 株主資本等変動計算書
- other
    - その他の項目
- related
    - 有価証券関係項目 (すべて)
    - 金融商品関係項目 (フラグ以外)
    - デリバティブ取引関係項目 (フラグ以外)
    - 退職給付関係項目 (フラグ以外)
- internalTransaction
    - 関係会社取引
- specificationPolicy
    - 社債・借入金明細表 (すべて)
    - 会計処理の方法 (フラグ以外)
- sgae
    - 売上高・営業収益明細 (すべて)
    - 売上原価・営業原価明細 (フラグ以外)
    - 製造原価明細 (フラグ以外)
    - 販売費及び一般管理費 (フラグ以外)
- giketsu
- `num_stock`
- `num_shareholder`

# arrnfq の手順

## 連結用のコードを単独用に変換

### 変換すべき点

- CONNECT
    - `SCSECSUB = {C8}` を `SCSECSUB = {C0}` に変更
- !SUBKEY
    - `SCSECSUB={C8}` を `SCSECSUB={C0}` に変更

### 変換スクリプト

cp2individual.py

## レポート結果出力 (MAKEXLS) の修正

### 変換スクリプト

forrewrite.py

## 一括 arrnfq

`find -iname '*_r.nfq' | xargs -i arrnfq base/base.txt 20 {}`

## 一括 unifiles

fq2017/data まで移動し、

`find -name 'csv' > unifilesScript.sh`

を実行。
その後、function/unifilesScript.sh のように加筆し、実行

## stockprice の unit ディレクトリの作成

各種 stockprice のディレクトリまで移動し、function/mkunit.sh を実行

## stockprice のファイル名問題の修正

FQ の株価データについて、企業 ID のリクエストと得られる結果についての
不一致が存在した (2017-03-24 時点)。
(2018-01-20 時点においては、日次データのみ)

delunit スクリプトは、リクエストした ID
(unit のファイル名) と、ファイルに収録されている企業コード (日経会社コ
ード) とが一致するかチェックし、一致しない ID のファイル名を抽出する。

`delunit.py --encoding cp932 -n 2 * | xargs rm`
