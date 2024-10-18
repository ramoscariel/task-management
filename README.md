# task-management

Vídeo: https://youtu.be/WeLWSDYp4E4

Este proyecto se basa en el en el Mini Core de David Terán: 

https://github.com/Davidm2606/FiltrarFechasWeb

Se añadió la funcionalidad de CRUD de tareas, y se utilizó Google Cloud SQL para la base de datos y Render para el despliegue de la aplicación.

Creación de bdd MySQL: 

```sql
CREATE DATABASE gestion_tareas;

USE gestion_tareas;

CREATE TABLE tareas (
	id_tarea INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    fecha_tarea DATE NOT NULL,
    tiempo_estimado INT NOT NULL,
    estado BOOL NOT NULL, -- 0 En progreso, 1 Completado
    encargado VARCHAR(255) NOT NULL
);
```

Insertar datos de prueba:

```sql
USE gestion_tareas;

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Diseñar interfaz de usuario', '2024-10-05', 5, 0, 'Carlos Martínez');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Implementar API de pagos', '2024-10-06', 8, 0, 'Sofía Rodríguez');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Escribir documentación técnica', '2024-10-07', 3, 1, 'Mateo Gómez');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Configurar servidor en AWS', '2024-10-08', 6, 0, 'Valentina Díaz');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Revisar seguridad de la aplicación', '2024-10-09', 4, 1, 'Daniela Pérez');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Realizar pruebas de carga', '2024-10-10', 7, 0, 'Lucas Torres');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Optimizar consultas SQL', '2024-10-11', 5, 0, 'Mariana Flores');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Desarrollar módulo de autenticación', '2024-10-12', 8, 1, 'Gabriel Sánchez');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Diseñar base de datos', '2024-10-13', 6, 1, 'Isabella Romero');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Implementar sistema de notificaciones', '2024-10-14', 7, 0, 'Emilio Castro');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Realizar pruebas unitarias', '2024-10-15', 4, 0, 'Julia Rivas');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Actualizar dependencias del proyecto', '2024-10-16', 3, 1, 'Tomás Fernández');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Corregir errores de interfaz', '2024-10-17', 5, 0, 'Victoria Morales');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Rediseñar página de inicio', '2024-10-18', 6, 1, 'David Castillo');

INSERT INTO tareas (nombre, fecha_tarea, tiempo_estimado, estado, encargado)
VALUES ('Implementar autenticación de dos factores', '2024-10-19', 7, 0, 'Andrea Ruiz');

```
