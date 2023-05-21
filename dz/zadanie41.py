from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('dz/templates')
env = Environment(loader=file_loader)

tm = env.get_template('one.html')
msg = tm.render()

print(msg)
