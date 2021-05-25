from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, flash, request
# from werkzeug import generate_password_hash, check_password_hash

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _EnrollNo = _json['Enrollment_Number']
    _name = _json['Full_Name']
    _contact = _json['Contact Number']
    _Male = _json['Gender']
    _date = _json['Birth_Date']
    _OCGPA = _json['Overall CGPA']
    _MCLG = _json['College_info']
    _PYR = _json['Passing_Year']

    _CGPAO = _json['CGPAo']
    _CGPATT = _json['CGPAtt']
    _CGPATTT = _json['CGPAttt']
    _CGPAF = _json['CGPAf']
    _CGPAFF = _json['CGPAff']
    _CGPAS = _json['CGPAs']
    _CGPASS = _json['CGPAss']
    _CGPAE = _json['CGPAe']

    _BACKO = _json['Backlogo']
    _BACKTT = _json['Backlogtt']
    _BACKTTT = _json['Backlogttt']
    _BACKF = _json['Backlogf']
    _BACKFF = _json['Backlogff']
    _BACKS = _json['Backlogs']
    _BACKSS = _json['Backlogss']
    _BACKE = _json['Backloge']

    _EventName = _json['event_name']
    _EventType = _json['event_type']
    _CCLG = _json['event_location']
    _CDATE = _json['event_date']

    if request.method == 'POST':

        query_i=mongo.db.user.insert_one(
        {
            "Enrollment_Number": _EnrollNo,
            "Information": {
                "Full_Name": _name,
                "Contact Number": _contact,
                "Gender": _Male,
                "Birth_Date": _date
            },
            "Qualification": {
                "Overall CGPA": _OCGPA,
                "College_info": _MCLG,
                "Passing_Year": _PYR
            },
            "Grade": {
                "Year1": {
                    "Sem1": {
                        "CGPA": _CGPAO,
                        "Backlog": _BACKO
                    },
                    "Sem2": {
                        "CGPA": _CGPATT,
                        "Backlog": _BACKTT
                    }
                },
                "Year2": {
                    "Sem3": {
                        "CGPA": _CGPATTT,
                        "Backlog": _BACKTTT
                    },
                    "Sem4": {
                        "CGPA": _CGPAF,
                        "Backlog": _BACKF
                    }
                },
                "Year3": {
                    "Sem5": {
                        "CGPA": _CGPAFF,
                        "Backlog": _BACKFF
                    },
                    "Sem6": {
                        "CGPA": _CGPAS,
                        "Backlog": _BACKS
                    }
                },
                "Year4": {
                    "Sem7": {
                        "CGPA": _CGPASS,
                        "Backlog": _BACKSS
                    },
                    "Sem8": {
                        "CGPA": _CGPAE,
                        "Backlog": _BACKE
                    }
                }
            },
            "Participation_information": {
                "event_name": _EventName,
                "event_type": _EventType,
                "event_location": _CCLG,
                "event_date": _CDATE
            }
        }
        )
        resp = jsonify("User added successfully!")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/users')
def users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp

@app.route('/user/<id>')
def user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

@app.route('/update', methods=['PUT'])
def update_user():
    _json = request.json
    _id = _json['_id']

    _EnrollNo = _json['Enrollment_Number']
    _name = _json['Full_Name']
    _contact = _json['Contact Number']
    _Male = _json['Gender']
    _date = _json['Birth_Date']
    _OCGPA = _json['Overall CGPA']
    _MCLG = _json['College_info']
    _PYR = _json['Passing_Year']

    _CGPAO = _json['CGPAo']
    _CGPATT = _json['CGPAtt']
    _CGPATTT = _json['CGPAttt']
    _CGPAF = _json['CGPAf']
    _CGPAFF = _json['CGPAff']
    _CGPAS = _json['CGPAs']
    _CGPASS = _json['CGPAss']
    _CGPAE = _json['CGPAe']

    _BACKO = _json['Backlogo']
    _BACKTT = _json['Backlogtt']
    _BACKTTT = _json['Backlogttt']
    _BACKF = _json['Backlogf']
    _BACKFF = _json['Backlogff']
    _BACKS = _json['Backlogs']
    _BACKSS = _json['Backlogss']
    _BACKE = _json['Backloge']

    _EventName = _json['event_name']
    _EventType = _json['event_type']
    _CCLG = _json['event_location']
    _CDATE = _json['event_date']

    if request.method == 'PUT':
        # do not save password as a plain text
        # _hashed_password = generate_password_hash(_password)
        # save edits
        mongo.db.user.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                                 {'$set': {
            "Enrollment_Number": _EnrollNo,
            "Information": {
                "Full_Name": _name,
                "Contact Number": _contact,
                "Gender": _Male,
                "Birth_Date": _date
            },
            "Qualification": {
                "Overall CGPA": _OCGPA,
                "College_info": _MCLG,
                "Passing_Year": _PYR
            },
            "Grade": {
                "Year1": {
                    "Sem1": {
                        "CGPA": _CGPAO,
                        "Backlog": _BACKO
                    },
                    "Sem2": {
                        "CGPA": _CGPATT,
                        "Backlog": _BACKTT
                    }
                },
                "Year2": {
                    "Sem3": {
                        "CGPA": _CGPATTT,
                        "Backlog": _BACKTTT
                    },
                    "Sem4": {
                        "CGPA": _CGPAF,
                        "Backlog": _BACKF
                    }
                },
                "Year3": {
                    "Sem5": {
                        "CGPA": _CGPAFF,
                        "Backlog": _BACKFF
                    },
                    "Sem6": {
                        "CGPA": _CGPAS,
                        "Backlog": _BACKS
                    }
                },
                "Year4": {
                    "Sem7": {
                        "CGPA": _CGPASS,
                        "Backlog": _BACKSS
                    },
                    "Sem8": {
                        "CGPA": _CGPAE,
                        "Backlog": _BACKE
                    }
                }
            },
            "Participation_information": {
                "event_name": _EventName,
                "event_type": _EventType,
                "event_location": _CCLG,
                "event_date": _CDATE
            }
        }})
        resp = jsonify('User updated successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run()

# {
#   "Enrollment_Number":"170090107022",
#   "Full_Name":"TIM DAVID COOKER",
#   "Contact Number":"9855412367",
#   "Gender":"Male",
#   "Birth_Date":"21-07-1998",
#   "Overall CGPA":"9.06",
#   "College_info":"C.K.P.C.E.T",
#   "Passing_Year":"2021",
#   "CGPAo":"7.93",
#   "Backlogo":"No",
#   "CGPAtt":"8.02",
#   "Backlogtt":"No",
#   "CGPAttt":"8.4",
#   "Backlogttt":"No",
#   "CGPAf":"9",
#   "Backlogf":"No",
#   "CGPAff":"8.45",
#   "Backlogff":"No",
#   "CGPAs":"8.25",
#   "Backlogs":"No",
#   "CGPAss":"8.39",
#   "Backlogss":"No",
#   "CGPAe":"8.9",
#   "Backloge":"No",
#   "event_name":"Tree Plantation",
#   "event_type":"Cultural",
#   "event_location":"S.C.E.T-Surat",
#   "event_date":"2019-11-08"
# }