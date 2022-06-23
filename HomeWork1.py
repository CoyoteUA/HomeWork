dict_homework = {
    "key1":{
        "d":44,
        "f":None,
        "s":{
            8:44,
            9:None,
            10:{"mm":["s", "GET ME", 7]},
        },
    },
    "key2":{
        "fff1":44,
        "f":None,
    },
}
a=dict_homework["key1"]["s"][10]["mm"]
x=a[1]
print(x)