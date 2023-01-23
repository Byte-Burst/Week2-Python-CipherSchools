user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes': ['awakening','fairy tale']
}
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))
