# 概要 (2018-01-08)

# base

- base.txt
    - 2018-01-08
- `base_stock.txt`
    - 2016-08-23
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

## 期間指定

195001 ～ 202012

## ターゲット指定

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
    - 有価証券関係項目
    - 金融商品関係項目
    - デリバティブ取引関係項目
    - 退職給付関係項目
- internalTransaction
    - 関係会社取引
- specificationPolicy
    - 社債・借入金明細表
    - 会計処理の方法
- sgae
    - 売上高・営業収益明細
    - 売上原価・営業原価明細
    - 製造原価明細
    - 販売費及び一般管理費

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
