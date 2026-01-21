## None ##

email = None

## list ##
list1 = [1, 2, 3, 6]
list2 = list((1, 2, 3, 6))
list3 = [1, False, True, 'Salam', [1, 2, 3]]
list_names = [
    'Mohammad Heydari',    #0  #-4
    'Yashar Vedadi',       #1  #-3
    'Mahan Piri',          #2  #-2
    'Amir Abas',           #3  #-1
]

## tuple ##
tuple1 = (1, 2, 3, 6)
tuple2 = tuple((1, 2, 4, 6))
tuple3 = (1, False, True, 'Salam', [1, 2], (3, 4))
tuple_names = (
    'Mohammad Heydari',    #0  #-4
    'Yashar Vedadi',       #1  #-3
    'Mahan Piri',          #2  #-2
    'Amir Abas',           #3  #-1
)

## set ##
set1 = {1, 2, 3, 6, 2}
set2 = set((1, 2, 3, 6, 2))
set3 = (1, True, False, 'Salam', [1, 2], (3, 4), {5, 6})
set_names = (
    'Mohammad Heydari',    #0  #-4
    'Yashar Vedadi',       #1  #-3
    'Mahan Piri',          #2  #-2
    'Amir Abas',           #3  #-1
)

## dict ##
dict1 = {
    'id': 1,
    'name': 'Mohammad',
    'last_name': 'Heydari',
    'age': 26,
    'students': [
        'Yashar Vedadi',       #1  #-3
        'Mahan Piri',          #2  #-2
        'Amir Abas',           #3  #-1
    ],
    'licence': True,
}

errors = {
    404: 'Page Not found',
    401: 'Denied',
    403: 'You are Persian',
}

## Methods ##
name = 'mohammad heydari'
print(name.title())

user_input = 'MOhammaD'

print(user_input.upper())
print(user_input)