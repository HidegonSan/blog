---
draft: false

date: "2023-02-25T00:01:11+09:00"
# url: ""

title: "PaperModでページネーションをカスタムする方法！"
description: ""
keywords: ""

tags: ["ブログ", "Hugo", "PaperMod"]
categories: []
---


この記事ではPaperModでページネーションをカスタム、数字をつける方法について解説します！  
このブログではテーマに[PaperMod](https://github.com/adityatelange/hugo-PaperMod)を使用しています。  
説明が下手なのですが、PaperModのページネーションは 前のページ/次のページ のような形式です。  
しかし、これでは最古のページにジャンプするのができなかったり、全部で何ページあるかがわかりにくいという問題があります。  
そこで今回はPaperModのページネーションを  
`| << | < | 1 | 2 | 3 | 4 | 5 | > | >> |`  
のように変更します。  
早速、Hugoのテンプレート機能を使ってPaperModのページネーション上書きしましょう！

## やり方

まずはページネーションを表示させるテンプレート本体を作っていきます。  
そのテンプレート本体を`list.html`から呼び出してページネーション変更します。  
ページネーションについて調べていたらこんなものを見つけました。  

**[【Hugo】ページネーションの作り方](https://joni.jp/pg/hugo-pagination/)**  

標準で用意されている！これは実装が楽そうで良かったです。  
この記事を参考に作成します。  
Hugoのテンプレート機能を使ってページネーションを変更しましょう。  

## テンプレートを作成する

### ページネーションのテンプレート

`layouts/partials/pagination.html` を作成します。  
そして次のコードをコピーして貼り付けてください。

```html
{{/*  Thanks: https://joni.jp/pg/hugo-pagination/  */}}
<nav>
  {{ template "_internal/pagination.html" . }}
</nav>
```

このコードはHugoの内部テンプレートを呼び出しています。  
元コードではナビゲーションタグで囲まれていなかったのですが、ナビゲーションリンク貼ってるんで適切でしょう。([参考](https://zenn.dev/tak_dcxi/articles/a8c9c37a0a3fe1#%E3%83%98%E3%83%83%E3%83%80%E3%83%BC%E3%83%A1%E3%83%8B%E3%83%A5%E3%83%BC%E3%81%AF-nav-%E3%81%A7%E5%9B%B2%E3%82%80))  
ついでに内部テンプレートがどこにあるのか気になったのでソースを見ました。  
[(Hugo)/tpl/tplimpl/embedded/templates/pagination.html](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/pagination.html)  
が実装っぽかったです。ちゃんと調べてないのでわかりませんが。  
とりあえず、これで関連記事のテンプレートは作成できました。  
次はこのページネーションのテンプレートを呼び出していきましょう。

### テンプレートの呼び出し

`themes/PaperMod/layouts/_default/list.html` を `layouts/_default/list.html` にコピーしてください。  
コピーしたら88行目に

```html{linenostart=88}
<footer class="page-footer">
```

と書かれていると思います。  
この下にテンプレートを呼び出すコードを書いていきます。  
まず、PaperMod標準のページネーションを無効にしましょう。  
89行目から106行目までをコメントアウトするか削除してください。  
これは知らなかったのですが、Hugoではコメントアウトする際、  

```html{linenos=false}
<!-- Comment -->
```

のようにするのではなく、  

```html{linenos=false}
{{/*  Comment  */}}
```

とするらしいです。  
ここらへんの仕様はあんまよくわかってないのでいつか勉強したいです。  
気を取り直して、呼び出す処理を書いていきましょう。  

コメントアウトするのは  

```html{linenostart=89}
  <nav class="pagination">
```

から

```html{linenostart=106}
  </nav>
```

までです。  

無効化が完了したら、次のコードをコピーして コメントアウト/削除 した行の下に貼り付けてください。  

```html
{{/*  Thanks: https://joni.jp/pg/hugo-pagination/  */}}
{{- partial "pagination.html" . -}}
```

これでテンプレートを呼び出すコードは終わりです。  

### CSSを適用する

これだけでも一応は機能しますが、見た目が最悪なのでCSSを書いていきます。  

`assets/css/extended/custom.css` を作成してください。  
ここに作成したCSSは1つのファイルにまとめられます。([詳細](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs#bundling-custom-css-with-themes-assets))  
次のコードをコピーして貼り付けてください。  

```css
/* ページネーションを書き換える PaperModのページネーションがベース */
/* ul */
.pagination-default {
    margin: 0;
    padding: 0;
    list-style: none;
}

/* li */
.pagination-default > .page-item {
    display: inline-block;
    width: 100%;
    text-align: center;
}

/* テキスト */
.pagination-default > .page-item a {
    display: block;
    color: var(--theme);
    font-size: 16px;
    line-height: 36px;
    background: var(--primary);
    border-radius: calc(36px / 2);
    padding: 0;
    margin-left: 5%;
    width: 90%;
}

/* 現在のページ */
.pagination-default > .active > a {
    background: var(--secondary);
}

/* ホバー */
.pagination-default > li:not(.active) > a:hover {
    background: var(--content);
}
```

これでCSSは終了です。  
PaperModのCSSを参考に作成しました。  
PaperModのCSSは `themes/PaperMod/assets/css/common/main.css` にあります。  
現在のページの強調やホバー時に背景が変わるようにしました。  
コレ、結構気に入ってます (笑)  
CSSで疑似クラスやセレクタをまじめに使用したことがなかったのですが、かなり融通が効きますね。  
HTML5 + CSS3 はチューリング完全だとか聞いたことがありますが納得です。  
このブログでも使用しているので**いつか**確認してみてください。  
その...記事が増えないと表示されないので...

## 完成

完成すると次のように表示されていると思います。  
十分な記事数がないと表示されないので注意してください。  

![完成したページネーションの見た目](/img/papermod-custom-pagination/result.png)

(これは少しカスタムしてあるのでちょっとだけ見た目が違うかもしれません)  
以上で終わりです！お疲れ様でした！  

## おわりに

今回はHugoのテンプレート機能を使ってPaperModのページネーションをカスタムしてみました。  
その他にもテンプレート機能を使うことでさまざまなことができます。  
このブログでは以前に [PaperModで関連コンテンツを表示する方法！](/posts/papermod-related/) という記事も投稿しているのでこちらもぜひご覧ください！  
最後まで読んでいただきありがとうございました。  
