# Search Solver
Repository developed with the aim of keeping in touch with artificial 
intelligence, in detailed, 
[search and mathematical optimization](https://en.wikipedia.org/wiki/Artificial_intelligence#Search_and_optimization).  
## Execution
In order to execute the definition of your problem in the solver, 
you have to execute the command below in root folder.
```
python3 -m search <definition> <search-algorithm> <arg0, arg1, ..., argn>
```
You ought to consider that each definition can have different 
positional or optional arguments.
## How can I make...
### My own definition of a problem
1. Create your file _.py_ in _search.definitions_ module.
    * Take into account that your class must extend _Interpretation_ class 
    and implement all the methods.
1. Create a _main_ function to get the additional arguments and 
   the call to the search algorithm.
   * In all the definition files, the argparse module is used in order to 
   get the arguments properly.
   * You can use `search.parse_algorithms(str)` 
   to create the parser and take the first argument.
1. Import the _main_ function in `search/definitions/__init__.py`, 
   create the most suitable alias for it.

In addition, you can do a pull request to share your definition! :grin:
### My algorithm solver
1. Create your file _.py_ in _search_ module.
    * Take into account that your class must extend _Solver_ class 
    and implement all the methods
1. Create a _main_ function to create the instance of the solver 
an solve the interpretation.
1. Import the _main_function in `search/__init__.py`, create the 
most suitable alias for it.
1. You must add the choice in the parser method in `search/__init__.py`. 
In case it is not done, you can not resolve the interpretations implemented.

In addition, you can do a pull request to share your algorithm! :grin:

## Unit testing
The module used to test the project is [_unittest_](https://docs.python.org/3/library/unittest.html).
In order to execute all the tests:
```
python3 -m unittest test
```