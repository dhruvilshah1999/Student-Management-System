from flask import Flask, render_template, request, url_for, redirect, session
import pymongo
import bcrypt
#set app as a Flask instance 
app = Flask(__name__)
app.secret_key = "testing"
#connoct to your Mongo DB database
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# #Create Database
# mydb = client['total_records']
#get the database name
db = client.get_database('total_records')
db_S = client.get_database('Students')
#get the particular collection that contains the data
records = db.register
Student_records = db_S.register


#assign URLs to have a particular route 
@app.route("/", methods=['post', 'get'])
def index():
    message = ''
    #if method post in index
    if "email" in session:
        return redirect(url_for("logged_in"))
    if request.method == "POST":
        user = request.form.get("fullname")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        #if found in database showcase that it's found 
        user_found = records.find_one({"name": user})
        email_found = records.find_one({"email": email})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('index.html', message=message)
        if email_found:
            message = 'This email already exists in database'
            return render_template('index.html', message=message)
        if password1 != password2:
            message = 'Passwords should match!'
            return render_template('index.html', message=message)
        else:
            #hash the password and encode it
            hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
            #assing them in a dictionary in key value pairs
            user_input = {'name': user, 'email': email, 'password': hashed}
            #insert it in the record collection
            records.insert_one(user_input)
            
            #find the new created account and its email
            user_data = records.find_one({"email": email})
            new_email = user_data['email']
            #if registered redirect to logged in as the registered user
            return render_template('logged_in.html', email=new_email)
    return render_template('index.html')



@app.route("/login", methods=["POST", "GET"])
def login():
    message = 'Please login to your account'
    if "email" in session:
        return redirect(url_for("logged_in"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        #check if email exists in database
        email_found = records.find_one({"email": email})
        if email_found:
            email_val = email_found['email']
            passwordcheck = email_found['password']
            #encode the password and check if it matches
            if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
                session["email"] = email_val
                return redirect(url_for('logged_in'))
            else:
                if "email" in session:
                    return redirect(url_for("logged_in"))
                message = 'Wrong password'
                return render_template('login.html', message=message)
        else:
            message = 'Email not found'
            return render_template('login.html', message=message)
    return render_template('login.html', message=message)

@app.route('/logged_in')
def logged_in():
    if "email" in session:
        email = session["email"]
        return render_template('logged_in.html', email=email)
    else:
        return redirect(url_for("login"))

@app.route('/Insert')
def Insert():
    return render_template('Insert.html')

@app.route('/insert', methods=["POST", "GET"])
def insert():
    if "email" in session:
        email = session["email"]
        enrollmentno = request.form.get("enrollmentno")
        StdName = request.form.get("fullname")
        batchyr = request.form.get("batchyr")
        aadharcard = request.form.get("aadharcard")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        number = request.form.get("number")
        emailp = request.form.get("email")
        Parentnumber = request.form.get("Parentnumber")
        Parentemail = request.form.get("Parentemail")
        Homeadd = request.form.get("Homeadd")
        Coursecode = request.form.get("Coursecode")
        Coursetype = request.form.get("Coursetype")
        Branchcode = request.form.get("Branchcode")
        Branchname = request.form.get("Branchname")
        Collegecode = request.form.get("Collegecode")
        Collegename = request.form.get("Collegename")
        Currentstatus = request.form.get("Currentstatus")
        CPI = request.form.get("CPI")
        CGPA = request.form.get("CGPA")
        Currentsem = request.form.get("Currentsem")
        Termend = request.form.get("Termend")
        # Enrollment_No = batchyr+Collegecode+Coursecode+Branchcode+
        Std_input = {'enrollmentno':enrollmentno,'StdName': StdName,'batchyr': batchyr,'aadharcard': aadharcard,'birthday': birthday,'gender': gender,
                     'number': number,'emailp': emailp,'Parentnumber': Parentnumber,'Parentemail': Parentemail,'Homeadd': Homeadd,'Coursecode': Coursecode,
                     'Coursetype': Coursetype,'Branchcode': Branchcode,'Branchname': Branchname,'Collegecode': Collegecode,'Collegename': Collegename,
                     'Currentstatus': Currentstatus,'CPI': CPI,'CGPA': CGPA,'Currentsem': Currentsem,'Termend': Termend}
        Student_records.insert_one(Std_input)
        print("Record Added Successfully")
        return render_template('Insert.html', StdName=StdName,email=email)

@app.route('/fetch')
def fetch():
    return render_template('fetch.html')

@app.route('/fetcher', methods=["POST", "GET"])
def fetcher():
    # err_no=request.values.get("enrollmentno")
    # task=Student_records.find({"enrollmentno":err_no})
    if "email" in session:
        email = session["email"]
        key = request.values.get("key")
        refer = request.values.get("refer")
        task = Student_records.find({refer: key})
    return render_template('viewfetch.html',search=task,email=email)


@app.route('/updation', methods=["POST", "GET"])
def updation():
    if "email" in session:
        email = session["email"]
        enrollmentno = request.form.get("enrollmentno")
        StdName = request.form.get("fullname")
        batchyr = request.form.get("batchyr")
        aadharcard = request.form.get("aadharcard")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        number = request.form.get("number")
        emailp = request.form.get("email")
        Parentnumber = request.form.get("Parentnumber")
        Parentemail = request.form.get("Parentemail")
        Homeadd = request.form.get("Homeadd")
        Coursecode = request.form.get("Coursecode")
        Coursetype = request.form.get("Coursetype")
        Branchcode = request.form.get("Branchcode")
        Branchname = request.form.get("Branchname")
        Collegecode = request.form.get("Collegecode")
        Collegename = request.form.get("Collegename")
        Currentstatus = request.form.get("Currentstatus")
        CPI = request.form.get("CPI")
        CGPA = request.form.get("CGPA")
        Currentsem = request.form.get("Currentsem")
        Termend = request.form.get("Termend")
        # Enrollment_No = batchyr+Collegecode+Coursecode+Branchcode+
        Student_records.update({"enrollmentno":enrollmentno}, {'$set':{'StdName': StdName,'batchyr': batchyr,'aadharcard': aadharcard,'birthday': birthday,'gender': gender,
                     'number': number,'emailp': emailp,'Parentnumber': Parentnumber,'Parentemail': Parentemail,'Homeadd': Homeadd,'Coursecode': Coursecode,
                     'Coursetype': Coursetype,'Branchcode': Branchcode,'Branchname': Branchname,'Collegecode': Collegecode,'Collegename': Collegename,
                     'Currentstatus': Currentstatus,'CPI': CPI,'CGPA': CGPA,'Currentsem': Currentsem,'Termend': Termend}})
        print("Record Added Successfully")
        return render_template('update.html', StdName=StdName,email=email)

@app.route("/update")
def update():
    enrollmentno=request.values.get("enrollmentno")
    task=Student_records.find({"enrollmentno":enrollmentno})
    return render_template('update.html',search=task)


@app.route("/logout", methods=["POST", "GET"])
def logout():
    if "email" in session:
        session.pop("email", None)
        return render_template("signout.html")
    else:
        return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)
