import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_test"])
    for index, alternative in enumerate(question["alternatives"]):
        print(str(index + 1) + "-" + alternative)
    user_choice = int(input("Enter your answer :"))
    question["user_choice"] = user_choice


count = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        count = count + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{result} {index+1} - You answer : {question['user_choice']}, " \
              f"Correct answer : {question['correct_answer']}"
    print(message)

print(data)
print(count, '/', len(data))
