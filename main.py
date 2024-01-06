#hello

try:
    user_select = int(input("Введіть число від 1 до 7:"))
    match userselect:
        case 1:
            print("Понеділок")
        case 2:
            print("Вівторок")
        case 3:
            print("Середа")
        case 4:
            print("Четверг")
        case 5:
            print("П'ятниця")
        case 6:
            print("Субота")
        case 7:
            print("Неділя")
        case :
            print("Введене число не входить в діапазон від 1 до 7.")
except ValueError:
    print("Введіть коректне число.")