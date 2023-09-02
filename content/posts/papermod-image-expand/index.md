---
draft: false

date: "2023-08-12T16:20:09+09:00"
# url: ""

title: "PaperModでクリック時に画像を拡大する"
description: ""
keywords: ""

tags: ["ブログ", "Hugo", "PaperMod"]
categories: []
---


PaperMod、素晴らしいテーマなのですが、ぼちぼち不満もあります。  
そんな不満をHugoのテンプレート機能で解決していこうプロジェクトN記事目になります。  
今回やることはタイトルにもある通り、クリック時の画像の拡大です。  
自分のブログをスマホから見たときに画像が小さくてわざわざ新規タブで見たので改善が必要だと思い、行いました。  
(そもそも適切な大きさの画像を表示しろというのは置いといて)

## やり方

Hugo image hover と適当に調べたら

[Magnific Image Pop-Up Modal for Hugo | GitHub](https://gist.github.com/zjeaton/0cdd7e4bed9d292ab6f3d76b0369f16d)  

がヒットしました。  
使えそうなのでこのまま使っていきます。  
ライセンスは各自見といてください。  

### 画像描画のフック

まずは画像描画をフックします。  

`/layouts/_default/_markup/render-image.html` を作成します。  

```html
<!-- Magnific Image Pop-Up Modal for Hugo | Thanks: https://gist.github.com/zjeaton/0cdd7e4bed9d292ab6f3d76b0369f16d -->


<!-- Images that use the standard image format for markdown will be displayed in a 
  magnific modal popup. Use format ![alt text](/path/to/image.img) -->
<!-- Place this file in layouts > _default > _markup > render-image.html -->
<!-- Also place the image-modal.css and partial/image-modal.html appropriately. -->
<!-- Id for the image on the page is set to a random 6 numbers, chosen from 1 to 500 -->
<!-- Onclick opens the modal, and displays/overlays the the image that has the id for the 
  clicked image. -->
<!-- attribution appreciated. github: zjeaton web: https://froglegs.co -->


<span class="image_modal_md_image">
    <img loading="lazy" id="{{ first 6 (shuffle (seq 1 500)) }}" src="{{ .Destination | safeURL }}" onclick="open_image_modal(this.id)" alt="{{ .Text }}" {{ with .Title}} title="{{ . }}"{{ end }} />
</span>
```

これを入力します。  
よくわかっていませんが、`<img>`タグの出力をフックしてこいつを呼び出せるみたいです。  
ランダムなIDを生成してonclickでイベント付与、`open_image_modal`がそのIDの画像をポップアップ、って流れっぽいです。  

### ポップアップ本体の作成

`/layouts/partials/image_modal.html` を作成します。  

```html
<!-- Magnific Image Pop-Up Modal for Hugo | Thanks: https://gist.github.com/zjeaton/0cdd7e4bed9d292ab6f3d76b0369f16d -->


<!-- Place in layouts > partials > image-modal.html -->
<!-- Use the partial at the bottom of any page in which you want magnific pop-up images,
  or simply place at the bottom of baseof.html -->
<!-- Modal will open upon clicking the image. Modal will close with clicking the x or image. -->


<!-- The Modal -->
<div id="image_modal" class="image_modal" onclick="close_image_modal()">
    <button class="image_modal_close" onclick="close_image_modal()">close</button>
    <div class="image_modal_content" onclick="close_image_modal()">
        <img class="image_modal_picture" id="image_modal_picture" onclick="close_image_modal()">
    </div>
</div>

<script>

    // Open the Modal
    function open_image_modal(target_id) {
        var src = document.getElementById(target_id).src;
        if (src.includes("#")) {
            src = src.substring(0, src.indexOf("#"));
        };
        document.getElementById("image_modal_picture").src = src;
        document.getElementById("image_modal").style.display = "block";
        // Ensures the site footer is not shown if front of the modal. Remove if this is not an issue or
        // there is no footer. "site-footer" id can also be changed appropriately.
        // document.getElementById("site-footer").style.display = "hidden";

        // 目次とページトップ非表示
        if (document.getElementsByClassName("toc").length) { document.getElementsByClassName("toc")[0].style.display = "none"; }
        if (document.getElementById("top-link").length)    { document.getElementById("top-link").style.display = "none"; }
    }


    // Close the Modal
    function close_image_modal() { 
        // prevents flashing last modal image while new id is loading on open
        document.getElementById("image_modal_picture").src = "";
        document.getElementById("image_modal").style.display = "none";
        // See note above regarding the footer 
        // document.getElementById("site-footer").style.display = "block";

        // 目次とページトップ表示
        if (document.getElementsByClassName("toc").length) { document.getElementsByClassName("toc")[0].style.display = "block"; }
        if (document.getElementById("top-link").length)    { document.getElementById("top-link").style.display = "block"; }
    }

</script>
```

これがポップアップ本体です。  
PaperModに合うよう、目次とページトップを隠すようにコードを変更しています。  
(目次は私がsticky_tocというCSSを適用しているからですが...)  
次はこのポップアップ本体を呼び出します。  

### ポップアップ本体の呼び出し

`/layouts/_default/baseof.html` の 6~15 行目が  

```html
<body class="
{{- if (or (ne .Kind `page` ) (eq .Layout `archives`) (eq .Layout `search`)) -}}
{{- print "list" -}}
{{- end -}}
{{- if eq site.Params.defaultTheme `dark` -}}
{{- print " dark" }}
{{- end -}}
" id="top">
```

となっていると思うので、ここから下に呼び出すコードを書いていきます。  
この下に以下のコードを追加で貼り付けてください。

```html
    <!-- Magnific Image Pop-Up Modal for Hugo | Thanks: https://gist.github.com/zjeaton/0cdd7e4bed9d292ab6f3d76b0369f16d -->
    {{- partial "image_modal.html" . -}}
```

これで呼び出し側も完了です。

### CSSの適用

最後にCSSを適用します。  

`/assets/css/extended/image_modal.css` を作成します。  

```css
/* Magnific Image Pop-Up Modal for Hugo | Thanks: https://gist.github.com/zjeaton/0cdd7e4bed9d292ab6f3d76b0369f16d */

/* The markdown image container */
.image_modal_md_image {
    cursor: pointer;
}

/* The Modal (background) */
.image_modal {
    display: none;
    position: fixed;
    z-index: 1;
    /* padding-top: 4em; */
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: var(--theme);
}

/* Modal Content */
.image_modal_content {
    position: relative;
    background-color: var(--theme);
    margin: auto;
    padding: 0;
    width: 90%;
    max-width: 1400px;
    display: flex;
    align-items: center;
    height: 100%;
}

.image_modal_picture {
    /* display: flex;
    align-content: center; */
    cursor: pointer;
    max-width: 100%; /* => 90% */
    max-height: 80vh;
    margin: auto;
    width: 100%;
    object-fit: contain;
}

/* The Close Button */
/* Optimized for accessibility by using a button named close but 
    shifting the close text out of the button and only showing x */
.image_modal_close {
    z-index: 2;
    color: var(--content);
    background-color: var(--theme);
    position: absolute;
    top: .5em;
    right: .5em;
    font-size: 2em;
    font-weight: bold;
    height: 1em;
    width: 1em;
    text-indent: 10em;
    overflow: hidden;
    border: 0;
}

.image_modal_close::after {
    position: absolute;
    line-height: 0.5;
    top: 0.2em;
    left: 0.1em;
    text-indent: 0;
    content: "\00D7"
}

.image_modal_close:hover,
.image_modal_close:focus {
    color: var(--primary);
    text-decoration: none;
    cursor: pointer;
}
```

上記のコードを貼り付けてください。  
ここにつっこんだCSSはHugoかPaperModかによって1ファイルにバンドルされます。(すごく便利)  
こちらも、PaperMod用にテーマ切り替えに対応するよう、カスタムしてあります。  
ついでに画像が中央寄せになるようにし、小さい画像の場合いい感じに拡大してくれるようにもしました。  

## 完成

適当に画像を配置して試してください。

<!-- ![sample image (favicon)](/favicons/android-chrome-192x192.png)   -->

`うちのファビコン`

...と書いた矢先、バグ発見！  
縦横比が維持されていません！！！  

調べたら `object-fit: contain;` を指定してあげたら良さそう？([MDN](https://developer.mozilla.org/ja/docs/Web/CSS/object-fit))  
ということで設定したらいい感じになってたのでこれで良しとします。  

以上、PaperModでクリック時に画像を拡大する方法でした。  
関連記事もぜひ =ω=  
