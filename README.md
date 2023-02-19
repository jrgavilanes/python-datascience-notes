# python-datascicence Notas curso

https://codigofacilito.com/videos/crear-arreglos

## Crea entorno e instala librerias

    $ python -m venv venv
    $ . venv/Scripts/activate       // windows
    $ . venv/bin/activate           // linux
    $ pip install ipython numpy     // pip install -r requirements.txt
    $ code .

# Docker

    docker build -t jrg_flask_api .
    docker run -p 4000:8000 jrg_flask_api

## Notas Python

en python es falso:
    False
    None
    ""
    ''
    0
    0.0
    []
    {}
    ()


## Notas Numpy

Funciones básicas de arrays

    import numpy as np

    a = np.array([1,2,3,4,5])
    In [6]: a.dtype
    Out[6]: dtype('int32')

    In [7]: a = np.array([1,2,3,4,5], dtype=float)
    In [8]: a.dtype
    Out[8]: dtype('float64')
    In [9]: a
    Out[9]: array([1., 2., 3., 4., 5.])

    In [13]: a = np.arange(0,10)
    In [14]: a
    Out[14]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    In [15]: a = np.arange(0,10,2)
    In [16]: a
    Out[16]: array([0, 2, 4, 6, 8])

    In [17]: np.zeros(10)
    Out[17]: array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

    In [18]: np.ones(5)
    Out[18]: array([1., 1., 1., 1., 1.])
    In [19]: np.ones(5, dtype=int)
    Out[19]: array([1, 1, 1, 1, 1])

    In [24]: np.empty(10, dtype=int)
    Out[24]: 
    array([         0, 1072693248,          0, 1072693248,          0, 
           1072693248,          0, 1072693248,          0, 1072693248])

    In [26]: np.random.randint(0,100,10)
    Out[26]: array([28, 25, 97, 39, 28, 71, 59, 90, 78,  2])

Obtener elementos del array

    In [27]: x = np.random.randint(0,10,10)

    In [28]: x
    Out[28]: array([9, 1, 3, 3, 8, 5, 7, 5, 6, 7])

    In [29]: x[-1]
    Out[29]: 7

    In [30]: x[0]
    Out[30]: 9

    In [31]: len(x)
    Out[31]: 10

    In [32]: x[-1] = 100

    In [33]: x
    Out[33]: array([  9,   1,   3,   3,   8,   5,   7,   5,   6, 100])


Subarrays, copias y vistas

    In [35]: a = np.random.randint(0,10,20)

    In [36]: a[:5]
    Out[36]: array([9, 2, 0, 4, 6])

    In [37]: a
    Out[37]: array([9, 2, 0, 4, 6, 6, 9, 8, 3, 1, 4, 9, 3, 7, 1, 0, 2, 4, 3, 0])

    In [38]: b = a.copy()

    In [39]: b
    Out[39]: array([9, 2, 0, 4, 6, 6, 9, 8, 3, 1, 4, 9, 3, 7, 1, 0, 2, 4, 3, 0])

    In [40]: b[0]=90

    In [41]: b
    Out[41]: 
    array([90,  2,  0,  4,  6,  6,  9,  8,  3,  1,  4,  9,  3,  7,  1,  0,  2,
            4,  3,  0])

    In [42]: a
    Out[42]: array([9, 2, 0, 4, 6, 6, 9, 8, 3, 1, 4, 9, 3, 7, 1, 0, 2, 4, 3, 0])

    In [43]: c = a.view()

    In [44]: c
    Out[44]: array([9, 2, 0, 4, 6, 6, 9, 8, 3, 1, 4, 9, 3, 7, 1, 0, 2, 4, 3, 0])

    In [45]: c[0]=80

    In [46]: c
    Out[46]: 
    array([80,  2,  0,  4,  6,  6,  9,  8,  3,  1,  4,  9,  3,  7,  1,  0,  2,
            4,  3,  0])

    In [47]: a
    Out[47]: 
    array([80,  2,  0,  4,  6,  6,  9,  8,  3,  1,  4,  9,  3,  7,  1,  0,  2,
            4,  3,  0])

    In [53]: a = np.arange(0,10)
    In [55]: a
    Out[55]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    In [54]: a[0:10:2]
    Out[54]: array([0, 2, 4, 6, 8])


    In [57]: a = np.random.randint(0,100,10)
    In [58]: a
    Out[58]: array([39, 35, 33, 69, 54,  1, 94,  0,  5, 18])

    In [59]: a[[0,5,9]]
    Out[59]: array([39,  1, 18])

    In [61]: b = np.array([1,2,3,4,5])
    In [62]: b
    Out[62]: array([1, 2, 3, 4, 5])

    In [63]: b[[True, False, False, False, True]]
    Out[63]: array([1, 5])

    In [64]: b[[0,-1]]
    Out[64]: array([1, 5])


