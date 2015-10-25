"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
>>> Brand.query.get(8)
<brands: id=8 name=Austin founded=1905 headquarters=Longbridge, England discontinued=1987>

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
>>> Model.query.filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

[<models: id=5 year=1953 brand_name=Chevrolet name=Corvette>,
<models: id=6 year=1954 brand_name=Chevrolet name=Corvette>,
<models: id=8 year=1955 brand_name=Chevrolet name=Corvette>,
<models: id=10 year=1956 brand_name=Chevrolet name=Corvette>,
<models: id=11 year=1957 brand_name=Chevrolet name=Corvette>, 
<models: id=13 year=1958 brand_name=Chevrolet name=Corvette>, 
<models: id=17 year=1959 brand_name=Chevrolet name=Corvette>, 
<models: id=20 year=1960 brand_name=Chevrolet name=Corvette>, 
<models: id=26 year=1961 brand_name=Chevrolet name=Corvette>, 
<models: id=28 year=1962 brand_name=Chevrolet name=Corvette>,
<models: id=38 year=1963 brand_name=Chevrolet name=Corvette>,
<models: id=39 year=1964 brand_name=Chevrolet name=Corvette>]


sqlite> SELECT*FROM Models WHERE name='Corvette' AND brand_name='Chevrolet';

id          year        brand_name  name      
----------  ----------  ----------  ----------
5           1953        Chevrolet   Corvette  
6           1954        Chevrolet   Corvette  
8           1955        Chevrolet   Corvette  
10          1956        Chevrolet   Corvette  
11          1957        Chevrolet   Corvette  
13          1958        Chevrolet   Corvette  
17          1959        Chevrolet   Corvette  
20          1960        Chevrolet   Corvette  
26          1961        Chevrolet   Corvette  
28          1962        Chevrolet   Corvette  
38          1963        Chevrolet   Corvette  
39          1964        Chevrolet   Corvette 

# Get all models that are older than 1960.

>>> db.session.query(Model.name).filter(Model.year<1960).group_by(Model.name).all()
[(u'2CV',), (u'600',), (u'Corvette',), (u'Fleetwood',), 
(u'Imperial',), (u'Mini',), (u'Minx Magnificent',), (u'Model T',), 
(u'Thunderbird',)]

sqlite> SELECT name FROM Models WHERE year<1960 GROUP BY name;
name      
----------
2CV       
600       
Corvette  
Fleetwood 
Imperial  
Mini      
Minx Magni
Model T   
Thunderbir

# Get all brands that were founded after 1920.

>>> db.session.query(Brand.name).filter(Brand.founded>1920).group_by(Brand.name).all()
[(u'Chrysler',), (u'Fairthorpe',), (u'Plymouth',), 
(u'Pontiac',), (u'Tesla',)]

sqlite> SELECT name FROM Brands WHERE founded>1920 GROUP BY name;
name      
----------
Chrysler  
Fairthorpe
Plymouth  
Pontiac   
Tesla     

# Get all models with names that begin with "Cor".

>>> db.session.query(Model.name).filter(Model.name.like("Cor%")).group_by(Model.name).all()
[(u'Corvair',), (u'Corvair 500',), (u'Corvette',)]

sqlite> SELECT name from Models WHERE name LIKE 'Cor%' GROUP BY name;
name      
----------
Corvair   
Corvair 50
Corvette  

# Get all brands with that were founded in 1903 and that are not yet discontinued.

>>> db.session.query(Brand.name).filter(Brand.founded==1903, Brand.discontinued==None).group_by(Brand.name).all()
[(u'Buick',), (u'Ford',)]

sqlite> SELECT name FROM Brands WHERE founded=1903 AND discontinued IS NULL GROUP BY name;
name      
----------
Buick     
Ford  

# Get all brands with that are either discontinued or founded before 1950.

>>> db.session.query(Brand.name).filter((Brand.discontinued.isnot(None)) | (Brand.founded<1950)).group_by(Brand.name).all()
[(u'Austin',), (u'BMW',), (u'Buick',), (u'Cadillac',), 
(u'Chevrolet',), (u'Chrysler',), (u'Citro\xebn',), (u'Fairthorpe',), 
(u'Ford',), (u'Hillman',), (u'Plymouth',), (u'Pontiac',), 
(u'Rambler',), (u'Studebaker',)]

sqlite> SELECT name FROM Brands WHERE discontinued NOT NULL OR founded<1950 GROUP BY name;
name      
----------
Austin    
BMW       
Buick     
Cadillac  
Chevrolet 
Chrysler  
Citroën  
Fairthorpe
Ford      
Hillman   
Plymouth  
Pontiac   
Rambler   
Studebaker


# Get any model whose brand_name is not Chevrolet.

>>> db.session.query(Model.brand_name).filter(Model.brand_name != 'Chevrolet').group_by(Model.brand_name).all()
[(u'Austin',), (u'BMW',), (u'Buick',), (u'Cadillac',), 
(u'Chrysler',), (u'Citro\xebn',), (u'Fairthorpe',), (u'Fillmore',), 
(u'Ford',), (u'Hillman',), (u'Plymouth',), (u'Pontiac',), 
(u'Rambler',), (u'Studebaker',)]

sqlite> SELECT brand_name FROM Models WHERE brand_name<>'Chevrolet' GROUP BY brand_name;
brand_name
----------
Austin    
BMW       
Buick     
Cadillac  
Chrysler  
Citroën  
Fairthorpe
Fillmore  
Ford      
Hillman   
Plymouth  
Pontiac   
Rambler   
Studebaker


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model name, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    print "Hello!!!!"
    
    print db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(year == Model.year).all()   
    
    # The "Hello" is for testing and I liked it, so I left it  :)
    # I couldn't remember how to indent without getting an error
    # I recognize that the print statement is very long!

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # print db.session.query(Model.brand_name).group_by(Model.brand_name).all()
    # print db.session.query(Model.name).group_by(Model.brand_name).all()

    brands_dict = {}

    brands_models = db.session.query(Model.name, Brand.name).outerjoin(Brand).all()
    # SELECT Brands.name, Models.name FROM Brands LEFT JOIN Models;
    print brands_models

    for item in brands_models:
        brands_dict[item[1]] = item[0]
    print brands_dict

    # for key, value in brands_dict.items():
    #     print key, ': ', value

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# Since this request does not end in .all(), .one() or .first() it is returning an object
# with information about where that information is stored (I think that's what the string is). 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is one whose purpose is to link two other tables to each other.
# It does this by including the primary keys from each of those tables as foreign keys on the association table

