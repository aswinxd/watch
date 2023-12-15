def Fallen_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "fallen_":
        uptime = get_readable_time((time.time() - StartTime))
        query.message.edit_text(
            text=f"fuck this code
            
            hhj
            ff
            
            fff
            fff                         
                                                     ffff",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="support", callback_data="fallen_support"
                        ),
                        InlineKeyboardButton(
                            text="commands", callback_data="help_back"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="develop", url=f"tg://user?id={OWNER_ID}"
                        ),
                        InlineKeyboardButton(
                            text="source",
                            callback_data="source_",
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="◁", callback_data="fallen_back"),
                    ],
                ]
            ),
        )
