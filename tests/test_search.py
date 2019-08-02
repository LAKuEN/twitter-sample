# -*- coding: utf-8 -*-
import pytest
import twitter

from search import search


class TestSeachTweets:
    """search_tweetsのテストケース."""

    return_value = \
        {
            "statuses": [
                {
                    "created_at": "Mon May 06 20:01:29 +0000 2019",
                    "id": 1125490788736032770,
                    "id_str": "1125490788736032770",
                    "text": "Today's new update means that you can finally add Pizza Cat to your Retweet with comments! Learn more about this ne… https://t.co/Rbc9TF2s5X",
                    "truncated": True,
                    "entities": {
                        "hashtags": [],
                        "symbols": [],
                        "user_mentions": [],
                        "urls": [
                            {
                                "url": "https://t.co/Rbc9TF2s5X",
                                "expanded_url": "https://twitter.com/i/web/status/1125490788736032770",
                                "display_url": "twitter.com/i/web/status/1…",
                                "indices": [
                                    117,
                                    140
                                ]
                            }
                        ]
                    },
                    "metadata": {
                        "iso_language_code": "en",
                        "result_type": "recent"
                    },
                    "source": "<a href='https://mobile.twitter.com' rel='nofollow'>Twitter Web App</a>",
                    "in_reply_to_status_id": None,
                    "in_reply_to_status_id_str": None,
                    "in_reply_to_user_id": None,
                    "in_reply_to_user_id_str": None,
                    "in_reply_to_screen_name": None,
                    "user": {
                        "id": 2244994945,
                        "id_str": "2244994945",
                        "name": "Twitter Dev",
                        "screen_name": "TwitterDev",
                        "location": "Internet",
                        "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https://t.co/mGHnxZU8c1 ⌨️ #TapIntoTwitter",
                        "url": "https://t.co/FGl7VOULyL",
                        "entities": {
                            "url": {
                                "urls": [
                                    {
                                        "url": "https://t.co/FGl7VOULyL",
                                        "expanded_url": "https://developer.twitter.com/",
                                        "display_url": "developer.twitter.com",
                                        "indices": [
                                            0,
                                            23
                                        ]
                                    }
                                ]
                            },
                            "description": {
                                "urls": [
                                    {
                                        "url": "https://t.co/mGHnxZU8c1",
                                        "expanded_url": "https://twittercommunity.com/",
                                        "display_url": "twittercommunity.com",
                                        "indices": [
                                            93,
                                            116
                                        ]
                                    }
                                ]
                            }
                        },
                        "protected": False,
                        "followers_count": 501947,
                        "friends_count": 1473,
                        "listed_count": 1507,
                        "created_at": "Sat Dec 14 04:35:55 +0000 2013",
                        "favourites_count": 2186,
                        "utc_offset": None,
                        "time_zone": None,
                        "geo_enabled": True,
                        "verified": True,
                        "statuses_count": 3389,
                        "lang": "en",
                        "contributors_enabled": False,
                        "is_translator": False,
                        "is_translation_enabled": None,
                        "profile_background_color": "None",
                        "profile_background_image_url": "None",
                        "profile_background_image_url_https": "None",
                        "profile_background_tile": None,
                        "profile_image_url": "None",
                        "profile_image_url_https": "https://pbs.twimg.com/profile_images/880136122604507136/xHrnqf1T_normal.jpg",
                        "profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1498675817",
                        "profile_link_color": "None",
                        "profile_sidebar_border_color": "None",
                        "profile_sidebar_fill_color": "None",
                        "profile_text_color": "None",
                        "profile_use_background_image": None,
                        "has_extended_profile": None,
                        "default_profile": False,
                        "default_profile_image": False,
                        "following": False,
                        "follow_request_sent": False,
                        "notifications": False,
                        "translator_type": "None"
                    },
                    "geo": None,
                    "coordinates": None,
                    "place": None,
                    "contributors": None,
                    "is_quote_status": True,
                    "quoted_status_id": 1125479034513645569,
                    "quoted_status_id_str": "1125479034513645569",
                    "quoted_status": {
                        "created_at": "Mon May 06 19:14:46 +0000 2019",
                        "id": 1125479034513645569,
                        "id_str": "1125479034513645569",
                        "text": "It's easy to express yourself by Retweeting with a comment. What if you could take it a step further and include me… https://t.co/YTqpNZZ8M9",
                        "truncated": True,
                        "entities": {
                            "hashtags": [],
                            "symbols": [],
                            "user_mentions": [],
                            "urls": [
                                {
                                    "url": "https://t.co/YTqpNZZ8M9",
                                    "expanded_url": "https://twitter.com/i/web/status/1125479034513645569",
                                    "display_url": "twitter.com/i/web/status/1…",
                                    "indices": [
                                        117,
                                        140
                                    ]
                                }
                            ]
                        },
                        "metadata": {
                            "iso_language_code": "en",
                            "result_type": "recent"
                        },
                        "source": "<a href='http://twitter.com' rel='nofollow'>Twitter Web Client</a>",
                        "in_reply_to_status_id": None,
                        "in_reply_to_status_id_str": None,
                        "in_reply_to_user_id": None,
                        "in_reply_to_user_id_str": None,
                        "in_reply_to_screen_name": None,
                        "user": {
                            "id": 17874544,
                            "id_str": "17874544",
                            "name": "Twitter Support",
                            "screen_name": "TwitterSupport",
                            "location": "Twitter HQ",
                            "description": "Your official source for Twitter Support. We're available 24/7 via Direct Message to answer account questions. Follow us for tips, tricks, and announcements.",
                            "url": "https://t.co/heEvRrl4yN",
                            "entities": {
                                "url": {
                                    "urls": [
                                        {
                                            "url": "https://t.co/heEvRrl4yN",
                                            "expanded_url": "https://help.twitter.com",
                                            "display_url": "help.twitter.com",
                                            "indices": [
                                                0,
                                                23
                                            ]
                                        }
                                    ]
                                },
                                "description": {
                                    "urls": []
                                }
                            },
                            "protected": False,
                            "followers_count": 5861908,
                            "friends_count": 17,
                            "listed_count": 15129,
                            "created_at": "Thu Dec 04 18:51:57 +0000 2008",
                            "favourites_count": 313,
                            "utc_offset": None,
                            "time_zone": None,
                            "geo_enabled": True,
                            "verified": True,
                            "statuses_count": 27955,
                            "lang": "en",
                            "contributors_enabled": False,
                            "is_translator": False,
                            "is_translation_enabled": None,
                            "profile_background_color": "None",
                            "profile_background_image_url": "None",
                            "profile_background_image_url_https": "None",
                            "profile_background_tile": None,
                            "profile_image_url": "None",
                            "profile_image_url_https": "https://pbs.twimg.com/profile_images/941807338171777025/PRP6vwDq_normal.jpg",
                            "profile_banner_url": "https://pbs.twimg.com/profile_banners/17874544/1499274456",
                            "profile_link_color": "None",
                            "profile_sidebar_border_color": "None",
                            "profile_sidebar_fill_color": "None",
                            "profile_text_color": "None",
                            "profile_use_background_image": None,
                            "has_extended_profile": None,
                            "default_profile": False,
                            "default_profile_image": False,
                            "following": False,
                            "follow_request_sent": False,
                            "notifications": False,
                            "translator_type": "None"
                        },
                        "geo": None,
                        "coordinates": None,
                        "place": None,
                        "contributors": None,
                        "is_quote_status": False,
                        "retweet_count": 1466,
                        "favorite_count": 3990,
                        "favorited": False,
                        "retweeted": False,
                        "possibly_sensitive": False,
                        "lang": "en"
                    },
                    "retweet_count": 20,
                    "favorite_count": 44,
                    "favorited": False,
                    "retweeted": False,
                    "possibly_sensitive": False,
                    "lang": "en"
                },
        ],
            "search_metadata": {
                "completed_in": 0.047,
                "max_id": 1125490788736032770,
                "max_id_str": "1125490788736032770",
                "next_results": "?max_id=1124690280777699327&q=from%3Atwitterdev&count=2&include_entities=1&result_type=mixed",
                "query": "from%3Atwitterdev",
                "refresh_url": "?since_id=1125490788736032770&q=from%3Atwitterdev&result_type=mixed&include_entities=1",
                "count": 2,
                "since_id": 0,
                "since_id_str": "0"
            }
        }

    def test_normal(self, mocker):
        """正常系."""
        keyword = "twitter"
        want = [
            {
                "text": "Today's new update means that you can finally add Pizza Cat to your Retweet with comments! Learn more about this ne… https://t.co/Rbc9TF2s5X",
             }
        ]
        mock_obj = mocker.MagicMock(name="Twitter")
        mock_obj.search.tweets.return_value = self.return_value
        got = search.search_tweets(mock_obj, keyword)
        assert want == got

    test_data = [
        # FIXME この関数をどうテストすべきか思案中
        #       Twitterオブジェクトのmockを作り分ける必要がある
        # TODO 実装
        # * クライアントの認証時エラー: twitter.api.TwitterHTTPError
        # details: {'errors': [{'code': 32, 'message': 'Could not authenticate you.'}]}
        # -> 不正なパラメータを設定した状態でリクエストを投げると再現できる
        # -> 検索ワードを空文字列として与えれば再現できる
        ["twitter", twitter.api.TwitterHTTPError],
        # * 検索ワードが空のエラー: twitter.api.TwitterHTTPError
        # details: {'errors': [{'code': 25, 'message': 'Query parameters are missing.'}]}
        ["", twitter.api.TwitterHTTPError],
        # * 存在しないkeyを取り出した場合のエラー: KeyError
        # -> 掲題の通りの方法で再現できる
        ["twitter", KeyError],
    ]

    @pytest.mark.parametrize("keyword, want", test_data)
    def test_abnormal(self, mocker, keyword, want):
        """異常系."""
        mock = mocker.MagicMock(name="Twitter")
        mock.search.tweets.return_value = self.return_value
        mock.search.tweets.side_effect = want

        # FIXME twitter.api.TwitterHTTPErrorオブジェクトの生成時に引数の指定がされてないってエラーが出てしまう
        with pytest.raises(want):
            search.search_tweets(mock, keyword)
