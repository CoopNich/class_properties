class Student():

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""
        

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for first_name')
    
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""
        

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for last_name')

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
        

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer value for age')

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0
        

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Please provide an integer value for cohort_number')
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


cooper = Student()

cooper.first_name = "Cooper"
cooper.last_name = "Nichols"
cooper.age = 100
cooper.cohort_number = 38
print(cooper.full_name)

    

