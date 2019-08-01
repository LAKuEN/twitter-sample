# -*- coding: utf-8 -*-
"""twutilのテストケース."""
import pytest
from twitter import Twitter

import src.lib.twutil as twutil


class TestGetEnvironmentVars:
    """get_environment_vars() のテストケース."""

    def test_normal(self, mocker):
        """正常系: 環境変数が全て設定されている場合."""
        with mocker.patch("os.getenv", mocker.MagicMock(return_value="")):
            twutil.get_environment_vars()

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
    """get_authorized_client() のテストケース."""

    def test_normal(self):
        """正常系."""
        # NOTE 当該関数はget_environment_vars() で予め環境変数が設定されることが前提となっている
        #      また、Twitterオブジェクトの生成時に不正な文字列を与えてもエラーを吐かない
        keys = {
            "consumer_key": "",
            "consumer_secret": "",
            "token": "",
            "token_secret": "",
        }
        want = Twitter
        got = twutil.get_authorized_client(keys)

        assert isinstance(got, want)

    def test_abnormal(self):
        """異常系: キーが欠損している場合."""
        keys = {
            "consumer_key": "",
            "consumer_secret": "",
            "token": "",
        }
        with pytest.raises(TypeError):
            twutil.get_authorized_client(keys)
