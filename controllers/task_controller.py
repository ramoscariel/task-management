from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from models.task_model import get_all_tasks, get_task_by_id, create_task, update_task, delete_task, buscar_por_fecha

task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def index():
    tareas = get_all_tasks()
    tareas_actualizadas = [] 

    for tarea in tareas:
        if tarea[4] == 0:
            estado = 'En progreso'
        else:
            estado = 'Completado'

        tarea_actualizada = (tarea[0], tarea[1], tarea[2], tarea[3], estado, tarea[5])
        tareas_actualizadas.append(tarea_actualizada)
    return render_template('index.html', tareas=tareas_actualizadas)

@task_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_tarea = request.form['fecha_tarea']
        tiempo_estimado = request.form['tiempo_estimado']
        estado = request.form['estado']
        encargado = request.form['encargado']
        create_task(nombre, fecha_tarea, tiempo_estimado, estado, encargado)
        return redirect(url_for('task.index'))
    return render_template('create_task.html')

@task_bp.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update(task_id):
    tarea = get_task_by_id(task_id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha_tarea = request.form['fecha_tarea']
        tiempo_estimado = request.form['tiempo_estimado']
        estado = request.form['estado']
        encargado = request.form['encargado']
        update_task(task_id, nombre, fecha_tarea, tiempo_estimado, estado, encargado)
        return redirect(url_for('task.index'))
    return render_template('update_task.html', tarea=tarea)

@task_bp.route('/delete/<int:task_id>', methods=['GET','POST'])
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('task.index'))

# Ruta de búsqueda de tareas
@task_bp.route('/buscar', methods=['POST'])
def buscar_tareas():
    fecha_inicio = request.form['fecha_inicio']
    fecha_fin = request.form['fecha_fin']

    tareas = buscar_por_fecha(fecha_inicio, fecha_fin)

    tareas_con_retraso = []
    for tarea in tareas:
        id_tarea = tarea[0]
        nombre = tarea[1]
        fecha_tarea = tarea[2]
        tiempo_estimado = tarea[3]
        estado = 'En progreso' if tarea[4] == 0 else 'Completado'
        encargado = tarea[5]

        # Calcular el retraso
        fecha_fin_estimada = fecha_tarea + timedelta(days=tiempo_estimado)
        dias_retraso = max((datetime.now().date() - fecha_fin_estimada).days, 0)

        tareas_con_retraso.append((id_tarea, nombre, fecha_tarea, tiempo_estimado, estado, encargado, dias_retraso))

    return render_template('index.html', tareas=tareas_con_retraso)