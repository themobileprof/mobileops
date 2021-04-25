# Python 3
# Author: Samuel Anyaele
# scripts/help/modules/github.py

import subprocess
import time
import os
from . import misc




class Github:
    def __init__(self):

        # Pretests to ensure system is github ready
        # 1. Ensure github cli is installed
        self.gh_inst_var = misc.which("gh")

        # 2. Ensure github cli is authenticated
        self.gh_auth_var = True if subprocess.run(['gh', 'auth', 'status'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False







    # Install github cli
    def gh_inst(self):
        print("Installing Github CLI...")
        print("ensure you are logged in as an admin user")
        subprocess.run(['sudo', 'su'], stderr=subprocess.DEVNULL)
        time.sleep(2)
        return True if subprocess.run(['apt', 'install', '-y', 'gh'], stdout=subprocess.DEVNULL) == 0 else False







    # Configure github cli
    def gh_auth_login(self):
        print("Configuring Github CLI...")
        print("Please ensure you copy the number below before pressing <Enter>, you'll past the number in the website that will open")
        time.sleep(4)
        subprocess.run(['gh', 'auth', 'login', '-w'])





    # Clone a Repo
    def gh_repo_clone(self):
        repo = input("What Repo are you Cloning?: ")
        directory = input("What do you want to call this project? \nPress <Enter> for default: ")
        clone_result = True if subprocess.run(["gh","repo","clone",repo,directory], stdout=subprocess.DEVNULL).returncode == 0 else False

        if clone_result:
            print("\nThe {} project directory has been successfully created".format(repo))

        return clone_result




    # Create a Pull Request
    def gh_pr_new(self,base="master",head="dev"):
        return True if subprocess.run(["gh","pr","create","--assignee","@me","--base",base,"--head",head,"--fill"]).returncode == 0 else False






    # Create new github repo
    def gh_repo_new(self):
        directory = os.path.basename(os.getcwd())
        public = input("Should this Github repo be visible to the public?: Y/n ")
        if public.lower() in ("y","yes"):
            visible = "--public"
        else:
            visible = "--private"

        return True if subprocess.run(["gh","repo","create",directory,visible,"--confirm"]).returncode == 0 else False



    # Fork a Repo
    def gh_repo_fork(self):
        repo = input("What Repo are you collaborating on?: ")
        # Get directory name
        repo_file = repo.split("/")
        dir_name = repo_file[-1].split(".")
        
        is_cloned = True if subprocess.run(["gh","repo","fork",repo,"--clone=true","--remote=true"]).returncode == 0 else False
        if os.path.exists(dir_name[0]):
            os.chdir(dir_name[0])

        if is_cloned:
            print("Enter \"cd ",dir_name[0],"\" to enter into the project directory")

        return is_cloned




    # List a user's repos
    def gh_repo_list(self,owner=""):
        return subprocess.run(["gh","repo","list",owner], capture_output=True, text=True).stdout



    # Add local SSH key to Github
    def gh_ssh_add(self):
        public_key = os.getenv('HOME')+'/.ssh/id_rsa.pub'
        return True if subprocess.run(["gh","ssh-key","add",public_key]).returncode == 0 else False
