from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
import random
import pyglet
import pygame
import datetime
import pyttsx3
from pygame import mixer
from translate import Translator
import webbrowser
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import wikipedia
import time
import pygame as pg
import math
















engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 300)     # скорость речи
engine.setProperty('volume', 1)   # громкость (0-1)






def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('скажите вашу команду')
        audio = r.listen(source)


    try:
        our_speach = r.recognize_google(audio,language='ru')
        print('Вы сказали:'+ our_speach)
        return our_speach
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"


def do_this_command(message):
    message = message.lower()
    if 'вопросы' in message:
        say_message(" таймер, поиск в википедии ,скажи время ,видео, прогноз погоды, открой телегу, открой контакты, нет, расскажи что нибудь, привет, ты откуда,включи песню,загадка,"
                    "камень ножницы бумага, голос, переводчик, калькулятор, спать,")
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()


    if 'таймер' in message:
        while True:
            i1 = 0 # секунды
            i2 = 0 # минуты
            i3 = 0 # часы

            say_message('Введите количество секунд')
            time_user = int(input('Введите кол-во секунд'))

            for q in range(time_user):
                time.sleep(1)
                i1 += 1
                print('Прошло секунд', i1)
                say_message(str(i1))

                if (i1 % 60) == 0:
                    i2 += 1
                    print('Прошло минут', i2)
                if (i1 % 3600) == 0:
                    print('Прошло часов', i3)



            say_message('Время окончено')
            break







    if 'поиск в википедии' in message:
        say_message('Введите термин который вы бы хотели найти')
        ls = ['0005101.mp3', 'r1.mp3', 'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()



        wikipedia.set_lang('ru')
        word = input()
        python_page = wikipedia.page(word)

        print(python_page.html)
        engine.say(python_page.html)
        engine.runAndWait()

        print(python_page.title)
        engine.say(python_page.title)
        engine.runAndWait()

        print(python_page.summary)
        engine.say(python_page.summary)
        engine.runAndWait()


    if 'скажи время' in message:
        print((datetime.datetime.now()))
        a = (datetime.datetime.now())
        engine.say(a)
        engine.runAndWait()

    if "видео"  in message:
        say_message('открываю видео')
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        webbrowser.open('https://www.youtube.com/')

    if 'прогноз погоды' in message:

        config_dict = get_default_config()  # Инициализация get_default_config()
        config_dict['language'] = 'ru'  # Установка языка
        say_message('Введите ваш город')
        place = input("Введите ваш город: ")  # Переменная для записи города

        country_and_place = place  # Запись города и страны в одну переменную через запятую

        owm = OWM('8feaad23b7a71508cefef8e594ef18a2')  # Ваш ключ с сайта open weather map
        mgr = owm.weather_manager()  # Инициализация owm.weather_manager()
        observation = mgr.weather_at_place(country_and_place)
        # Инициализация mgr.weather_at_place() И передача в качестве параметра туда страну и город

        w = observation.weather

        status = w.detailed_status  # Узнаём статус погоды в городе и записываем в переменную status
        w.wind()  # Узнаем скорость ветра
        humidity = w.humidity  # Узнаём Влажность и записываем её в переменную humidity
        temp = w.temperature('celsius')['temp']  # Узнаём температуру в градусах по цельсию и записываем в переменную temp


        def weather():  # Функция с выводом погоды
            say_message('Данные о погоде в вашем городе')
            ls = ['0005101.mp3', 'r1.mp3', 'r3.mp3', 'r4.mp3']

            a = random.choice(ls)
            pygame.mixer.init()
            pygame.mixer.music.load(a)
            pygame.mixer.music.play()
            print("В городе " + str(place) + " сейчас " + str(status) +  # Выводим город и статус погоды в нём
                  "\nТемпература " + str(
                round(temp)) + " градусов по цельсию" +  # Выводим температуру с округлением в ближайшую сторону
                  "\nВлажность составляет " + str(humidity) + "%" +  # Выводим влажность в виде строки
                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")  # Узнаём и выводим скорость ветра

            engine.say("В городе " + str(place) + " сейчас " + str(status) +
                  "\nТемпература " + str(
                round(temp)) + " градусов по цельсию" +
                  "\nВлажность составляет " + str(humidity) + "%" +
                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
            engine.runAndWait()


        weather()  # Вызов функции


        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()




    if 'открой телегу' in message:
        say_message('открываю телеграмм')
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        webbrowser.open('https://web.telegram.org/z/')
    if 'открой контакты' in message:
        say_message('открываю вконтакте')
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        webbrowser.open('https://vk.com/jonioninadevuah')


    elif 'переводчик'in message:
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        while True:
            say_message('введите слово которое хотите перевести')
            text = str(input())
            a = Translator(from_lang='ru', to_lang='en')
            end_text = a.translate(text)
            print(text, '-----> ',end_text)
            say_message(end_text)
            break



    if "нет" in message:
        ls = ["Как хочешь", "На нет и суда нет", "Раз нет так нет", "Нет так нет"]
        say_message(random.choice(ls))
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()

    if "расскажи что-нибудь" in message:
        ls = [" В 1889 году королева Италии Маргарита Савойская заказала первую доставку пиццы", "В Японии можно купить мороженое со вкусом угря",
              " В Португалии считается неприличным писать красными чернилами", " Кальций в наших костях и железо в нашей крови появились от древнего взрыва огромных звезд",
              " Каждое лето Эйфелева башня становится на 15 сантиметров выше.", "В среднем человек засыпает в течение 7 минут.",
              "В 1500 году до н. э. бритая голова считалась идеалом женской красоты", "Панда — это не медведь, а енот",
              "Алкоголь защищает от радиации", "39-й президент США Джимми Картер однажды отправил в химчистку свой пиджак, оставив в кармане записку с кодами запуска ядерных ракет",
              "На западе Китая в чай кладут соль", "В Чили можно встретить на улице полицейскую собаку, обутую в кроссовки для животных",
              "На Филиппинах продаются чипсы Pringles в бумажной упаковке", " Люди с голубыми глазами имеют более высокую толерантность к алкоголю.",
              "Курица появилась раньше яйца согласно Книге бытия 1:20-22.", "10% от общего дохода РФ составляет продажа алкогольной и табачной продукции",
              "Курица рекордсмен смогла лететь 13 секунд подряд",
              "Плотность человеческой головы и арбуза одинакова", "Единственная страна, занимающая целый континент – это Австралия",
              "Когда человек храпит, он не может видеть сны", "Новое исследование показало, что мыши на самом деле не любят сыр",
              "Самая большая в мире улитка имеет длину 91 сантиметр", "Барак Обама в подростковом возрасте был пристрастен к кокаину и марихуане.",
              "Самый длинный боксёрский поединок длился 110 раундов", "Голливудским актёрам когда-то платили за курение в фильмах."]
        say_message(random.choice(ls))
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()




    if 'спасибо' in message:
        ls = ['пожалуйста','рада помочь','спасибо в карман не положишь','обращайтесь','еще что нибудь']
        say_message(random.choice(ls))
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
    if 'калькулятор'in message:
        say_message('введите значение')
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()
        print("результат: ", eval(input("Введите: ")))


    if 'привет' in message:
        ls = [  "И тебе привет, коли не шутишь!"
              ,'Привет! – С тебя килограмм конфет!','А теперь спросите меня: "Как дела?','Здравствуй, здравствуй.','Здравия желаю.'
              'Привет, если не шутишь','И тебе тоже привет','Слушаюсь, товарищ майор','Хеллоу']
        say_message(random.choice(ls))
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()




    elif 'включи песню' in message:
        mus = ['песня.mp3','песня1.mp3','песня3.mp3','песня4.mp3','песня5.mp3','песня6.mp3']
        a = random.choice(mus)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()

    elif 'загадка' in message:
        ls1 = ['Какое колесо не крутится при правом развороте?','Все меня топчут, а я — всё лучше.'
            ,'Что имеет голову, но не имеет мозгов?','Кто говорит на всех языках?',
              'Чем больше из неё берёшь, тем больше она становится.',
              'Вот короткая загадка:У кого за носом пятка?','Что не является вопросом, но требует ответа?',
              'Перед каким простым смертным даже президент снимает шапку?',
              'Что никогда не врёт?','Человек при жизни получает это трижды: два раза абсолютно бесплатно, на третий раз ему приходится за это платить. Догадайтесь, о чем идет речь.'
                'Что больше: сумма всех цифр или их произведение?','Что это: стоит черное, на одной ноге?',
              'Два гвоздя упали в воду. Как фамилия грузина?']
        say_message(random.choice(ls1))
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()


    elif 'пока'in message:
        ls1 = [ "До свидания!", "Аривидерчи!", "Бай бай!", "Увидимся",
                     "До скорых встреч!", "До скорых!", "Всего доброго!", "Гуд бай!",
                     "Пока!", "Пока, Удачи!", "Чау!"]
        say_message(random.choice(ls1))
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()




    elif 'ты откуда'in message:
        say_message('Из Копыля')
        ls = ['0005101.mp3', 'r1.mp3',  'r3.mp3', 'r4.mp3']

        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()





    elif 'камень ножницы бумага' in message:
        say_message('Добро пожаловать в игру камень ножницы бумага')
        say_message('Правило игры Бумага побеждает камень .Камень побеждает ножницы .Ножницы побеждают бумагу ')
        ls = ['камень', 'ножницы', 'бумага']

        k1 = 0
        k2 = 0
        i = 1

        while i <= 3:
            say_message('Введите элемент')
            a = input('Введите элемент')
            b = random.choice(ls)
            print('я выбрала',b)

            if a == 'камень':
                if a == b:
                    say_message('у нас ничья')
                if b == 'ножницы':
                    say_message('вы выйграли')
                    k1 += 1
                if b == 'бумага':
                    say_message('проиграл')
                    k2 += 1

            if a == 'ножницы':
                if a == b:
                    say_message('у нас ничья')
                if b == 'камень':
                    say_message('проиграл')
                    k2 += 1
                if b == 'бумага':
                    k1 += 1
                    say_message('вы выйграли')

            if a == 'бумага':
                if a == b:
                    say_message('у нас ничья')
                if b == 'ножницы':
                    k2 += 1
                    say_message('проиграл')
                if b == 'камень':
                    say_message('вы выйграли')
                    k2 += 1

            i += 1
        if k1 < k2:
            print('у меня',k2, 'очков' ,'а у вас',k1 ,'очков')
            say_message('я выйграла игру')
            ls = ['0005101.mp3', 'r1.mp3', 'r3.mp3', 'r4.mp3']

            a = random.choice(ls)
            pygame.mixer.init()
            pygame.mixer.music.load(a)
            pygame.mixer.music.play()


        if k1 > k2:
            print('у меня', k2, 'очков', 'а у вас', k1, 'очков')
            say_message('вы проиграли')
            ls = ['0005101.mp3', 'r1.mp3', 'r3.mp3', 'r4.mp3']

            a = random.choice(ls)
            pygame.mixer.init()
            pygame.mixer.music.load(a)
            pygame.mixer.music.play()

    elif 'голос' in message:
        ls = ['0005101.mp3', 'r1.mp3', 'r3.mp3', 'r4.mp3']
        a = random.choice(ls)
        pygame.mixer.init()
        pygame.mixer.music.load(a)
        pygame.mixer.music.play()


    elif 'спать' in message:
       exit()













def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name ="_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print('Ассистент',message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)


