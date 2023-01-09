class Student:
    def __init__(self,name,address,phone,course,index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getInfo(self):
        print("Student: ",self.name,self.address,self.phone,self.course,self.index_number)

student_1 = Student("Ognjen","Vrbanja","112233","OET","12/13")
student_1.getInfo()

student_2 = Student("Zarko","Bijeljina","221133","DIR","1219/09")
student_2.getInfo()

student_3 = Student("Ugljesa","Prijedor","331122","NGiTC","01/12")
student_3.getInfo()
