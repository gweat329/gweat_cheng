import xml.etree.ElementTree as et

tree = et.parse(r'to_edit.xml')

root = tree.getroot()

for xe in root.iter('Name'):
    print(xe.text)

for stud in root.iter('Student'):
    name = stud.find('Name')

    if name != None:
        name.set('test', name.text * 2)
        print(name)

stu = root.find('Student')

# 生成一个新的元素
e = et.Element('ADDer')
e.attrib = {'a':'b'}
e.text = '我加的'

stu.append(e)

# 一定要不修改后的内容写回文件，否则修改无效
tree.write('to_deit.xml')