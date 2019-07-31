# -*- coding: utf-8 -*-
"""Twitter APIの共通関数のモジュール."""
import os

from twitter import OAuth, Twitter


def get_environment_vars() -> (str, str, str, str):
    """環境変数の取得.

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
