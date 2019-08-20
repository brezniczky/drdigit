DrDigit
=======

DrDigit is a digit doctoring detection package at an early stage.
If interested in contributing, please feel free to contact me.

Requirements
------------

DrDigit requires Python 3.5 or later.

Concept
-------

The tests are based on the statistics of the last digit of numbers which are 
assumed to have a uniform distribution.

On a smaller scale, you can query for the probablity of a digit sequence using 
probability mass functions represented by Python functions.

There are larger scale tests for a sequence of digit groups. This is so to 
support situations where different groups are expected to be doctored by 
different people - testing for an overarching, consistent anomaly could be too 
strict in such cases.

Based on the current features (entropy, digit repetition, coincident digits in 
parallel sequences), it is possible to sort a data frame containing digit groups 
by probability, so then it is possible to inspect if there is any apparent 
sanity behind the doctoring.

A couple of advice
------------------

* Handle results with care, there is always some uncertainity
* Try to focus on interesting groups, this should yield much sharper results

Quick start
-----------

DrDigit can be installed using pip:

    $ pip install drdigit

More to come ...

Tests
-----

Coming soon ...
