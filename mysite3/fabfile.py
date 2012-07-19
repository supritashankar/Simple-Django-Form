from fabric.api import local

def hello(name="world"):
    print("Hello %s!!" % name)


def prepare_deploy():
    local("./manage.py test books")
