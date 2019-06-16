PyEL
=====

This project aims to facilitate the execution of codes before and after a method using decorator.
the Decorator @PreEL and @PosEL accept as input codes to run, you can use simple codes as a `logging` or else more complex codes written by you.

Installing
----------

Install and update using `pip`_:

.. code-block:: text

    pip install PyEL


A Simple Example
----------------

.. code-block:: python

    from pyel import PreEL

    @PreEL('logging.info("Potato")')
    def function():
        pass



Example with variables
----------------

.. code-block:: python

    from pyel import PreEL

    @PreEL('logging.error("Log:{}".format(#param))')
    def function(param):
        pass


Example with your code
----------------

.. code-block:: python

    from pyel import PosEL

    @PosEL('yourpackage.subpackage.yourfunction(#param)')
    def function(param):
        pass