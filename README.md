# OutfitGen-22

Python application to Generate different outfit every day!.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install discord-webhook, random.

```bash
pip install discord-webhook
pip install random
```

## Usage

```python
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
         #more color coding
    else:
        yesterdaytxt.close()
        outfitgen()

outfitgen()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Brokiemag](https://brokiemag.me/License/License.pdf)
