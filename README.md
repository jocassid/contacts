# contacts
An example Django app for a demo/tutorial

## Notes
- created contacts directory to hold source code (did this via
`git clone`) and ran `django-admin startproject contacts .` from 
within it.  I think if you leave off the `.` you might get an 
extra level of directories
- then ran `./manage.py startapp main` to create a `main` directory
for models views etc.  Technically I could skip this step and
add a models and views in where the `settings.py` file lives.
- There are migrations in the Django codebase so you can run
`./manage.py migrations` at this point to setup tables for sessions
content types, etc.
- add `'main'` to the list of `INSTALLED_APPS` in `settings.py`
- added `include` for main app to `contacts/urls.py`
- make sure to add `./manage.py` to source control
- added STATICFILES_DIRS to create a project-wide location for static files
- Downloaded latest JQuery code and placed in `static` directory.