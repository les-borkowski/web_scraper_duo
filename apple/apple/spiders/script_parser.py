import chompjs


def parse_script(string):
    
    # parse string using chompjs to retrieve array of js object
    # NOTE: second element in the array is what i'm looking for
    result = chompjs.parse_js_object(string, unicode_escape=True, jsonlines=True)

    # print(test3[1])
    
    
    return result

    
