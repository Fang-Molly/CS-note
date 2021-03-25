# Chapter 13  Using Web Services

## 13.1 eXtensible Markup Language - XML

* XML document sample

```python
<person> 
  <name>Chuck</name> 
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" /> 
</person>
```

## 13.2 Parsing XML

```python
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
 </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

$ xml.py
Name: Chuck
Attr: yes
```

## 13.3 Looping through nodes





