import re
class password():
    pattern = re.compile(r'^\d{3}$')
    
    b_type = re.compile(r'^[rR]|[vV]{1}$')
    
    def password_valid(self,x, password):
        a = re.search(x, password)
        if a == None:
            flag = 1
            print("invalid")
        else:
            flag = 0
            print("valid")

        return flag
    
 
        
if __name__ == "__main__":
    pass_word = password()
    password = input("Input password := ")
    flag = pass_word.password_valid(pass_word.b_type,password)
    if flag == 1:
        print("invalid password")
    

