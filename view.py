# юда все функции отправляющие сообщения


from aiogram import types
from bot import bot


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки\n'
                           f'Основные правила игры: \n'
                           f'Нам будет дано некоторое количество конфет(150), '
                           f'за один ход мы можем взять\n'
                           f'не более определённого количества(от 1 до 28) '
                           f'выйграл тот, кто сделал последний ход'
                           f'Итак, начнём!\n')
