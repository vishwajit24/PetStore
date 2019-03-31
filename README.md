This project contains the calls for CRUD APIs of a pet store. 
The code is written in python2.
The tst folder contains the tests for all the APIs.

This uses the pytest framework for the test to execute.

#To Run the test 

Go to the bin folder and run below 
```
chmod +x installer.sh
./installer.sh
```

# Locally Run

##To Run all the tests 

1) Go to the folder of PetStore/bin
2) Run the below command - 1

```applescript
python run_test.py
```
This will run all the test in present tst folder and will generate the result of the test in result.xml accessible 
under the same the current directory. 

## To Run the individual test

1) Go to the folder of stackexchange
2) Run the below command - 

```applescript
python -m pytest tst/test_create_pet_entry.py -k test_just_passing_mandatory_fields --junitxml=result_file_name.xml
```

## To Run the test in the CI 
Jenkins UserScript
```
cd bin
chmod +x installer.sh
./installer.sh
python run_test.py
```

