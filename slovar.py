from fastapi import FastAPI, Body
from fastapi.responses import FileResponse, RedirectResponse, PlainTextResponse


app = FastAPI()


@app.get("/")
def root():
    return FileResponse('public/index2.html')


file = open("public/words.txt", "r").read().split()
final_word = []
for i in file:
    if i != "-":
        if "," in i:
            final_word.append(i[0:-1])
        else:
            final_word.append(i)


@app.post("/hello")
def hello(data=Body()):
    word = data["word"]
    if word in final_word:
        if final_word.index(word) % 2 == 0:
            word = final_word[final_word.index(word) + 1]
        else:
            word = final_word[final_word.index(word) - 1]
    return {"message": f"{word}"}


@app.get("/old")
def old():
    return RedirectResponse("/new")


@app.get("/new")
def new():
    return PlainTextResponse("New Page")
