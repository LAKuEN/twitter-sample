# -*- coding: utf-8 -*-
"""Twitter API のStandard search APIによる検索を行うモジュール."""
import argparse
from typing import Dict

from twitter import Twitter

from lib import twutil


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
        keys = twutil.get_environment_vars()
    except IOError:
        raise
    tw = twutil.get_authorized_client(*keys)

    return search_tweets(tw, keyword)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str)
    args = parser.parse_args()

    res = main(args.keyword)
    print(res)
