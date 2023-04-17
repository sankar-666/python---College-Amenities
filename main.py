from flask import Flask,render_template
from public import public
from admin import admin
from principal import principal
from user import user
from api import api

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail


app=Flask(__name__)

app.secret_key="prayulla"

app.register_blueprint(admin)
app.register_blueprint(principal)
app.register_blueprint(user)
app.register_blueprint(public)
app.register_blueprint(api,url_prefix="/api")


mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sngistoutpass@gmail.com'
app.config['MAIL_PASSWORD'] = 'izgqjuqneorhokje'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

app.run(debug=True,port=5089,host="0.0.0.0")