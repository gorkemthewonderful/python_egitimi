#Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer(self, answer):
        return self.answer == answer
        
class Quiz:
    def __init__(self,Questions):
        self.Questions = Questions
        self.Score = 0
        self.QuestionIndex = 0 #questionindex soruların 1. sorudan başlamasını sağlamak için 0 !!!

    def getQuestion(self):
        return self.Questions[self.QuestionIndex] 

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.QuestionIndex + 1}: {question.text} ')
        
        for q in question.choices:
            print("-" + q)
        answer = input("Cevap: ")
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.Score += 1
        self.QuestionIndex += 1

    def loadQuestion(self):
        if len(self.Questions) == self.QuestionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("Score: ",self.Score)

    def displayProgress(self):
        totalQuestion = len(self.Questions)
        questionNumber = self.QuestionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti.")
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,"*"))

q1 = Question("En iyi programlama dili hangisidir?", ['C#','Python','Javascript','Java'], "Python")
q2 = Question("En popüler programlama dili hangisidir?", ['Python','Javascript','C#','Java'], "Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?", ['C#','Javascript','Java','Python'], "Python")
questions = [q1,q2,q3]

quiz = Quiz(questions)
# question = quiz.getQuestion()
# print(question.text) #metod displayQuestion yazmamak için bu ikisi yazılabilir.

quiz.loadQuestion()