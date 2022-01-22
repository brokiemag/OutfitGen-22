# importing nescessary modules 
import random 
from discord_webhook import DiscordWebhook

t_shirt = ['Grey(Exploring unknown territories)','Black(Studio-fit --constant evolution)','Black(No-Handshake)','Grey(Pantaloons)','Red(Wrogn)','Red(Levis)','Blue(Nuevo wave)','Orange(See You on the moon)','White(Lee-Copper)','Green(DNMX I am Global)'] 
shorts = ['Black(Domyos --military textured Short)','Black(Tarmak --basketball short)','Black(Decathlon --track)','Green(Max --Short)','Red(Max --Track)','Grey(Studiofit --track)']
# method 1 to generate a random word from the list 
def outfitgen():
    random_shirt = random.choice(t_shirt) 
    random_short = random.choice(shorts)
    yesterdaytxt = open("outfit.txt","r+")
    yesterdayoutfit = yesterdaytxt.read()
    if random_shirt not in yesterdayoutfit or random_short not in yesterdayoutfit:
        yesterdaytxt = open("outfit.txt","w")
        yesterdaytxt.write(random_shirt + random_short)
        if "Grey" in random_shirt:
            if "Black" in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Blue" in random_shirt:
            if "Green" in random_short or 'Red' in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "White" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Red" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Orange" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Black" in random_shirt:
            if "Black" in random_short or 'Grey' in random_short or 'Red' in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
        if "Green" in random_shirt:
            if "Black" in random_short or 'Red' in random_short:
                webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/934516203173580830/OFtNjUVmhjFyFAIyfnay39M-ooZh3RHMclE0ELH3MbbhZ6Qd31Pd53Z0lArz4s9Xd_0U', rate_limit_retry=True,
                                content=f"Today's Outfit:- {random_shirt} + {random_short}")
                response = webhook.execute()
            else:
                outfitgen()
    else:
        yesterdaytxt.close()
        outfitgen()

outfitgen()
# method 2 to generate a random word 
# this method will generate a random index, 
# lying inside the list indices, then get the word at the index 
# random_word = t_shirt[random.randint(0,len(t_shirt))] 
# print(random_word)