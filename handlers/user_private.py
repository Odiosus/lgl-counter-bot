from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("hi, I'm a virtual assistant")


@user_private_router.message(F.text.lower().contains("услуги"))
@user_private_router.message(or_f(Command('services')), (F.text.lower() == "услуги"))
async def menu_cmd(message: types.Message):
    await message.answer("Список услуг:")


@user_private_router.message((F.text.lower().contains("о боте")) | (F.text.lower() == "о боте"))
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О боте")


@user_private_router.message((F.text.lower().contains("оплата")) | (F.text.lower() == "варианты оплаты"))
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.answer("Оплата")


@user_private_router.message((F.text.lower().contains("выгруз")) | (F.text.lower() == "варианты выгрузки"))
@user_private_router.message(Command('extract'))
async def shipping_cmd(message: types.Message):
    await message.answer("Выгрузить")


@user_private_router.message(F.text.lower().contains("помощь"))
@user_private_router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Итак, приступим")
