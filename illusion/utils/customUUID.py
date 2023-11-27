import random

def custom_id(length=8):
    values = [random.randint(1,36) for i in range(length)]
    translated = [(chr(ord('`')+i)) if i<27 else i-26 for i in values]
    return ''.join(str(x) for x in translated)
    