Vectorizar funciones

    In [69]: b
    Out[69]: array([1, 2, 3, 4, 5])

    In [65]: def cuadrado(x:int) -> int:
        ...:     return x*x
        ...: 

    In [66]: cuadrado(3)
    Out[66]: 9

    In [67]: haz_cuadrado = np.vectorize(cuadrado)

    In [68]: haz_cuadrado(b)
    Out[68]: array([ 1,  4,  9, 16, 25])


Vectorizar con lambdas

    In [69]: b
    Out[69]: array([1, 2, 3, 4, 5])

    In [70]: vector = np.vectorize(lambda valor: valor*valor)

    In [71]: vector(b)
    Out[71]: array([ 1,  4,  9, 16, 25])

Matrices

    In [73]: A = np.array([
        ...: [1,2,3,4,5],
        ...: [10,20,30,40,50],
        ...: [100,200,300,400,500]])

    In [74]: A
    Out[74]: 
    array([[  1,   2,   3,   4,   5],
            [ 10,  20,  30,  40,  50],
            [100, 200, 300, 400, 500]])

    In [75]: A.ndim
    Out[75]: 2

    In [76]: A.shape
    Out[76]: (3, 5)

    In [77]: A[1][1]
    Out[77]: 20

    In [78]: A[0][0]
    Out[78]: 1

    In [79]: A[-1][-1]
    Out[79]: 500

    In [80]: A
    Out[80]: 
    array([[  1,   2,   3,   4,   5],
        [ 10,  20,  30,  40,  50],
        [100, 200, 300, 400, 500]])

    In [81]: A[0,0]
    Out[81]: 1

    In [82]: A[1,1]
    Out[82]: 20

    In [83]: A[2,4]
    Out[83]: 500

    In [87]: A[1,:3]
    Out[87]: array([10, 20, 30])

    In [90]: A[-1,-3:]
    Out[90]: array([300, 400, 500])

    A[:,3]
    Out[91]: array([  4,  40, 400])

    In [92]: A[[0,2],3]
    Out[92]: array([  4, 400])

## Pandas



importación

    import pandas as pd

uso

    usuarios = {
        'id': [1,2,3],
        'username': ['user1','user2','user3'],
        'email': ['email1','email2','email3'],
        'age': [23,10,30],
        'status': [False, True, True]
    }

    usuariosDB = pd.DataFrame(usuarios)
    usuariosDB.set_index('id')
    usuariosDB.query('email.str.contains("2") & age == 10')
    
    Out[61]: 
    id username   email  age  status
    1   2    user2  email2   10    True

    In [70]: usuariosDB.query('email.str.contains("2") or age != 10').head(5)
    Out[70]: 
    id username   email  age  status
    0   1    user1  email1   23   False
    1   2    user2  email2   10    True
    2   3    user3  email3   30    True


