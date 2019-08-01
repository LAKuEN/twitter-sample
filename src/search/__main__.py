# -*- coding: utf-8 -*-
"""Twitter API のStandard search APIによる検索を行うモジュール."""
import argparse

from lib import twutil
from search import search


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
    tw = twutil.get_authorized_client(keys)

    return search.search_tweets(tw, keyword)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str)
    args = parser.parse_args()

    res = main(args.keyword)
    print(res)
