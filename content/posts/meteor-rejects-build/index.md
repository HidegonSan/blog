---
draft: false

date: "2023-10-05T17:48:59+09:00"
# url: ""

title: "Meteor Rejects をビルドする"
description: ""
keywords: ""

tags: ["Minecraft"]
categories: []
---

## Meteor Rejects とは

MinecraftのUtility Mod(ホント？)の[Meteor Client](https://github.com/MeteorDevelopment/meteor-client)に機能を追加するModです。  
[GitHub](https://github.com/AntiCope/meteor-rejects)  

## ビルドする

なぜなのか知りませんがREADMEにビルド方法が書いてません。  
まあどう考えても `./gradlew build` ですが、一応[Actions](https://github.com/AntiCope/meteor-rejects/blob/master/.github/workflows/gradle.yml)を見ときました。  
そのままだったので実行していきます。  

```sh
git clone git@github.com:AntiCope/meteor-rejects.git
cd meteor-rejects
./gradlew build
```

放置してたらエラー吐かれました。  

```
Starting a Gradle Daemon, 1 incompatible Daemon could not be reused, use --status for details

> Configure project :
Fabric Loom: 1.1.14

> Task :compileJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':compileJava'.
> error: release version 17 not supported

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.

* Get more help at https://help.gradle.org

BUILD FAILED in 3s
1 actionable task: 1 executed
```

release version 17 はサポートされないらしいので切り替えます。  
なんで17が入ってるのかわかりません (おい)  
多分もっと良い切り替え方があるんでしょうが私はビルドできたらそれで良いので手早くいきます。  

```sh
export JAVA_HOME=/usr/lib/jvm/java-20-openjdk/
```

これでビルドできました。  
めでたしめでたし (環境を整備しろ)  
みなさんも良いModライフを〜
