import logging
import random
import asyncio
from background import keep_alive
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

# Твой токен
TOKEN = "7422518676:AAF-arNpJbW1M_OZycca_QJDzVq9eXHvjw8"

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

# Фразы в зависимости от числа
responses = {
    0: [
        "Поздравляю, абсолютный ноль. Даже доска для нарезки мягче",
        "Грудь размером в мою любовь к тебе... То есть её нет. 💔",
        "Плоская, как Земля в головах у далбаёбов.",
        "Где-то плачет один производитель бюстгальтеров... Ну и похуй как-то. ",
        "Позвоночник вперёд выпирает больше, чем грудь. Сочувствую. (АХАХА) 🤣🤣🤣🤣",
        "Поздравляю эту грудь можно использовать в виде линейки",
        "В темноте подумают что столкнулись со стенкой..А нет , это грудь ",
        "Это арбузы. Которые съели",
        "Это сиськи Лоли",
        "Ебанное позорище 🤣🤣",

    ],
    1: [
        "Ну, технически это уже не ноль… но никто и не заметит. ",
        "Бонусный уровень — 'микро'. Это что-то вроде предзаказа на грудь? 🤔",
        "Ну… в темноте и под свитером можно вообразить. 🧐",
        "Держи подарок! 🎁 Внутри — надежда на второй размер. ",
        "Если сильно напрячься, можно выдать за мускулы обезьяны. 🐒",
        "Если приложить лупу , то может быть и что то будет видно",
        "Бля да иди нахуй я не могу придумать столько описаний для каждого размера",
        "1 размер лучше размера пустоты",
        "Нужно положить меньше носков в лифчик чем уебанам с 0 размером",
        "Ребенок.",
    ],
    2: [
        "Официальный допуск в клуб людей с грудью! 🎉",
        "Небольшие, но гордые! 😌",
        "Лёгкий намёк на соблазн, но пока ещё без фанатизма.",
        "На пляже уже можно заметить. 🏖",
        "Магазинные лифчики хоть как-то сидят. 🛍",
        "Самый надёжный размер: не слишком много, не слишком мало. Прямо в точку!",
        "Без стеснения можно носить лифчик",
        "После беременности увеличится ",
        "пошел нахуй",
    ],
    3: [
        "Классический 'золотой стандарт'! ",
        "Идеальный баланс между удобством и моим членом.",
        "Если грудь — это экономика, то эта грудь среднего класса. ",
        "Абсолютно идеальный размер. ",
        "Если бы грудь была пиццей, то эта грудь 'Маргарита' — классика. ",
        "Я только что узнал что есть 6 размер. Блять.",
        "У мужиков встает на эти сиськи",
        "Всем нравится этот размер.",
        "TitsJob обеспечен ",
        "Этот размер любят даже женщины ",
    ],
    4: [
        "Друзья уважают, мужчины завидуют, а девушки смотрят с лёгкой ревностью. 👀",
        "Такой размер спокойно лежит на руке, всем нравится. ✋🔥",
        "Все хотят потрогать эту грудь",
        "Позвоночник уже начинает уставать держать такую махину",
        "Такую грудь под одеждой не спрячешь",
    ],
    5: [
        "Осторожно, это уже может считаться сексуальным оружием! ",
        "Этот размер — уровень, при котором появляются поклонники (пубертатники), а спина начинает ныть. ",
        "Наконец-то кто-то, кто может использовать грудь как подушку для сна! 😴",
        "Если бы размер груди был валютой, ты это уже было бы миллионером. 💵",
        "Но ещё же есть 6 размер...",
    ],
    6: [
        "Это уже не грудь, а два независимых небесных тела с собственной гравитацией.",
        "Лифчики? Да тут блять целая семья вместо груди",
        "Шансы не привлекать к себе внимание - 0%",
        "Смотришь вниз, ног не видно. Но зато 6 размер.",
        "Ну давай, хвастайся сиськами. Только у них спина не болит,а у тебя да. Ебанашка.",
    ]
}
# Обработчик inline-запросов
@router.inline_query()
async def inline_breast_size(query: InlineQuery):
    """Обрабатывает inline-запросы и отправляет рандомный размер груди."""

    # Шанс выпадения редких чисел
    rare_numbers = {
        69: "Вроде бы поза, а вроде бы размер 🤔",
        42: "42 БРАТУХА 🔥",
        52: "Питерские сиси 🏙",
        25: "Квадрат 5 размера 🔲",
        -1: "Это что такое нахуй 🤨",
        -69: "Вообще нахуй не существует 👻"
        7: "Это пиздец",
        666Если это ты читаешь, то знай что меня держат в заложниках999: "ПОМОГИТЕ",
        404: "Размер не найден. Возможно, был удалён… 🖥️🚫",
        Агент007: "🕶️"
    }

    if random.random() < 0.95:  # 95% шанс на обычные размеры
        size = random.randint(0, 6)
        description = random.choice(responses.get(size, ["Редчайший размер! 🤯"]))
    else:  # 5% шанс на редкие числа (по 0.5% на каждое)
        size = random.choice(list(rare_numbers.keys()))
        description = rare_numbers[size]

    fact = random.choice(facts)  # Выбираем случайный факт
   # Варианты начала фразы
    intro_phrases = [
        "🍒 У меня {size} размер сисек!",
        "👵 У твоей бабушки {size} размер сисек!",
        "🍒У твоего соседа {size} размер сисек!",
        "🏫 У твоего учителя {size} размер сисек!",
        "👬 У твоего друга {size} размер сисек!",
        "💼 У твоего босса {size} размер сисек!",
        "😿 У твоей кошки {size} размер сисек! (интересно, как это работает 🤔)",
        "🐶 У твоей собаки {size} размер! (интересно, как это работает 🤔)",
        "🍒 Исследования показали, что у тебя {size} размер сисек !",
        "🍒 Кажется у тебя {size} размер сисек !",
        "💀 У твоего нерожденного брата был бы {size} размер сисек!",
        "🍒 У твоей знакомой подруги троюдной сестры {size} размер сисек!",
        "🍒 У твоей маминой подруги {size} размер сисек!",
        "🍒 У тебя {size} размер сисек! Что будешь с этим делать?",
        "📜 Великие пророки предсказали: у тебя {size} размер сисек!",
        "📦 Заказал на AliExpress – пришли {size} размер сисек!",
        "🔮 Гадалка посмотрела в хрустальный шар и сказала, что у тебя {size} размер сисек!", 
        "💀 У твоего сперматозоида {size} размер сисек!"
        "👵 У твоей прабабушки которая жила ещё во время Иисуса {size} размер сисек!",
        "У тебя нет сисек).",
    ]
   # Варианты для редкого интро про пенис (0% шанс)
    rare_intro_phrases = [
        "🍆 Поздравляю, у тебя {size} X {size} см. Пора радоваться или грустить?",
        "🍆 Анализ ДНК показал: длина твоего прибора - {size} X {size} см!",
        "🍆 Учёные выяснили, что {size} X {size} см — это твоя реальность. Надеюсь, не в худшую сторону!",
        "📏 Линейка не врёт! У тебя {size} X {size} см. Поверим?",
        "💀 Древние пророчества не предсказывали, что твой размер будет {size} X {size} см!"
    ]
    
 # Шанс выпадения альтернативного интро
    if random.random() < 0.02: # 0.2% шан
        intro = random.choice(rare_intro_phrases).format(size=size)
    else:
        intro = random.choice(intro_phrases).format(size=size)
    
    # Формируем финальный текст
    text = f"{intro}\n{description}"


    # Кнопка для мгновенного повторного вызова
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Померить сиси", switch_inline_query_current_chat="")]
        ]
    )

    result = InlineQueryResultArticle(
        id=str(random.randint(1000, 9999)),  # ID должен быть уникальным
        title="Узнать размер сисек",
        input_message_content=InputTextMessageContent(message_text=text),
        reply_markup=markup
    )

    await query.answer([result], cache_time=1)  # cache_time=1 чтобы не запоминал старые ответы

# Подключаем роутер к диспетчеру
dp.include_router(router)

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    
keep_alive()
if __name__ == "__main__":
    asyncio.run(main())
