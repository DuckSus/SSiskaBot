import logging
import random
import asyncio
from background import keep_alive
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton

# Твой токен
TOKEN = "7774543442:AAGtOJN6VZdQ_KnJFCdgjyzlfx2X_QhNhgU"

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
# Описание для размеров писюнчика
penis_responses = {
    0: " Ты кастрирован или что?",
    1: "🔬 Микроскоп уже купил?",
    2: "🐛 Маленький, но гордый!",
    3: "🌱 Ещё подрастёт, наверное...",
    4: "🍌 Мини-бананчик!",
    5: "📏 Уже можно измерять без лупы!",
    6: "🥒 Не стыдно, но и не гордость.",
    7: "📏 Средний результат!",
    8: "👍 Уже неплохо!",
    9: "💪 Вполне достойно!",
    10: "🔥 Золотая середина!",
    11: "💦 Готов к подвигам!",
    12: "💪 Уже можно хвастаться!",
    13: "🚀 Уверенный размер!",
    14: "🔝 Хороший результат!",
    15: "👑 Впечатляющий!",
    16: "🍆 Это уже уровень!",
    17: "🔥 Легенда!",
    18: "💎 Эталонный писюн!",
    19: "🏆 Чемпионский размер!",
    20: "⚡ Бог среди смертных!",
    21: "😵 Женщины боятся, но любят!",
    22: "👀 Это точно влезет?",
    23: "🚀 Космический масштаб!",
    24: "💀 Опасность для человечества!",
    25: "🌍 Гравитация начала искажаться!"
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
        -69: "Вообще нахуй не существует 👻",
        7: "Это пиздец",
        404: "Размер не найден. Возможно, был удалён… 🖥️🚫",
    }

    if random.random() < 0.95:  # 95% шанс на обычные размеры
        size = random.randint(0, 6)
        description = random.choice(responses.get(size, ["Редчайший размер! 🤯"]))
    else:  # 5% шанс на редкие числа (по 0.5% на каждое)
        size = random.choice(list(rare_numbers.keys()))
        description = rare_numbers[size]

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
    intro = random.choice(intro_phrases).format(size=size)
    
    # Формируем финальный текст
    text = f"{intro}\n{description}"

# Описание для размеров писюнчика с шансами
penis_sizes = {
    "common": (list(range(1, 26)), 60),
    "uncommon": (list(range(25, 51)), 20),
    "rare": (list(range(50, 101)), 10),
    "epic": (list(range(100, 201)), 6),
    "secret": ([201, -1, 6969, 0], 4)
}

# Описание для всех размеров
size_descriptions = {size: f"📏 Твой писюнчик {size} см! Это достойно!" for size in range(1, 201)}

# Описание для секретных чисел
secret_descriptions = {
    201: "🚀 Ты обладатель легендарного суперписюна!",
    -1: "❌ Тебя просто нет...",
    6969: "🔥 Священное число среди братанов!",
    0: "😱 Полный ноль! Где он?!"
}
    # Кнопка для мгновенного повторного вызова
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🍒Померить сиси", switch_inline_query_current_chat="")]
        ]
    )

    result_breast = InlineQueryResultArticle(
        id=str(random.randint(1000, 9999)),  # ID должен быть уникальным
        title="🍒Узнать размер сисек",
        input_message_content=InputTextMessageContent(message_text=text),
        reply_markup=markup
    )
# Генерация размера писюнчика от 0 до 25 см
    penis_size = get_random_penis_size()
    penis_description = secret_descriptions.get(penis_size, size_descriptions.get(penis_size, "🤷 Неизвестный результат!"))
    
    penis_text = f"🍆 {penis_description}"

    result_penis = InlineQueryResultArticle(
        id=str(random.randint(1000, 9999)),
        title="🍆 Измерить свой писюнчик",
        input_message_content=InputTextMessageContent(message_text=penis_text),
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Померить писюнчик", switch_inline_query_current_chat="")]
            ]
        )
    )

await query.answer([result_breast, result_penis], cache_time=1)

# Подключаем роутер к диспетчеру
dp.include_router(router)

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    
keep_alive()
if __name__ == "__main__":
    asyncio.run(main())
