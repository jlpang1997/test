class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path,name=None):
        if path=='users':
            def add_usrname(usrname):
                return Chain('%s/%s/%s'%(self._path,path,usrname))
            return add_usrname
        elif path=='repos':
            def add_reposname(reposname):
                return Chain('%s/%s'%(self._path,reposname))
            return add_reposname
        elif path=='commits':
            def add_commitsname(commitsname='master'):
                return Chain('%s/%s/%s'%(self._path,path,commitsname))
            return add_commitsname
        else:
            return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
    def __call__(self):
        print('I am called')

s=Chain().users('jlpang1997').repos('hello-world').commits()
print(s)
s()