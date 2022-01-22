# importing nescessary modules 
import random 
from discord_webhook import DiscordWebhook
#list of outfits
t_shirt = ['#yourshirts/t-shirts'] 
shorts = ['#yourshorts/tracks']
#generate outfit
def outfitgen():
    #avoiding previous day worn outfit
    random_shirt = random.choice(t_shirt) 
    random_short = random.choice(shorts)
    yesterdaytxt = open("outfit.txt","r+")
    yesterdayoutfit = yesterdaytxt.read()
    if random_shirt not in yesterdayoutfit or random_short not in yesterdayoutfit:
        yesterdaytxt = open("outfit.txt","w")
        yesterdaytxt.write(random_shirt + random_short)
        #color coding according to my taste
        if "Grey" in random_shirt:
            if "Black" in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Blue" in random_shirt:
            if "Green" in random_short or 'Red' in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "White" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Red" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Orange" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Black" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short or 'Red' in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Green" in random_shirt:
            if "Black" in random_short or 'Red' in random_short:
                webhook = DiscordWebhook(url='#yourwebhoook', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
    else:
        yesterdaytxt.close()
        outfitgen()

outfitgen()
