Pep8ify: Clean your code with ease
==================================


Pep8ify is a library that modifies python source code to conform to
`pep8<http://www.python.org/dev/peps/pep-0008/>`_.


Installation
------------

To install pep8ify, simply: ::

    $ pip install pep8ify


Usage
------------

To print a diff of changes that pep8ify will make against a particular source
file or directory: ::

    $ pep8ify source_folder

To have those changes written to the files: ::

    $ pep8ify -w source_folder

By default, this will create backup files for each file that will be changed.
You can add the `-n` option to not create the backups. Please do not do this
if you are not using a version control system. Although this code is
well-tested, there are most likely bugs still.

For more options about running particular fixers, read the
`lib2to3 documentation<http://docs.python.org/library/2to3.html>_`. This
library is built on top of that one.

Fixes
------------

A list of the available fixers can be found with the following: ::

    $ pep8ify -l
    Available transformations for the -f/--fix option:
    blank_lines
    compound_statements
    extraneous_whitespace
    imports_on_separate_lines
    indentation
    maximum_line_length
    missing_newline
    missing_whitespace
    tabs
    trailing_blank_lines
    trailing_whitespace
    whitespace_around_operator
    whitespace_before_inline_comment
    whitespace_before_parameters
