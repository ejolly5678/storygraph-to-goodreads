def rename(dictionary, new_key, old_key):
    if old_key in dictionary:
        dictionary[new_key] = dictionary.pop(old_key)
