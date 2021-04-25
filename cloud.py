#!/usr/bin/env python3
# Python 3

# Author: Samuel Anyaele
# Source: TheMobileProf.com
#
# Manage basic Cloud installations and management on Terminal
#
# CLI Includes Google Cloud, Amazon AWS, Microsoft Azure, Digital Ocean, Alibaba Cloud
#
########################
from modules import misc.py




def entry (provider):
    print("You are currently on the " + provider + " Cloud CLI")


def no_support ():
    print("Sorry, this Provider is currently not supported")

def main ():
    # Intro
    print ("""Welcome to TheMobileProf Cloud CLI tool

    What Cloud Platform do you want to manage?
    1. Google Cloud
    2. Amazon AWS Cloud
    3. Microsoft Azure Cloud
    4. Digital Ocean
    5. Alibaba Cloud
    6. Huawei Cloud
    """)

    cloud = input("Select an option [1-5]: ")

    if cloud == '1':
        entry ("Google")
        # check if Gcloud is installed
        if not misc.which("gcloud"):
            # Install Gcloud
            pass
    elif cloud == '2':
        entry ("AWS")
        no_support
    elif cloud == '3':
        entry ("Azure")
        no_support
    elif cloud == '4':
        entry ("Digital Ocean")
        no_support
    elif cloud == '5':
        entry ("Alibaba")
        no_support
    elif cloud == '6':
        entry ("Huawei")
        no_support
    elif cloud == '0':
        print("Menu Cancelled")

    else:
        print("Sorry, we cannot identify the Cloud service you chose")

if __name__ == "__main__":
    main()
