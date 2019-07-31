# summary
Twitter APIをPythonから使うサンプル

# 準備
1. 環境構築
`Python 3.6` にて動作確認済  

```linux
pip3 install -r requirements.txt
```

2. API keyとAPI secret keyの取得
    1. TwitterのDeveloperアカウントを取得
    2. [Access tokens: Twitter Developers](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)に従い、API keyとAPI secret keyを取得

3. 環境変数の設定

```linux
export TWITTER_KEY=<your own consumer api key>
export TWITTER_KEY_SECRET=<your own consumer api secret key>
export TWITTER_TOKEN=<your own access token>
export TWITTER_TOKEN_SECRET=<your own access token secret>
```

# 使い方
## 検索API

```
cd src
python3 -m search <keyword>
```
