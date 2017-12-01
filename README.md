


                               README.txt   
                            June 11th, 2010


I. Introduction

For more information on the Google App Engine, please visit:

    http://code.google.com/appengine/

The source code of this application does the following:

  1) It 

II. Requirements

III. Setup

2. Google Application Engine Application Setup

Install the Googple Application Engine SDK.  For deployment of your 
application on the Google Application Engine cloud you will need to create a
named application with Google.  Visit http://appengine.google.com and
give your application a name.

A. Modify Source Code to Match Your Configuration

Certain source code files will have to be modified to match your
user-specific configuration information.

The modifications necessary are given below.
  
i. src/app.yaml

Modify the "application:" field to match the name of your application
you registered with the Google Application Engine.


B. Starting Your Application

You are now ready to start a local instance of your Google Application
Engine application for testing purposes.  This is done by using Google's
dev_appserver.py script.  On the Window's platform, this may be
accomplished by the following command line: 

    C:\Python25\python.exe \
        "C:\Program Files\Google\google_appengine\dev_appserver.py" \
        src
        
Where "src" is the src directory of this application.  Pleas note that
there are no line breaks in the above command line.

You may now test your application by navigating to http://localhost:8080


C. Deploying your Application

You may deploy your application to the Google Application Engine cloud by
running the following command:

    C:\Python25\python.exe \
        "C:\Program Files\Google\google_appengine\appcfg.py" update src
        
Once your application is deployed you should be able to access it from
anywhere in the world you have an Internet connection--including from
web-enabled mobile phones and other mobile devices.  If we named our
application "twansform" your URL would be:

http://twansform.appspot.com


IV.  Theory of Operation

          
V. References
          
1. Google Applications Engine References:

   * Google Applications Engine Home:   
      - http://code.google.com/appengine/
     
2. Python References

   * Python Language Home Page
      - http://www.python.org/
      
   * Python Documentation
      - http://www.python.org/doc/
      
   * Python Tutorial
      - http://docs.python.org/tutorial/
