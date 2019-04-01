import glob
import os
import shutil
import shlex
import subprocess
from django.core.management import call_command

def run():
    for item in glob.glob("apps/*/migrations/*"):
        if os.path.isfile(item):
            os.unlink(item)
        else:
            shutil.rmtree(item)
    for it in glob.glob("apps/*/migrations"):
        open(os.path.join(it, "__init__.py"), "a").close()
    call_command("makemigrations")
    
    for item in glob.glob("apps/*/migrations/*"):
        if os.path.isfile(item):
            if os.uname().sysname == "Linux":
                command = "sed -i '1d' %s" % item
            elif os.uname().sysname == "FreeBSD":
                command = "sed -i '' '1d' %s" % item
            subprocess.call(shlex.split(command))

    for item in glob.glob("apps/*/migrations/0002_*"):
        new_path = "/".join(item.split("/")[0:3]) + "/" + "0002_auto.py"
        os.rename(item, new_path)
