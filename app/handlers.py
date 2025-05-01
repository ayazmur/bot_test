from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    phone = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=kb.main)
    await message.reply("Как дела")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Помощь")


@router.message(F.text == "Каталог")
async def catalog(message: Message):
    await message.answer("Вы открыли каталог", reply_markup=kb.catalog)


@router.callback_query(F.data == "t-shorts")
async def tshorts(callback: CallbackQuery):
    await callback.answer("Вы выбрали категорию")
    await callback.message.answer('Вы выбрали футболки')


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя")


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Введите возраст")


@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.phone)
    await message.answer("Введите номер телефона", reply_markup=kb.get_number)


@router.message(Register.phone, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваше имя {data['name']} ваш возраст {data['age']} ваш номер {data['phone']}")
    await state.clear()
