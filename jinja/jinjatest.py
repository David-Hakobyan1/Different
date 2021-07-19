from jinja2 import Environment, FileSystemLoader

my_dict={'name': 'asd', 'a': 4, 'b': 3}

file_loader = FileSystemLoader('template')
env = Environment(loader=file_loader)

template = env.get_template('jinja.template.jinja')

output = template.render(d=my_dict)
print(output)
