# Telegram Forwarder

## Setup

### Python modules
```
pip install telethon
pip install -U py-cord
```

### Telegram bot.
```
Login to to your Telegram core.
Go to your [Telegram apps page](https://my.telegram.org/auth?to=apps) and fill out the form.
Copy your api_name, api_id and api_hash and paste it in main.py in line 11 to 13.
```

### Discord webhook
```
Go to Discord > Server Settings > Integrations and create the webhook.
Make sure the webhook is set to the channel you want the messages in.
Copy the webhook url and paste it in main.py line 16: webhook_url = '<url>'
```

### Select Telegram chats
Specify which Telegram chats to track in main.py, line 19.  
Make sure your account is in the chats.

#### Python3
Install Python 3.10 or a new version.   
Run the script in your terminal by running Python3 main.py

## Help

If you need any help with the script feel free to reach out.  
Discord: edlzitrone    -    Telegram: @beamertaken