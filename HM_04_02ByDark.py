text = [
    "60b90c1c13067a15887e1ae1,Tayson,3\n",
    "60b90c2413067a15887e1ae2,Vika,1\n",
    "60b90c2e13067a15887e1ae3,Barsik,2\n",
    "60b90c3b13067a15887e1ae4,Simon,12\n",
    "60b90c4613067a15887e1ae5,Tessi,5\n"
]
all_text = "".join(text)

path = "/Users/macbook/pythonProject8/PyPro/home.txt2"

with open("home.txt2", "wb+") as fl:
    fl.write(all_text.encode('utf-8'))


def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r+', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    cats.append({'id': id, 'name': name, 'age': age})
                except ValueError:
                    print(f"Помилка в ряду: {line.strip()}")
    except FileNotFoundError:
        print("Файлу не знайдено")
    except Exception as e:
        print(f"Помилка при читанні: {e}")
    return cats


cats_info = get_cats_info(path)
print(cats_info)


