# CoinGeckoDiscordPriceBot

Very simple price bot for coins listed on coingecko. Just edit the info.json to your own custom values depending on the coin, then run the main.py script.

### Requirements

Use "pip install -r requirements.txt" to install needed packages

### info.json
{   

    "api":"[DISCORD-API-KEY-HERE]",
    
    "coin":"[NAME-OF-COIN]",
    
    "id":"[ID-OF-COIN]",
    
    "length":[MAX-CHARACTERS-OF-PRICE],
   
    "updatefreq":[UPDATE-FREQUENCY-IN-SECONDS] 
    
}

Coin ID's can be found at: https://docs.google.com/spreadsheets/d/1wTTuxXt8n9q7C4NDXqQpI3wpKu1_5bGVmP9Xz0XGSyU/edit#gid=0

CoinGecko has a limit for the free API of 10-50 calls per minute, plan accordingly when setting the updatefreq
