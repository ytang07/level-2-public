# Question Class
class Question:
    # requires a question, four answer choices, and which one is correct
    def __init__(self, question: str, a: str, b: str, c: str, d: str, correct: str):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.correct = correct
    
    def is_right(self, answer):
        if answer == self.correct:
            return True
        else:
            return False

# Quiz Class
class Quiz:
    def __init__(self, questions:dict = {}):
        self.questions = questions
        self.answers = {}
        
    @property
    def num_questions(self):
        return len(self.questions)

    def add_question(self, question: Question):
        index = self.num_questions
        self.questions[index] = question

    def give_quiz(self):
        for index, question in self.questions.items():
            print(question.question)
            print(f"A: {question.a}")
            print(f"B: {question.b}")
            print(f"C: {question.c}")
            print(f"D: {question.d}")
            answer = input("Type Your Answer Here: ")
            self.answers[index] = answer

    def score(self):
        num_questions = self.num_questions
        num_correct = 0
        for index in range(num_questions):
            question = self.questions[index]
            answer = self.answers[index]
            if question.is_right(answer):
                num_correct += 1
        return f"You scored {num_correct} out of {num_questions}"
    
# initialize quiz and ask for questions
def make_quiz():
    quiz = Quiz()
    adding_questions = True
    while adding_questions:
        _question = input("What is the question? ")
        _a = input("What is option A? ")
        _b = input("What is option B? ")
        _c = input("What is option C? ")
        _d = input("What is option D? ")
        _correct = input("Which of the answers is correct? ")
        _question = Question(_question, _a, _b,_c, _d, _correct)
        quiz.add_question(_question)
        still_adding = input("Are there more questions to add?(y/n) ").lower()
        if still_adding == "n":
            adding_questions = False
    return quiz

def take_quiz(quiz: Quiz):
    quiz.give_quiz()
    results = quiz.score()
    print(results)
    return results

# _quiz = make_quiz()
q1 = Question("Who's the best software content creator?", "Yujian Tang", "Tom Brady", "Taylor Swift", "Michael Jordan", "Yujian Tang")
q2 = Question("What's the name of the most comprehensive Text API on the web?", "A Text API", "Another Text API", "I Don't Know", "The Text API", "The Text API")
q3 = Question("Which Python Blog is the best?", "Some Python Blog", "Medium", "PythonAlgos", "Some other Python Blog", "PythonAlgos")
q4 = Question("Which of the following letters is B?", "A", "B", "C", "D", "B")
_quiz = Quiz({
    0: q1,
    1: q2,
    2: q3,
    3: q4
})
take_quiz(_quiz)
