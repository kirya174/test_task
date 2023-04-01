def my_code(dictionary: dict, depth=0) -> None:
    for key, value in dictionary.items():
        print("\t"*depth + key + ":")
        if isinstance(value, str):
            print("\t"*(depth + 1) + value)
        else:
            my_code(value, depth + 1)
        
my_code({'first': 'first_value','second': 'second_value'})

'''
first:
        first_value
second:
        second_value
'''


my_code({
    '1': {
        'child': '1/child/value'
    },
    '2': '2/value'
})

'''
1:
        child:
                1/child/value
2:
        2/value
'''
