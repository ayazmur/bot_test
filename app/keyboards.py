from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Оплата'),
                                      KeyboardButton(text="О нас")]],
                           resize_keyboard=True,
                           input_field_placeholder='Выбери пункт меню')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Футболки", callback_data="t-shorts")],
    [InlineKeyboardButton(text="Обувь", callback_data="shoes")],
    [InlineKeyboardButton(text="Джинсы", callback_data="jeans")]
])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить номер", request_contact = True)]],
                                 resize_keyboard=True)