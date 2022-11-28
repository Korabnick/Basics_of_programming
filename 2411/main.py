import xml.etree.ElementTree as et

def houses():
    print('\nВведите "0/создать/create - Чтобы создать дом"'
          '\nИли "1/посмотреть/see - Чтобы увидеть уже существующие дома"')
    inp = input('—> ').lower()
    gen, look = ['0', 'создать', 'create'], ['1', 'посмотреть', 'see']
    tree = et.ElementTree(file='houses.xml')
    root = tree.getroot()
    if inp in gen:
        print('Создание дома...\nВведите имя дома: ', end='')
        nm = input()
        print('Введите кол-во этажей: ', end='')
        fls = input()
        print('Введите высоту дома: ', end='')
        hgt = input()
        print('Введите ширину дома: ', end='')
        wth = input()
        try:        
            if (int(fls) and int(hgt) and int(wth)) > 0:
                house = root[0]
                name, flrs, hght, wdth = et.Element("Name"), et.Element("Floors"), et.Element("Height"), et.Element("Width")
                name.text, flrs.text, hght.text, wdth.text = nm, fls, hgt, wth
                house.append(name)
                house.append(flrs)
                house.append(hght)
                house.append(wdth)
                tree.write('houses.xml')
                print('—> Дом успешно создан!')
            else:
                print('—> Ошибка! Высота, ширина и кол-во этажей должны быть больше нуля!')
        except ValueError:
            print('—> Ошибка! Введенные данные высоты, ширины и кол-ва этажей должны быть числами!')
    elif inp in look:
        counter = 0
        for child in root[0]:
            if "Width" in child.tag:
                print(child.tag + ":", child.text, '\n')
                counter += 1
            else:
                print(child.tag + ":", child.text)
        print('Кол-во домов = {0}'.format(counter))
    else:
        print('—> Данной команды не существует')
    
houses()