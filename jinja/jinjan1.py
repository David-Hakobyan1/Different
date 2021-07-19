from jinja2 import Template, escape
# Poxum e {{name}}-n num-i parunakutyunov_________________
num = "pogos"
st  = "barev im qaj im anunne {{name}} urax em qez tesnel"
temp = Template(st)
ms = temp.render(name = num)
print(ms)
#_________________________________________________________

# {% raw %}{% endraw %}-i shnorhiv mnum e nuyn@ d-i parunakutyun@____________
nam = "Flora"
d = "{% raw %}barev im qaj im anunne {{name}} urax em qez tesnel{% endraw %}"
temp1 = Template(d)
msg = temp1.render(name = nam)
print(msg)
#____________________________________________________________________________

# Stanum enq nuyn nm-i meji grvac@,bayc ekranin cuyce talis ssilka_____ 
nm = '''texapoxum@ katarvum e hetevyal hxumov <a href="#">ssilka</a>'''
temp2 = Template(nm)
ms2 = temp2.render()
print(ms2)
#____________________________________________________________________________

# Stanum enq mi ayl kod,vor@ ekranin cuyc e talis nm3-i parunakutyun@________
nm3 = '''hxman kod  <a href="#">ssilka</a>'''
temp3 = Template("{{link | e}}")
msg3 = temp3.render(link=nm3)
print(msg3)
# KAM NUYN@ <<escape>> - ov
nm4 = '''hxman kod  <a href="#">ssilka</a>'''
msg4 = escape(nm4)
print(msg4)
#____________________________________________________________________________

cityes = [{"id":1,"city":"erevan"},
        {"id":2,"city":"gyumri"},
        {"id":3,"city":"mexri"},
        {"id":4,"city":"xapan"},
        {"id":5,"city":"goris"},]

link = '''<select name="cityes">
{% for c in cityes -%}
    <option value="{{c['id']}}">"{{c['city']}}</option>
{% endfor -%}
    </select>'''
temp5 = Template(link)
msg5 = temp5.render(cityes=cityes)
print(msg5)

