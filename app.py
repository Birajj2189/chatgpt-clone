from flask import Flask , render_template , jsonify,  request
from flask import Flask
from flask_pymongo import PyMongo

import openai

openai.api_key = "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"



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://birajj2001:Biraj2189@cluster0.dn8qugk.mongodb.net/ChatGPT"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html",mychats=mychats)

@app.route("/api", methods=["GET","POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        print(chat)
        if chat:
            data = {"result": f"{chat['answer']}"}
            return jsonify(data)
        else : 
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": question
                }
            ],
            temperature=0.7,
            max_tokens=100,
            )
            print(response);
            generated_answer = response.choices[0].message["content"]
            data = {"result": generated_answer}
            mongo.db.chats.insert_one({"question": question, "answer": generated_answer})
            return jsonify(data)



    data = { "What is your name" : "Hello , I am ChatGPT !!" }
    return  jsonify(data)

if __name__=="__main__":
    app.run(debug=True)