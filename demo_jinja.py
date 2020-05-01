"""This module demonstrates various features of Jinja2 template rendering
engine. This code is meant for learning the functionalities of Jinja and for a
quick reference.

In order to keep the code simple, most functions will not use any arguments.

@author: Nikhil Pattisapu, iREL, IIIT-H"""


from jinja2 import Environment, FileSystemLoader


ENV = Environment(loader=FileSystemLoader('templates')) # Global variable
ENV.line_statement_prefix = '#'


def demo_delimiters_variables():
    """Demos delimiters"""
    template = ENV.get_template('demo_delimiters_variables.html')
    fav_ragas = ['hamsadhwani', 'kalyani', 'kharaharapriya']
    kritis = [{'kriti': 'Nidhichaala sukhama'}, {'kriti': 'Nadatanumanisham'}]
    res_str = template.render(fav_ragas=fav_ragas, fav_kritis=kritis)
    with open('rendered_html/demo_delimiters_variables.html', 'w') as res:
        res.write(res_str)


def demo_filters():
    """Demo filters"""
    template = ENV.get_template('demo_filters.html')
    num, name = -7.63e1, 'nikhil Pattisapu '
    mlist, mlist2 = [3, 2, 4, 3], [{'k1':True, 'k2':30}, {'k1':False, 'k2':20}]
    mdict = {'k1': 40, 'k2': 50}
    res_str = template.render(num=num, name=name, mlist=mlist, mlist2=mlist2,
                              mdict=mdict)
    with open('rendered_html/demo_filters.html', 'w') as res:
        res.write(res_str)


def demo_tests():
    """Demo filters"""
    template = ENV.get_template('demo_tests.html')
    num, name = -7.63e1, 'nikhil Pattisapu '
    mlist, mlist2 = [3, 2, 4, 3], [{'k1':True, 'k2':30}, {'k1':False, 'k2':20}]
    mdict = {'k1': False, 'k2': True}
    mbool = False

    def identity_func(inp):
        return inp

    res_str = template.render(mbool=mbool, num=num, name=name, mlist=mlist,
                              mlist2=mlist2, mdict=mdict, mfunc=identity_func)
    with open('rendered_html/demo_tests.html', 'w') as res:
        res.write(res_str)

def demo_whitespace_control():
    """Renders HTMLs which shows how whitespace can be controlled in jinja2"""
    template = ENV.get_template('demo_whitespace_control.html')
    ENV.trim_blocks = False
    ENV.lstrip_blocks = False
    res_str = template.render()
    with open('rendered_html/demo_whitespace_control.html', 'w') as res:
        res.write(res_str)


if __name__ == '__main__':
    # demo_delimiters_variables()
    # demo_filters()
    # demo_tests()
    demo_whitespace_control()
