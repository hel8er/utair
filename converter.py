# Ключ - буквеннное обозначение меры, значение - множитель по отношению к милиметрам
units = {"mm": 1, "cm": 10, "m": 1000, "km": 1000*1000, "inch": 25.4, "foot": 304.8, "yard": 914.4, "mile": 1609000}

def convert(inp_text: str):
    """Перевести исходную меру в милиметры, помножить милиметры на множитель целевой меры"""
    
    data = inp_text.split(" ") # Извлекаем подстроки по пробелу
    unit_from = data[1] # Исходная мера
    unit_to = data[3] # Целевая мера
    mp_from = float(units[unit_from]) # Множитель исходной меры
    mm = float(data[0]) * mp_from # Количество милиметров
    mp_to = float(units[unit_to]) # Множитель целевой меры
    res = round(mm / mp_to, 5) # Округляем до 5 знаков после запятой
    return f'Результат равен {res} {unit_to}'
    
    
while 1:
    try:
        inp_text = input("Enter data: ")
        print(convert(inp_text))
    except Exception as e:
        print(f'Ошибка: {e}')