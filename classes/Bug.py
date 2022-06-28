from classes.Data import Data


class Bug:
    def __init__(self, title, project, btype, priority, status, author, date):
        self.title = title
        self.project = project
        self.btype = btype
        self.priority = priority
        self.status = status
        self.author = author
        self.date = date

    def get_title(self):
        return self.title

    def get_project(self):
        return self.project

    def get_btype(self):
        return self.btype

    def get_priority(self):
        return self.priority

    def get_status(self):
        return self.status

    def get_author(self):
        return self.author

    def get_date(self):
        return self.date

    def set_title(self, title):
        self.title = title

    def set_project(self, project):
        self.project = project

    def set_btype(self, btype):
        self.btype = btype

    def set_priority(self, priority):
        self.priority = priority

    def set_status(self, status):
        self.status = status

    def set_author(self, author):
        self.author = author

    def set_date(self, date):
        self.date = date

    def print_bug(self):
        print("Title : " + self.title + "\n" +
              "Project title : " + self.project + "\n" +
              "Bug type : " + self.btype + "\n" +
              "Priority : " + self.priority + "\n" +
              "Status : " + self.status + "\n" +
              "Author : " + self.author + "\n" +
              "Date : " + self.date + "\n" +
              "\n")

    @classmethod
    def print_by_index(cls, bugs_list, index_store):
        for index in index_store:
            bugs_list[index].print_bug()

    @classmethod
    def search_by(cls, bugs_list, search=0, title=None, btype=None, project=None, priority=None, status=None,
                  date=None):
        index_store = []
        if search == 0:  # search by title
            if title is not None:
                print("-------------Searching bugs-----------------\n")
                print("Title : " + title + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].title == title:
                        index_store.append(count)
                Bug.print_by_index(bugs_list, index_store)
                return index_store
            else:
                print("You did not give a title!")
        elif search == 1:  # search by type
            if project is not None:
                print("-------------Searching bugs-----------------\n")
                print("Project : " + project + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].project == project:
                        index_store.append(count)
                Bug.print_by_index(bugs_list, index_store)
                return index_store
            else:
                print("You did not give a type!")
        elif search == 2:  # search by project name
            if btype is not None:
                print("-------------Searching bugs-----------------\n")
                print("Type : " + btype + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].btype == btype:
                        index_store.append(count)
                Bug.print_by_index(bugs_list, index_store)
                return index_store
            else:
                print("You did not give a project title!")
        elif search == 3:  # search by priority
            if priority is not None:
                print("-------------Searching bugs-----------------\n")
                print("Priority : " + priority + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].priority == priority:
                        index_store.append(count)
                Bug.print_by_index(bugs_list, index_store)
                return index_store
            else:
                print("You did not give a priority!")
        elif search == 4:  # search by date
            if date is not None:
                print("-------------Searching bugs-----------------\n")
                print("Date : " + date + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].date == date:
                        index_store.append(count)
                Bug.print_by_index(bugs_list, index_store)
                return index_store
            else:
                print("You did not give a date!")
        elif search == 5:  # search by status
            if status is not None:
                print("-------------Searching bugs-----------------\n")
                print("Status : " + status + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].status == status:
                        index_store.append(count)
                Bug.print_by_index(bugs_list, index_store)
                return index_store
            else:
                print("You did not give a status!")
        else:
            print("Not searching anything! \n")

    @classmethod
    def delete_bug(cls, bugs_list, user_name, title):
        count = 0
        index_store = []
        while count < len(bugs_list):
            if bugs_list[count].author == user_name:
                if bugs_list[count].title == title:
                    index_store.append(count)
            count += 1
        print("-----------------Bugs to be deleted-----------------\n")
        Bug.print_by_index(bugs_list, index_store)
        if index_store:
            for index in index_store:
                del(bugs_list[index])
                print("-----------------Bugs deleted-----------------\n")
        else:
            print("Bugs not found!!!!")
            return False
        return True

    @classmethod
    def show_by(cls, bugs_list, show_by=0, user_name=None):
        flag = False
        if show_by == 0:  # show all
            print("-------------Showing all bugs-----------------\n")
            for count in range(len(bugs_list)):
                bugs_list[count].print_bug()
        elif show_by == 1:  # show by name
            if user_name is not None:
                print("-------------Showing all bugs of user-----------------\n")
                print("Author : " + user_name + "\n\n")
                for count in range(len(bugs_list)):
                    if bugs_list[count].author == user_name:
                        flag = True
                        bugs_list[count].print_bug()
                if not flag:
                    print("That user does not exist!!")
            else:
                print("You did not give a name!")
        else:
            print("Not showing anything! \n")

    @classmethod
    def save_data(cls, data, bugs_list, num_bugs):
        data.check_database()
        if bugs_list[num_bugs:] is not None:
            for bug in bugs_list[num_bugs:]:
                sql = "INSERT INTO Bugs VALUES ('{}', '{}', '{}', {}, '{}', '{}', {})".format(bug.get_title(), bug.get_project(),
                                                                                              bug.get_btype(), bug.get_priority(),
                                                                                              bug.get_status(), bug.get_author(),
                                                                                              bug.get_date())
                data.send_query(sql)

    @classmethod
    def retrieve_data(cls, data):
        data.check_database()
        sql_bugs = "SELECT * FROM Bugs"
        Bugs_List = []
        num_bugs = 0
        try:
            bugs_table = data.send_query(sql_bugs)
            num_bugs = len(bugs_table)
            if num_bugs > 0:
                for bug in bugs_table:
                    Bugs_List.append(Bug(str(bug['title']), str(bug['project']), str(bug['btype']), str(bug['priority']), str(bug['status']),
                                         str(bug['author']), str(bug['_date_'])))
        except TypeError as e:
            print("")
        return Bugs_List, num_bugs
