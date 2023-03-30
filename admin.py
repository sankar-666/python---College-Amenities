from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')


@admin.route('/admin_manage_staff',methods=['get','post'])
def admin_manage_staff():
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
            q="insert into login values(null,'%s','%s','staff')"%(uname,pwd)
            lid=insert(q)
            q="insert into staff values (NULL,'%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,place,phone,email)
            insert(q)
            flash("Registration successfull")
            return redirect(url_for("admin.admin_manage_staff"))


    q="select * from staff"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        sid=request.args['sid'] 
        lid=request.args['lid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from staff where staff_id='%s'"%(sid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            fname=request.form['fname']
            lname=request.form['lname']
            place=request.form['place']
            
            phone=request.form['phone']
            email=request.form['email']

            q="update staff set fname='%s', lname='%s', place='%s', phone='%s', email='%s' where staff_id='%s' "%(fname,lname,place,phone,email,sid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_staff"))
    if action == "delete":
        q="delete from staff where staff_id='%s' "%(sid)
        delete(q)
        q="delete from login where login_id='%s' "%(lid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_staff"))
    return render_template('admin_manage_staff.html',data=data) 



@admin.route('/admin_view_room_bookings')
def admin_view_room_bookings():
    data={}
    q="SELECT * FROM `booking`,`user`,`room` WHERE `booking`.`user_id`=`user`.`user_id` AND `booking`.`room_id`=`room`.`room_id`"
    data['res']=select(q)
    return render_template('admin_view_room_bookings.html',data=data)

