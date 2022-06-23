# Добавить сумму транзакции, если add = True и среди продуктов есть "Хлеб"
# Должно выйти 172



transactions_homework = [
    {
        "add":True,
        "amount":69,
        "products":[
            "Хлеб",
            "Масло",
            "Сок",
        ]
    },
    {
        "add":True,
        "amount":30,
        "products":[
            "Сок",
        ]
    },
    {
        "add":True,
        "amount":94,
        "products":[
            "Мука",
            "Хлеб",
            "Масло",
        ]
    },
    {
        "add":False,
        "amount":24,
        "products":[
            "Конфеты",
            "Хлеб",
        ]
    },
    {
        "add":True,
        "amount":9,
        "products":[
            "Хлеб",
            "Шоколад",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":91,
        "products":[
            "Апельсин",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":84,
        "products":[
            "Помидоры",
            "Сок",
        ]
    },
    {
        "add":False,
        "amount":45,
        "products":[
            "Хлеб",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":9,
        "products":[
            "Лимон",
            "Сок",
        ]
    },
]

# ПЕРШИЙ ВАРІАНТ
sum=0
q=0
for i in transactions_homework:
    a = False
    products=list(transactions_homework[q]["products"])
    for product in products:
        if product=="Хлеб":
            a=True
    if transactions_homework[q]["add"]==True and a==True:
        sum+=transactions_homework[q]["amount"]
    q+=1
print("sum:",sum)

#ДРУГИЙ ВАРІАНТ

total=0
for transaction in transactions_homework:
    if transaction["add"] and "Хлеб" in transaction["products"]:
        total+=transaction["amount"]
print("total",total)








