# Financial News Telegram Bot
Financial news for Telegram bot. Once activated it will send a financial Reddit headline every 6 hours for a total of 4 a day
## Creation of a credentials.py file

You will have to create a separate `credentials.py` file once you clone the repository. In this file you must include the following variables:

### Telegram credentials

  `bot_token` - this is the ID of the Telegram bot you plan on using as alert, full information on Telegram Bots and API can be found [here](https://core.telegram.org/bots)
  
  `bot_chatID` - this is the ID of the Telegram group chat you plan the bot to alert you on, full information on Telegram Bots and API can be found [here](https://core.telegram.org/bots)
  
### Reddit credentials

You will need to get a Reddit API key. You can find more info [here](https://www.reddit.com/wiki/api). Once you have the information, you'll need to create the below credentials
  
  `client_id`
  
  `client_secret`
   
  `username`
   
  `password`
   
  `user_agent`
  
  
The script will call all these variables
