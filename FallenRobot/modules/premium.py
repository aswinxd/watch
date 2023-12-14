from telethon.tl.custom import Button

__help__ = """
*Admins Only*

 /nightmode*:* Adds Group to NightMode Chats
 /rmnight*:* Removes Group From NightMode Chats

*Note:* Night Mode chats get Automatically closed at 12 am(IST) and Automatically opened at 6 am(IST) to Prevent Night Spam.

*Additional Options:*
 - `/nightmodehelp`: Show additional commands for Night Mode settings
"""

# Add callback buttons directly in __help__
__help__ += "\n*Additional Options:*"
__help__ += "\n - `/nightmodehelp`: Show additional commands for Night Mode settings"
__help__ += f"\n - {Button.callback('Enable Night Mode', data='enable_night_mode')}"
__help__ += f"\n - {Button.callback('Disable Night Mode', data='disable_night_mode')}"

__mod_name__ = "Night mode"
