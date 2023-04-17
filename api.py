from flask import *
from database import *
import uuid

api=Blueprint('api',__name__)



@api.route("/login")
def login():
	data={}

	uname=request.args['username']
	pwd=request.args['password']


	print(uname,pwd)
	q="select * from login where username='%s' and password='%s'"%(uname,pwd)
	res=select(q)
	if res:
		
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return str(data)

@api.route("/make_payment")
def make_payment():
	data={}

	amount=request.args['amount']
	bid=request.args['bid']
	aid=request.args['aid']

	q="insert into payment values (null,'%s','%s',curdate(),'%s','pending')"%(bid,aid,amount)
	insert(q)
	q="update bookings set status='Payment Completed' where bookings_id='%s'"%(bid)
	update(q)
		
	data['status']='success'

	return str(data)


@api.route('/view_my_bookings')
def view_my_bookings():
    data={}
    lid=request.args['log_id']
    q="SELECT * FROM `user`,`bookings`,`amenites`,amenity_type WHERE `user`.`user_id`=`bookings`.`user_id` AND `bookings`.`amenity_id`=`amenites`.`amenity_id` and `amenites`.`amenity_type_id`=`amenity_type`.`amenity_type_id` and bookings.user_id=(select user_id from user where login_id='%s') and type_name='Externally'"%(lid)
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_my_bookings"
    return str(data)



@api.route('/view_booked_dates')
def view_booked_dates():
    data={}
    # lid=request.args['log_id']
    q="select * from bookings inner join USER using (user_id)"
    res=select(q)
    if res:
        data['data']=res
        data['status']="success"
    else:
        data['status']="failed"
    data['method']="view_booked_dates"
    return str(data)