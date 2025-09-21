from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import random
from datetime import datetime
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
TOKEN = '8243151682:AAHcITfIJKMBtv4MV5cIZfLVrv4WdMyzS14'
bot = Bot(TOKEN)

daily_tips = [
    "Планируй свой день заранее, чтобы успевать больше.",
    "Выделяй время для отдыха, чтобы повысить продуктивность.",
    "Ставь конкретные, измеримые цели на день.",
    "Начинай день с самой важной задачи.",
    "Используй таймеры, чтобы не отвлекаться.",
    "Не бойся делать ошибки, они часть обучения.",
    "Делай короткие перерывы каждые 60 минут работы.",
    "Питайся правильно — это влияет на твою энергию.",
    "Занимайся физическими упражнениями хотя бы 15 минут в день.",
    "Поддерживай позитивное мышление и избегай негатива.",
    "Читайте полезные книги или статьи каждый день.",
    "Веди дневник благодарности, чтобы улучшить настроение.",
    "Используй списки задач для организации дел.",
    "Учись чему-то новому каждый день, даже немного.",
    "Общайся с интересными людьми для расширения кругозора."
]

dp = Dispatcher()

my_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/start"), KeyboardButton(text="/premium")]],
            resize_keyboard=True
            )

class User(StatesGroup):
    name = State()
    age = State()

@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
        await message.answer("Нажимай на нужную кнопку и подпписывайс на 10 каналов-партнёров", reply_markup=my_keyboard)
        await message.answer("Назови своё имя: ")
        await state.set_state(User.name)
        
@dp.message(User.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Назови свой возраст: ")
    await state.set_state(User.age)

@dp.message(User.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    age = data.get("age")
    name = data.get("name")
    await message.answer(f"Тебе {age} лет и тебя зовут {name}")
    await state.clear()
        
@dp.message(Command("premium"))
async def prem(message: Message):
    name = message.from_user.first_name
    premium = message.from_user.is_premium
    if premium:
        await message.answer(f"Привет {name}, ты с премкой, поздравляю!")
    else:
        await message.answer(f"Привет {name}, рад тебя видеть!")
        
@dp.message(Command("advice"))
async def advice(message: Message):
        await message.answer(random.choice(daily_tips))
        
@dp.message(Command("flip"))
async def flip(message: Message):
    result = ["Орёл", "Решка"]
    await message.answer(random.choice(result))
    
@dp.message(Command("dice"))
async def dice(message: Message):
    await message.answer_dice() # Отправляет анимированный кубик Telegram
        
@dp.message(Command("help"))
async def help_command(message: Message):
    text = """
/start - Начало общения
/advice - Совет на день  
/flip - Орёл Решка
/dice - Кубик 6 граней
    """
    await message.answer(text)

@dp.message(Command("time"))
async def show_time(message: Message):
    current_time = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Текущее время: {current_time}")

if __name__ == "__main__":
    dp.run_polling(bot) 