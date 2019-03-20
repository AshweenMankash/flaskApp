from flask import Flask,redirect,url_for
from flask import g,render_template, request
import requests
import sqlite3

app = Flask(__name__,template_folder="template")


def connect_database():
     return sqlite3.connect("//run//media//ashweenmankash//Grand Line//Flask//library.db")

@app.route("/")
def main():
     return redirect(url_for("authors"),code=301)



@app.route("/authors")
def authors():

     db_connection = connect_database()
     query = db_connection.execute('SELECT a.id, a.Aname, c.Aname FROM author a INNER JOIN country c ON a.country_id = c.id;')
     fetched = query.fetchall()
     authors = [dict(id=row[0], name =row[1],country=row[2]) for row in fetched]
     print(authors) 
     url="http://api.ipstack.com/{}?access_key=9f15db97f8d7859e0a449db1dcad28dc".format(request.remote_addr)
     location = requests.get(url).json()
     return render_template("routing/authors.html",authors=authors,location=location)
   

@app.route("/routing/form",methods=['POST','GET'])
def form():
     if request.method == 'GET':
         return render_template('routing/form')
     
     elif request.method == 'POST':
          kwargs = {
               'title':request.form['title'],
               'isbn':request.form['isbn'],
               'author':request.form['author'],
               'secret_key':request.form['SECRET_KEY'],
               'submit_value':request.form['submit'],
          }
     return render_template('routing/form_result.html',**kwargs)


@app.route("/author/<author>")
def author(author):

#     if author not in authors : 

#         return render_template("routing/authorNotFound.html",author=author)

    return render_template("routing/author.html",author = author)