def greeting(name: str) -> str:
    cap_name = ' '.join([initial.capitalize() for initial in name.split()])
    cap_name = name.title()
    return 'Привет, {0}'.format(cap_name)
    
for i in range(97, 110):
    msg = greeting('Hello ' + chr(i))
    print(msg)