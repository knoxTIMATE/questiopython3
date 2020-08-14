def myfunc(var1, **kwargs):
    print ('var1:', var1)
    print ()
    
    print ('Other args:')
    print (list(kwargs))
    for param in list(kwargs):
        print ("\t", param + ':', kwargs[param])
        
myfunc(10, fancy_var2=20, fancy_var3='thirsty')
