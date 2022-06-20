
Bugs_List = []


class Bug:
    def __init__(self, title, project, btype, priority, status, author, date):
        self.title = title
        self.project = project
        self.btype = btype
        self.priority = priority
        self.status = status
        self.author = author
        self.date = date
        Bugs_List.append(self)

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
    def print_by_index(cls, index_store):
        for index in index_store:
            Bugs_List[index].print_bug()

    @classmethod
    def search_by(cls, search=0, title=None, btype=None, project=None, priority=None, status=None, date=None):
        index_store = []
        if search == 0:  # search by title
            if title is not None:
                print("-------------Searching bugs-----------------\n")
                print("Title : " + title + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].title == title:
                        index_store.append(count)
                Bug.print_by_index(index_store)
                return index_store
            else:
                print("You did not give a title!")
        elif search == 1:  # search by type
            if project is not None:
                print("-------------Searching bugs-----------------\n")
                print("Project : " + project + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].project == project:
                        index_store.append(count)
                Bug.print_by_index(index_store)
                return index_store
            else:
                print("You did not give a type!")
        elif search == 2:  # search by project name
            if btype is not None:
                print("-------------Searching bugs-----------------\n")
                print("Type : " + btype + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].btype == btype:
                        index_store.append(count)
                Bug.print_by_index(index_store)
                return index_store
            else:
                print("You did not give a project title!")
        elif search == 3:  # search by priority
            if priority is not None:
                print("-------------Searching bugs-----------------\n")
                print("Priority : " + priority + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].priority == priority:
                        index_store.append(count)
                Bug.print_by_index(index_store)
                return index_store
            else:
                print("You did not give a priority!")
        elif search == 4:  # search by date
            if date is not None:
                print("-------------Searching bugs-----------------\n")
                print("Date : " + date + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].date == date:
                        index_store.append(count)
                Bug.print_by_index(index_store)
                return index_store
            else:
                print("You did not give a date!")
        elif search == 5:  # search by status
            if status is not None:
                print("-------------Searching bugs-----------------\n")
                print("Status : " + status + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].status == status:
                        index_store.append(count)
                Bug.print_by_index(index_store)
                return index_store
            else:
                print("You did not give a status!")
        else:
            print("Not searching anything! \n")

    @classmethod
    def delete_bug(cls, user_name, title):
        count = 0
        index_store = []
        while count < len(Bugs_List):
            if Bugs_List[count].author == user_name:
                if Bugs_List[count].title == title:
                    index_store.append(count)
            count += 1
        print("-----------------Bugs to be deleted-----------------\n")
        Bug.print_by_index(index_store)
        if index_store:
            for index in index_store:
                del(Bugs_List[index])
                print("-----------------Bugs deleted-----------------\n")
        else:
            print("Bugs not found!!!!")
            return False
        return True

    @classmethod
    def show_by(cls, show_by=0, user_name=None):
        flag = False
        if show_by == 0:  # show all
            print("-------------Showing all bugs-----------------\n")
            for count in range(len(Bugs_List)):
                Bugs_List[count].print_bug()
        elif show_by == 1:  # show by name
            if user_name is not None:
                print("-------------Showing all bugs of user-----------------\n")
                print("Author : " + user_name + "\n\n")
                for count in range(len(Bugs_List)):
                    if Bugs_List[count].author == user_name:
                        flag = True
                        Bugs_List[count].print_bug()
                if not flag:
                    print("That user does not exist!!")
            else:
                print("You did not give a name!")
        else:
            print("Not showing anything! \n")

