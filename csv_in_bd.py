import sqlite3
import pandas as pd
from datetime import datetime

start_time = datetime.now() # Начало загрузки таблицы в бд

df = pd.read_csv('police-department-calls-for-service.csv') # Наш csv-файл
print('Количество строк и столбцов в исходном csv-файле:', df.shape) # (строки, cтолбцы)

con = sqlite3.connect("city_spec.db") # Cоздаём базу sqlite3 city-spec,в которую помещаем наш csv-файл

df.to_sql("MyTable", con) # Даём название нашей таблице в базе 'MyTable'

cursor = con.cursor() #Создаем курсор - это специальный объект который делает запросы и получает их результаты

cursor.execute("select * from MyTable") # Выполняем запрос на получение всех строк из таблицы

results = cursor.fetchall() # Результат нашего запроса
print('Количество строк в таблице MyTable:', len(results))

con.close() # Закрываем коннект к базе

end_time = datetime.now() # Время завершения загрузки в бд

result_time = end_time - start_time # Конечное время загрузки в бд
print('Время загрузки таблицы в бд :', result_time)

