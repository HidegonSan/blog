---
draft: false

date: "2023-08-25T20:48:35+09:00"
# url: ""

title: "TwiHubで動画を直接再生できるUserScriptを作った"
description: ""
keywords: ""

tags: ["UserScript", "ブラウザ"]
categories: []
---

## 何がしたい

[TwiHub](https://twihub.me/v2/ranking.php)は、Twitterで人気な動画を取得し、まとめて紹介しているサイトです。  
何に使用しているかは置いておいて、私はこのサイトをぼちぼち使います。  
で、このTwiHubなんですが、動画を再生するときに1クリック余計な動作をして、直リンクへ飛ばないとダメなわけです。  
それは面倒なのでUserScriptを作りました。  

## コード

```js
// ==UserScript==
// @name         TwiHub直再生
// @version      0.0.4
// @description  TwiHubで動画を直接再生できるようにします
// @match        *://twihub.me/v2/detail.php*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=twihub.me
// @grant        none
// ==/UserScript==

// License: WTFPL

try {
    var card = document.getElementsByClassName("c_detail-card")[0]
    var video_url = document.querySelectorAll("a[href^='https://video.twimg.com/']")[0].href
    var video_extension = video_url.split(".").slice(-1)[0].split("?")[0]
    var element = `<video controls=""><source src="${video_url}" type="video/${video_extension}" autoplay></video>`
    card.childNodes.forEach(e => { e.remove() })
    card.insertAdjacentHTML("afterbegin", element)
    card.style.cssText += "margin: auto!important;"
    card.childNodes[0].style.cssText += "max-height: 80vh;"
} catch (e) { }
```

こいつを適当なユーザスクリプトマネージャに追加すれば終わりです。  
私はViolentmonkeyを使用しています。  
ライセンスはWTFPLです。煮るなり焼くなりご自由に。  
