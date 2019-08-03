# -*- coding: utf-8 -*-
"""Twitter APIの共通関数のモジュール."""
import configparser
import os
from pathlib import Path
from typing import Dict

from twitter import OAuth, Twitter


CONFIG_PATH = Path("../config/env.ini")


def get_environment_vars() -> (str, str, str, str):
    """環境変数の取得.

    Returns:
        Dict[str, str]: Twitterへのアクセスのためのkey
    Raises:
        IOError: 環境変数が取得できないときに発火

    """
    if not CONFIG_PATH.exists():
        raise IOError(f"Cannot read config file: {CONFIG_PATH}.")
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    env_var_keys = config["DEFAULT"]

    env_vars = {k: os.getenv(v) for k, v in env_var_keys.items()}

    if None in env_vars.values():
        raise IOError("""\
Need to set environment variables.
see README.md""")

    return env_vars


def get_authorized_client(keys: Dict[str, str]) -> Twitter:
    """認証済のクライアントを返す.

    Args:
        keys (Dict[str, str]): 認証に必要なkey
                               詳細はREADMEを参照
    Returns:
        Twitter: 認証済のクライアント

    """
    return Twitter(auth=OAuth(**keys))
