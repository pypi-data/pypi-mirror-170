# django-query-blocker
Prevents django to perform any query within the context or decorated method

## Table of Contents
1. [Why Should I Use This?](#why-should-i-use-this?)
2. [How To Install](#how-to-install)
3. [How To Use](#how-to-use)
    1. [Context](#context)
    2. [Decorator](#decorator)

## Why Should I Use This?

Django ORM is great and easy to use but can easily hide some very back behaviours. Just by calling a property here and there you can cascade a chain of hundreds of queries hidden behind the easy-to-use model abstractions. This lib prevents it to happen by locking the ORM not allowing it to perform the queries by raising an exception.

## How To Install
- Install with
```
pip install django-query-blocker
```

## How To Use
- It can be used as a context or decorator

### Context

```python
from query_blocker import block_extra_queries

my_object = MyModel.objects.first()
print(my_object)  # works fine
with block_extra_queries:
    print(obj.foreign_key_obj) # will raise a NoExtraQueryException
```

### Decorator

```python
from query_blocker import block_extra_queries

@block_extra_queries
def my_method(obj):
    print(obj.foreign_key_obj)

my_object = MyModel.objects.first()
print(my_object)  # works fine
my_method(my_object)  # will raise a NoExtraQueryException
```
