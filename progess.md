[^MarkdownGuide]
[^LearnDJango]
# Completado:

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
## versiones de prueba de las vistas de index y detalle
- [x] Se mejora pagina [curso_index](cursos/templates/cursos/curso_index.html) para agregar filtro  y pequeñas correcciones de estilo
- [x] Se agrega la funcion, vista y url necesaria para poder tener un boton en [Home](pages/templates/pages/home.html) que lleve al [curso_index](cursos/templates/cursos/curso_index.html)
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
## Escuelas y categorias:
- [x] se agrega categorias a modelo de cursos
- [x] se agrega modelo de escuelas
- [x] se agrega escuelas a modelo de curso
- [ ] se agrega filtros por etiquetas y escuelas
## Funcion Estudiantes y Matriculas
- [X] modificado el modelo de estudiantes segun la necesidad
- [ ] Generar formulario para crear perfil de estudiante
- [ ] Revisar y  modificar modelo de matricula
- [ ] Generar formulario para matricula

# Pendiente:

## Formularios: 
*https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Forms#proceso_del_manejo_de_formularios_de_django*
- formulario de registro de usuario
- formulario de matricula

## vistas: 
*https://realpython.com/get-started-with-django-1/#create-the-views*
- Estilizar home page: 
  - [ ] boton para login 
  - [ ] logout 
  - [ ] register 
  - [ ] password reset
  - [ ] mostrar el nombre del usuario logeado
- user details page: 
  - [ ] login 
  - [ ] logout 
  - [ ] cambio de contraseña 
  - [ ] detalles del usuario logeado
- ver cursos: 
  - [ ] cursos_index.html debe mostrar las categorias
- detalles de cursos:
  - [ ] mostrar detalles del curso
  - [ ] boton para matricula
- registro de usuario:
  - [ ] Debe permitir agregar detalles de usuario como documento y fecha de nacimiento
- matricular curso
- cursos matriculados
- sesiones agendadas
- Mejorar diseño de paginas
  - [ ] [login](templates/registration/login.html)
  - [ ] [signup](templates/registration/signup.html)
  - [ ] [home](pages/templates/pages/home.html)
  - [ ] [curso details](cursos/templates/cursos/curso_detail.html)
  - [ ] [curso index](cursos/templates/cursos/curso_index.html)

[^TutorialPortfolio]: https://realpython.com/get-started-with-django-1
[^MarkdownGuide]: https://markdownguide.offshoot.io/extended-syntax/
[^LearnDJango]:https://learndjango.com/