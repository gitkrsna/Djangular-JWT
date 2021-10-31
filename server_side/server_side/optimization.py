'''
1) Retrieve everything at once if you know you will need it:-
    Use QuerySet.select_related() and prefetch_related()
    a) Use QuerySet.prefetch_related() :: to retrieve all related (one to many and many to many) objects at once.
    b) use QuerySet.select_related() :: to retrieve all related (one to one and foreign key) objects at once.

2) Don’t retrieve things you don’t need:- 
    Use QuerySet.values() and values_list() :: to retrieve only the fields you need. 
    Use QuerySet.defer() and only() :: defer() for fields you don’t need, only() for fields you do need.
    Use QuerySet.count() rather than doing len(queryset) :: to count the number of objects in a QuerySet.
    Use QuerySet.exists() :: to check if a QuerySet contains any objects.
    Don’t overuse count() and exists() :: they are expensive operations.
 
3) Use QuerySet.update() and delete() :: to update and delete objects in a QuerySet.

4) Use foreign key values directly:-
    entry.blog_id instead of entry.blog.id :: to access the foreign key value directly. 

5) Don’t order results if you don’t care :: order_by() :: to order the results.

6) Use bulk methods:-
    bulk_update() :: to update multiple objects in a QuerySet.
    bulk_create() :: to create multiple objects in a QuerySet.
    add() :: to add an object to a QuerySet.
    remove() :: to remove an object from a QuerySet.

7) Use iterator() :: to iterate over a QuerySet.
8) Use explain() :: to get the SQL query that Django will execute.


Source : https://docs.djangoproject.com/en/3.2/topics/db/optimization/
'''
