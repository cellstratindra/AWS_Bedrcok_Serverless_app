
## Python Syntax Review

*●* Review basic Python syntax

*●* The ‘with’ statement

*●* Datatypes overview (list, dict, tuple, set, string)

## Advanced Data Types and Functional Programming

*●* Datatypes: namedtuple, defaultdict, ordereddict, deque, etc

*●* Functional programming: closures and decorators

## Object-oriented Programming in Python

*●* Class syntax

*●* Class vs. Instance attributes

*●* Attribute and method visibility

*●* Inheritance

*●* The @classmethod, @staticmethod, and @property decorators

## Testing in Python

*●* Review of key testing concepts: unit, functional, integration, etc

*●* Overview of test-driven development (TDD) concepts

*●* Writing tests unit test with a test-first approach

*●* Unit testing with the unittest module

*●* Creating test suites with nosetests as a test collector

*●* Performing simple code coverage analysis with coverage

## Python Parallelism and Concurrency

*●* Process class and using the multiprocessing module

*●* Synchronization between process

*●* Exchanging objects between process: pipes, queues, and circular buffers

*●* Sharing state between process (shared memory and server process)

*●* Python Semaphores and Mutex

*●* Synchronization events

*●* Overview of asyncio

## Network Programming

*●* Brief overview of REST and HATEOAS topics of API design

*●* Using the Python Requests module to consume REST API’s

*●* Creating a simple JSON-REST client using Flask

## Context Manager (as time permits)

*●* What is context manager

*●* Working with a context manager: contextlib.closing, enter and exit

*●* Using contextlib.contextmanager

### Follow PEP Guide: https://pep8.org/  for instructions & recommendations

#### Some important points on code structure and format
- Import statements go at the top , and each have their own line
- Indent code using spaces instead of tabs
- Use four spaces for each indentation level
- Limit lines to 79 characters ( 72 for docstrings/comments)
- Separate functions and classes by 2 blank lines
- Imports should usually be on separate lines
- Winthin classes separate methods by 1 blank line
- No spaces around function calls, indexes , keywords args

#### Python whitespace conventions

| DO | DON'T |
|-----------------|-----------------|
| spam(ham[1], {eggs: 2}) | spam ( ham [ 1 ], { eggs : 2 } ) |
| fn(arg) | fn (arg) |
| dct['key'] = lst[index] | dct [ 'key' ] = lst[ index ] |
| x = 1 | x  =                      1 |
| y = 2 | y  =                      2 |
| hypot = x*x + y*y | hypot = x * x + y * y |
| i = i + 1 | i=i+1|


#### Python Usecases 

*●* Network automation
*●* Web Development
*●* Data Science
*●* Machine Learning
*●* Generative Ai
