calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    my_cortege = len(string), string.upper(), string.lower()
    count_calls()
    return (my_cortege)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for l in range(0, len(list_to_search)):
        if string == list_to_search[l].lower():
            control = True
            break
        else:
            control = False
    return (control)


print(string_info('Вызов фУнкциИ'))
print(string_info('вТОроЙ ВызоВ'))
print(string_info('ТРетИЙ ВЫзов ФУНкцИИ'))
print(is_contains('Кот', ['СобаКа', 'КоТ', 'ДятЕл']))
print(is_contains('вОлк', ['СоБаКа', 'КонЬ', 'ВолК']))
print(is_contains('Морж', ['СоБаКа', 'Кит', 'ВолК']))
print('счётчик: ', calls)
