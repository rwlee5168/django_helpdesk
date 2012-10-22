Helpdesk Documentation
==========================================================================
Table of Contents:

    i. Downloading the server application
    ii. Setting up the application
    iii. Getting started with Helpdesk
    iv. Browsing and Features

==========================================================================
SECTION I. DOWNLOADING THE APPLICATION

Welcome to the Helpdesk! This django based web application is designed to give 
assistance to those experiencing wifi problems in the UC Berkeley EECS department.
It is primarily designed for smartphone and cell phone use and incorporates

Make sure your python version is up to date. This project is based on python 
2.7. To check, run the command:

        python -V

If your python version is less then 2.7, we reccommend updating to 2.7.

        how do I update python?
    
You will need pip for some of the installs:

        sudo apt-get install python-pip

If needed, install git, the revision control system used for this project:

        sudo apt-get install git
    
Make a git repository in your home directory, to house ALL your git repositories:

        mkdir ~/GITREPONAME
 
Django is necessary to run the application as it's based on the Django
framework. To install Django enter in the command:

        sudo pip install django

Helpdesk also makes use of Amazon AWS services, primarily Simple Notification 
Service, or SNS, to notify IT staff and Helpdesk members of wifi issues existing
inthe department. Boto, a python library that links amazon services with this
application, is used. In order to install, enter in the command:
        
        sudo pip install boto

This application also includes an SMS based notification feature to alert the 
Helpdesk as well. Specifically, it uses the Twilio python library to do this.
To download, enter in the command: 
        
        sudo pip install twilio

Finally, to download the files necessary to run Helpdesk, use github. Browse to:

        https://github.com/rwlee5168/django_helpdesk

and either fork the repository to your own account for editing on line OR clone
the repository directly onto your new git repo using the commands:

        cd ~/GITREPONAME
        git clone https://github.com/rwlee5168/django_helpdesk.git

==========================================================================
SECTION II. SETTING UP THE APPLICATION

Once all the dependencies are installed, set up is very straight forward.
In order to start the server, enter in the command:

        python manage.py runserver

Bear in mind that you must be in the directory containing manage.py for 
this to work. Afterwards, in your browser, type in the URL:

        localhost:8000

==========================================================================
SECTION III. GETTING STARTED WITH HELPDESK

Now that you have entered the website, you can visit any of the four tabs 
on the main page. Please bear in mind that this site is meant for mobile 
phones and some features may not work if accessed via computer.

The "Troubleshoot" button includes simple fixes that someone struggling with
the wifi could try.

The "Find Us" button shows a map of the location of the Helpdesk office.

The "Call Us" button brings up the dialer on a cellphone and calls the Helpdesk.
Please note that if you are accessing this website from a computer, it will
not work.

The "Send Help" button sends a SNS message to the helpdesk.

==========================================================================
SECTION IV. BROWSING AND FEATURES

