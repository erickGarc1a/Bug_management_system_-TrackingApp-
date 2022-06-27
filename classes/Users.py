
class User:
    def __init__(self, name, password, email, phone, id_user):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.id_user = id_user
        self.admin = False

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_id_user(self):
        return self.id_user

    def get_admin(self):
        return self.admin

    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def print_user(self):
        print("User name : " + self.name + "\n" +
              "Email : " + self.email + "\n" +
              "Phone : " + self.phone + "\n" +
              "\n")

    @classmethod
    def login_for_user(cls, users_list, name, password):
        count = 0
        while count < len(users_list):
            if users_list[count].name == name:
                if users_list[count].password == password:
                    return True, users_list[count]
            count += 1
        return False, False


class Admin(User):

    def __init__(self, name, password, email, phone, id_user):
        super().__init__(name, password, email, phone, id_user)
        self.admin = True

    @classmethod
    def remove_user(cls, users_list, email, name):
        count = 0
        index_store = []
        while count < len(users_list):
            if users_list[count].name == name:
                if users_list[count].email == email:
                    index_store.append(count)
            count += 1
        print("------------------User to be deleted-----------------\n")
        if index_store:
            for index in index_store:
                users_list[index].print_user()
                del(users_list[index])
                print("-----------------User deleted-----------------\n")
        else:
            print("Users not found!!!!!!!")
            return False
        return True

    @classmethod
    def search_user(cls, users_list, email, name):
        count = 0
        index_store = []
        for count in range(len(users_list)):
            if users_list[count].name == name:
                if users_list[count].email == email:
                    index_store.append(count)
        return index_store

    @classmethod
    def print_all(cls, users_list):
        for count in range(len(users_list)):
            users_list[count].print_user()
