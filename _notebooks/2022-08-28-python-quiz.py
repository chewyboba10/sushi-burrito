import getpass, sys

questions = 10
correct = 0
skipped = 0

def question_with_response(question, answer):
    print("Question: " + question)
    msg = input()
    if msg == answer:
        print(msg + " is correct")
        global correct
        correct += 1
    elif msg == "skip":
        print("Question has been skipped")
        global skipped
        skipped += 1
    else:
        print(msg + " is incorrect")

def percentage(right, wrong):
    percentage = 100 * float(right)/float(wrong)
    return str(percentage) + "%" 

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
print("Are you ready to take a test?")
rsp = input()
if rsp == "yes":
    print("Great! Good luck!")
if rsp == "no":
    print("too bad")

question_with_response("Name the Python output command mentioned in this lesson?", "print")
question_with_response("If you see many lines of code in order, what would College Board call it?", "sequence")
question_with_response("Describe a keyword used in Python to define a function?", "def")
question_with_response("What command is used to evaluate correct or incorrect response in this quiz?", "if")
question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?", "expression")
question_with_response("What is an input to a function or method called?", "parameter")
question_with_response("If Input is data the computer receives, what is the data that the computer sends back?", "output")
question_with_response("What is a reusable block of code called?", "function")
question_with_response("What operator is used for string concatenation in Python?", "+")
question_with_response("Which function can be used to turn numbers turned into string in Python?", "str() function")

print("Congratulations " + getpass.getuser() + "! You got " + percentage(correct, questions) + " and skipped " + str(skipped) + " questions!")
    