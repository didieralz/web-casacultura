[^MarkdownGuide]
[^LearnDJango]
# Tareas:

## proyecto inicalizado
## app pages inicalizada e instalada
- [x] urls en pages creada
- [x] templates dir creado
- [x] se agrega [Home](pages/templates/pages/home.html)

## Implementacion de bootstrap 5
- [base](templates/base.html) contiene la inicializacion de bootstrap, esto permite ahorrar tiempo al crear nuevas paginas asi:
```html
{% extends "base.html" %}
{% block title %}titulo{% endblock %}
{% block page_content %}
<h1>contenido html</h1>
{% endblock page_content %}
```
## app cursos inicalizada e instalada 
*esta reemplaza la app "pages" del tutorial* [^TutorialPortfolio]
- [x] se agrega placeholder [home](pages/templates/pages/home.html)

## crear el modelo 
*https://realpython.com/get-started-with-django-1/#define-a-model*
- [x] se agregan los modelos: Curso, Estudiante, Matricula, Instructor, Categoria, Sesion, Asistencia
- [x] se ejectuan comando makemigrations y migrate
- [x] se agregan los modelos a [admin](cursos/admin.py)

## agregar datos de prueba a la base de datos
- [x] se han agregado 3 cursos y 2 categorias

## Paginas de cursos index y detalle
- [x] Se mejora pagina [curso_index](cursos/templates/cursos/curso_index.html) para agregar filtro  y pequeñas correcciones de estilo
- [x] Se agrega la funcion, vista y url necesaria para poder tener un boton en [Home](pages/templates/pages/home.html) que lleve al [curso_index](cursos/templates/cursos/curso_index.html)
- [ ] [curso_index](cursos/templates/cursos/curso_index.html) debe mostrar las categorias
- [ ] [curso_details](cursos/templates/cursos/curso_detail.html) mostrar detalles del curso
- [ ] [curso_details](cursos/templates/cursos/curso_detail.html) boton para matricula

## Agregar imagenes
- [x] modificar modelo de cursos para poder subir imagenes *https://realpython.com/get-started-with-django-1/#upload-images*
- [x] Se añaden imagenes desde la interfaz de admin
- [x] se modifican las primeras vistas de index y details para comprobar que las imagenes se renderizan correctamente

## Manejo de  usuarios
- [x] se crea [registration](templates/registration) para las paginas relacionadas al login de usuarrios
- [x] se agrega [login](templates/registration/login.html) para el login de usuarios
- [x] se agrega boton logout en home

## Se crea app Accounts para manejar la logica de las cuentas
*https://learndjango.com/tutorials/django-login-and-logout-tutorial#:~:text=to%20log%20out%3F%22-,Sign%20Up%20Page,-Now%20that%20we*
>The auth app we've now included provides us with multiple authentication views and URLs for handling login, logout, password change, password reset, etc. It notably does not include a view and URL for signup, so we have to configure that ourselves.
- [x] se crea la pagina para el [signup](templates/registration/signup.html) siguiendo los pasos en: [signupTutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial#:~:text=to%20log%20out%3F%22-,Sign%20Up%20Page,-Now%20that%20we)

## Home page: 
- [x] boton para login 
- [x] logout 
- [x] register 
- [x] password reset
- [x] mostrar el nombre del usuario logeado
- [x] boton para navegar a vistas de estudiantes

## Escuelas y categorias:
- [x] se agrega categorias a modelo de cursos
- [x] se agrega modelo de escuelas
- [x] se agrega escuelas a modelo de curso
- [ ] se agrega filtros por etiquetas y escuelas

## registro de usuario:
- [x] generar prmera version
- [ ] Debe permitir agregar detalles de usuario como correo y fecha de nacimiento

## Funcion Estudiantes y Matriculas
- [x] modificado el modelo de estudiantes segun la necesidad
- [x] Generar formulario para crear perfil de estudiante
- [x] Generar vista de estudiantes [Estudiantes_list](cursos/templates/cursos/Estudiante_list.html)
- [x] formulairo de nuevo estudiante debe tener selector de fecha [widget calendario para form](https://pythonassets.com/posts/date-field-with-calendar-widget-in-django-forms/)
- [x] Revisar y  modificar modelo de matricula
- [x] Generar formulario para matricula
- [ ] Generar alternativas del formulario de matricula que traigan el estudiante o el cruso fijo

## Mejorar diseño de paginas
- [ ] [login](templates/registration/login.html)
- [ ] [signup](templates/registration/signup.html)
- [ ] [home](pages/templates/pages/home.html)
- [ ] [curso details](cursos/templates/cursos/curso_detail.html)
- [ ] [curso index](cursos/templates/cursos/curso_index.html)
- [ ] [Estudiante_new](cursos/templates/cursos/estudiante_new.html)
- [ ] [Estudiantes_list](cursos/templates/cursos/Estudiante_list.html)

## Estilizado Home:
- [x] Agregar Nav bar a la plantilla par aque seiempre sea visible la opcion de home, log in y otras
- [ ] Agregar carousel a home page
- [ ] Agregar Mision y vision a home page
- [ ] (opcional) Agregar carousel nuestro equipo con overviews de los profesores creados

## user management: 
- [x] login 
- [x] logout 
- [x] cambio de contraseña 
- [ ] pagina de detalles del usuario logeado
  
## cursos matriculados
- [ ] Consultar cursos matriculados por estudiante
- [ ] Vista calendario de estudiante (requiere featur sesiones)

## sesiones agendadas
- [ ] Formulario para agendar sesiones de clases

[^TutorialPortfolio]: https://realpython.com/get-started-with-django-1
[^MarkdownGuide]: https://markdownguide.offshoot.io/extended-syntax/
[^LearnDJango]:https://learndjango.com/