from telethon import events
from telethon.tl.custom import Button

# Assume you have an appropriate `client` object

@events.register(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond(
        "Available Commands For Night mode :\n\n"
        "Admins Only\n\n"
        "/nightmode: Adds Group to NightMode Chats\n"
        "/rmnight: Removes Group From NightMode Chats\n\n"
        "Note: Night Mode chats get Automatically closed at 12 am(IST) "
        "and Automatically opened at 6 am(IST) to Prevent Night Spam.\n\n"
        "Additional Options:\n"
        " - /nightmodehelp: Show additional commands for Night Mode settings\n\n"
        "Additional Options (Clickable Buttons):\n"
        "- Enable Night Mode"
        "- Disable Night Mode"
        "- Visit our Website"
        "- GitHub Repository",
        buttons=[
            [Button.inline("Enable Night Mode", data="enable_night_mode")],
            [Button.inline("Disable Night Mode", data="disable_night_mode")],
            [Button.inline("Visit our Website", data="visit_website")],
            [Button.inline("GitHub Repository", data="github_repo")],
        ]
    )

@events.register(events.CallbackQuery(pattern=b"enable_night_mode"))
async def enable_night_mode_callback(event):
    await event.respond("Enabling Night Mode...")

# Similar handlers for other callback queries
