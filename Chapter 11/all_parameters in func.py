# function with all parameters
# very important to understand

# PADK

# Parameters
# *args
# Default Parameters
# **kwargs

def all_par_func(name,*args,last_name="unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

print(all_par_func("Darshan",(1,2,3),a="Joy",b="fun"))