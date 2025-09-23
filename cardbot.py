from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import random

TOKEN = '8495932018:AAHW2TycvUj0m42rcSj5o5SyPo4r6gTNXI0'
bot = Bot(TOKEN)
dp = Dispatcher()

class CardGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.enemy_hand = []
        self.player_score = 0
        self.enemy_score = 0

def create_deck(self):
    suits = ["♥", "♦", "♣", "♠"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [f"{suit}{value}" for suit in suits for value in values]
    random.shuffle(deck)
    return deck


card_game = CardGame()
deck = card_game.create_deck()
print(deck)

@dp.message(Command("start"))
async def start(message: Message):
        await message.answer("Привет")