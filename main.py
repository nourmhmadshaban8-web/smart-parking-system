# class Member:
#     def __init__(self):
#         print("a new member has been added")


# member_one=Member()
# print(member_one.__class__)# To know this from wich class   Ex:- <class '__main__.Member'>



#=========================================================================================




# class Member:
#     def __init__(self,first_name,middle_name,last_name,gender):
#         print("a new member has been added")
#         self.fname=first_name
#         self.mname=middle_name
#         self.lname=last_name
#         self.gender=gender.lower()

#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender=="male":
#             return f"Mr / {self.fname}"
#         elif self.gender=="female":
#             return f"Mrs / {self.fname}"
#         else:
#             return f"{self.fname}"
        
#     def get_all_info(self):
#         return f"{self.name_with_title()} , Your name is {self.full_name()}"


# member1=Member("Ahmed","Shrief","Samir","Male")

# print(member1.full_name())

# print(member1.name_with_title())

# print(member1.get_all_info())




#=========================================================================================




# class Member:

#     not_allowed_names=["Sief","Batoot","Miecky","Programmer"]

#     users_num=0

#     def __init__(self,first_name,middle_name,last_name,gender):
#         print("a new member has been added")
#         self.fname=first_name
#         self.mname=middle_name
#         self.lname=last_name
#         self.gender=gender.lower()
#         if self.fname in Member.not_allowed_names or self.mname in Member.not_allowed_names or self.lname in Member.not_allowed_names:
#             raise ValueError("Name Not Allowed")
#         Member.users_num+=1

#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender=="male":
#             return f"Mr / {self.fname}"
#         elif self.gender=="female":
#             return f"Mrs / {self.fname}"
#         else:
#             return f"{self.fname}"
        
#     def get_all_info(self):
#         return f"{self.name_with_title()} , Your name is {self.full_name()}"


# member1=Member("Ahmed","Shrief","Samir","Male")
# member2=Member("Programmer","Ahmed","Shrief","Male") # => Error Not Allowed Name

# print(member1.full_name())

# print(member1.name_with_title())

# print(member1.get_all_info())

# print(Member.users_num)




# #=========================================================================================




# class Member:

#     not_allowed_names=["Sief","Batoot","Miecky","Programmer"]

#     users_num=0

#     @classmethod
#     def show_users_count(cls):# Class Method 

#         print(f"We have {cls.users_num} users in our system")

#     @staticmethod
#     def say_hello():# Static method
#         print("Hello from static method")

#     def __init__(self,first_name,middle_name,last_name,gender): # Instance method
#         print("a new member has been added")
#         self.fname=first_name
#         self.mname=middle_name
#         self.lname=last_name
#         self.gender=gender.lower()
#         if self.fname in Member.not_allowed_names or self.mname in Member.not_allowed_names or self.lname in Member.not_allowed_names:
#             raise ValueError("Name Not Allowed")
#         Member.users_num+=1

#     def full_name(self):
#         return f"{self.fname} {self.mname} {self.lname}"

#     def name_with_title(self):
#         if self.gender=="male":
#             return f"Mr / {self.fname}"
#         elif self.gender=="female":
#             return f"Mrs / {self.fname}"
#         else:
#             return f"{self.fname}"
        
#     def get_all_info(self):
#         return f"{self.name_with_title()} , Your name is {self.full_name()}"


# member1=Member("Ahmed","Shrief","Samir","Male")
# #member2=Member("Programmer","Ahmed","Shrief","Male") # => Error Not Allowed Name

# print(member1.full_name())
# print(Member.full_name(member1))

# print(member1.name_with_title())

# print(member1.get_all_info())

# print(Member.users_num)

# Member.show_users_count()




# #=========================================================================================




class Skill:
    def __init__(self):
        self.skills=["HTML","CSS","JS"]

    def __str__(self): # return a Human readable output
        return f"This is My Skills => {self.skills}"

    def __len__(self):
        return len(self.skills)

profile=Skill()
print(profile)

profile.skills.append("PHP")
print(len(profile))
