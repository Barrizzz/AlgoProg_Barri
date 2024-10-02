class Binusmaya:
    def __init__(self):
        self.Lecturer = [
            {'Name':'Prof. Dr. Ir. Mr. Ms. Jude S.Kominfo', 'Subject':'Algorithm and Praying', 'LecturerID':'1234567'}, 
            {'Name':'Prof. Prabowo Gibran', 'Subject':'Music', 'LecturerID':'7267367'},
            {'Name':'Prof. Anies Baswedan', 'Subject':'Human Computer Loving', 'LecturerID':'72222222'},
            {'Name':'Prof. Dr. Ir. H. Legolas S.Kom (with honors)', 'Subject':'Mathing', 'LecturerID':'766644'},
        ]
        self.Classes = ['L1AC', 'L1BC', 'L1CC']
        self.Schedule = []

    def add_lec_data(self, lecName, subject, lecID):
        Flag = False
        for i in self.Lecturer:
            if i['Name'] == lecName or i['Subject'] == subject or i['LecturerID'] == lecID:
                print('The same data has already been entered')
                Flag = True

        if Flag == False:
            new_lecture = {
                'Name': lecName,
                'Subject': subject,
                'LecturerID': lecID
            }      
            self.Lecturer.append(new_lecture)
            return self.Lecturer

    def remove_lec_data(self, lecturerID):
        myList = []
        for i in self.Lecturer:
            myList.append(i.get('LecturerID'))

            if lecturerID in myList:
                self.Lecturer.pop(len(myList) - 1)
                break
            else:
                print("That data doesn't exist")
                break
        return self.Lecturer

    def input_class_code(self, classCode):
        Flag = False
        for i in self.Classes:
            if classCode == i:
                print('The same data has already been entered')
                Flag = True
                break
        if Flag == False:
            self.Classes.append(classCode)
            return self.Classes
        
    def remove_class_code(self, classCode):
        for i in self.Classes:
            if classCode in self.Classes:
                self.Classes.remove(i)
                break
            else:
                print("That data doesn't exist")
                break
        return self.Classes
    
    def tup_to_schedule(self, classCode, time, subject):
        myList = [classCode, time, subject]
        for i in self.Lecturer:
            if i['Subject'] == subject:
                myList.append(i['Name'])
                break
        t = tuple(myList)
        return self.Schedule.append(t)
                

#THIS IS THE INPUT THINGY

test = Binusmaya()
#test.add_lec_data('John Doe', 'Music', '3456789')
#test.remove_lec_data('')
#test.input_class_code('')
#test.remove_class_code('L1BC')
#test.tup_to_schedule('L1AC', '10 AM', 'Music')

#print(test.Lecturer)
#print(test.Classes)
#print(test.Schedule)

            
