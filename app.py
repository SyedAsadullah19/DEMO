from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return "Hello World"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run()