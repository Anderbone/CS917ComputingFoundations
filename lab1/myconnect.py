def connect(uname, pword, server='jiyu', port=400):
    print('ok')


connect('admin','cats','.com')

connect(uname='admin',pword='123')
# connect(uname='admin',pword='123','ian')
# wrong because keyword follow positional arg
connect(uname='admin',pword='123', server='ian',port=344)

def connect2(uname, *args, **kw):
    print(uname)
    for arg in args:
        print(arg+'this is arg')
    for key in kw.keys():
        print(key,":",kw[key])

connect2('admin','love','arg33',sp='dd',server='loc',port=135,fss='ffff')