---
draft: false

date: "2023-08-05T11:11:09+09:00"
# url: ""

title: "GIGABYTEのマザーボードのBIOSをアップデートした"
description: ""
keywords: ""

tags: ["PC"]
categories: []
---

こんにちは、Hidegonです。久々のブログ更新です。(サボってました)  
タイトルのままなのですがGIGABYTEのマザーボードのBIOSをアップデートしました。  
(UEFIが正しいんだと思いますが、どっこもかしこもBIOSって書いてあるのでBIOSで。)  
BIOSなんて更新しなくてもエエだろ的なスタイルで生きてきましたが、

[Gigabyte App Center バックドアによるサプライチェーン攻撃のリスク (Eclypsium)](https://eclypsium.com/blog/supply-chain-risk-from-gigabyte-app-center-backdoor/)  

だのなんだのの記事があったのでとりあえず更新したわけです。  
そもそも影響を受けるマザーボード一覧に記載されていませんでしたし、Windowsでもないので更新する必要はないのですが、なんとなく。  

[https://www.gigabyte.com/jp/Support/Motherboard](https://www.gigabyte.com/jp/Support/Motherboard)

からBIOSを落とせます。  
私が使っているマザーボードは B660M DS3H AX DDR4 (rev. 1.x) ですので、検索してみます。  
検索するとページに飛んで、下の方にいくと BIOS と書かれた場所があります。  
適当にダウンロードするんですが、詳細にチェックサムがあります。  
値的にCRC16かと思って計算したのですが、一致せず。。。  
調べてたら

[What's the deal with the ancient bios checksum algorithm on the Gigabyte site? | Reddit](https://www.reddit.com/r/gigabyte/comments/x0z0kj/whats_the_deal_with_the_ancient_bios_checksum/)  

という投稿がありガックリ。  
なんで独自実装なんだよ！標準的なやつにせんかーい！と思いつつも、仕方ないので検証はQ-Flashにまかせて続けていきます。  
(誰かが解析して計算ツール出してくれないかな)  

落としたzipの中身の `モデル名.バージョン` のファイル (私の場合 `B660MDS3HAXDDR4.F23`) を適当なUSBフラッシュメモリにコピーします。  
それをPCに挿して起動時に F2 か Delete か End を連打してQ-Flashに入ります。  
あとは画面の指示通りにやれば更新されます。途中で焦って操作したりしなければダイジョブ、なはず。  
10分もかからなかったと思います。思ってたよりは長い。  
更新完了したら自動で再起動します。  
停電とかおこらなくて良かった。。。更新中はヒヤヒヤですw

以上、GIGABYTEのBIOSをアップデートした話でした。  
