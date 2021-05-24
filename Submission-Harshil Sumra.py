class Quiz():
    questions={}
    student_wise_responses={}
    def add_ques(self):
        self.topic=input("Input Quiz name: ")
        self.difficultylevel=input("easy/medium/hard: ")
        self.y=1
        self.question=input("Input Question: ")
        self.oa=input("option A: ")
        self.ob=input("option B: ")
        self.oc=input("option C: ")
        self.od=input("option D: ")
        self.correct_option=input("A/B/C/D: ")
        while self.y!=0:
            if self.topic in self.questions:
                if [self.difficultylevel,self.question,self.oa,self.ob,self.oc,self.od,self.correct_option] not in self.questions[self.topic]:
                    self.questions[self.topic].append([self.difficultylevel,self.question,self.oa,self.ob,self.oc,self.od,self.correct_option])
                else:
                    self.y=0
            else:
                self.questions[self.topic]=[[self.difficultylevel,self.question,self.oa,self.ob,self.oc,self.od,self.correct_option]]
    def remove_ques(self):
        self.topic=input("Input quiz topic")
        self.difficultylevel=input("easy/medium/hard: ")
        self.y=1
        self.question=input("Type your question: ")
        self.oa=input("option A: ")
        self.ob=input("option B: ")
        self.oc=input("option C: ")
        self.od=input("option D: ")
        self.correct_option=input("A/B/C/D: ")
        while self.y!=0:
            if [self.difficultylevel,self.question,self.oa,self.ob,self.oc,self.od,self.correct_option] in self.questions[self.topic]:
                self.questions[self.topic].remove([self.difficultylevel,self.question,self.oa,self.ob,self.oc,self.od,self.correct_option])
            else:
                y=0
    def take_quiz(self,s_name,topic):
        self.t=topic
        self.name=s_name
        self.score=0
        self.count=0
        self.l=[]
        if self.t in self.questions:
            for i in self.questions[self.t]:
                print("Difficulty= "+i[0])
                print(i[1])
                print("A: "+ i[2])
                print("B: "+ i[3])
                print("C: "+ i[4])
                print("D: "+ i[5])
                self.a=input("choose the correct answer[A/B/C/D]: ")
                if self.a==[i][-1]:
                    self.score+=1
                self.l.append([i[1],self.a])
        if self.name in self.student_wise_responses:
            self.student_wise_responses[self.name].append((self.t,self.score,self.l))
        else:
            self.student_wise_responses[self.name]=[(self.t,self.score,self.l)]
        print("Name: {}".format(self.name))
        print("You scored {0} out of {1}".format(self.score,len(self.l)))
    
    def answer_key(self,name,quiz_topic):
        self.name=name
        self.top=quiz_topic
        for i in self.student_wise_responses[self.name]:
            if i[0]==self.top:
                print("structure is (topic,score,responses)")
                print(i)
        if self.top in self.questions:
            for i in self.questions[self.top]:
                print("Difficulty: "+i[0])
                print(i[1])
                print("A: "+ i[2])
                print("B: "+ i[3])
                print("C: "+ i[4])
                print("D: "+ i[5])
    
    def display(self,topic):
        self.top=topic
        if self.top in self.questions:
            for i in self.questions[self.top]:
                print("Difficulty: "+i[0])
                print(i[1])
                print("A: "+ i[2])
                print("B: "+ i[3])
                print("C: "+ i[4])
                print("D: "+ i[5])
                
t_pword="abcd"
stu_pword="xyz"
x=10
q=Quiz()
while x!=0:
    for i in q.student_wise_responses:
        print("student name: "i,"topic and score: "q.student_wise_responses[i][:2])
    print("Are you a student or a teacher: S/T [any other key will help you exit]")
    status=input()
    if status=="S":
        info_temp=input("Enter your unique user name and access password(comma seperated)").split(",")
        if info_temp[1]==stu_pword:
            quiz_name=input("Enter quiz name: ")
            if quiz_name in q.questions:
                if info_temp[0] not in q.student_wise_responses:
                    if input("Are you ready to take the quiz(Y for Yes any other response will mean No): ")=="Y":
                        q.take_quiz(info_temp[0],quiz_name)
                        print("Here is your the answer key. Please review your answers")
                        q.answer_key(info_temp[0],quiz_name)
                    else:
                        print("Are you sure?, If Yes then Exit the system by inputing 0")
                        x=int(input())
            else:
                print("no such quiz exists")
    elif status=="T":
        info_temp=input("Enter your access password: ")
        if info_temp==t_pword:
            print("Welcome Teacher")
            print("1. Add quizes or quiz questions ")
            print("2. Display all questions of a particular topic ")
            print("Any response except 1 or 2 means exit ")
            resp=int(input())
            if resp==1:
                n=int(input("number of questions you want to add: "))
                for i in range(n):
                    q.add_ques()
            elif resp==2:
                c=input("quiz Topic: ")
                q.display(c)
            else:
                x=0
    else:
        print("Incorrect Response")
        x=0
