from django import template


register = template.Library()


CURRENCIES_SYMBOLS = {
    'rub': 'Р',
    'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
    """
    value: значение, к которому нужно применить фильтр
    code: код валюты
    """
    postfix = CURRENCIES_SYMBOLS[code]

    return f'{value} {postfix}'


PROFANITIES = ['lorem', 'dummy', 'text']
# PROFANITIES = []


@register.filter()
def censor_profanities(value):
    # Разделяем текст на слова по пробельным символам
    words = value.split()

    for idx, word in enumerate(words):
        lower_word = word.lower()
        # Проверяем, является ли слово ругательным
        if lower_word in [prof.lower() for prof in PROFANITIES]:
            # Формируем новое слово с первой буквой и звездочками для остальных символов
            censored_word = word[0] + '*' * (len(word) - 1)
            # Заменяем исходное слово на отфильтрованное в списке слов
            words[idx] = censored_word

    # Возвращаем отфильтрованный текст
    return ' '.join(words)
