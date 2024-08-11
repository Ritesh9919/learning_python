
def user(**kargs):
    print(type(kargs))
    for key,value in kargs.items():
        print(f"{key}:{value}")
    
    
user(name="Ritesh", age=25)
    