
# coding: utf-8

# In[1]:


import csv
import datetime, pytz, time
import tori_time


# In[2]:


# 大体の語彙によってCategoryを分類する
Disaster_words = ["台風", "大雨", "災", "自衛隊", "停電", "死", "避難", "見舞い","復興"]
def chack_disaster_words(text):
    flag = False
    for word in Disaster_words:
        if word in text:
            flag = True
    return flag

Political_words = ["政治", "予算", "国会", "官邸", "議員", "会議", "政策", "サミット", "候補","選挙", "社会", "国際", "大統領"]
def chack_political_words(text):
    flag = False
    for word in Political_words:
        if word in text:
            flag = True
    return flag


# In[3]:


# AM8:45-AM5:30の時Trueを返す関数
def check_transaction(t_time):
    if ((5*60+30) < t_time) and (t_time < (8*60 + 45)):
        return False
    return True

# DEBUG
#print(chack_disaster_words("官邸スタッフです。\n本日、安倍総理はフランシスコ ローマ教皇台風を官邸にお迎えし、"))
#print(chack_political_words("官邸スタッフです。\n本日、安倍総理はフランシスコ ローマ教皇を官邸にお迎えし、"))
# print(check_transaction(tori_time.encode(10,20)))
# print(check_transaction(tori_time.encode(5,41)))
# print(check_transaction(tori_time.encode(5,30)))
# print(check_transaction(tori_time.encode(8, 45)))


# In[16]:


def remake(tweet, b_time):
    data = []
    # 時間関係のデータ
    jst_time = tori_time.change_time(tweet['created_at'])
    data.append(jst_time.year)
    data.append(jst_time.month)
    data.append(jst_time.day)
    data.append(jst_time.hour)
    data.append(jst_time.minute)

   
    t_time = tori_time.encode(jst_time.hour, jst_time.minute)
    data.append(t_time) 
    data.append(jst_time.strftime("%H:%M")) # 連結した時刻
    
    # datetimeで取引が行われていない時間は除去する
    if(not(check_transaction(t_time))):
        return []
    # 近い時刻は除去する
    if(abs(t_time - b_time) < 10):
        return []
    b_time = t_time
    # いいねとリツイート数
    data.append(int(tweet['retweet_count'])) 
    data.append(int(tweet['favorite_count'])) 
    text = tweet['text']
    
# ツイートの分類
    # 他人のRT
    if "RT" in text[0:2]:
            data.append(1)
     # 災害関係のツイート       
    elif chack_disaster_words(text):
        data.append(2)
    # 政治関係のツイート
    elif chack_political_words(text):
        data.append(3)
    # その他のツイート
    else:
        data.append(0)
    data.append(text) 
    return data, b_time


# In[17]:


