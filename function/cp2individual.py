#!/usr/bin/env python3

import os, sys, re

# alias

element = re.compile(r'/C_([^/]*/code/[^/]*nfq)$')
cbar = re.compile(r'/C_')

# ファイル名の取得

def gf(path):
    for (root, dirs, files) in os.walk(path):
        for file in files:
            yield os.path.join(root, file)


if __name__ == '__main__':

    # 基本ディレクトリ
    basepath = "/home/ugos/share/ACQFQ/fq2017"

    # コピー対象のファイルの取得
    flist = filter(element.search, gf(os.path.join(basepath, "data")))

    # ループ
    for path in flist:
        # ファイルの読み込み
        with open(path, "r", encoding="cp932") as rf:
            # 変換
            tmp = rf.read() \
                  .replace("SCSECSUB = {C8}", "SCSECSUB = {C0}") \
                  .replace("SCSECSUB={C8}", "SCSECSUB={C0}")
    
            with open(path.replace("/C_", "/I_"), "w", \
                      encoding="cp932", newline="\r\n") as wf:
                wf.write(tmp)
