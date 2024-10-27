#dictionary key and value

dictionary= {
    'bug':'problem of code',
    'complier':'complies the code',
    123:'just numbers',
    True:'bool'
    }

#it can has more than one type of key

# print(dictionary[True])
# dictionary['add item'] = 'like this'
# print(dictionary)


# nested list

countries_and_cities = {
    "Türkiye": ["İstanbul", "Ankara", "İzmir", "Antalya"],
    "Amerika": ["New York", "Los Angeles", "Chicago", "Miami"],
    "Japonya": ["Tokyo", "Osaka", "Kyoto", "Hiroşima"],
    "Fransa": ["Paris", "Marsilya", "Lyon", "Nice"],
    "Brezilya": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"]
    }

# print(countries_and_cities)

# print(countries_and_cities["Japonya"][2])

# nested=['a','b','c',[5,7]]
# print(nested)

# print(nested[3][1])


countries= {
    "Türkiye" : {
        'cities': ['istanbul', 'ankara'],
        'total visit': 12
    },
    "Germany" : {
        'cities': ['berlin', 'dortmund'],
        'total visit': 2
    } 
      }

print(countries["Türkiye"]['cities'][1])