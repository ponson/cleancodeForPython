def attrs(**kwds):
    def decorate(mym):
        print(f"in decorate: {id(mym)}")
        for k in kwds:
            setattr(mym, k, kwds[k])
        return mym
    return decorate


@attrs(versionadded = "2.2", author="Guido van Rossum")
def mymethod(f):
    print(f"in mymethod:{id(f)}")
    f['one'] = 1
    f['two'] = 2

    print(f)
    return
    
thef = {}
print(f"thef id: {id(thef)}")
print(f"mymethod id: {id(mymethod)}")
print(f"mymethod attr: {mymethod.author}")
mymethod(thef)
print(thef)



