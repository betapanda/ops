from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['localhost']

def test():
    with settings(warn_only=True):
        result = local('python manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    local("git add -p && git commit")
    
def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()
    
def deploy():
    code_dir = '/Users/rene/python/mysite'
    with settings(warn_only=True):
        if local("test -d %s " % code_dir ).failed:
            local("git clone betapanda@gitlab.com/betapanda/ops.git %s " % code_dir)
    with cd(code_dir):
        local("git pull")
        local("touch app.wsgi")