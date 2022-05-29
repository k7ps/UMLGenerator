# UMLGenerator

App that generates UML diagram based on your code

- [_UML diagram_](https://drive.google.com/file/d/13hQxgnLXyTex5LXOH4W1Y4LQ3_niyQiS/view?usp=sharing)

### Modification syntax
- ##### Ignore
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
- ##### Compositions / Aggregations
To indicate a composition, point the type of variable using [_typing_](https://docs.python.org/3/library/typing.html#module-typing)
``` Python
class A:
    pass
    
class B:
    def __init__(self):
        # a is composition of class A
        self.a: A = A()
```
If this an aggregation, just write ```#@UML aggr``` after variable:
(any prefix of "aggregation" can be used instead of "aggr")
``` Python
self.a: A = A() #@UML aggr
```
- ##### Class groups
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
**Note:** If you want to use several modifications at once, separate them with **';'** :
``` Python
#@UML clusters Group1, Group2; ignore
class B:
    def __init__(self):
        self.a: int = 10 #@UML ignore; aggr
```
