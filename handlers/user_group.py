from string import punctuation

from aiogram import types, Router
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

bullshit_dict = {'бля', 'гондон', 'мудил'}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if bullshit_dict.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.first_name}, без мата!")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
