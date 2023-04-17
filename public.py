from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')


@public.route('/login',methods=['post','get'])
def login():

    if 'btn' in request.form:
        uname=request.form['uname']
        pasw =request.form['pasw']

        q="select * from login where username='%s' and password='%s'"%(uname,pasw)
        res=select(q)


        if res:
            session['loginid']=res[0]["login_id"]
            session['utype']=res[0]["usertype"]
            utype=res[0]["usertype"]
            if utype == "admin":
                flash("Login Success")
                return redirect(url_for("admin.adminhome"))
            elif utype == "principal":
                q="select * from principal where login_id='%s'"%(session['loginid'])
                val=select(q)
                if val:
                    session['pid']=val[0]['principal_id']
                    flash("Login Success")
                    return redirect(url_for("principal.principalhome"))
            elif utype == "user":
                q="select * from user where login_id='%s'"%(session['loginid'])
                val=select(q)
                if val:
                    session['uid']=val[0]['user_id']
                    flash("Login Success")
                    return redirect(url_for("user.userhome"))
                
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("Invalid Username or Password!")
            return redirect(url_for("public.login"))


    return render_template("login.html")


@public.route("/userregistration",methods=['post','get'])
def userregistration():
    
    if "submit" in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pasd=request.form['pasd']
        q="insert into login values(null,'%s','%s','user')"%(uname,pasd)
        ids=insert(q)
        print(ids)
        s="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(ids,fname,lname,place,phone,email)
        insert(s)
        flash("Registration Successfull")
        return redirect(url_for("public.login"))
    return render_template("userregistration.html")
