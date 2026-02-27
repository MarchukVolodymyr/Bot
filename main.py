from fastapi import FastAPI
import uvicorn
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import threading


BOT_TOKEN = "8425242719:AAHTAviHj8N0-eraWv_gEknIIAxf099nAak"
PORT = 10000



disp = Dispatcher(bot=Bot)
app = FastAPI()


@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot active")

@app.get("/")
async def check():
    return {"Status : Bot it running"}

async def main():
    bot = Bot(token=BOT_TOKEN)
    await disp.start_polling(bot)


async def runner():
    asyncio.run(main())
    
    
if __name__ == "__main__":
    threading.Thread(target=runner).start()
    uvicorn.run(app,host = "0.0.0.0", port=PORT)