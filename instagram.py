#TODO complete the instagram scraper with ALL the banks
from instascrape import *
import pandas as pd

bank_usernames = {
    'Kapital_Bank': 'kapital_bank',
    #'IBA': 'azerbaycan_beynelxalq_banki',
    #'Pasha Bank': 'pashabank',
    'E-Pul': 'epul.az',
    'Unibank': 'unibank.az',
    'eManat':'emanat.az',
    'MilliOn': 'milli0n.az',
    'Dost_Bank': 'bankofbaku',
    'Rabita_Bank': 'rabita_bank',
    'Expresspay': 'expresspay.az',

}

def get_info(bank):
    prof = Profile(bank)
    prof.scrape()

    recent_posts = prof.get_recent_posts()

    posts_data = [post.to_dict() for post in recent_posts]

    return posts_data




def retrieve():
    print('Starting Instagram retrieval')
    print()
    for bank_name in bank_usernames:
        print('Starting retrieval of',bank_name,'info')
        posts = get_info(bank_usernames[bank_name])

        if posts:
            posts_df = pd.DataFrame(posts)
            posts_df[['upload_date', 'accessibility_caption', 'likes', 'comments']].to_csv('Instagram/'+bank_name+'.csv')
        else:
            print('Could not retrieve data.')

    return