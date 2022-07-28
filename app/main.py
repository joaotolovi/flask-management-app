from flask import render_template, Blueprint, Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin
from flask import request
from flask_login import login_required, current_user
from .models import Owner, Cars
from . import db

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/owners", methods=['POST','GET'])
@login_required
def owners():
    name=''
    messages=[]
    if request.method == 'POST':
        if 'del_id' in request.form:
            id_=request.form['del_id']
            owner = Owner.query.filter_by(id=id_).first()
            if owner:
                db.session.delete(owner)
                db.session.commit()
                messages.append('Deleted user')
                

        elif 'test' in request.form: 
            name = request.form['test']
            user = Owner.query.filter_by(name=name).first()
            if name=='':name=messages.append('Campo vazil')
            elif user==None:
                db.session.add(Owner(name=name))
                db.session.commit()
                messages.append('Created user')
            else:messages.append('User already exists')
            

    return Response(
        render_template('owners.html', owners=Owner.query.all(), messages=messages),
        status=200,
    )

@main.route("/cars", methods=['POST','GET'])
@login_required
def cars():
    messages=[]
    if request.method == 'POST':
        if 'del_id' in request.form:
            id_=request.form['del_id']
            car = Cars.query.filter_by(id=id_).first()
            if car:
                db.session.delete(car)
                db.session.commit()
                messages.append('Deleted car')
            
        if 'owner' in request.form:
            owner = Owner.query.filter_by(name=request.form['owner']).first()
            owner_cars_size = len(owner.mycars)
            if owner_cars_size>=3:
                messages.append('User has reached car limit.')
            else:
                car = Cars(color=request.form['color'], model=request.form['model'], myowner=owner)
                db.session.add(car)
                db.session.commit()
            
    return render_template('cars.html', cars=Cars.query.all(), owners=Owner.query.all(), messages=messages)
        
'''if __name__ ==  '__main__':
    db.create_all()
    main.run(debug=True)
'''
