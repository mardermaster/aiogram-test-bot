from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram import Bot
import asyncio
router = Router()

subscribers = set()

async def notif(bot: Bot):
  while True:
    if subscribers:
      for user_id in list(subscribers):
        try:
          await bot.send_message(user_id, 'Новости: в Якутии сегодня ничего не произошло!😱')
        except Exception:
          pass
    
    await asyncio.sleep(10)


@router.message(Command('start'))
async def start(message: Message):
  await message.answer('Привет, вот список комманд:\n\n/subscribe - подписаться на новости\n/unsubscribe - отписаться от новостей\n/subscribers - список подписчиков.')

@router.message(Command('subscribe'))
async def subscribe(message: Message):
  user_id = message.from_user.id
  subscribers.add(user_id)
  await message.answer('Вы успешно подписались!')

@router.message(Command('unsubscribe'))
async def unsubscribe(message: Message):
  user_id = message.from_user.id
  subscribers.discard(user_id)
  await message.answer('Вы отписались🙁')

@router.message(Command('subscribers'))
async def subscriber(message: Message):
  if not subscribers:
    await message.answer('Подписчиков нет!')
    return
  
  text = 'Подписчики:\n'
  for uid in subscribers:
    text += f'{uid}\n'
  await message.answer(text)
