from fabric.api import local,settings,run, abort
from fabric.contrib.console import confirm

def test():
    with settings(warn_only=True):
        result = local('python manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def deploy():
    code_dir = '/Users/rene/python/mysite'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")