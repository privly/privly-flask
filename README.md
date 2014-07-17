## About ##

Privly is a developing set of browser extensions for protecting content wherever it is posted on the internet. It allows users to view content on any website, without the host site being able to read the content. This content server is meant to store content for users with a Privly extension, but it also provides support for extension-less operation using the [Privly Applications](https://github.com/privly/privly-applications).

For more information on what Privly is, [read about us](https://priv.ly/pages/about).

## Development Status ##

**Alpha**

For information about our development path, please see the [central wiki](https://github.com/privly/privly-organization/wiki/Version-List).

The Privly Flask content server is currently maintained by [Garrett Seward](https://github.com/spetralsun), on behalf of the [Privly Foundation](http://www.privly.org).

## About this Content Server ##

This server currently supports:

* All the applications found in the [Privly Applications](https://github.com/privly/privly-applications) repository.
* Serialized JSON storage for any text content.
* Sharing by email, domain, and IP Address.

**Server API**  

Read about the [API](https://github.com/privly/privly-web/blob/master/API.md).

## Development Server Installation ##

Prerequisites:

* Python 2.X
 * To check what version of Python you are running, type `python --version` in your terminal
* Pip
* Virtualenv 

These shell commands step through a standard installation.

    # Clone this repository and the privly-applications repository.
    # The `--recursive` flag ensures you get the privly-applications
    # repository.
    git clone --recursive https://github.com/privly/privly-flask.git
    cd privly-flask
    
    # You need to setup config. For a development install you should use
    # since you will not need to setup MySQL.
    cp config.py.dist config.py
    vim config.py # or use the editor of your choice on the config 
    
    # Install depedencies and run
    python manage.py init_db # Creates the database
    python manage.py seed_db # Seed the database [optional]
    python manage.py runserver # Starts the server

## Testing the Server

From the projects root directory, run:

        nosetests
        
## Managing Users

The seed command (run with `python manage.py seed_db`) will create several users for you in development, including: `admin@priv.ly`, `demonstration@priv.ly`, `development@priv.ly`. All these accounts have the same password, `password`. 

## Testing/Submitting Bugs ##

If you have discovered a bug, only [open a public issue](https://github.com/privly/privly-flask/issues/new) on GitHub if it could not possibly be a security related bug. If the bug affects the security of the system, please report it privately at [privly.org](http://www.privly.org/content/bug-report). If it is an urgent issue, please email privly@privly.org. We will then fix the bug and follow a process of responsible disclosure.

## Developer Documentation ##

Discussion of system concepts and high level processes are found in the [central wiki](https://github.com/privly/privly-organization/wiki).

## Resources ##

[Foundation Home](http://www.privly.org)  
[Privly Project Repository List](https://github.com/privly)  
[Development Mailing List](http://groups.google.com/group/privly)  
[Testing Mailing List](http://groups.google.com/group/privly-test)  
[Announcement Mailing List](http://groups.google.com/group/privly-announce)  
[Central Wiki](https://github.com/privly/privly-organization/wiki)  
[Submit a Bug](http://www.privly.org/content/bug-report)  
[IRC](http://www.privly.org/content/irc)  
[Production Content Server](https://privlyalpha.org)  
[Development Content Server](https://dev.privly.org)  
[Download Extension](https://priv.ly/pages/download)  

## Contacts ##

**Email**:  
Community [the 'at' sign] privly.org  

**Mail**:  
Privly  
PO Box 79  
Corvallis, OR 97339 
 
**IRC**:  
Contact the Nick "[spectralsun](https://github.com/spectralsun)" or "[smcgregor](https://github.com/smcgregor)" on irc.freenode.net #privly

**Issue**:  
If you [open an issue](https://github.com/privly/privly-flask/issues) on this repository, you'll get someone's attention.