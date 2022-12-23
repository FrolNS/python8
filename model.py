# Модуль для выполнения опреаций
import sympy as sp


def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    return str(eval(expr))


def solve_eq(expr: str) -> str:                   # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    try:
        x = sp.Symbol('x')
        ans = sp.solve(expr, x)
        ans = list(map(str, ans))
        return ans
    except ValueError:
        print('Incorrect input')


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    try:
        x = sp.Symbol('x')
        ans = str(sp.simplify(expr))
        return ans
    except ValueError:
        print('Incorrect input')
