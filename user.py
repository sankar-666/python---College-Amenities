from flask import *
from database import *

user=Blueprint('user',__name__)

@user.route('/userhome')
def userhome():
    return render_template('userhome.html')

@user.route('/user_view_type')
def user_view_type():
    data={}
    q="SELECT * FROM amenity_type"
    data['res']=select(q)
    return render_template('user_view_types.html',data=data)

@user.route('/user_view_internal')
def user_view_internal():
    data={}
    q="SELECT * FROM amenity_type INNER JOIN `amenites` USING(`amenity_type_id`) WHERE type_name='Internally'"
    data['res']=select(q)
    return render_template('user_view_internal.html',data=data)

@user.route('/user_view_external')
def user_view_external():
    data={}
    q="SELECT * FROM amenity_type INNER JOIN `amenites` USING(`amenity_type_id`) WHERE type_name='Externally'"
    data['res']=select(q)
    return render_template('user_view_external.html',data=data)

@user.route('/user_view_other')
def user_view_other():
    data={}
    q="SELECT * FROM amenity_type INNER JOIN `amenites` USING(`amenity_type_id`) WHERE type_name='Others'"
    data['res']=select(q)
    return render_template('user_view_other.html',data=data)

@user.route('/user_view_dept')
def user_view_dept():
    data={}
    q="SELECT * FROM department INNER JOIN `principal` USING(`principal_id`)"
    data['res']=select(q)
    return render_template('user_view_dept.html',data=data)

@user.route('/user_view_class')
def user_view_class():
    data={}
    q="SELECT * FROM department INNER JOIN `class` USING(`department_id`)"
    data['res']=select(q)
    return render_template('user_view_class.html',data=data)

@user.route('/user_view_bookings')
def user_view_bookings():
    data={}
    q="SELECT * FROM `user`,`bookings`,`amenites`,amenity_type WHERE `user`.`user_id`=`bookings`.`user_id` AND `bookings`.`amenity_id`=`amenites`.`amenity_id` and `amenites`.`amenity_type_id`=`amenity_type`.`amenity_type_id`"
    data['res']=select(q)
    return render_template('user_view_mybookings.html',data=data)


@user.route('/user_book_external',methods=['get','post'])
def user_book_external():
    data={}
    from datetime import date

    # Returns the current local date
    today = date.today()
    bid=request.args['bid']
    # name=request.args['name']
    ty=request.args['ty']

    if 'btn' in request.form:
        fdate=request.form['fdate']
        time=request.form['time']
        purpose=request.form['purpose']
    
        q="insert into bookings values (NULL,'%s','%s','%s','%s','%s','%s',curdate(),'pending')"%(session['uid'],bid,ty,fdate,time,purpose)
        id=insert(q)
        
        flash("Booking Completedd successfully")
        return redirect(url_for("user.userhome"))
    return render_template("user_book_external.html",data=data,today=today)
