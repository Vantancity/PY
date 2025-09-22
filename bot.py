from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random
from datetime import datetime

TOKEN = '8243151682:AAHcITfIJKMBtv4MV5cIZfLVrv4WdMyzS14'
bot = Bot(TOKEN)
dp = Dispatcher()

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

my_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/start"), KeyboardButton(text="/premium")]],
    resize_keyboard=True
)

class User(StatesGroup):
    name = State()
    age = State()

@dp.message(Command("start"))
async def start(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Нажимай на нужную кнопку и подпишись на 10 каналов-партнёров", reply_markup=my_keyboard)
        await message.answer("Назови своё имя:")
        await state.set_state(User.name)
    else:
        await message.answer("Заверши ввод или нажми /cancel")

@dp.message(User.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Назови свой возраст:")
    await state.set_state(User.age)

@dp.message(User.age)
async def get_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введи возраст цифрами (например, 13)")
        return
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    await message.answer(f"Тебя зовут {data['name']}, тебе {data['age']} лет!")
    await state.clear()

@dp.message(Command("premium"))
async def prem(message: Message):
    name = message.from_user.first_name
    if message.from_user.is_premium:
        await message.answer(f"🎉 {name}, ты с Premium! Круто!")
    else:
        await message.answer(f"👋 {name}, попробуй Premium — будет интереснее!")

@dp.message(Command("advice"))
async def advice(message: Message):
    today = datetime.now().date().toordinal()
    random.seed(today)
    tip = random.choice(daily_tips)
    random.seed()
    await message.answer(tip)

@dp.message(Command("flip"))
async def flip(message: Message):
    await message.answer("Орёл" if random.random() < 0.5 else "Решка")

@dp.message(Command("dice"))
async def dice(message: Message):
    await message.answer("Бросаю кубик...")
    await message.answer_dice(emoji="🎲")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("/start - Начало\n/advice - Совет дня\n/flip - Орёл/Решка\n/dice - Кубик\n/premium - Проверить Premium\n/time - Время\n/cancel - Отмена")

@dp.message(Command("time"))
async def show_time(message: Message):
    current_time = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Время: {current_time}")

@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено. /start")

if __name__ == "__main__":
    dp.run_polling(bot)