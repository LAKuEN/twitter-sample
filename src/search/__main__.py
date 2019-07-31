# -*- coding: utf-8 -*-
"""Twitter API の Standard search APIによる検索を行うモジュール."""
import argparse
import os
from typing import Dict

from twitter import OAuth, Twitter


def get_environment_vars() -> (str, str, str, str):
    """環境変数の取得.

    Args:
        None
    Returns:
        Tuple(str, str, str, str): Twitterへのアクセスに必要な情報
    Raises:
        IOError: 環境変数が取得できないときに発火

    """
    api_key = os.getenv("TWITTER_KEY")
    api_key_secret = os.getenv("TWITTER_KEY_SECRET")
    token = os.getenv("TWITTER_TOKEN")
    secret = os.getenv("TWITTER_TOKEN_SECRET")

    if None in [api_key, api_key_secret, token, secret]:
        raise IOError("""\
Need to set the following environment variables: $TWITTER_TOKEN, \
$TWITTER_TOKEN_SECRET.
see README.md""")

    return api_key, api_key_secret, token, secret


def get_authorized_client(api_key: str, api_key_secret: str,
                          token: str, token_secret: str) -> Twitter:
    """認証済のクライアントを返す.

    Args:
        api_key (str)
        api_key_secret (str)
        token (str)
        token_secret (str)
    Returns:
        Twitter: 認証済のクライアント

    """
    return Twitter(auth=OAuth(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        token=token,
        token_secret=token_secret,
    ))


def search_tweets(client: Twitter, keyword: str,
                  keys: [str] = ["text"]) -> [Dict[str, str]]:
    """Tweetの検索.

    Args:
        client (Twitter): 認証済のクライアント
        keyword (str): 検索キーワード
        keys ([str]): 検索結果から取り出すkeyのlist
    Returns:
        [{str: str}]: 検索結果

    """
    tweets = client.search.tweets(q=keyword)
    extracted = []
    for tweet in tweets["statuses"]:
        elems = {key: tweet[key] for key in keys}
        extracted.append(elems)

    return extracted


def main(keyword: str):
    """main.

    Args:
        keyword (str): 検索キーワード
    Returns:
        [{str: str}]: 検索結果
    Raises:
        IOError: 認証失敗時に発火

    """
    try:
        keys = get_environment_vars()
    except IOError:
        raise
    tw = get_authorized_client(*keys)

    return search_tweets(tw, keyword)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str)
    args = parser.parse_args()

    res = main(args.keyword)
    print(res)
