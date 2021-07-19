from jinja2 import Template

cityes = [{"id":1,"city":"erevan"},
           {"id":2,"city":"gyumri"},
           {"id":3,"city":"dilijan"},
           {"id":4,"city":"ijevan"}]

link = '''<select name = "citiyes">
{% for c in cityes -%}
{% if c.id < 3 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "dilijan" -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''
temp = Template(link)
msg = temp.render(cityes = cityes)
print(msg)
  
