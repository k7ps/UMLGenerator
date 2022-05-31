# UMLGenerator

App that generates UML diagram based on your code

- [_UML diagram_](https://drive.google.com/file/d/13hQxgnLXyTex5LXOH4W1Y4LQ3_niyQiS/view?usp=sharing)

## Setup
For the UMLGenerator to work, you should download [_Graphviz_](https://graphviz.org/download/)

## Modification syntax
- #### Ignore
Write ```#@UML ignore``` before defintition of the class, so that it is ignored:
``` Python
# class A won't be drawn
#@UML ignore
class A: 
```
To ignore field / method, write ```#@UML ignore``` on the same line:
``` Python
# variable example won't be drawn
self.example = 10 #@UML ignore
```
``` Python
# function func won't be drawn
def func(self): #@UML ignore
```
- #### Compositions / Aggregations
To indicate a composition, point the type of variable using [_typing_](https://docs.python.org/3/library/typing.html#module-typing)
``` Python
class A:
    pass
    
class B:
    def __init__(self):
        # a is composition of class A
        self.a: A = A()
```
![uml](https://user-images.githubusercontent.com/95523848/171259245-763a0bcf-0e03-4fec-826f-5dea326775d7.png)

If this an aggregation, just write ```#@UML aggr``` after variable:
(any prefix of "aggregation" can be used instead of "aggr")
``` Python
self.a: A = A() #@UML aggr
```
![uml](https://user-images.githubusercontent.com/95523848/171259398-da39fe0a-72a7-46fd-b035-833e38a3270e.png)

- #### Class groups
In order for the class in the diagram to be in some group / groups, write before definition ```#@UML clusters``` and then names of all groups, separated by commas. It is better to write names from a larger group to a smaller one, but not necessarily
``` Python
#@UML clusters Group1
class A:
    pass
    
#@UML clusters Group1, Group2
class B:
    pass
    
#@UML clusters Group1, Group2, Group3
class CorrectOrder:
    pass
    
#@UML clusters Group2, Group1, Group4, Group3
class IncorrectOrder:
    pass
```
![uml](https://user-images.githubusercontent.com/95523848/171259608-90cb597e-7ff2-4f6b-8ea9-8989e571b24e.png)

**Note:** If you want to use several modifications at once, separate them with **';'** :
``` Python
#@UML clusters Group1, Group2; ignore
class B:
    def __init__(self):
        self.a: int = 10 #@UML ignore; aggr
```
## Settings
If you want to enable option, write ```true```/```1```/```yes```, otherwise - ```false```/```0```/```no```
- #### IgnorePrivate
Ignores private fields

_By default_ - ```true```
- #### IgnoreProtected
ignores protected fields

_By default_ - ```true```
- #### IgnorePrivateComps
If _IgnorePrivate_ enabled, ignores private fields that are composition/aggregation

_By default_ - ```false```
- #### IgnoreProtectedComps
If _IgnoreProtected_ enabled, ignores protected fields that are composition/aggregation

_By default_ - ```false```
- #### ReadFilesOnlyInThisDir
If enabled, reads files only in this directory, otherwise goes recursively through all folders

_By default_ - ```true```
- #### DrawUndefinedClasses
Enable drawing classes that are someone's composition/aggregation or parent class, but have no declaration in the code

_By default_ - ```true```
- #### GroupByFiles
Enables grouping of classes into groups in the same way as they are defined in files

_By default_ - ```false```
- #### DrawOneClassGroup
If _GroupByFiles_ enabled, enable drawing group (not its classes) which contains one class

_By default_ - ```false```
- #### RemoveAccessPrefix
Remove access prefixes from private and protected fields

_By default_ - ```false```
- #### AlternativeEngine
Enable alternative graphviz engine. By default it is DOT engine, the alternative - FDP. Almost always FDP works much worse

_By default_ - ```false```
- #### Color
Changes the color of diagram. There can be any HTML color here

_By default_ - ```yellow```
- #### Files
There you can write a list of local file paths to be read

_By default_ - Read all ```*.py``` files 
- #### IgnoreFiles
There you can write a list of local file paths to be ignored

_By default_ - ignores nothing 
