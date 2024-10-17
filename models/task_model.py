import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqlpass974.",
    database="gestion_tareas"
)

cursor = db.cursor()

def get_all_tasks():
    cursor.execute("SELECT * FROM tareas")
    return cursor.fetchall()

def get_task_by_id(task_id):
    cursor.execute("SELECT * FROM tareas WHERE id_tarea = %s", (task_id,))
    return cursor.fetchone()

def create_task(nombre, fecha_tarea, tiempo_estimado, estado, encargado):
    query = "INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nombre, fecha_tarea, tiempo_estimado, estado, encargado))
    db.commit()

def update_task(task_id, nombre, fecha_tarea, tiempo_estimado, estado, encargado):
    query = "UPDATE tareas SET nombre = %s, fecha_tarea = %s, tiempo_estimado = %s, estado = %s, encargado = %s WHERE id_tarea = %s"
    cursor.execute(query, (nombre, fecha_tarea, tiempo_estimado, estado, encargado, task_id))
    db.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tareas WHERE id_tarea = %s", (task_id,))
    db.commit()

def buscar_por_fecha(fecha_inicio, fecha_fin):
        cursor = db.cursor()
        query = "SELECT * FROM tareas WHERE estado = 0 AND fecha_tarea BETWEEN %s AND %s"
        cursor.execute(query, (fecha_inicio, fecha_fin))
        return cursor.fetchall()