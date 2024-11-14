#  General Purpose Validator- Breeze Airways


### Objective
 Create a general purpose data validator in python that is initially to support two expectations of the data namely "expect values" and "expect range of values". The 00 design is to allow for future expectations. This is a greatly simplified version of the Great Expectations python module.

### Validator and Expectations: 
The core of the validator accepts the paths to csv files whose contents are to be validated and the path to the file to which the results of the validation are written. The validator also accepts the path to the configuration file (json) that specifies the single expectation suite and the collection of expectations within that suite. it is to leverage classes that provide the validator
implementation of each expectation. For simplicity, the validator knows up front what expectations are supported avoiding the need to dynamically import the modules.

### Configuration 
Each expectation has a code specified by the user, the identifier of the supported expectation together with any params associated with that expectation.
assume the input files contains a header line and that the entire content is well
the
formed. The delimiter is the pipe character and can be relied upon to delimit the fields. There are no multi-line records to be concerned about.
Make use of the
csv.DictReader module.

### Testing  
Covering unit testing.




Please Refer to the image file attached in this repo for more details.

### Prerequisites
please install pytest and pyyaml.

```pip install pytest ```

```pip install pyyaml ```

### Run 
To run, run command

```python main.py```


### Alternatively, you can run build and run the docker image

```docker build -t breeze .```

```docker run -it --name breeze breeze```


### Files in repository
 - Dockerfile
 - README
 - config.yml
 - main.py
 - requirements.txt
 - test.py
 - validator.py
