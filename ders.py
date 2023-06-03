eng_menu = {
    'num1': 'Enter the first number: ',
    'num2': 'Enter the second number: ',
    'operation': 'Enter the operation: (+,-,*,/,%,**) -> ',
    'result': 'Result: '
}

ru_menu = {
    'num1': 'Введите первое число: ',
    'num2': 'Введите второе число: ',
    'operation': 'Введите транзакцию: ',
    'result': 'Результат: ',
}

az_menu = {
    'num1': 'Birinci ədədi daxil edin: ',
    'num2': 'Ikinci ədədi daxil edin: ',
    'operation': 'Əməliyyatı daxil edin: (+,-,*,/,%,**) -> ',
    'result': 'Netice: '
}

with open('menu.txt', 'w', encoding='utf8') as f:
    f.write("eng_menu = {\n")
    for key, value in eng_menu.items():
        f.write(f"    '{key}': '{value}',\n")
    f.write("}\n\n")

    f.write("ru_menu = {\n")
    for key, value in ru_menu.items():
        f.write(f"    '{key}': '{value}',\n")
    f.write("}\n\n")

    f.write("az_menu = {\n")
    for key, value in az_menu.items():
        f.write(f"    '{key}': '{value}',\n")
    f.write("}\n")

menu = {}
with open('menu.txt', 'r', encoding="utf8") as f:
    exec(f.read(), menu)

while True:
    language = input("Dil secimi edin: (Az, En, Ru) ->  ")

    if language == 'Az' or language == 'AZ' or language == "":
        num1 = int(input(f"{menu['az_menu']['num1']}"))
        num2 = int(input(f"{menu['az_menu']['num2']}"))
        operation = input(f"{menu['az_menu']['operation']}")

        if operation == '+':
            netice = num1 + num2
            print(f"{menu['az_menu']['result']} {netice}")
        elif operation == '-':
            netice = num1 - num2
            print(f"{menu['az_menu']['result']} {netice}")
        elif operation == '*':
            netice = num1 * num2
            print(f"{menu['az_menu']['result']} {netice}")
        elif operation == '/':
            netice = num1 / num2
            print(f"{menu['az_menu']['result']} {netice}")
        elif operation == '%':
            netice = num1 % num2
            print(f"{menu['az_menu']['result']} {netice}")
        elif operation == '**':
            netice = num1 ** num2
            print(f"{menu['az_menu']['result']} {netice}")
        else:
            print('Bele bir emeliyyat yoxdur')





    elif language == 'EN' or language == 'En':
        num1 = int(input(f"{menu['eng_menu']['num1']}"))
        num2 = int(input(f"{menu['eng_menu']['num2']}"))
        operation = input(f"{menu['eng_menu']['operation']}")

        if operation == '+':
            netice = num1 + num2
            print(f"{menu['eng_menu']['result']} {netice}")
        elif operation == '-':
            netice = num1 - num2
            print(f"{menu['eng_menu']['result']} {netice}")
        elif operation == '*':
            netice = num1 * num2
            print(f"{menu['eng_menu']['result']} {netice}")
        elif operation == '/':
            netice = num1 / num2
            print(f"{menu['eng_menu']['result']} {netice}")
        elif operation == '%':
            netice = num1 % num2
            print(f"{menu['eng_menu']['result']} {netice}")
        elif operation == '**':
            netice = num1 ** num2
            print(f"{menu['eng_menu']['result']} {netice}")
        else:
            print('Unknown operation')


    elif language == 'Ru' or language == 'RU':
        num1 = int(input(f"{menu['ru_menu']['num1']}"))
        num2 = int(input(f"{menu['ru_menu']['num2']}"))
        operation = input(f"{menu['ru_menu']['operation']}")

        if operation == '+':
            netice = num1 + num2
            print(f"{menu['ru_menu']['result']} {netice}")
        elif operation == '-':
            netice = num1 - num2
            print(f"{menu['ru_menu']['result']} {netice}")
        elif operation == '*':
            netice = num1 * num2
            print(f"{menu['ru_menu']['result']} {netice}")
        elif operation == '/':
            netice = num1 / num2
            print(f"{menu['ru_menu']['result']} {netice}")
        elif operation == '%':
            netice = num1 % num2
            print(f"{menu['ru_menu']['result']} {netice}")
        elif operation == '**':
            netice = num1 ** num2
            print(f"{menu['ru_menu']['result']} {netice}")
        else:
            print('Rusca operation yoxdur')
    else:
        print("Dil sehvdir")
    is_continue = input("Davam etmek isteyirsiniz ? (h/y) -> ")
    if is_continue == 'y':
        break