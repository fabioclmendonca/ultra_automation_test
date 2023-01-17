1) Installing and Running:

   1) Install Python 3.*
   2) Navigate to project folder
   3) Create a Python Virtual Environment (Optional)
   4) Install requirements (pip install -r requirements.txt)
   5) Download and install Google Chrome
   6) Download Chrome Driver based on Google Chrome version. (https://chromedriver.chromium.org/downloads)
   7) Unzip Chrome Driver in a desired folder
   8) Add the folder to the system path.
      1) Windows: set Path=%Path%;>> Chrome Driver folder here <<
      2) Linux/Mac: export Path=$Path:>> Chrome Driver folder here <<
   9) Run test suite using the following command:

       nosetests -v tests/TestSauceDemo.py --with-html --html-file=nosetests.html --with-xunit --xunit-file=nosetests.xml

2) Project Definition:

   2.1) Folder Structure:

       ultra_automation_test
       |_config
       |_page_object
       |_step_definition
       |_tests
       |_.env
       |_.gitignore
       |_README.md
       |_requirements.txt
    
        config:
            Factory method and Abstract factory pattern implemented responsible to build the suitable driver based on config file (.env)
        
        page_object:
            Page Object layer.

        step_definition:
            Step Definition layer. 

        tests:
            Test layer.

        .env:
            File which contains all environment variables tests will use.

        requirements.txt
             Requirements file containing all project dependencies.

