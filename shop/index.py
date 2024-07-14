import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
print(""""
      Если вы хотите добавить в бд Введите 1.
      Если вы хотите закрыть напишите 2.
      """)

whattouneed = input("Введите значение!: ")
if whattouneed == "1":
    print('Заолните данные в 5 строки Имя, почту, возраст!')
    name = input(str('Название товара: '))
    description = input(str('Описание: '))
    price = input(float('Цена: '))
    img = input(str('Путь до фотографии: '))
    amount = input(float('Количество: '))
    cursor.execute('INSERT INTO pyshop_product (name, description, price, image_url, amount) VALUES (?, ?, ?, ?, ?)', (name, description, price, img, amount))
    connection.commit()
    connection.close()
else:
    print('bye')
# Сохраняем изменения и закрываем соединение
