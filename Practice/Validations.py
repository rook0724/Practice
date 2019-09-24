import re

class reValidation():
    studentID = re.compile(r'^\d{3}$')
    teacherID = re.compile(r'^\d{4}$')
    bookID = re.compile(r'^\d{5}$')
    Mobile = re.compile('^[6-9]$|^[0-9]\d{9}$')
    name_valid = re.compile('^[a-zA-z]+([\s]*[a-zA-Z]+)+$')
    type = re.compile(r'^[rR]|[vV]{1}$')
    def validation(self, x, password):
        a = re.search(x, password)
        if a == None:
            flag = 1
        else:
            flag = 0
        return flag

    def bookDTO_validation(self,name,author,type,dept):
        print("checking regex validations")
        
        b_name = re.search(self.name_valid, name)
        print("b_name checked", b_name)
        b_auth = re.search(self.name_valid, author)
        print("b_auth checked", b_auth)
        b_type = re.search(self.type,type)
        print("b_type checked", b_type)
        b_dept = re.search(self.name_valid,dept)
        print("b_dept checked", b_dept)
        
        if b_name == None:

            print("Invalid name, please try again!")


        elif b_auth == None:
            print("Invalid name, please try again!")

            return
        elif b_type == None:
            print("Invalid name, please try again!")

            return
        elif b_dept == None:
            print("Invalid name, please try again!")

            return
        else:
            print("Success")

        

if __name__ == "__main__":
    
    valid = reValidation()    
    flag = 0
    name = input("Enter the Book name: ")
    Id = int(input("Enter the Book Id: "))
    author = input("Please enter the Author name: ?")
    type = input("Enter the gender (R/V) : ")
    dept = input("Please enter the department: ")
    valid.bookDTO_validation(name,author,type,dept)
    
    



