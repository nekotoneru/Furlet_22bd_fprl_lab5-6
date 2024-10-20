import datetime

class User:
    def __init__(self, name=None, phone=None, email=None):
        self.__id = datetime.datetime.now()
        self.__name = name
        self.__phone = phone
        self.__email = email

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_email(self):
        return self.__email
    
dbase = []

def new_user(dbase):
    name = input("введіть ім'я: ")
    phone = input("введіть номер телефону: ")
    email = input("введіть пошту: ")
    user = User(name, phone, email)
    dbase.append(user)
    print(f"користувача {name} додано")

def user_id(dbase):
    user_id = input("введіть ID користувача: ")
    for user in dbase:
        if str(user.get_id()) == user_id:
            print(f"ім'я: {user.get_name()}, ттелефон: {user.get_phone()}, пошта: {user.get_email()}")
            return
    print("користувача не знайдено")

def user_name(dbase):
    name = input("введіть ім'я для пошуку: ")
    filtered_users = [user for user in dbase if name.lower() in user.get_name().lower()]
    filtered_users.sort(key=lambda user: user.get_name())
    for user in filtered_users:
        print(f"ID: {user.get_id()}, ім'я: {user.get_name()}")

def all(dbase):
    dbase.sort(key=lambda user: user.get_name())
    for user in dbase:
        print(f"ID: {user.get_id()}, ім'я: {user.get_name()}")

def del_user(dbase, user_id):
    for user in dbase:
        if str(user.get_id()) == user_id:
            dbase.remove(user)
            print(f"користувача з ID {user_id} видалено")
            return
    print(f"користувача з ID {user_id} не знайдено")

def del_user_id(dbase):
    user_id = input("введіть ID: ")
    del_user(dbase, user_id)

def del_user_ids(dbase):
    user_ids = input("введіть IDs через кому: ").split(',')
    for user_id in user_ids:
        del_user(dbase, user_id)

def del_user_range(dbase):
    user_ids = input("введіть IDs через кому: ").split(',')
    deleted = 0
    for user in dbase:
        if (user.get_id() >= datetime.datetime.strptime(user_ids[0], '%Y-%m-%d %H:%M:%S.%f')) and (user.get_id() <= datetime.datetime.strptime(user_ids[1], '%Y-%m-%d %H:%M:%S.%f')):
            del_user(dbase, str(user.get_id()))
            deleted += 1
    print(f"видалено користувачів: {deleted}")


while True:
    command = input("введіть команду (new_user, user_id, user_name, all, del_user_id, del_user_ids, del_user_range, exit): ")
        
    if command == "new_user":
        new_user(dbase)
    elif command == "user_id":
        user_id(dbase)
    elif command == "user_name":
        user_name(dbase)
    elif command == "all":
        all(dbase)
    elif command == "del_user_id":
        del_user_id(dbase)
    elif command == "del_user_ids":
        del_user_ids(dbase)
    elif command == "del_user_range":
        del_user_range(dbase)
    elif command == "exit":
        print("вихід з програми")
        break
    else:
        print("невідома команда")