***users.csv***
```csv
id;email;password;name;country
1;gisela91@example.com;Cv!705FG#$;Delfina Parejo Fuertes;Kazajstán
2;abrilbenitez@example.com;nM7HjnKx##;Adriana Torralba Urrutia;Estados Unidos de América
3;eliasselena@example.net;u$V0Evlu@x;Rosaura Marti;Maldivas
4;tbernal@example.net;+0OZ*aJq)m;Moisés Madrigal Beltran;Ucrania
5;jorge12@example.net;aJ70R3h*J*;Ruben Ramiro Roura Coello;Maldivas
6;jose-angelgaray@example.org;LT#1Ga*w)%;Marc Granados Ávila;Alemania
7;nicanor99@example.org;kn(0Zw#L0u;Pelayo Valenciano Molins;Rwanda
8;pablo55@example.org;@&8AQE2jsJ;Nicolasa Aguilar;El Salvador
9;cbarriga@example.com;%G4Fg&Icqa;Raquel Belén Lara Pozo;Mozambique
10;nayaraacuna@example.com;j@8C^Wl27Z;Reyes Garay Calvet;Botswana
```

Load CSV

    In [48]: x = pd.read_csv("users.csv", sep=";")


Devuelve listado

    In [41]: [user for user in users.to_dict("records")]
    Out[41]: 
    [{'id': 1,
    'email': 'gisela91@example.com',
    'password': 'Cv!705FG#$',
    'name': 'nu;evo',
    'country': 'Kazajstán'},
    {'id': 2,
    'email': 'abrilbenitez@example.com',
    'password': 'nM7HjnKx##',
    'name': 'Adriana Torralba Urrutia',
    'country': 'Estados Unidos de América'},
    {'id': 3,
    'email': 'eliasselena@example.net',
    'password': 'u$V0Evlu@x',
    'name': 'Rosaura Marti',
    'country': 'Maldivas'},
    {'id': 4,
    'email': 'tbernal@example.net',
    'password': '+0OZ*aJq)m',
    'name': 'Moisés Madrigal Beltran',
    'country': 'Ucrania'},
    {'id': 5,
    'email': 'jorge12@example.net',
    'password': 'aJ70R3h*J*',
    'name': 'Ruben Ramiro Roura Coello',
    'country': 'Maldivas'},
    {'id': 6,
    'email': 'jose-angelgaray@example.org',
    'password': 'LT#1Ga*w)%',
    'name': 'Marc Granados Ávila',
    'country': 'Alemania'},
    {'id': 7,
    'email': 'nicanor99@example.org',
    'password': 'kn(0Zw#L0u',
    'name': 'Pelayo Valenciano Molins',
    'country': 'Rwanda'},
    {'id': 8,
    'email': 'pablo55@example.org',
    'password': '@&8AQE2jsJ',
    'name': 'Nicolasa Aguilar',
    'country': 'El Salvador'},
    {'id': 9,
    'email': 'cbarriga@example.com',
    'password': '%G4Fg&Icqa',
    'name': 'Raquel Belén Lara Pozo',
    'country': 'Mozambique'},
    {'id': 10,
    'email': 'nayaraacuna@example.com',
    'password': 'j@8C^Wl27Z',
    'name': 'Reyes Garay Calvet',
    'country': 'Botswana'},
    {'id': 11,
    'email': 'janrax@',
    'password': nan,
    'name': 'janraxxx',
    'country': 'españa'}]

Selecciona Row por id

    In [49]: x.query('id == 1')['name']
    Out[49]: 
    0    Delfina Parejo Fuertes
    Name: name, dtype: object

    # o con 

    In [86]: x.loc[x['id']==1,'name'][0]
    Out[86]: 'Delfina Parejo Fuertes'

