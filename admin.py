from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@admin.route('/admin_manage_principal',methods=['get','post'])
def admin_manage_principal():
    data={}


    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        pwd=request.form['pwd']
        uname=request.form['uname']
        
    
        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("This Username already exist!, try register with new one.")
        else:
            q="insert into login values(null,'%s','%s','principal')"%(uname,pwd)
            lid=insert(q)
            q="insert into principal values (NULL,'%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,place,phone,email)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("admin.admin_manage_principal"))


    q="select * from principal"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid'] 
        lid=request.args['lid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from principal where principal_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            fname=request.form['fname']
            lname=request.form['lname']
            place=request.form['place']
            
            phone=request.form['phone']
            email=request.form['email']

            q="update principal set fname='%s', lname='%s', place='%s', phone='%s', email='%s' where principal_id='%s' "%(fname,lname,place,phone,email,pid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_principal"))
    if action == "delete":
        q="delete from principal where principal_id='%s' "%(pid)
        delete(q)
        q="delete from login where login_id='%s' "%(lid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_principal"))
    return render_template('admin_manage_principal.html',data=data) 



@admin.route('/admin_view_department')
def admin_view_department():
    data={}
    q="SELECT * FROM department"
    data['res']=select(q)
    return render_template('admin_view_department.html',data=data)

@admin.route('/admin_view_class')
def admin_view_class():
    did=request.args['did']
    data={}
    q="SELECT * FROM class where department_id='%s'"%(did)
    data['res']=select(q)
    return render_template('admin_view_class.html',data=data)

@admin.route('/admin_view_bookings')
def admin_view_bookings():
    data={}
    q="SELECT * FROM `user`,`bookings`,`amenites` WHERE `user`.`user_id`=`bookings`.`user_id` AND `bookings`.`amenity_id`=`amenites`.`amenity_id`"
    data['res']=select(q)
    return render_template('admin_view_bookings.html',data=data)



@admin.route('/room_payment')
def room_payment():
    data={}
    bid=request.args['bid']
    q="select * from payment where booking_id='%s'"%(bid)
    data['res']=select(q)

    return render_template('room_payment.html',data=data)


import qrcode

@admin.route('/admin_add_accountdetails',methods=['get','post'])
def admin_add_accountdetails():
    data={}


    if 'btn' in request.form:
        acno=request.form['acno']
        branch=request.form['branch']
        ifsc=request.form['ifsc']
    
        q="select * from account where acc_no='%s'"%(acno)
        res=select(q)
        if res:
            flash("This Account already exist!, try with new one.")
        else:
            q="insert into account values (NULL,'%s','%s','%s','pending')"%(acno,branch,ifsc)
            id=insert(q)
            s=qrcode.make(str(id))
            path="static/qrcode/"+str(uuid.uuid4())+".png"
            s.save(path)
            q="update account set qr_code='%s' where account_id='%s'"%(path,id)
            update(q)
            flash("Account Created successfully")
            return redirect(url_for("admin.admin_add_accountdetails"))


    q="select * from account"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        aid=request.args['aid'] 
    else:
        action=None

    
    # if action == "update":
    #     q="select * from principal where principal_id='%s'"%(pid)
    #     val=select(q)
    #     data['raw']=val

    #     if 'update' in request.form:
    #         fname=request.form['fname']
    #         lname=request.form['lname']
    #         place=request.form['place']
            
    #         phone=request.form['phone']
    #         email=request.form['email']

    #         q="update principal set fname='%s', lname='%s', place='%s', phone='%s', email='%s' where principal_id='%s' "%(fname,lname,place,phone,email,pid)
    #         update(q)
    #         flash("Updated Successfully")
    #         return redirect(url_for("admin.admin_add_accountdetails"))
    if action == "delete":
        q="delete from account where account_id='%s' "%(aid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_add_accountdetails"))
    return render_template('admin_add_accountdetails.html',data=data) 