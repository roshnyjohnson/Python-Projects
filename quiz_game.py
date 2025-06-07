print("WELCOME TO THE QUIZ")
question_bank = [
    {"text": "The ability of one class to acquire methods and attributes of another class is called ____.", "answer": "A"},
    {"text": "Which of the following is a type of inheritance?", "answer": "D"},
    {"text": "What type of inheritance has multiple subclasses to a single superclass?", "answer": "C"},
    {"text": "What is the depth of multilevel inheritance in Python?", "answer": "C"},
    {"text": "What does MRO stand for?", "answer": "B"}
]

options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
    ["A. Single", "B. Double", "C. Multiple", "D. both A and C"],
    ["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Hierarchical Inheritance", "D. None of these"],
    ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
    ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Object", "D. Method Resource Operation"]
]
score=0
def check_answer(given_answer,correct_answer):
    if given_answer==correct_answer:
        return True
    else:
        return False

for i in range(len(question_bank)):
    print(question_bank[i]["text"])
    for j in options[i]:
        print(j)
    value=(input("enter your guess(A/B/C/D)")).upper()
    quiz=check_answer(value,question_bank[i]["answer"])

    if quiz:
        print("correct answer")
        score=score+1

    else:
        print("incorrect answer")
        print(f"The correct anser is {question_bank[i]["answer"]}")


print(f"your score is {score}")