Actualiza campo

    In [54]: x.loc[x['id']==1,'name']='nuevo'

    In [55]: x
    Out[55]: 
    id                           email  password                         name                    country
    0   1         gisela91@example.com  Cv!705FG#$                      nuevo                  Kazajstán
    1   2     abrilbenitez@example.com  nM7HjnKx##   Adriana Torralba Urrutia  Estados Unidos de América
    2   3      eliasselena@example.net  u$V0Evlu@x              Rosaura Marti                   Maldivas
    3   4          tbernal@example.net  +0OZ*aJq)m    Moisés Madrigal Beltran                    Ucrania
    4   5          jorge12@example.net  aJ70R3h*J*  Ruben Ramiro Roura Coello                   Maldivas
    5   6  jose-angelgaray@example.org  LT#1Ga*w)%        Marc Granados Ávila                   Alemania
    6   7        nicanor99@example.org  kn(0Zw#L0u   Pelayo Valenciano Molins                     Rwanda

Extrae registro

    In [105]: r = x.loc[x['id']==1,['name','email']]

    In [106]: r
    Out[106]: 
                        name                 email
    0  Delfina Parejo Fuertes  gisela91@example.com

    In [107]: name = r['name'][0]

    In [108]: name
    Out[108]: 'Delfina Parejo Fuertes'

    In [109]: email = r['email'][0]

    In [110]: email
    Out[110]: 'gisela91@example.com'

Elimina registro

    In [115]: x.drop(x.index[x['id']==1])
    Out[115]: 
    id                        email    password                       name                    country
    1   2     abrilbenitez@example.com  nM7HjnKx##   Adriana Torralba Urrutia  Estados Unidos de América
    2   3      eliasselena@example.net  u$V0Evlu@x              Rosaura Marti                   Maldivas
    3   4          tbernal@example.net  +0OZ*aJq)m    Moisés Madrigal Beltran                    Ucrania
    4   5          jorge12@example.net  aJ70R3h*J*  Ruben Ramiro Roura Coello                   Maldivas
    5   6  jose-angelgaray@example.org  LT#1Ga*w)%        Marc Granados Ávila                   Alemania
    6   7        nicanor99@example.org  kn(0Zw#L0u   Pelayo Valenciano Molins                     Rwanda
    7   8          pablo55@example.org  @&8AQE2jsJ           Nicolasa Aguilar                El Salvador
    8   9         cbarriga@example.com  %G4Fg&Icqa     Raquel Belén Lara Pozo                 Mozambique
    9  10      nayaraacuna@example.com  j@8C^Wl27Z         Reyes Garay Calvet                   Botswana

Añade registro

    users = users.append({"id": 11, "email": "janrax@", "name": "janraxxx", "country": "españa"}, ignore_index=True)

    In [39]: users
    Out[39]: 
        id                        email    password                       name                    country
    0    1         gisela91@example.com  Cv!705FG#$                     nu;evo                  Kazajstán
    1    2     abrilbenitez@example.com  nM7HjnKx##   Adriana Torralba Urrutia  Estados Unidos de América
    2    3      eliasselena@example.net  u$V0Evlu@x              Rosaura Marti                   Maldivas
    3    4          tbernal@example.net  +0OZ*aJq)m    Moisés Madrigal Beltran                    Ucrania
    4    5          jorge12@example.net  aJ70R3h*J*  Ruben Ramiro Roura Coello                   Maldivas
    5    6  jose-angelgaray@example.org  LT#1Ga*w)%        Marc Granados Ávila                   Alemania
    6    7        nicanor99@example.org  kn(0Zw#L0u   Pelayo Valenciano Molins                     Rwanda
    7    8          pablo55@example.org  @&8AQE2jsJ           Nicolasa Aguilar                El Salvador
    8    9         cbarriga@example.com  %G4Fg&Icqa     Raquel Belén Lara Pozo                 Mozambique
    9   10      nayaraacuna@example.com  j@8C^Wl27Z         Reyes Garay Calvet                   Botswana
    10  11                      janrax@         NaN                   janraxxx                     españa

Guarda dataframe y exporta a csv

    In [10]: x.to_csv("users.csv", sep=";", index=False)



## Flask

https://www.youtube.com/watch?v=Esdj9wlBOaI&t=1551s

    pip install Flask


## JSON to CSV y viceversa

    import pandas as pd
    import json
    
    # users = pd.read_csv("users.csv", sep=";", index_col="id")
    users = pd.read_csv("users.csv", sep=";")
    
    dict_users = users.to_dict("records")
    
    users_db = {}
    
    for x in dict_users:
        users_db[x["id"]] = x
    
    print(users_db)
    
    users_db_json = json.dumps(list(users_db.values()))
    
    # In [76]: list(users_db.keys())
    # Out[76]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
    print("pues")
    print(x)
    print("y")
    csv_json = pd.read_json(users_db_json)
    csv_json.to_csv("users.csv", sep=";", index=False)


 

