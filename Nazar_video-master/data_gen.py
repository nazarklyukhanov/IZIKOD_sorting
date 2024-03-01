import random
from data_driver import DataDriver

# chars - alphabet + digits + special characters
chars = ["a", "b", "c", "d", "e", "f", "g", "h",
         "i", "j", "k", "l", "m", "n", "o", "p",
         "q", "r", "s", "t", "u", "v", "w", "x",
         "y", "z", "A", "B", "C", "D", "E", "F",
         "G", "H", "I", "J", "K", "L", "M", "N",
         "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z", "0", "1", "2", "3",
         "4", "5", "6", "7", "8", "9", "!", "@",
         "#", "$", "%", "^", "&", "*", "(", ")",
         "_", "+", "-", "=", "{", "}", "[", "]",
         "|", ":", ";", "'", "<", ">", ",", ".", ]


# generate random string of length n
def gen_string(n):
    return ''.join(random.choice(chars) for i in range(n))


def gen_data(n):
    data = []
    for i in range(n):
        data.append(gen_string(random.randint(8, 12)))
        print(data[-1], file=open("data.txt", "a"))
    write_db(data)


def write_db(data):
    data_driver = DataDriver()
    for i in range(len(data)):
        data_driver.insert_data(data[i])
    data_driver.close_connection()


def read_db():
    data_driver = DataDriver()
    data = data_driver.get_data()
    data = [i[1] for i in data]
    data_driver.close_connection()
    return data

