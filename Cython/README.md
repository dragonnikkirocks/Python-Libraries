Basic Idea behind cython: parameters and variables can be declared to have C data types. So basically defining type, and thus increasing execuetion speed.

Commands

python setup.py build_ext --inplace

For performance check:

cython -a furthertesting.pyx where furthertesting is the cython file

Will look something like this:
![image](https://user-images.githubusercontent.com/69155972/127327622-26b06250-137b-46de-9769-40a93d91a245.png)


For more informations:https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html
