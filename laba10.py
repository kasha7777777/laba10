import json

def z1():
    with open("10.json" , "r", encoding="utf-8") as f:
        s = json.load(f)

    for i in range(len(s.get("products"))):
        k = s.get("products")[i]
        print("Название: " + str(k.get("name")))
        print("Цена: " + str(k.get("price")))
        print("Вес: " + str(k.get("weight")))
        if str(k.get("available")) == str("True"):
            print("В наличии", "\n")
        else:
            print("Нет в наличии", "\n")

def z2():
    with open("10.json" , "r", encoding="utf-8") as f:
        s = json.load(f)

    for i in range(len(s.get("products"))):
        k = s.get("products")[i]
        print("Название: " + str(k.get("name")))
        print("Цена: " + str(k.get("price")))
        print("Вес: " + str(k.get("weight")))
        if str(k.get("available")) == str("True"):
            print("В наличии", "\n")
        else:
            print("Нет в наличии", "\n")

    new = {}
    new["name"] = input("Название: ")
    new["price"] = input("Цена: ")
    new["weight"] = input("Вес: ")
    new["available"] = input("Есть в наличии (True или False)?: ")

    s["products"].append(new)

    with open("10.json", "w", encoding="utf-8") as f:
        json.dump(s,f, indent=4, ensure_ascii=False)


def z3():
    en = open("en-ru.txt" , "r", encoding="utf-8").read().split("\n")
    s = {}
    for i in range(len(en)):
        en[i] = en[i].split(" - ")
        s[en[i][0]] = en[i][1:]
    print(s)

    s1 = {}
    for i in s:
        for r in s[i]:
            r = r.split(", ")
            for j in r:
                if j not in s1:
                    s1[j] = i

    s1 = dict(sorted(s1.items()))
    print(s1)

    s2 = ""
    for i in s1:
        s2 += i + " - " + s1[i] + "\n"

    ru = open("ru-en.txt", "w+", encoding="utf-8")
    ru.write(s2)

z3()