import os , sys
from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from flask_sqlalchemy import SQLAlchemy
current_dir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(current_dir, "superhero.sqlite3")
db= SQLAlchemy()
db.init_app(app)
app.app_context().push()

class User(db.Model):
    __tablename__= 'superhero'
    id= db.Column( db.Integer,autoincrement=True,primary_key=True )
    name=db.Column(db.String,unique=True)
    cont1=db.Column(db.String)
    cont2=db.Column(db.String)
    cont3=db.Column(db.String)
    cont4=db.Column(db.String)


@app.route("/", methods = ["GET", "POST"])
def articles():
    art = User.query.all()
    return render_template("home.html",articles=art)

@app.route("/<user_name>",methods=["GET","POST"])
def articles_by_authors(user_name):
    data= User.query.filter_by(name=user_name).first()
    return render_template("super.html",user=data)

#@app.route("/article_like/<article_id>",methods=["GET","POST"])
#def like(article_id):
#    print("Article with article_id={},was liked".format(article_id))
#    #Create a table for article likes and store it.
#    return "OK" ,200
#
#@app.route("/<name>",methods = ["GET"])
#def search(name):
#    q=name
#    #app.logger.debug('In Search ,returning from DB{}'.format(q))
#    search = ArticleSearch.query.filter(ArticleSearch.content.op("MATCH")(q)).all()
#    print(search,"1111")
#    return render_template("search.html",q=q,searchs=search)
#
@app.route("/feedback",methods=["GET","POST"])
def feedback():
    if request.method=="GET":
        return render_template("feedback.html",error=None)
    if request.method=="POST":
        form= request.form
        email=form["email"]
        if '@' in email:
            pass
        else:
            error="Enter a valid email"
            return render_template("feedback.html",error=error)
        return render_template("thanks.html")

if __name__ =="__main__":
    app.run(
        debug=True,
        #host = '0.0.0.0', port= 8080
        )