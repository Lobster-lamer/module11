import requests
from PIL import Image, ImageFilter
import io
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import timeit
from consoleTextStyle import ConsoleTextStyle as CoTeSt


def declension(number, declensions: tuple) -> str:
    if number % 10 == 1 and number // 10 != 1:
        return declensions[0]
    elif 1 < number % 10 < 5 and number // 10 != 1:
        return declensions[1]
    else:
        return declensions[2]


def compare_timeit(func1, func1_name, func2, func2_name, number_of_execution) -> None:
    time_of_func1 = timeit.timeit(func1, number=number_of_execution)
    time_of_func2 = timeit.timeit(func2, number=number_of_execution)
    color_of_func1 = CoTeSt.Color.GREEN if time_of_func1 < time_of_func2 else CoTeSt.Color.RED
    color_of_func2 = CoTeSt.Color.GREEN if time_of_func1 > time_of_func2 else CoTeSt.Color.RED
    print(f"Время выполнения {func1_name} для {number_of_execution} "
          f"запуск{declension(number_of_execution, ("а", "ов", "ов"))}: "
          f"{color_of_func1}{time_of_func1}{CoTeSt.REGULAR}")
    print(f"Время выполнения {func2_name} для {number_of_execution} "
          f"запуск{declension(number_of_execution, ("а", "ов", "ов"))}: "
          f"{color_of_func2}{time_of_func2}{CoTeSt.REGULAR}")


CoTeSt.colorful_text("Смотрим библиотеку numpy и matplotlib", CoTeSt.Color.CYAN)
compare_timeit(lambda: random.randint(-1, 1), "random.randint для одной ячейки",
               lambda: np.random.randint(-1, 2, size=(1, 1)), "numpy.random.randint для одной ячейки",
               100)

compare_timeit(lambda: [random.randint(-1, 1) for _ in range(1000)], "random.randint для 1000 ячеек",
               lambda: np.random.randint(-1, 2, size=(1, 1000)), "numpy.random.randint для 1000 ячеек",
               1)

"""Дальше не используется random из numpy из-за желания зделать более инерционный массив значений, для чего нужно
рандомизировать значение в ячейке, а не целый массив значений, для чего по большей части и полезен numpy.
Использование np.random.randint приведёт к излишней нагруженности кода в данном случае"""
# Вопрос к проверяющему: есть ли возможность создать списковую сборку, в которой можно использовать предыдущее значение
# предыдущего элемента списка?
time = np.arange(0, 10, 0.1)
Ut = np.zeros((1, len(time)), np.int8)
for Uti in range(len(Ut[0])):
    if Uti == 0:
        Ut[0][Uti] = random.randint(-1, 1)
    else:
        Ut[0][Uti] = random.randint(Ut[0][Uti-1]-1, Ut[0][Uti-1]+1)

plt.setp(plt.plot(time, Ut[0]), "linewidth", 5, "color", "black")
plt.grid()
plt.title("График какой-то фигни с обратной связью")
plt.xlabel("Время, сек")
plt.ylabel("Напряжение, В")
plt.show()


plt.figure()
plt.title("Вырисовываем Python", fontweight="bold")
plt.subplot(161)
plt.setp(plt.plot([0, 0], [0.5, -2]), "linewidth", 5, "color", "black")
plt.xticks([])
plt.yticks([])
time = np.arange(0, 1, 0.1)
circle = np.power(0.25 - np.power(time, 2), 0.5)
plt.setp(plt.plot(circle, time), "linewidth", 5, "color", "black")
plt.setp(plt.plot(circle, -time), "linewidth", 5, "color", "black")
plt.text(0, 0.6, "Yeah, Python!", color="white",fontweight="bold", rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(0.1, 0.1, 0.1),
                   fc=(0, 0, 0),
                   )
         )
plt.subplot(162)
plt.setp(plt.plot([0, 1], [0, 1]), "linewidth", 5, "color", "black")
plt.setp(plt.plot([0, 0.5], [1, 0.5]), "linewidth", 5, "color", "black")
plt.xticks([])
plt.yticks([])
plt.subplot(163)
plt.setp(plt.plot([0, 0], [0, 1]), "linewidth", 5, "color", "black")
plt.setp(plt.plot([-0.5, 0.5], [1, 1]), "linewidth", 5, "color", "black")
plt.xticks([])
plt.yticks([])
plt.subplot(164)
plt.setp(plt.plot([-0.5, -0.5], [0, 1]), "linewidth", 5, "color", "black")
plt.setp(plt.plot([-0.5, 0.5], [0.5, 0.5]), "linewidth", 5, "color", "black")
plt.setp(plt.plot([0.5, 0.5], [0, 1]), "linewidth", 5, "color", "black")
plt.xticks([])
plt.yticks([])
plt.subplot(165)
time = np.arange(0, 1, 0.01)
circle = np.power(0.25 - np.power(time, 2), 0.5)
plt.setp(plt.plot(circle, time), "linewidth", 5, "color", "black")
plt.setp(plt.plot(circle, -time), "linewidth", 5, "color", "black")
plt.setp(plt.plot(-circle, time), "linewidth", 5, "color", "black")
plt.setp(plt.plot(-circle, -time), "linewidth", 5, "color", "black")
plt.xticks([])
plt.yticks([])
plt.subplot(166)
plt.setp(plt.plot([-0.5, -0.5], [0, 1]), "linewidth", 5, "color", "black")
plt.setp(plt.plot([-0.5, 0.5], [1, 0]), "linewidth", 5, "color", "black")
plt.setp(plt.plot([0.5, 0.5], [0, 1]), "linewidth", 5, "color", "black")
plt.xticks([])
plt.yticks([])
plt.show()


print("\n")
CoTeSt.colorful_text("Смотрим библиотеку requests и PIL", CoTeSt.Color.CYAN)
url = "https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png"
r = requests.get(url)
if r.status_code == 200:
    print(f"Заголовки сайта, с которого скачали картинку:\n {r.headers}")
    img = Image.open(io.BytesIO(r.content))
    print(f"Расширение картинки: {CoTeSt.Color.PURPLE}{img.format}{CoTeSt.REGULAR},"
          f" размер картинки в пикселях: {CoTeSt.Color.PURPLE}{img.size}{CoTeSt.REGULAR}")
    img.show()
    img.thumbnail((128, 128))
    img.filter(ImageFilter.BLUR).show()
    img.convert("RGB").save("размытая хрень.jpg")


print("\n")
CoTeSt.colorful_text("Смотрим библиотеку requests", CoTeSt.Color.CYAN)
url = "https://swapi.dev/api/people/1/"
r = requests.get(url)
print(f"Код ответа: {r.status_code}")
if r.status_code == 200:
    print("Посмотрим json пришедший с сайта:")
    pprint(r.json())
