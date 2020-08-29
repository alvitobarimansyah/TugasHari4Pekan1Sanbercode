# soal no 1

Jenis data apa saja yang bisa ada di dalam List?

- string
- integer
- float
- boolean

# soal no 2

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
a[1:5]

# soal no 3

a = [1.32, 22.1, 2.34]
b = ['1', '13b', 'aa1']
c = [3, 40, 100]

x = [a,c,b]

print(x)

# soal no 4

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

b = a[1][1:]

print(b)

# soal no 5

p = [0, 5, 2, 10, 4, 9]

print(sorted(p, reverse=False))
print(max(p))

# soal no 6

a = [1, 3, 5]
b = [5, 1, 3]

c = b + a

print(c)

# soal no 7

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

a[0][2] = 10
a[1][0] = 11

print(a)

# soal no 8

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

del areas[8:10]

print(areas)

# soal no 9

S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x %2 == 0]

print(T)

# soal no 10

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

print(europe.keys())
print(europe['france'])

# soal no 11

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

europe.update({'itali':'roma'})

print('itali' in europe)

# soal no 12

europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

europe['germany'] = 'berlin'

del europe['australia']

print(europe)

# soal no 13

country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } 
         }

print(country['germany']['population'])
country.update({'indonesia': {'capital':'jakarta', 'population':250}})
print(country)

# soal no 14

country = { 
           'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 },
           'indonesia' : {'capital':'jakarta', 'population':250}
         }

for x,y in country.items():
    print('Ibukota ' +  x  +  ' adalah ' + y['capital'])

# tugas tambahan soal no 1

def remove_duplicate(obj_list):
    new_list = list(dict.fromkeys(obj_list))
    return new_list

def remove_duplicate_with_set(obj_list):
    new_list = list(set(obj_list))
    return new_list

obj_list = [1, 2, 4, 6, 2, 1, 4, 5, 7, 8, 6]
print(remove_duplicate(obj_list))
print(remove_duplicate_with_set(obj_list))

# tugas tambahan soal no 2

from datetime import datetime
import random

nama  = "Alvito Barimansyah"
tanggal = datetime.now().day
default = "maaf, aku tidak tahu jawaban dari pertanyaanmu"

jawaban_nama = [
      "nama saya  {0}".format(nama),
      "orang-orang memanggil saya {0}".format(nama),
      "panggil saja saya {0}".format(nama)
   ]

jawaban_tanggal = [
      "hari ini tanggal {0}".format(tanggal),
      "ya ampun masa tidak tahu, hari ini tanggal".format(tanggal)
    ]

pertanyaan = {
  "nama kamu siapa?": jawaban_nama,
  "kamu siapa?" : jawaban_nama,
  "tanggal berapa hari ini?": jawaban_tanggal,
  "hari ini tanggal berapa?" : jawaban_tanggal,
  "default": default
}

statement =  [
                  'ceritakan lebih banyak!',
                  'kenapa kamu berpikir begitu?',
                  'sudah berapa lama kamu merasa seperti ini?',
                  'Itu sangat menarik!',
                  'oh wow!',
                  ':)'
              ]

responses = {
    'pertanyaan' : pertanyaan,
    'statement' : statement
}

def chatbot(message):
    if 'pertanyaan' in message:
        if message in pertanyaan:
            return random.choice(responses['pertanyaan'][message])
        elif message not in pertanyaan:
            return responses['pertanyaan']['default']
    else:
        return random.choice(responses['statement'])

print(chatbot('Selamat Pagi'))
print(chatbot('Mau bermain bersamaku?'))
print(chatbot('nama kamu siapa?'))
print(chatbot('hari ini tanggal berapa?'))