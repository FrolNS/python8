# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('ДЗ 8\history.csv', 'a') as h:
        h.write(f'\n{expr};{result}')
    print('Результат сохранен в истории')


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('ДЗ 8\history.csv', 'r') as h:
        return h.read()
