import random
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft


class Lab3:
    def __init__(self):
        self.N = 1024
        self.w = 1200
        self.n = 8
        self.t = [i for i in range(self.N)]
        self.pi = math.pi

    def count_sin(self):
        """Розрахунок n сигналів"""
        res = []
        for i in range(self.n):
            A = random.random()
            fi = random.random() * 6.28
            res_i = [A * math.sin(self.w * self.t[i] * i + fi) for i in range(self.N)]
            res.append(res_i)
        return res

    def count_x_t(self):
        """Розрахунок випадкового сигналу"""
        res = self.count_sin()
        x_t = []
        for i in range(self.N):
            x = 0
            for j in range(self.n):
                x += res[j][i]
            x_t.append(x)
        return x_t

    def count_f_x(self, x_t):
        """Розрахунок ДФТ за формулою з методички"""
        Fx = []
        for i in range(len(x_t)):
            s = 0
            for j in range(len(x_t)):
                s += x_t[j] * complex(math.cos(-2 * self.pi * j * i / len(x_t)),
                                      math.sin(-2 * self.pi * j * i / len(x_t)))
            Fx.append(s)
        return Fx

    def count_f_x_form(self, x_t):
        """Перевірка розрахунків вбудованою формулою"""
        return fft(x_t)

    def show_spectr(self, Fx, Fx_form):
        """Показує графік двох функцій(вбудованої і з методички) і їх різницю"""
        x = []
        y = []
        for i in Fx:
            x.append(i.real)
        for i in Fx_form:
            y.append(i.real)
        res = []
        for i in range(self.N):  # віднімання від графіка порахованого вручну, графіка порахованого формулою
            res.append(x[i] - y[i])

        plt.figure()
        plt.plot([i for i in range(self.N)], x, label='Fx', color='gold')
        plt.plot([i for i in range(self.N)], y, label='Fx_form', color='green')
        plt.plot([i for i in range(self.N)], res, label='res', color='red')
        plt.legend()
        plt.grid(True)
        plt.show()

    def result(self):
        x_t = self.count_x_t()
        self.show_spectr(self.count_f_x(x_t), self.count_f_x_form(x_t))


Lab3().result()
