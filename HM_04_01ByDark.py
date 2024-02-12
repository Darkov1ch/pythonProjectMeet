# Створили та закодували файл
with open("home.txt1","wb+") as fl:
    fl.write(b"Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")
# абсолютний шлях
path = ("/Users/macbook/pythonProjectMeet/home.txt1")

# власне функція
def total_salary(path):
    zp1 = 0
    count = 0
    try:
        with open(path, "rb+") as fl:
            for v in fl:
                try:
                    key, value = v.decode("utf-8").strip().split(",", 1)
                    value = int(value)
                except ValueError:
                    print("Упс! Щось пішло не так з обробкою рядка.")
                    continue
                count += 1
                zp1 += value
            if count == 0:
                return "Файл пошкоджений або порожній"
            ar = zp1 / count
            result = (zp1, ar)
            return result
    except FileNotFoundError:
        return "Файл не знайдено"


