### 1.Работа с логами
#### 1.1 Ошибка при апгрейде:
  
```
"is_valid_for_upgrade": false, # НЕДОСТУПНО ДЛЯ АПГРЕЙДА
{"business": 0, "econom": 9}

```

#### 1.2 Ошибка приобретения дополнительного багажа

```
<ns1:confirmed_price>0</ns1:confirmed_price>
```

### 4.Работа с базой данных
#### 4.1 MongoDB

```
db.users.find({
$or: [{
    $and: 
    [{"channels.email.verified": false},
    {"channels.phone.verified": true}]},
{$and: 
    [{"channels.email.verified": false},
    {"channels.phone.verified": true}]
}]

}).limit(3)
```

#### 4.2 PostgreSQL
  
```
SELECT * FROM Transactions tr LEFT JOIN TransactionBalances trb ON tr.id = trb.transactionId WHERE tr.accountId=12345 AND trb.amount > 0 ORDER BY tr.createdAt
```

### 9.Python
#### Написать конвертор мер длины

[*converter.py*](https://raw.githubusercontent.com/hel8er/utair/2fde15b7d6a95815885f13f39b35079885125468/converter.py)

```
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
    res = round(mm / mp_to, 5)
    return f'Результат равен {res} {unit_to}'
    
    
while 1:
    try:
        inp_text = input("Enter data: ")
        print(convert(inp_text))
    except Exception as e:
        print(f'Ошибка: {e}')
```
