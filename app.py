from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = "student_secret"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'UDAY@2004'
app.config['MYSQL_DB'] = 'student_management'
mysql = MySQL(app)
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM admins WHERE username=%s AND password=%s",
            (username,password)
        )
        admin = cur.fetchone()
        if admin:
            session['admin'] = username
            return redirect('/dashboard')
    return render_template('login.html')
@app.route('/faculty_login', methods=['GET','POST'])
def faculty_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("""
        SELECT * FROM faculty
        WHERE email=%s AND password=%s
        """,
        (email,password))
        faculty = cur.fetchone()
        if faculty:
            session['faculty'] = faculty[2]
            return redirect('/faculty_dashboard')
    return render_template('faculty_login.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        cur = mysql.connection.cursor()
        cur.execute(
            """
            INSERT INTO users
            (username,email,password,role)
            VALUES (%s,%s,%s,%s)
            """,
            (username,email,password,role)
        )
        mysql.connection.commit()
        message = "Account Created Successfully"
    return render_template(
        'register.html',
        message=message
    )
@app.route('/faculty_register', methods=['GET', 'POST'])
def faculty_register():
    if request.method == 'POST':
        faculty_id = request.form['faculty_id']
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("""
        INSERT INTO faculty
        (faculty_id,name,email,department,password)
        VALUES(%s,%s,%s,%s,%s)
        """,
        (
            faculty_id,
            name,
            email,
            department,
            password
        ))
        mysql.connection.commit()
        return redirect('/faculty_login')
    return render_template('faculty_register.html')
@app.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect('/')
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    total_students = cur.fetchone()[0]
    return render_template(
        'dashboard.html',
        total_students=total_students
    )
@app.route('/faculty_dashboard')
def faculty_dashboard():
    if 'faculty' not in session:
        return redirect('/faculty_login')
    return render_template(
        'faculty_dashboard.html',
        faculty=session['faculty']
    )
@app.route('/students')
def students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    return render_template(
        'students.html',
        students=data
    )
@app.route('/add_student', methods=['GET','POST'])
def add_student():
    print(request.form)
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form.get('dob')
        email = request.form['email']
        phone = request.form['phone']
        department = request.form.get('department','')
        address = request.form.get('address')
        cur = mysql.connection.cursor()
        cur.execute("""
        INSERT INTO students
        (
            student_id,
            name,
            gender,
            dob,
            email,
            phone,
            department,
            address
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            student_id,
            name,
            gender,
            dob,
            email,
            phone,
            department,
            address
        ))
        mysql.connection.commit()
        return redirect('/students')
    return render_template('add_student.html')
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form['department']
        address = request.form['address']
        cur.execute("""
        UPDATE students
        SET
            student_id=%s,
            name=%s,
            gender=%s,
            dob=%s,
            email=%s,
            phone=%s,
            department=%s,
            address=%s
        WHERE id=%s
        """,
        (
            student_id,
            name,
            gender,
            dob,
            email,
            phone,
            department,
            address,
            id
        ))
        mysql.connection.commit()
        return redirect('/students')
    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cur.fetchone()
    return render_template(
        'edit_student.html',
        student=student
    )
@app.route('/delete_student/<int:id>')
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute(
        "DELETE FROM students WHERE id=%s",
        (id,)
    )
    mysql.connection.commit()
    return redirect('/students')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)