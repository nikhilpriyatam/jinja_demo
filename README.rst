=====
Jinja
=====

Jinja is a powerful template engine. One can define a wide range of templates and then render them by passing values.

* Jinja template file is a plain text file which could have any extension such as html, rst or txt.

* Variables can be modified by filters. 
  
   * Filters are separated from vaariables by a pipe symbol (|)
   * Filters can have optional arguments in paranthesis
   * Multiple filters can be chained together
   * Jinja has several `built-in features <https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters>`__
   * You can also create your own filters.
   * `Ansible <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-with-pip>`__ offers several other filters which can be used with Jinja2.

* Besides filters there are **tests** which can be used to test a variable againt a common expression.

   * To test a variable or expression we add **is** keyword along with the name of the tet after the variable.
   * Tests can accept arguments too. In which case, we use regular paranthesis to pass the arguments.
   * If there is only single argument, then the paranthesis can be dropped.

* Whitespace can be controlled in jinja2. There are two main ways to do that

   * Setting the trim_blocks and lstrip_blocks value in the python code

   .. code-block:: python

      from jinja2 import Environment, FileSystemLoader
      ENV = Environment(loader=FileSystemLoader('templates')) # Global variable
      ENV.trim_blocks = False
      ENV.lstrip_blocks = False

   * Setting the lstrip_block value explicitly in the template

* If the text actually requires special characters such as '{{' which are part of jinja2 syntax, they can be escaped. There is also help available for escaping HTML.
* One of the powerful features of Jinja2 is Template inheritance. It can be used to simplify the templates by splitting them into multiple files.
* Jinja offers several special variables inside control structures which makes writing templates convenient.
* In order to not repeat yourself, Jinja2 allows you to define and use **Macros**
* Jinja allows you to use a range of math, comparisons, logic and other operators in your templates.
* Read the `Template Designer Documentation <https://jinja.palletsprojects.com/en/2.11.x/templates/>`__ for more details.
