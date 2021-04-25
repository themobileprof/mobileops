# Python 3
# Author: Samuel Anyaele
# scripts/help/modules/git.py

import subprocess
import time
import os
from . import misc

class Git:
    def __init__(self):
        # Get current directory
        self.pwd = misc.current_dir()

        # Pre-tests to ensure system is git ready
        # 1A. Ensure git is installed
        self.git_inst_var = misc.which("git")

        # 2A. Ensure git user.name is configured
        config_name=subprocess.run(['git', 'config', 'user.name'], capture_output=True, text=True)
        self.config_name_var = True if config_name.returncode == 0 and config_name.stdout.strip() != "" else False

        # 2B. Ensure git user.email is configured
        config_email=subprocess.run(['git', 'config', 'user.email'], capture_output=True, text=True)
        self.config_email_var = True if config_email.returncode == 0 and config_email.stdout.strip() != "" else False





    # Install git
    def git_inst(self):
        print("Installing Git...")
        print("ensure you are logged in as an admin user")
        time.sleep(2)
        return True if subprocess.run(['apt', 'install', '-y', 'git']) == 0 else False






    # Configure git
    def git_conf(self, config, value=""):
        print("Configuring git ", config)
        time.sleep(1)
        subprocess.run(['git', 'config', '--global', config, value])







    # Initialize a directory for git
    def git_init(self):
        print("Please ensure you are INSIDE the directory you want to initialize on git. ")
        print("You are currently inside " + self.pwd)
        time.sleep(2)
        print("Do you want to continue?")
        start = input("Yes/No: ")

        if start.lower() == 'yes' or start.lower() == 'y':
            # Start git init
            print("Git is initializing in this directory")
            git_init = subprocess.run(["git","init"])
            
            if git_init.returncode == 0:
                return True
            else:
                return False
        else:
            return False







    # Stage files for git
    def git_add(self):
        return True if subprocess.run(['git', 'add', '-A'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False



    # Commit Staged files with a commit message
    def git_commit(self, description=""):
        if description == "":
            description = input("Label the changes you made: ")
        return True if subprocess.run(["git","commit","-m",description], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False


    
    # Git checkout for navigating branches and undoing changes
    def git_checkout(self, opt1, opt2=""):
        if opt2 == "":
            commands = ["git","checkout",opt1]
        else:
            commands = ["git","checkout",opt1,opt2]
        
        return True if subprocess.run(commands, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False




    # Confirm a Fork
    def confirm_fork(self):
        remotes = subprocess.run(["git","remote","-v"], capture_output=True, text=True).stdout

        if remotes.find("upstream") == -1:
            return False
        else:
            return True




    # Git Undo a project
    def git_stash(self):
        # Add files before stashing them
        self.git_add()

        # Stash changes
        stash = True if subprocess.run(["git","stash"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False
        if stash:
            return True if subprocess.run(["git","stash","clear"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else False




    # Git push to Remote repo
    def git_push(self,local,option="",remote="origin"):
        return True if subprocess.run(["git","push",option,remote,local], stdout=subprocess.DEVNULL).returncode == 0 else False

    

    # git pull updates from remote
    def git_pull(self):
        return True if subprocess.run(["git","pull"], stdout=subprocess.DEVNULL).returncode == 0 else False
    

    # git merge branches
    def git_merge(self,branch):
        return True if subprocess.run(["git","merge",branch], stdout=subprocess.DEVNULL).returncode == 0 else False

    # Git list commit logs
    def git_logs(self):
        return subprocess.run(["git","log","--oneliner"], capture_output=True, text=True).stdout


    # Git reset to previous commits
    def git_reset(self):
        commit = input("Input the commit code you want to go back to: ")
        return True if subprocess.run(["git","reset","--hard",commit], stdout=subprocess.DEVNULL).returncode == 0 else False









