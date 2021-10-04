import json

data = '{"var1": "harry", "var2":56}'

parsed = json.loads(data)
print(parsed['var1'])

# data2 = {"channel_name": "Chill_Out",
#          "Cars": ["BMW", "Audi a8", "ferrari"],
#          "fridge": ("loki", "Aalu", "pasta"),
#          "isbad": False
# }
# jscomp = json.dumps(data2)
# print(jscomp)
