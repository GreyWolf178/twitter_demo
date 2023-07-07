import json
import pandas as pd
from requests import get as get


def start_main():
    url = 'https://twitter.com/i/api/graphql/x8SpjuBpqoww-edf0aUUKA/UserTweets?variables=%7B%22userId%22%3A%222988404436%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22rweb_lists_timeline_redesign_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Afalse%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Afalse%7D'

    headers = {
        "authority": "twitter.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "referer": "https://twitter.com/iMShami_",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "x-csrf-token": "4aaf6ef6948ad2718dcdc52a5d9b567e1f9274bf38b1f9251968d46504cd85966f8c5d07f30301f3067706d1f34e5aa9bee9b5455afaed50f96aa672bd014b2d74d295eec9f5587c5109868bf39ec4cf",
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en"
    }

    cookies = {
        "guest_id_marketing": "v1%3A168665924373188685",
        "guest_id_ads": "v1%3A168665924373188685",
        "guest_id": "v1%3A168665924373188685",
        "gt": "1677189950717173765",
        "external_referer": "padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D",
        "_gid": "GA1.2.587208178.1688708319",
        "g_state": "{\"i_l\":0}",
        "kdt": "HwYpazN6cgBHX8LFpKQ6bpG208evgmKWmMPMheTT",
        "auth_token": "3033fbe161e939f12f773b6e78b1f4adad6a12ba",
        "ct0": "4aaf6ef6948ad2718dcdc52a5d9b567e1f9274bf38b1f9251968d46504cd85966f8c5d07f30301f3067706d1f34e5aa9bee9b5455afaed50f96aa672bd014b2d74d295eec9f5587c5109868bf39ec4cf",
        "twid": "u%3D745577399778148352",
        "att": "1-vP3hynHvCOfLu8JmRLMIDwjiZHvSH5ALDtBF4wKr",
        "mbox": "session#b724d3f202f74f38afd9640b2370e31c#1688712712|PC#b724d3f202f74f38afd9640b2370e31c.38_0#1751955652",
        "des_opt_in": "N",
        "_ga_34PHSZMC42": "GS1.1.1688710854.1.1.1688710906.0.0.0",
        "_ga": "GA1.2.1288348034.1688708319",
        "lang": "en",
        "personalization_id": "\"v1_a923YdW7Jfeq5uxqCywo2w==\""
    }

    request = get(url=url, headers=headers, cookies=cookies)
    response = json.loads(request.text)

    all_boxes = response['data']['user']['result']['timeline_v2']['timeline']['instructions'][2]['entries']
    complete_data = list()

    for box in all_boxes:
        try:
            tweet_check = box['entryId']
        except:
            tweet_check = ''
        if 'tweet' not in tweet_check or not tweet_check:
            continue
        try:
            description = box['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
        except:
            description = ''
        try:
            url = box['content']['itemContent']['tweet_results']['result']['legacy']['entities']['media'][0][
                    'media_url_https']
        except:
            url = ''
        try:
            created_at = box['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
        except:
            created_at = ''
        try:
            likes = box['content']['itemContent']['tweet_results']['result']['legacy']['favorite_count']
        except:
            likes = ''
        try:
            retweet_count = box['content']['itemContent']['tweet_results']['result']['legacy']['retweet_count']
        except:
            retweet_count = ''
        try:
            reply_count = box['content']['itemContent']['tweet_results']['result']['legacy']['reply_count']
        except:
            reply_count = ''
        try:
            views = box['content']['itemContent']['tweet_results']['result']['views']['count']
        except:
            views = ''

        data = {"Description": description,
                'URL': url,
                'Created_At': created_at,
                'Likes': likes,
                'Retweet_Count': retweet_count,
                'Reply_Count': reply_count,
                'Views': views}
        complete_data.append(data)

    return complete_data


def save_data(data):
    df = pd.DataFrame(data)
    df.to_csv('twitter_demo.csv', index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    # for url==> 'https://twitter.com/iMShami_'
    # posts data
    final_data = start_main()
    save_data(data=final_data)

