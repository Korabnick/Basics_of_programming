import csv

class House:
    def __init__(self, nm, fls, hght, wdth):
        self.nm = nm
        self.fls = fls
        self.hght = hght
        self.wdth = wdth
    
    def to_tuple(self):
        return self.nm, self.fls, self.hght, self.wdth
    
    @classmethod
    def from_tuple(cls, data):
        return cls(*data)

def houses():
    print('\nВведите "0/создать/create - Чтобы создать дом"'
          '\nИли "1/посмотреть/see - Чтобы увидеть уже существующие дома"')
    inp = input('—> ').lower()
    gen, look = ['0', 'создать', 'create',], ['1', 'посмотреть', 'see']
    if inp in gen:
        print('Создание дома...\nВведите имя дома: ', end='')
        name = input()
        print('Введите кол-во этажей: ', end='')
        floors = input()
        print('Введите высоту дома: ', end='')
        height = input()
        print('Введите ширину дома: ', end='')
        width = input()
        try:        
            if (int(floors) and int(height) and int(width)) > 0:
                hs = House(name, int(floors), int(height), int(width))
                with open('houses', 'a', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow([hs.nm, hs.fls, hs.hght, hs.wdth])
                print('—> Дом успешно создан!')
            else:
                print('—> Ошибка! Высота, ширина и кол-во этажей должны быть больше нуля!')
        except ValueError:
            print('—> Ошибка! Введенные данные высоты, ширины и кол-ва этажей должны быть числами!')
    elif inp in look:
        with open('houses', 'rt') as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                print('Name: {0}\nFloors: {1}\nHeight: {2}\nWidth: {3}\n'.format(line[0],line[1],line[2],line[3]))
        with open('houses', 'rt') as file:
            csv_reader = csv.reader(file)
            houses_csv = [House.from_tuple(row) for row in csv_reader]
            print('Количество домов на данный момент:', len(houses_csv))
            
houses()