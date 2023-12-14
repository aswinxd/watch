from telethon.tl.custom import Button

__help__ = """
*Admins Only*

 /nightmode*:* Adds Group to NightMode Chats
 /rmnight*:* Removes Group From NightMode Chats

*Note:* Night Mode chats get Automatically closed at 12 am(IST) and Automatically opened at 6 am(IST) to Prevent Night Spam.

*Additional Options:*
 - `/nightmodehelp`: Show additional commands for Night Mode settings
"""

# Add URL buttons under the message
url_buttons = [
    Button.inline('Enable Night Mode', data='enable_night_mode'),
    Button.inline('Disable Night Mode', data='disable_night_mode'),
    Button.url('Visit our Website', url='http://yourwebsite.com'),
    Button.url('GitHub Repository', url='https://github.com/your_username/your_repo')
]

__help__ += "\n*Additional Options:*"
__help__ += "\n - " + "\n - ".join(str(button) for button in url_buttons)

__mod_name__ = "Night mode"