# DEBUG
tweet = {
    'created_at': 'Fri Nov 29 08:47:32 +0000 2019', 
    'id': 1200335474251857920, 
    'id_str': '1200335474251857920', 
    'text': '日本に対する心からの感謝、防衛大学校で学ぶことができたことへの大きな誇り、母国で国防の中枢を担う強い使命感。流ちょうな日本語でのスピーチの数々に、本当に感動しました。 https://t.co/xdI7cwkZGo', 
    'truncated': False, 
    'entities': {
        'hashtags': [], 
        'symbols': [], 
        'user_mentions': [], 
        'urls': [], 
        'media': [{
            'id': 1200335440684830720, 
            'id_str': '1200335440684830720', 
            'indices': [84, 107], 
            'media_url': 'http://pbs.twimg.com/ext_tw_video_thumb/1200335440684830720/pu/img/wN7VMvMyUK5e-z1Q.jpg', 
            'media_url_https': 'https://pbs.twimg.com/ext_tw_video_thumb/1200335440684830720/pu/img/wN7VMvMyUK5e-z1Q.jpg', 
            'url': 'https://t.co/xdI7cwkZGo', 'display_url': 'pic.twitter.com/xdI7cwkZGo', 
            'expanded_url': 'https://twitter.com/AbeShinzo/status/1200335474251857920/video/1', 
            'type': 'photo', 
            'sizes': {
                'thumb': {
                    'w': 150, 
                    'h': 150, 
                    'resize': 'crop'
                }, 
                'large': {
                    'w': 848, 
                    'h': 480, 
                    'resize': 'fit'
                }, 
                'medium': {
                    'w': 848, 
                    'h': 480, 
                    'resize': 'fit'
                }, 
                'small': {
                    'w': 680, 
                    'h': 385, 
                    'resize': 'fit'
                }
            }, 'features': {}
        }]
    }, 
    'extended_entities': {
        'media': [{
            'id': 1200335440684830720, 
            'id_str': '1200335440684830720', 
            'indices': [84, 107], 
            'media_url': 'http://pbs.twimg.com/ext_tw_video_thumb/1200335440684830720/pu/img/wN7VMvMyUK5e-z1Q.jpg', 
            'media_url_https': 'https://pbs.twimg.com/ext_tw_video_thumb/1200335440684830720/pu/img/wN7VMvMyUK5e-z1Q.jpg', 
            'url': 'https://t.co/xdI7cwkZGo', 'display_url': 'pic.twitter.com/xdI7cwkZGo', 'expanded_url': 'https://twitter.com/AbeShinzo/status/1200335474251857920/video/1', 
            'type': 'video', 
            'sizes': {
                'thumb': {
                    'w': 150, 
                    'h': 150, 
                    'resize': 'crop'
                }, 
                'large': {
                    'w': 848, 
                    'h': 480, 
                    'resize': 'fit'
                }, 
                'medium': {
                    'w': 848, 
                    'h': 480, 
                    'resize': 'fit'
                }, 
                'small': {
                    'w': 680, 
                    'h': 385,
                    'resize': 'fit'
                }
            }, 
            'video_info': {
                'aspect_ratio': [53, 30], 
                'duration_millis': 27833, 
                'variants': [
                    {
                        'bitrate': 2176000, 
                        'content_type': 'video/mp4', 
                        'url': 'https://video.twimg.com/ext_tw_video/1200335440684830720/pu/vid/848x480/DzM9_8cYD84vnmLY.mp4?tag=10'
                    }, 
                    {
                        'content_type': 'application/x-mpegURL', 'url': 'https://video.twimg.com/ext_tw_video/1200335440684830720/pu/pl/NXGvHVbt9Z5Pjslq.m3u8?tag=10'
                    }, 
                    {
                        'bitrate': 256000, 
                         'content_type': 'video/mp4', 
                         'url': 'https://video.twimg.com/ext_tw_video/1200335440684830720/pu/vid/476x270/WRHQ27XvSCK9RbP_.mp4?tag=10'
                    }, 
                    {
                        'bitrate': 832000, 
                         'content_type': 'video/mp4', 
                         'url': 'https://video.twimg.com/ext_tw_video/1200335440684830720/pu/vid/636x360/l2m48rwmLbac4W5d.mp4?tag=10'
                    }
                ]
            }, 'features': {
                
            },
            'additional_media_info': {
                'monetizable': False
            }
        }
        ]
    }, 
    'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
    'in_reply_to_status_id': 1200335434103967744, 
    'in_reply_to_status_id_str': '1200335434103967744', 
    'in_reply_to_user_id': 468122115, 
    'in_reply_to_user_id_str': '468122115', 
    'in_reply_to_screen_name': 'AbeShinzo', 
    'user': {
        'id': 468122115, 
        'id_str': '468122115', 
        'name': '安倍晋三', 
        'screen_name': 'AbeShinzo', 
        'location': '', 
        'description': '衆議院議員安倍晋三（あべしんぞう）の公式twitterです。 \nPrime Minister of Japan. Leader of Liberal Democratic Party.', 
        'url': 'http://t.co/hTEyS9iLvU', 
        'entities': {
            'url': {
                'urls': [{
                    'url': 'http://t.co/hTEyS9iLvU', 
                    'expanded_url': 'http://www.s-abe.or.jp/',
                    'display_url': 's-abe.or.jp',
                    'indices': [0, 22]}]}, 
            'description': {
                'urls': []}
        }, 
        'protected': False, 
        'followers_count': 1611144, 
        'friends_count': 18, 
        'listed_count': 11934, 
        'created_at': 'Thu Jan 19 06:02:29 +0000 2012', 
        'favourites_count': 10, 
        'utc_offset': None, 
        'time_zone': None, 
        'geo_enabled': True, 
        'verified': True,
        'statuses_count': 1831, 
        'lang': None, 
        'contributors_enabled': False, 
        'is_translator': False, 
        'is_translation_enabled': False, 
        'profile_background_color': '000000', 
        'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme16/bg.gif', 
        'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme16/bg.gif', 
        'profile_background_tile': False, 
        'profile_image_url': 'http://pbs.twimg.com/profile_images/1765776666/s-abetwitter1_normal.png', 
        'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1765776666/s-abetwitter1_normal.png', 
        'profile_banner_url': 'https://pbs.twimg.com/profile_banners/468122115/1507347517', 
        'profile_link_color': '3B94D9', 'profile_sidebar_border_color': '000000', 
        'profile_sidebar_fill_color': '000000', 
        'profile_text_color': '000000', 
        'profile_use_background_image': False, 
        'has_extended_profile': False, 
        'default_profile': False, 
        'default_profile_image': False,
        'can_media_tag': True,
        'followed_by': False,
        'following': True, 
        'follow_request_sent': False, 
        'notifications': False,
        'translator_type': 'none'
    }, 
    'geo': None, 
    'coordinates': None, 
    'place': None,
    'contributors': None, 
    'is_quote_status': False, 
    'retweet_count': 864, 
    'favorite_count': 5313, 
    'favorited': False, 
    'retweeted': False, 
    'possibly_sensitive': False,
    'lang': 'ja'
}




remake(tweet, -100)


