---
draft: false

date: "2023-03-02T23:54:47+09:00"
# url: ""

title: "SearXNGのすゝめ"
description: ""
keywords: ""

tags: []
categories: []
---

## SearXNGとは

SearXNGは、複数の検索サイトの検索結果を集めるメタ検索エンジンです。  
個人情報の収集や追跡なく使用できます。  
要はプライバシに配慮した検索エンジンです。  
GoogleやBing、その他さまざまな検索エンジンから検索結果を集めてきて表示してくれます。  
ちなみに、SearXNGはSearXのフォークです。  

## SearXとの違い

興味ないかもしれませんが一応書いておきます。  
<https://github.com/searxng/searxng> から原文を読めます。  

### ユーザーエクスペリエンス

**シンプルテーマの大幅なアップデート:**

* デスクトップ、タブレット、モバイルで使用可能
* ライト/ダークテーマ の実装
* RTL言語のサポート
* 最新の翻訳を使用でき、Weblateから貢献できる

**設定のページの更新:**

* どの検索エンジンが信頼できるか、確認できる
* エンジンは各タブでグループ化されている
* 各エンジンに説明がある
* 匿名メトリクスのおかげで、エンジンのバグを報告しやすくなり、エンジンがより早く修正されるようになった
* メトリクスを記録したくない場合は、サーバでそれを無効にできる
* 検索結果のURLをブロックしたり、置き換えたりできる

### セットアップ

* 画像プロキシに Morty は必要ない
* ボットをブロックするためにFiltronは必要ない
* ARM64 と ARM/v7 用の Docker イメージの用意
* 最新のインストールスクリプトの用意

SearXに比べるとさまざまな機能が追加されていることがわかります。  
[SearXのREADME](https://github.com/searx/searx)によると、SearXNGは公開インスタンス用、SearXはプライベートな用途用に使ってくれ、とのことです。  

## インスタンスの選び方

SearXNGはボランティアが公開インスタンスを建ててくれています。  
私達はそのインスタンスの中から好きなものを選びます。  
が、インスタンスを選ぶ時にポイントがあります。  
それは

**地理的に近いサーバを使う**  

これが重要なポイントです。結構体感速度が結構違います。  
表示上の速度を信用するとえらい目にあいます。  
日本から計測されてるわけじゃないので...  
インスタンスの一覧は<https://searx.space/>から確認できます。  
Countryに自分の国に近い国コードを入力して検索してください。  
日本に住んでる人ならシンガポール(SG)とかがオススメです。  

## 設定

右上の設定ボタンから変更できます。  
SearXNGには設定をURLにして保存できる機能があるのでコレを使った設定を貼っておきます。  

[設定](https://priv.au/preferences?preferences=eJx1VzuP5DYM_jVxY9wgyRVBiqkCpEhzB-R6g5Y4NteS6NNjPN5fH2psj-X1plhj9Emi-PzIVRCxY08Yrh069GAqA65L0OH1Db78870yrMDkRQUpsmI7Gox47Zg7gxVZOdmMnh_z9YdPWFmMPevr92___qgC3DAgeNVff61ijxavgfL9ymNIJoaGXeNwaiK0y23N1Mgemzv6K4MsL-y7arnVhDiLJhr8UCl0EX0Dhjpn5ff1bzABK9B3cAp1sz67oD8T-rkh10SKImAByd3IURSpyrMx6_sUoDVyH11HTpzyZwdd07Ao73_5_S8Yh9qS9-xLTFSr5VuHyB6LDVGA7lhTaJrVt080kmqap9-CrFtwWoEdm8amQCoj5LryRkuxTWrAKLdiXkdNXaGUUupLvDfNnTRyFskjOvFfwOIZsTEEj7dGzCUUFwk241i-o5I3hB8QL2fnEtOI7-L4l7Ya7wQuilnFa1p3tcanf4ndwX70PJHetZ9oIA0RDm-Iufmv43oRWYre9yaELORjKCyMYcfQ8huNqAl2LEpo54Olvz2KJ26G1OBLwCPWgW9xAo-1Jo9KQj2v8bh5cgNBGVQRTCnsTuqok7SCEMs35VdkXoV0kpnQrgvFGlv03bb3LLV6NDDnPCuMK3cs3yl76pUG3chal6HqofWQP6tcsrrdZZGD4jI5-UmcwufYJvKNQs-7jEEcB6FQ0JA86ec6Wx3okw2-1YpdJzVfBtlICdwPKWG4DREvPqy6w7uZPalCFSEeUCO49YClhzKc9H7AjXbdczMU2ZDLBSSmY2ol8LBm7F4meV92udB-BLGzo7CVpFy9SCHsKysUUoj4OUmJlOY8gVqoT4Tm7ws65fsCLzEoYhFwJFhIrkAhDKlNLqZVk5BG9CngFvHlQk6vOn9eCQwWckDwdczKo6TqoHo24EtTQi71MZN-YU7kYebIkgtDDsDmpuSCpGboC3Nm6HPO71efwNETGsjMlnMgCtvuZJGL9UTtgZgseKFsseOQN9K6HsKw_ohm0mmZh_ARPOiRgZ-JI348FTh5dUIz5VKcTzDPH7ylScV3dkcC-vr1j8fuOZ00Fo4M-O7AHqzlN8ShRBzcc5x3wKd27tBuFTMi-phaLFxoMy3KE4MwxzRhW2z5ZKUPlu7mBw3sJM3rMDt2sy1aXXgbL-Pkjqxuhf4PfcyLhiUwSsWaLYc_hc_lIGm6k8AShz7FnShfgiop6kMnf8oTYkmPOmu38Yh_0L3M77y3touyBbvurMsTPWTMEznVqmbp3r7u08bvew87dMYoSe9Ew8KxN-257JbSJnYxC_sfWsrSD06arvhB1xU7abvin5R-v7638CtI03sRy8ahuZMHjCf-DFFaaJTOXHCozrm4Hxt7YZAihUbyMpu2MBfQPG5xk6c0xSIDOckcdSR8oSo1sFTFzfD0ShlDWpq3zDWxIPQ4UYzlKDFz-lAsL2QTL5mSKQp8oeHEZmHTsS86jJVisTIw1NGDC0bMKgcg9trRUAAx-gttnthH0tEkyeRwzaXxuKyrS88hCjegjM3CtQtFHw4Ibzbi2gHn8KqJ_xGVqXpZnKQwNMtsPnmZmU_baxVL_NTyD8UsE7iRMemTk-Ymo_iNTzsSlUb1qIbzjodcQY0MqKKBzSGtpOVIWl3_A-MV0t8=&save=1)

僕は[priv.au](https://priv.au/)を使っています。  
別のインスタンスでもクエリを移植すれば使えると思います。  

## おわりに

メタ検索エンジン SearXNG のすゝめでした。  
その他にもいろいろな検索エンジンがあるのでまたいつか比較したいです。  
最後まで読んでいただきありがとうございました。  
