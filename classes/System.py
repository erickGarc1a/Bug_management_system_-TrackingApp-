from classes.Bug import Bug
from classes.Users import User, Admin
from classes.Validation import Validation as Val
from classes.Data import Data

# Main class to control de system connecting all others classes


class System:
    Bugs_List = []
    Users_List = []
    data = Data()
    id_user_global = 0

    def __init__(self):
        self.Users_List.append(Admin("admin", "password", "admin@admin", "0000000000", self.id_user_global))
        self.Bugs_List.append(Bug("sampleBug", "sampleProject", "minor", "0", "unresolved", "admin", "12/12/1212"))
        self.id_user_global += 1

    def save_data(self):
        self.data.check_database()
        for bug in self.Bugs_List:
            sql = "INSERT INTO Bugs VALUES ({}, {}, {}, {}, {}, {}, {})".format(bug.get_title(), bug.get_project(),
                                                                                bug.get_btype(), bug.get_priority(),
                                                                                bug.get_status(), bug.get_author(),
                                                                                bug.get_date())
            self.data.send_query(sql)
        for user in self.Users_List:
            sql = "INSERT INTO Users VALUES ({}, {}, {}, {}, {}, {})".format(user.get_name(), user.get_password(),
                                                                             user.get_email(), user.get_phone(),
                                                                             user.get_id_user(), user.get_admin())
            self.data.send_query(sql)

    def retrieve_data(self):
        self.data.check_database()
        sql_bugs = "SELECT * FROM Bugs"
        bugs_table = self.data.send_query(sql_bugs)
        sql_users = "SELECT * FROM Users"
        users_table = self.data.send_query(sql_users)
        if len(bugs_table) > 0:
            for bug in bugs_table:
                self.Bugs_List.append(Bug(bug['title'], bug['project'], bug['btype'], bug['priority'], bug['status'],
                                          bug['author'], bug['_date_']))
        if len(users_table) > 0:
            for user in users_table:
                if user['admin']:
                    self.Bugs_List.append(Admin(user['name'], user['password'], user['email'], user['phone'],
                                                user['id_user']))
                else:
                    self.Bugs_List.append(User(user['name'], user['password'], user['email'], user['phone'],
                                               user['id_user']))

    def start(self):
        print("---------------------HOME---------------------")
        while 1:
            try:
                condition = int(input("\nChoose an option:  \n 1. login \n 2. register \n 3. exit \n "))
            except ValueError:
                condition = 0
            if condition == 1:
                System.login(self)
            elif condition == 2:
                System.register(self)
            elif condition == 3:
                # exit
                print("Goodbye, have a nice day!\n")
                self.data.close_connect()
                break
            else:
                print("Invalid!!! Choose from the given options.\n")

    def add_bug(self, user):
        print("--------------Adding new bug to track---------------")
        title = ""
        flag = True
        while flag:
            title = input("Input title : \n")
            if Val.check_text(title):
                flag = False
            else:
                print("\nInvalid title\n")

        project = ""
        flag = True
        while flag:
            project = input("Input project name : \n")
            if Val.check_text(project):
                flag = False
            else:
                print("\nInvalid project name\n")

        btype = ""
        flag = True
        while flag:
            btype = input("Input type of bug : \n")
            if Val.check_text(btype):
                flag = False
            else:
                print("\nInvalid bug type\n")

        priority = ""
        flag = True
        while flag:
            priority = input("Input priority : \n")
            if Val.check_text(priority):
                flag = False
            else:
                print("\nInvalid priority\n")

        status = ""
        flag = True
        while flag:
            status = input("Input status : \n")
            if Val.check_text(status):
                flag = False
            else:
                print("\nInvalid status\n")

        date = ""
        flag = True
        while flag:
            date = input("Input date : \n")
            if Val.check_date(date):
                flag = False
            else:
                print("\nInvalid date\n")
        print(user.get_name())
        return self.Bugs_List.append(Bug(title, project, btype, priority, status, user.get_name(), date))

    def search_bugs(self):
        print("---------------------Searching bugs---------------------")
        while 1:
            try:
                condition = int(input("\nSearch by :  \n 1. title \n 2. project \n 3. btype \n 4. priority \n "
                                      "5. status \n 6. author \n 7. date \n 8. Cancel search \n"))
            except ValueError:
                condition = 0
            if condition == 1:
                input_b = str(input("Write the title you want to find : \n"))
                Bug.search_by(self.Bugs_List, search=0, title=input_b)
                break
            elif condition == 2:
                input_b = str(input("Write the project title you want to search by : \n"))
                Bug.search_by(self.Bugs_List, search=1, project=input_b)
                break
            elif condition == 3:
                input_b = str(input("Write the bug type you want to search by : \n"))
                Bug.search_by(self.Bugs_List, search=2, btype=input_b)
                break
            elif condition == 4:
                input_b = str(input("Write the bug priority you want to search by : \n"))
                Bug.search_by(self.Bugs_List, search=3, priority=input_b)
                break
            elif condition == 5:
                input_b = str(input("Write the bug status you want to search by : \n"))
                Bug.search_by(self.Bugs_List, search=5, status=input_b)
                break
            elif condition == 6:
                input_b = str(input("Write the author you want to search by : \n"))
                Bug.show_by(self.Bugs_List, 1, input_b)
                break
            elif condition == 7:
                input_b = str(input("Write the date you want to search by : \n"))
                Bug.search_by(self.Bugs_List, search=4, date=input_b)
                break
            elif condition == 8:
                # exit
                print("Canceling searching! \n")
                break
            else:
                print("Invalid!!! Choose from the given options.\n")

    def update_bug_author(self, new_author, former_author):
        print("--------------Updating bug author---------------")
        print("Author : " + former_author + "\n\n")
        for count in range(len(self.Bugs_List)):
            if self.Bugs_List[count].author == former_author:
                self.Bugs_List[count].set_author(new_author)

    def update_user(self, user):
        print("--------------Updating user information---------------")
        while 1:
            try:
                condition = int(input("\nChoose what parameter to update from this account:  "
                                      "\n 1. name \n 2. email \n 3. phone \n 4. password \n 5. exit \n"))
            except ValueError:
                condition = 0
            if condition == 1:
                print("\n---------updating user information----------\n")
                flag = True
                name = ""
                while flag:
                    name = input("Input new name of user : \n")
                    if Val.check_name(name):
                        flag = False
                    else:
                        print("\nInvalid name\n")
                System.update_bug_author(self, name, user.get_name())
                user.set_name(name)
            elif condition == 2:
                print("\n---------updating user information----------\n")
                flag = True
                email = ""
                while flag:
                    email = input("Input new email of user (.@. format): \n")
                    if Val.check_email(email):
                        flag = False
                    else:
                        print("\nInvalid email\n")
                user.set_email(email)
            elif condition == 3:
                print("\n---------updating user information----------\n")
                flag = True
                phone = ""
                while flag:
                    phone = input("Input new phone of user (10 digits): \n")
                    if Val.check_phone(phone):
                        flag = False
                    else:
                        print("\nInvalid phone for user\n")
                user.set_phone(phone)
            elif condition == 4:
                print("\n---------updating user information----------\n")
                flag = True
                password = ""
                while flag:
                    password = input("Input new password of user (alphanumeric format): \n")
                    if Val.check_password(password):
                        flag = False
                    else:
                        print("\nInvalid password\n")
                user.set_password(password)
            elif condition == 5:
                # exit
                print("No update!!!\n")
                break
            else:
                print("Invalid!!! Choose from the given options.\n")

    def user_actions(self, user):
        if user.admin:
            while 1:
                print("\nWelcome user " + user.get_name() + "\n")
                try:
                    condition = int(input("\nChoose an option:  \n 1. Add bug \n 2. See all bugs \n 3. See all "
                                          "my bugs \n 4. Search a bug \n 5. Delete one of my bugs \n 6. See all users "
                                          "\n 7. Update user data \n 8. Remove user \n 9. See my data "
                                          "\n 10. Update my data \n 11. exit \n "))
                except ValueError:
                    condition = 0
                if condition == 1:  # add bug
                    System.add_bug(self, user)
                elif condition == 2:  # See all bugs
                    Bug.show_by(self.Bugs_List)
                elif condition == 3:  # See all current user bugs
                    Bug.show_by(self.Bugs_List, 1, user.name)
                elif condition == 4:  # Search a bug
                    System.search_bugs(self)
                elif condition == 5:  # Delete one of current user bugs
                    title_bug = str(input("Write the title of the bug you want to erase (Case sensitive): \n"))
                    Bug.delete_bug(self.Users_List, user.name, title_bug)
                elif condition == 6:  # See all users
                    print("---------------Seeing all users---------------")
                    user.print_all(self.Users_List)
                elif condition == 7:  # Update a user data
                    print("---------------Updating user---------------")
                    input_n = input("Write user's name to update : \n")
                    input_e = input("Write user's email to update : \n")
                    index_user = user.search_user(self.Users_List, input_e, input_n)
                    if len(index_user) == 1:
                        System.update_user(self, self.Users_List[index_user[0]])
                    else:
                        print("Update of given user not possible at the moment or does not exist ...")
                elif condition == 8:  # Remove user
                    print("---------------Removing user---------------")
                    input_n = input("Write user's name to delete : \n")
                    input_e = input("Write user's email to delete : \n")
                    user.remove_user(self.Users_List, input_e, input_n)
                elif condition == 9:  # See current user data
                    print("---------------User " + user.name + " data---------------")
                    user.print_user()
                elif condition == 10:  # Update current user data
                    System.update_user(self, user)
                elif condition == 11:  # Exit
                    print("Log out!!!")
                    break
                else:
                    print("Invalid!!! Choose from the given options.")
        else:
            while 1:
                print("Welcome user " + user.get_name())
                try:
                    condition = int(input("\nChoose an option:  \n 1. Add bug \n 2. See all bugs \n 3. See all "
                                          "my bugs \n 4. Search a bug \n 5. Delete one of my bugs \n 6. See my data \n"
                                          "7. Update my data \n 8. exit \n "))
                except ValueError:
                    condition = 0
                if condition == 1:  # add bug
                    System.add_bug(self, user)
                elif condition == 2:  # See all bugs
                    Bug.show_by(self.Bugs_List)
                elif condition == 3:  # See all current user bugs
                    Bug.show_by(self.Bugs_List, 1, user.name)
                elif condition == 4:  # Search a bug
                    System.search_bugs(self)
                elif condition == 5:  # Delete one of my bugs
                    title_bug = str(input("Write the title of the bug you want to erase (Case sensitive): \n"))
                    Bug.delete_bug(self.Bugs_List, user.name, title_bug)
                elif condition == 6:  # See current user data
                    print("---------------User " + user.name + " data---------------")
                    user.print_user()
                elif condition == 7:  # Update current user data
                    System.update_user(self, user)
                elif condition == 8:  # Exit
                    print("Log out!!!")
                    break
                else:
                    print("Invalid!!! Choose from the given options.")

    def login(self):
        while 1:
            print("Login with you username and password:")
            name_user = str(input("Username : "))
            password_user = str(input("Password : "))
            log, current_user = User.login_for_user(self.Users_List, name_user, password_user)
            if log:
                System.user_actions(self, current_user)
                break
            else:
                print("\nUser not found or invalid password\n")
                break
        pass

    def register(self):
        print("---------------------Register---------------------")
        name = ""
        flag = True
        while flag:
            name = input("Input name of user : \n")
            if Val.check_name(name):
                flag = False
            else:
                print("\nInvalid name\n")

        email = ""
        flag = True
        while flag:
            email = input("Input email of user (.@. format): \n")
            if Val.check_email(email):
                flag = False
            else:
                print("\nInvalid email\n")

        phone = ""
        flag = True
        while flag:
            phone = input("Input phone of user (10 digits): \n")
            if Val.check_phone(phone):
                flag = False
            else:
                print("\nInvalid phone for user\n")

        password = ""
        flag = True
        while flag:
            password = input("Input password of user (alphanumeric format): \n")
            if Val.check_password(password):
                flag = False
            else:
                print("\nInvalid password\n")

        self.id_user_global += 1
        print("Welcome to Bug Management System!!! \n")
        return self.Users_List.append(User(name, password, email, phone, self.id_user_global))
