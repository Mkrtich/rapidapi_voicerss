# Task Description
https://rapidapi.com/voicerss/api/text-to-speech-1/
Here is the free API from https://www.voicerss.org. It supports 2 methods GET and POST.
Write some automated test cases for the API.

# Solution Notes

- Main tools - Python: Request and Pytest
- Main test objects - GET method and two versions of POST method
- Test types - positive,  negative and some specific tests (audio comparisons, non-standard output checks, default values usage, etc)
- Repo structure
    -  **cfg**: &nbsp; general configs file and the file of test cases
    -  **golden_audios**: &nbsp; golden audio files for some tests
    -  **src**:&nbsp; classes for each request type
    -  **test_generation_system**:&nbsp; prototype of test generation system for the full test. Can be developed and run with parametrization
    -  **tests**:&nbsp; test functions and pytest conftest
    - **requirements.txt**:&nbsp; environment dump
- To make the solution look simple - parametrization runs are skipped on this small set
- Both request methods use the same source of test cases. There are only couple of tests which require different approach
- Several accounts were used during the development, because there are request number limitations. The current credentials are almost fresh. Only a single full run was conducted on it
- Beside the main one - couple of more account keys are setupped for testing inactive state and account limitations
- Tests were prepared using the API documentation info https://www.voicerss.org/api/
 

# Setup and Run Instructions
-- create python virtual evnironment
```sh
python3 -m venv voicerss_venv
```
-- activate the environment
```sh
source voicerss_venv/bin/activate
```
-- install requirements
```sh
pip3 install -r requirements.txt
```
-- 'cd' to the main directory of this repository and run the below command
```sh
python3 -m pytest . -s
```
Successful run looks like this

<img width="1420" alt="Run_Example" src="https://user-images.githubusercontent.com/15815455/217891214-c5cdc486-b233-4270-88fe-112907c7df30.png">
