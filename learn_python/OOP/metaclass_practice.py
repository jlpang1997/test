# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):

#         attrs['add']=lambda self,value: self.append(value)
#         for k,v in attrs.items():
#             print(k,v)
#         return type.__new__(cls,name,bases,attrs)

# class MyList(list,metaclass=ListMetaclass):
#     def __init__(self,score):
#         self.score=10
#     pass
# class List:
#     pass

# # L=MyList(10)
# # L.add(1)
# # print(L)

# # L2=List()
# # L2.add(1)

# class UpperAttrMetaclass(type):
#     def __new__(cls,clsname,bases,attr):
#         NewAttr={}
#         for attrname,v in attr.items():
#             print('*************',attrname)
#             if attrname.startswith('__'):
#                 NewAttr[attrname.replace('__','LL')]=v
#             else:
#                 NewAttr[attrname.upper()]=v
#         return super(UpperAttrMetaclass,cls).__new__(cls,clsname,bases,NewAttr)

# class Student(metaclass=UpperAttrMetaclass):
#     def apple(self):
#         pass
#     def __banana(self):
#         pass
# print('******************')
# ming=Student()
# # print(hasattr(ming,'apple'))
# for i in dir(ming):
#     print(i)
import asyncio
# import logging日志模块先不处理，先把核心做完
import aiomysql
# def log(sql,args=()):
#     logging.info('SQL:%s'%sql)

async def create_pool(loop,**kw):
    global __pool
    __pool=await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

async def select(sql,args,size=None):
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?','%s'),args or ())
            if size:
                rs=await cur.fetchmany(size)
            else:
                rs=await cur.fetchall()
        return rs

async def execute(sql,args,autocommit=True):
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?','%s'),args)
                affected=cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise e
        return affected


def create_args_string(num):
    L=[]
    for n in range(num):
        L.append('?')
    return ', '.join(L)


class Field(object):
    def __init__(self,name,column_type,primary_key,default):
        self.name=name
        self.column_type=column_type
        self.primary_key=primary_key
        self.default=default
    def __str__(self):
        return '<name:%10s\tcolumn_tpye:%15s\tpk:%10s\tdefault:%10s>'%(self.name,self.column_type,str(self.primary_key),str(self.default))
    __repr__=__str__

class BooleanField(Field):
    def __init__(self,name=None,primary_key=False,default=False):
        super(BooleanField,self).__init__(name,'boolean',primary_key,default)
class IntegerField(Field):
    def __init__(self,name=None,primary_key=False,default=0):
        super(IntegerField,self).__init__(name,'bigint',primary_key,default)
class FloatField(Field):
    def __init__(self,name=None,primary_key=False,default=0.0):
        super(FloatField,self).__init__(name,'real',primary_key,default)
class StringField(Field):
    def __init__(self,name=None,primary_key=False,default=None,ddl='varchar(100)'):
        super(StringField,self).__init__(name,ddl,primary_key,default)
class TextField(Field):
    def __init__(self,name=None,primary_key=False,default=None):
        super(TextField,self).__init__(name,'text',primary_key,default)


class ModerMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if(name=='Model'):
            return super(ModerMetaclass,cls).__new__(cls,name,bases,attrs)
        else:
            tableName=attrs.get('__table__',None) or name
            fields=[]
            primary_key=None
            # print('Found model:%s'%name)
            mappings={}
            for k,v in attrs.items():
                if isinstance(v,Field):
                    # print('Found mapping:%10s ==> %s'%(k,v))
                    mappings[k]=v
                    if v.primary_key:
                        if primary_key:
                            raise Exception('Duplicate primary key for field:%s'%k)
                        primary_key=k
                    else:
                        fields.append(k)#除去primary key字段的所有字段
            if not primary_key:
                raise Exception('Primary key not found')
            for k in mappings.keys():
                attrs.pop(k)
            escaped_fields=list(map(lambda f:'`%s`'%f,fields))
            attrs['__mappings__']=mappings
            attrs['__table__']=tableName
            attrs['__primary_key__']=primary_key
            attrs['__fields__']=fields

            attrs['__select__']="select `%s`,%s from `%s`"%(primary_key,', '.join(escaped_fields),tableName)

            attrs['__insert__']='insert into `%s` (%s,`%s`) values (%s)'%(tableName, ', '.join(escaped_fields),primary_key,create_args_string(len(escaped_fields)+1))

            attrs['__upadate__']='updata `%s` set %s where `%s`=?'%(tableName,', '.join(map(lambda f: '`%s`=?'%(mappings.get(f).name or f),fields)),primary_key)

            attrs['__delete__']='delete from `%s` where `%s`=?'%(tableName,primary_key)

            return super(ModerMetaclass,cls).__new__(cls,name,bases,attrs)
class Model(dict,metaclass=ModerMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'"%attr)
    def __setattr__(self,attr,value):
        self[attr]=value

    def getValue(self,key):
        return getattr(self,key,None)
    def getValueOrDefault(self,key):
        value=getattr(self,key,None)
        if value is None:
            field=self.__mappings__[key]
            if field.default is not None:
                value=field.default() if callable(field.default) else field.default
                setattr(self,key,value)
        return value

    # @classmethod 
    async def save(self):
        args=list( map( self.getValueOrDefault,self.__fields__ ) )
        args.append(self.getValueOrDefault(self.__primary_key__))
        print('SQL:%s'%self.__insert__)
        print('args:%s'%str(args))
        # rows=await execute(self.__insert__,args)
        # if rows!=1:
        #     print('failed to insert record:affected row:%s'%rows)

    async def updata(self):
        args=list( map( self.getValue,self.__fields__ ) )
        args.append(self.getValue(self.__primary_key__))
        print('SQL:%s'%self.__upadate__)
        print('args:%s'%str(args))
        rows=await execute(self.__update__,args)
        if rows!=1:
            print('failed to update by primary key:affected row:%s'%rows)       
    
    async def remove(self):
        args=[self.getValue(self.__primary_key__)]
        print('SQL:%s'%self.__delete__)
        print('args:%s'%str(args))

        rows=await execute(self.__delete__,args)
        if rows!=1:
            print('failed to remove by primary key:affected row:%s'%rows)

    @classmethod
    async def find(cls,pk):
        # print('''%s('%s where `%s`=?)'''%(select',cls.__select__,cls.__primary_key__,))
        print('SQL:%s where `%s`=?'%(cls.__select__,cls.__primary_key__))
        print("args:[%s,1]"%str(pk))
        rows=await select('%s where `%s`=?'%(cls.__select__,cls.__primary_key__),[pk],1)
    
    @classmethod
    async def findAll(cls,where=None,args=None,**kw):
        sql=[cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args=[]
        orderBy=kw.get('orderBy',None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit=kw.get('limit',None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit,int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit,tuple) and len(limit)==2:
                sql.append('?,?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value:%s'%str(limit))
        rs=await select(' '.join(sql),args)
        return [cls(**r) for r in rs]
    
    @classmethod
    async def findNumber(cls,selectField,where=None,args=None):
        sql=['select %s _num_ from `%s`'%(selectField,cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs=await select(' '.join(sql),args,1)
        if len(rs)==0:
            return None
        else:
            return rs[0]['_num_']



class User(Model):
    id=IntegerField('id',primary_key=True)
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')
    price=FloatField('price')
    resume=TextField('resume')
    handsome=BooleanField('handsome')

u=User(id=12345,email='test@test.com',password='NARUTO20141110',handsome=True,price=123.456)

u.save()
# u.find(12345)    
# u.updata()
# u.remove()        


