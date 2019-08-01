# -*- coding: utf-8 -*-
"""Twitter API のStandard search APIによる検索を行うモジュール."""
from typing import Dict

from twitter import Twitter


def search_tweets(client: Twitter, keyword: str,
                  keys: [str] = ["text"]) -> [Dict[str, str]]:
    """Tweetの検索.

    Args:
        client (Twitter): 認証済のクライアント
        keyword (str): 検索キーワード
        keys ([str]): 検索結果から取り出すkeyのlist
    Returns:
        [{str: str}]: 検索結果
    Raises:
        twitter.api.TwitterHTTPError: クライアントかクエリパラメータが不正な場合に発火
        KeyError: APIの返却値に含まれないkeyがkeysに含まれている場合に発火

    """
    tweets = client.search.tweets(q=keyword)
    extracted = []
    for tweet in tweets["statuses"]:
        elems = {key: tweet[key] for key in keys}
        extracted.append(elems)

    return extracted
