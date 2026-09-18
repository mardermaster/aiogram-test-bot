from os import getenv
from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
from forms.routes import router, notif

load_dotenv()

TOKEN = getenv('BOT_TOKEN')
dp = Dispatcher()
dp.include_router(router)
async def main():
  bot = Bot(token=TOKEN)
  asyncio.create_task(notif(bot))
  print('start...')
  await dp.start_polling(bot)
if __name__ == '__main__':
  asyncio.run(main())

