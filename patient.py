class Patient():

    def __init__(self, ssn, dob, account_number, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__account_number = account_number
        self.__full_name = first_name + " " + last_name
        self.__address = address

    

    @property
    def ssn(self):
            return self.__ssn
    
    @property
    def dob(self):
            return self.__dob

    @property
    def account_number(self):
            return self.__account_number
    
    @property
    def full_name(self):
            return self.__full_name

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""
        

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string value for the address')
    

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)


print(cashew.full_name)
print(cashew.ssn)
print(cashew.dob)

print(dir(cashew))

    
    
    
    
    # @first_name.setter
    # def first_name(self, new_first_name):
    #     if type(new_first_name) is str:
    #         self.__first_name = new_first_name
    #     else:
    #         raise TypeError('Please provide a string value for first_name')