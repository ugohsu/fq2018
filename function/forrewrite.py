#!/usr/bin/env python3

import os, sys, re

# alias

nfq = re.compile(r'nfq$')
codefile = re.compile(r'/code/[^/]*nfq$')
makexls = re.compile(r'^MAKEXLS .*$', re.MULTILINE)

# ファイル名の取得

def gf(path):
    for (root, dirs, files) in os.walk(path):
        for file in files:
            yield os.path.join(root, file)


if __name__ == '__main__':

    # 基本ディレクトリ
    displaypath = "C:/ACQFQ/fq2017"
    basepath = "/home/ugos/share/ACQFQ/fq2017"

    # コピー対象のファイルの取得
    flist = filter(nfq.search, gf(os.path.join(basepath, "data")))

    # ループ
    for path in flist:
        # MAKEXLS に挿入するパスの作成
        inputpath = codefile.sub('/xls/foofoo.xls', path) \
                    .replace(basepath, displaypath) \
                    .replace("/", r"\\")
    
        # ファイルの読み込み
        with open(path, "r", encoding="cp932") as rf:
            # 変換
            tmp = makexls.sub('MAKEXLS /F=' + inputpath, rf.read())
            
            # ファイルの書き込み
            outpath, _ = os.path.splitext(path)
            with open(outpath + '_r.nfq', "w", encoding="cp932", \
                      newline="\r\n") as wf:
                wf.write(tmp)
