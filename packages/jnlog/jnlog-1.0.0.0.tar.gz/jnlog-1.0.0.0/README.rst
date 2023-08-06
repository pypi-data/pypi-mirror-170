jnlog
=====

**Simple to use colored text logger for python**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How to use:
^^^^^^^^^^^

.. code:: python

   from jnlog import jnlog
   name = 'MyScript' #used to identify one logger in many
   loglevel = jnlog.INFO
   logger = jnlog.jnlog(name=name, loglevel=loglevel)
   logger.info('Hello, World!')

result:
^^^^^^^

|image0|

See example.py for more

loglevels:
~~~~~~~~~~

================== ==== ======= =====
fn:raw-latex:`\ll` INFO WARNING ERROR
================== ==== ======= =====
info()             +    -       -
warn()             +    +       -
error()            +    +       +
================== ==== ======= =====

license: MIT
~~~~~~~~~~~~

.. |image0| image:: https://gitlab.com/seeklay/jnlog/-/raw/main/prev.png
