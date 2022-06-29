import re


class Validation:

    @classmethod
    def check_text(cls, text):
        # Alphanumeric format
        comm_val = re.compile(r"[A-Za-z\d@#$%^&+=]+")
        if re.match(comm_val, text):
            return True
        else:
            return False
        pass

    @classmethod
    def check_name(cls, name):
        # Alphanumeric format
        comm_val = re.compile(r"[A-Za-z\d]+")
        if re.match(comm_val, name):
            return True
        else:
            return False
        pass

    @classmethod
    def check_password(cls, password):
        # Alphanumeric format
        comm_val = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,}')
        if re.match(comm_val, password):
            return True
        else:
            return False
        pass

    @classmethod
    def check_phone(cls, n_phone):
        # Phone format
        phone_val = re.compile('\d{10}')
        if re.match(phone_val, n_phone):
            return True
        else:
            return False
        pass

    @classmethod
    def check_email(cls, email):
        # Phone format
        email_val = re.compile('.*@.*')
        if re.match(email_val, email):
            return True
        else:
            return False
        pass

    @classmethod
    def check_date(cls, date):
        date_val = re.compile('.{4}-.{2}-.{2}')
        if re.match(date_val, date):
            return True
        else:
            return False
