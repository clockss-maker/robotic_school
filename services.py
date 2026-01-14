from database import connect

# ---------- INIT DATA ----------

def seed_data():
    con = connect()
    cur = con.cursor()

    cur.executemany(
        "INSERT OR IGNORE INTO school_class VALUES(?,?)",
        [(1,"10"),(2,"11"),(3,"12")]
    )

    cur.executemany("""
        INSERT OR IGNORE INTO student VALUES(?,?,?)
    """,[
        (1,"Андрій Коваль",1),
        (2,"Марія Петренко",1),
        (3,"Ігор Шевченко",1),
        (4,"Олена Бойко",2),
        (5,"Дмитро Литвин",2),
        (6,"Анна Романюк",2),
        (7,"Максим Сидоренко",3),
        (8,"Софія Гнатюк",3),
        (9,"Богдан Ткаченко",3),
    ])

    cur.executemany("""
        INSERT OR IGNORE INTO teacher VALUES(?,?,?)
    """,[
        (1,"Іваненко Олег","Робототехніка"),
        (2,"Коваль Наталія","Програмування")
    ])

    cur.executemany("""
        INSERT OR IGNORE INTO equipment VALUES(?,?,?)
    """,[
        (1,"LEGO EV3",5),
        (2,"Arduino набори",7)
    ])

    cur.executemany("""
        INSERT OR IGNORE INTO lesson VALUES(?,?)
    """,[
        (1,"Робототехніка"),
        (2,"Програмування"),
        (3,"Електроніка"),
        (4,"Механіка"),
        (5,"Алгоритми")
    ])

    con.commit()
    con.close()


# ---------- STUDENTS ----------

def find_student(name):
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE name=?", (name,))
    res = cur.fetchone()
    con.close()
    return res


def get_students():
    con = connect()
    cur = con.cursor()
    cur.execute("""
        SELECT student.id, student.name, school_class.name
        FROM student
        JOIN school_class ON student.class_id = school_class.id
    """)
    data = cur.fetchall()
    con.close()
    return data


def add_student(name, class_id):
    con = connect()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO student(name,class_id) VALUES(?,?)",
        (name,class_id)
    )
    con.commit()
    con.close()


def update_student(id, name, class_id):
    con = connect()
    cur = con.cursor()
    cur.execute(
        "UPDATE student SET name=?,class_id=? WHERE id=?",
        (name,class_id,id)
    )
    con.commit()
    con.close()


def delete_student(id):
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()


def search_student(key):
    con = connect()
    cur = con.cursor()
    cur.execute("""
        SELECT student.id, student.name, school_class.name
        FROM student
        JOIN school_class ON student.class_id = school_class.id
        WHERE student.name LIKE ?
    """,(f"%{key}%",))
    data = cur.fetchall()
    con.close()
    return data


# ---------- EQUIPMENT ----------

def get_equipment():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM equipment")
    data = cur.fetchall()
    con.close()
    return data


def add_equipment(name, qty):
    con = connect()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO equipment(name,quantity) VALUES(?,?)",
        (name,qty)
    )
    con.commit()
    con.close()


# ---------- TEACHERS ----------

def get_teachers():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM teacher")
    data = cur.fetchall()
    con.close()
    return data


# ---------- LESSONS ----------

def get_lessons():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM lesson")
    data = cur.fetchall()
    con.close()
    return data

def search_student(key):
    con = connect()
    cur = con.cursor()
    cur.execute("""
        SELECT student.id, student.name, school_class.name
        FROM student
        JOIN school_class ON student.class_id = school_class.id
        WHERE student.name LIKE ?
    """,(f"%{key}%",))
    data = cur.fetchall()
    con.close()
    return data


# ---------- EQUIPMENT ----------

def get_equipment():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM equipment")
    data = cur.fetchall()
    con.close()
    return data


def add_equipment(name, qty):
    con = connect()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO equipment(name,quantity) VALUES(?,?)",
        (name,qty)
    )
    con.commit()
    con.close()


# ---------- TEACHERS ----------

def get_teachers():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM teacher")
    data = cur.fetchall()
    con.close()
    return data


# ---------- LESSONS ----------

def get_lessons():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM lesson")
    data = cur.fetchall()
    con.close()
    return data
