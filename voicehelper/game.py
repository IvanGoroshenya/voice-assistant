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



ls = ['камень','ножницы','бумага']

k1 = 0
k2 = 0
i = 1



while i <= 3:
    a = input('Введите элемент')
    b = random.choice(ls)
    print(b)
    if a == 'камень':
      if a == b:
          print('ничья')
      if b == 'ножницы':
          print(' проиграл')
          k2 += 1
      if b == 'бумага':
          print('выйграл')
          k1 += 1


    if a == 'ножницы':
       if a == b:
           print('ничью')
       if b == 'камень':
           print(' проиграл')
           k2 += 1
       if b == 'бумага':
           k1 += 1
           print('выйграл')

    if a == 'бумага':
       if a == b:
           print('ничья')
       if b == 'ножницы':
           k1 += 1
           print(' выйграл')
       if b == 'камень':
           print('проиграл')
           k2 += 1

    i += 1
if k1 < k2:
    print('вы проиграли')
else:
    print('выйграла')








