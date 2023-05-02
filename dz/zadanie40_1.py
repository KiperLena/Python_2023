from jinja2 import Template

menu = [
    {'href': '/index', 'box': 'Главная'},
    {'href': '/news', 'box': 'Новости'},
    {'href': '/about', 'box': 'О компании'},
    {'href': '/shop', 'box': 'Магазин'},
    {'href': '/contacts', 'box': 'Контакты'}
]

link = """
<ul>
 {% for c in menu -%}
 {% if c.box == 'Главная' -%}
    <li><a href="{{c['href']}}" class="active">  {{ c['box']}} </a> </li>
 {% else -%}
    <li><a href="{{c['href']}}">  {{ c['box']}} </a> </li>
 {% endif -%}
 {% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(menu=menu)

print(msg)
