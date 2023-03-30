from flask import *
from database import *
import uuid

principal=Blueprint('principal',__name__)

@principal.route('/principalhome')
def principalhome():
    return render_template('principalhome.html')
