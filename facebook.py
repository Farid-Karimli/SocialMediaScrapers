from facebook_scraper import get_posts
import banks
import pandas as pd

bank_names = ['KapitalBank',
'ABB',
'PashaBank',
'E-Pul.az',
'Hesab.az',
'eManat',
'milli0n.az',
'BankofBaku',
'Yelobank',
'AccessBankAz' ,
'BankRespublika',
'Payonix',
'azerbaijanfinancebank',
'YapiKrediAZ',
'azerturkbank',
]

# problem with Anipay, MilliOn, Rabita Bank, Expresspay, Portmanat, Payonix, Yapi Kredi Azerbaijan

def get_posts_info(bank):
    posts = []

    for post in get_posts(bank, pages=2,options={"comments": 100},credentials=('karimli.farid@yahoo.com','FGKGHK1234')):
        posts.append([post['post_id'], post['text'], post['likes'], post['comments'], post['shares']])
    return posts


def retrieve():
    print('Starting Facebook retrieval')
    print()
    for bank in bank_names:
        print('Retrieving info about',bank)
        filename = 'Facebook/'+bank+".csv"
        posts = get_posts_info(bank)

        if posts:
            posts_pd = pd.DataFrame(posts, columns=['Post ID', 'Text','Likes','Comments','Shares'])
            posts_pd.to_csv(filename)
        else:
            print('Couldn\'t find post info about',bank)
