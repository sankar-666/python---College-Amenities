from flask import *
from database import *
import uuid

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

principal=Blueprint('principal',__name__)

@principal.route('/principalhome')
def principalhome():
    return render_template('principalhome.html')



@principal.route('/principal_manage_dept',methods=['get','post'])
def principal_manage_dept():
    data={}


    if 'btn' in request.form:
        dep=request.form['dep']
        hod=request.form['hod']

        q="insert into department values(null,'%s','%s','%s')"%(session['pid'],dep,hod)
        lid=insert(q)
        flash("Added successfull")
        return redirect(url_for("principal.principal_manage_dept"))


    q="select * from department"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        did=request.args['did'] 
   
    else:
        action=None

    
    if action == "update":
        q="select * from department where department_id='%s'"%(did)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            dep=request.form['dep']
            hod=request.form['hod']

            q="update department set dep_name='%s', hod_name='%s' where department_id='%s' "%(dep,hod,did)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("principal.principal_manage_dept"))
    if action == "delete":
        q="delete from department where department_id='%s' "%(did)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("principal.principal_manage_dept"))
    return render_template('principal_manage_dept.html',data=data) 


@principal.route('/principal_manage_class',methods=['get','post'])
def principal_manage_class():
    data={}
    did=request.args['did']

    if 'btn' in request.form:
        name=request.form['name']

        q="insert into class values(null,'%s','%s')"%(did,name)
        lid=insert(q)
        flash("Added successfull")
        return redirect(url_for("principal.principal_manage_class",did=did))


    q="select * from class where department_id='%s'"%(did)
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid'] 
   
    else:
        action=None

    
    if action == "update":
        q="select * from class where class_id='%s'"%(cid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
          
            q="update class set class_name='%s' where class_id='%s' "%(name,cid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("principal.principal_manage_class",did=did))
    if action == "delete":
        q="delete from class where class_id='%s' "%(cid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("principal.principal_manage_class",did=did))
    return render_template('principal_manage_class.html',data=data,did=did) 



@principal.route('/principal_manage_aminity_type',methods=['get','post'])
def principal_manage_aminity_type():
    data={}
    if 'btn' in request.form:
        name=request.form['name']

        q="select * from amenity_type where type_name='%s'"%(name)
        val=select(q)
        if val:
            flash("Type Already Added, try different type")
        else:
            q="insert into amenity_type values(null,'%s')"%(name)
            lid=insert(q)
            flash("Added successfull")
        return redirect(url_for("principal.principal_manage_aminity_type"))


    q="select * from amenity_type "
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid'] 
   
    else:
        action=None

    
    if action == "update":
        q="select * from amenity_type where amenity_type_id='%s'"%(cid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
          
            q="update amenity_type set type_name='%s' where amenity_type_id='%s' "%(name,cid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("principal.principal_manage_aminity_type"))
    if action == "delete":
        q="delete from amenity_type where amenity_type_id='%s' "%(cid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("principal.principal_manage_aminity_type"))
    return render_template('principal_manage_aminity_type.html',data=data) 




@principal.route('/principal_manage_amenity',methods=['get','post'])
def principal_manage_amenity():
    data={}
    tid=request.args['tid']

    if 'btn' in request.form:
        name=request.form['name']
        amount=request.form['amount']

        q="insert into amenites values(null,'%s','%s','%s')"%(tid,name,amount)
        lid=insert(q)
        flash("Added successfull")
        return redirect(url_for("principal.principal_manage_amenity",tid=tid))


    q="select * from amenites where amenity_type_id='%s'"%(tid)
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        aid=request.args['aid'] 
   
    else:
        action=None

    
    if action == "update":
        q="select * from amenites where amenity_id='%s'"%(aid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            amount=request.form['amount']
          
            q="update amenites set name='%s', amount='%s' where amenity_id='%s' "%(name,amount,aid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("principal.principal_manage_amenity",tid=tid))
    if action == "delete":
        q="delete from amenites where amenity_id='%s' "%(aid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("principal.principal_manage_amenity",tid=tid))
    return render_template('principal_manage_amenity.html',data=data,tid=tid) 



@principal.route('/principal_view_internal_bookings')
def principal_view_internal_bookings():
    data={}
    q="SELECT * FROM `user`,`bookings`,`amenites`,amenity_type WHERE `user`.`user_id`=`bookings`.`user_id` AND `bookings`.`amenity_id`=`amenites`.`amenity_id` and `amenites`.`amenity_type_id`=`amenity_type`.`amenity_type_id` and type_name='Internally'"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        bid=request.args['bid']
        uid=request.args['uid']
    else:
        action=None

    if action == "accept":
        q="update bookings set status='accepted' where bookings_id='%s'"%(bid)
        update(q)
        q="select * from user where user_id='%s'"%(uid)
        email=select(q)[0]['email']

        pwd="Your Amenity Request Has beed Accepted by the Principal"

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'Amenity Request Verification'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        return redirect(url_for("principal.principal_view_internal_bookings"))
    
    
    if action == "reject":
        q="update bookings set status='Rejected' where bookings_id='%s'"%(bid)
        update(q)
        q="select * from user where user_id='%s'"%(uid)
        email=select(q)[0]['email']

        pwd="Your Amenity Request Has beed rejected by the Principal"

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'Amenity Request Verification'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        return redirect(url_for("principal.principal_view_internal_bookings"))
        


    return render_template('principal_view_internal_bookings.html',data=data)




@principal.route('/principal_view_external_bookings')
def principal_view_external_bookings():
    data={}
    q="SELECT * FROM `user`,`bookings`,`amenites`,amenity_type WHERE `user`.`user_id`=`bookings`.`user_id` AND `bookings`.`amenity_id`=`amenites`.`amenity_id` and `amenites`.`amenity_type_id`=`amenity_type`.`amenity_type_id` and type_name='Externally'"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        bid=request.args['bid']
        uid=request.args['uid']
    else:
        action=None

    if action == "accept":
        q="update bookings set status='accepted' where bookings_id='%s'"%(bid)
        update(q)
        q="select * from user where user_id='%s'"%(uid)
        email=select(q)[0]['email']

        pwd="Your Amenity Request Has beed Accepted by the Principal"

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'Amenity Request Verification'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        return redirect(url_for("principal.principal_view_external_bookings"))
    
    
    if action == "reject":
        q="update bookings set status='Rejected' where bookings_id='%s'"%(bid)
        update(q)
        q="select * from user where user_id='%s'"%(uid)
        email=select(q)[0]['email']

        pwd="Your Amenity Request Has beed rejected by the Principal"

        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login('sngistoutpass@gmail.com','izgqjuqneorhokje')
        except Exception as e:
            print("Couldn't setup email!!"+str(e))

        pwd = MIMEText(pwd)

        pwd['Subject'] = 'Amenity Request Verification'

        pwd['To'] = email

        pwd['From'] = 'sngistoutpass@gmail.com'

        try:
            gmail.send_message(pwd)
   
            flash("EMAIL SENED SUCCESFULLY")
            


        except Exception as e:
            print("COULDN'T SEND EMAIL", str(e))
        else:
            flash("INVALID DETAILS")
        return redirect(url_for("principal.principal_view_external_bookings"))


    return render_template('principal_view_external_bookings.html',data=data)



@principal.route('/principal_view_payment')
def principal_view_payment():
    data={}
    bid=request.args['bid']
    q="select * from payment where booking_id='%s'"%(bid)
    data['res']=select(q)
    return render_template('principal_view_payment.html',data=data)



# @admin.route('/room_payment')
# def room_payment():
#     data={}
#     bid=request.args['bid']
#     q="select * from payment where book_id='%s' and type='room'"%(bid)
#     data['res']=select(q)
#     if 'action' in request.args:
#         action=request.args['action']
#     else:
#         action=None
#     if action == "accept":
#         q="update booking set status='Payment Accepted' where booking_id='%s'"%(bid)
#         update(q)
#         flash("Payment Accepted")
#         return redirect(url_for("admin.room_payment",bid=bid))
#     return render_template('room_payment.html',data=data,bid=bid)