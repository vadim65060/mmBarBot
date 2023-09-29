import asyncio

from bot_create import bot, dp
import handlers.bar_handlers


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    print('bot starting')
    asyncio.run(main())
    print('end')
