# -*- coding: utf-8 -*-
"""twutilのテストケース."""
import configparser

import pytest

import src.lib.twutil as twutil


class TestGetEnvironmentVars:
    def test_normal(self, mocker):
        """正常系: 環境変数が全て設定されている場合."""
        with mocker.patch("os.getenv", mocker.MagicMock(return_value="")):
            twutil.get_environment_vars()

    # TODO iniファイルを読み込むように修正する
    test_data_abnormal = [
        (
            # 環境変数が全て設定されていない場合
            {
                "TWITTER_KEY": None,
                "TWITTER_KEY_SECRET": None,
                "TWITTER_TOKEN": None,
                "TWITTER_TOKEN_SECRET": None,
            },
            IOError,
        ),
        (
            # 環境変数が1つ設定されていない場合
            {
                "TWITTER_KEY": "",
                "TWITTER_KEY_SECRET": None,
                "TWITTER_TOKEN": "",
                "TWITTER_TOKEN_SECRET": "",
            },
            IOError,
        )
    ]

    @pytest.mark.parametrize("env_vars, want", test_data_abnormal)
    def test_abnormal(self, mocker, env_vars, want):
        """異常系."""
        with pytest.raises(want), \
            mocker.patch("os.getenv",
                         mocker.MagicMock(side_effect=lambda k: env_vars[k])):
            twutil.get_environment_vars()


class TestGetAuthorizedClient:
    # NOTE 入力値の組み合わせのテストはmockで行うのが望ましい
    #      疎通確認は正しい環境変数を設定した環境で行うのが良いが、そもそも必要か？
    # 全ての環境変数に正しい値を設定している場合
    # 全ての環境変数に不正な値を設定している場合
    # 一部の環境変数に不正な値を設定している場合
    pass
