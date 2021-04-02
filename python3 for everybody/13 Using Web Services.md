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

```python
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text) 
    print('Id', item.find('id').text) 
    print('Attribute', item.get('x'))
    
$ nodes.py
User count: 2
Name Chuck
Id 001
Attribute 2
Name Brent
Id 009
Attribute 7
```

```python
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)

lst = stuff.findall('users/user')
print('User count:', len(lst))

lst2 = stuff.findall('user')
print('User count:', len(lst2))

$ 
User count: 2
User count: 0
```

## 13.4 JavaScript Object Notation - JSON

```python
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}
```

## 13.5 Parsing JSON

```python
import json

data = ''' 
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  },
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
  print('Name', item['name'])
  print('Id', item['id'])
  print('Attribute', item['x'])

$

User count: 2
Name Chuck
Id 001
Attribute 2
Name Brent
Id 009
Attribute 7
```

## 13.6 Application Programming Interfaces (APIs)

## 13.7 Security and API Usage




