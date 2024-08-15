import requests
import random


# Below code extracts the quiz questions from api
parameters={
    "amount":10,
    "type":"boolean"
}
response=requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
question_data=response.json()["results"]
# print(question_data)
# quizdata=random.choices(quiz)
# question_text=html.unescape(quizdata[0]["question"])
# correct_answer=html.unescape(quizdata[0]["correct_answer"].lower())
# incorrect_answer=html.unescape(quizdata[0]["incorrect_answers"][0].lower())
# # print(question_text,correct_answer,incorrect_answer)