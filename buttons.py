from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

buttons = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="button1"),
            KeyboardButton(text="button2")

        ],
        [
            KeyboardButton(text="button3")
        ],
        [
            KeyboardButton(text="button4"),
            KeyboardButton(text="button5")

        ],
    ],
    resize_keyboard=True
)
inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="button1",callback_data='button1'),
            InlineKeyboardButton(text="button2",callback_data='button2')
        ],
        [
            InlineKeyboardButton(text="button3",callback_data='button3')
        ],
        [
            InlineKeyboardButton(text="button4",callback_data='button4'),
            InlineKeyboardButton(text="button5",callback_data='button5')
        ]
    ]
)

lst = ['btn1', 'btn2','btn3','btn4']
async def generate_btn():
    btns = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    for i in lst:
        btns.insert(KeyboardButton(text=i))
    return btns



