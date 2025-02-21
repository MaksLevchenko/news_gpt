from datetime import time
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import StateFilter
from aiogram.types import Message

from ..logic.logic import get_news, is_url
from ..states import FSMFillLink
from ..gigachat import get_gpt_response


router = Router()


@router.message(Command(commands="news_analysis"))
async def fill_link(callback: CallbackQuery, state: FSMContext):
    """Этот хэндлер будет срабатывать на команду "/news_analysis" и предложит ввести ссылку на новость"""
    await callback.answer(
        text="Пожалуйста введите ссылку на новость, которую надо проанализировать:"
    )
    await state.set_state(FSMFillLink.fill_link)


@router.message(StateFilter(FSMFillLink.fill_link))
async def view_news(message: Message, state: FSMContext):
    """Этот хэндлер сработает после ввода ссылки на новость,
    проверит на то, что введённое является ссылкой и передаст её на анализ"""
    link = message.text
    if is_url(link):
        await message.answer(text="Всё супер начинаю анализ!")
        news_data = get_news(link)
        if news_data:
            news_analis = get_gpt_response(news_data)
            await message.answer(text=news_analis)
            await state.clear()
        else:
            await message.answer(
                text="К сожалению, я не смог найти информацию по этой новости."
            )
            await message.answer(
                text="Пожалуйста введите ссылку на новость, которую надо проанализировать:"
            )
    else:
        await message.answer(
            text="Ой, то, что вы ввели не похоже на ссылку. Пожалуйста, попробуйте ещё раз."
        )
        return await message.answer(
            text="Пожалуйста введите ссылку на новость, которую надо проанализировать:"
        )
