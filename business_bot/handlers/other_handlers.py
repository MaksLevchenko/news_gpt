from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext


router = Router()


# Этот хэндлер будет срабатывать на команду "/cancel" в состоянии
# по умолчанию и сообщать, что эта команда работает внутри машины состояний
@router.message(Command(commands="cancel"), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(text="Отменять нечего.")


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text="Всё успешно отменено!")
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()


@router.message(Command(commands="start"))
async def get_start(message: Message):
    print(message.bot.context)
    await message.answer(text="start")


# Этот хэндлер будет срабатывать если вводить что-то не тогда, когда просят
@router.message(StateFilter(default_state))
async def send_echo(message: Message):
    if not message.chat.type == "supergroup":
        await message.reply(text="Извините, моя твоя не понимать")
