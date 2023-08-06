from ..dao.event import EventDao
from ..schema.base import ListArgsSchema, RespListSchema, RespIdSchema, RespBaseSchema


class BaseService(object):
    """Base(基础)服务，用于被继承.

    CRUD基础服务类，拥有基本方法，可直接继承使用

    Attributes:
        auth_data: 认证数据，包括用户、权限等
        user_id: 当前操作用户id
        event_dao: 业务事件dao
        dao: 当前业务数据处理类
    """

    auth_data: dict = {}
    user_id: int = 0
    event_dao: EventDao
    dao = None
    Model = None

    def __init__(self, user_id: int = 0, auth_data: dict = {}):
        """Service初始化."""

        self.user_id = user_id
        self.auth_data = auth_data
        self.event_dao = EventDao(user_id)

    def read(self, id: int) -> Model:
        """读取单条数据.

        Args:
            id: 数据id

        Returns:
            一个model实体
        """

        return self.dao.read(id)

    def list_count(self, args: ListArgsSchema,ModelIn) -> RespListSchema:
        """读取多条数据.

        Args:
            args: 列表请求参数，详见ListArgsSchema

        Returns:
            多个model实体组成的List
        """

        return self.dao.read_list_count(args,ModelIn)

    def list(self, args: ListArgsSchema) -> RespListSchema:
        """读取多条数据.

        Args:
            args: 列表请求参数，详见ListArgsSchema

        Returns:
            多个model实体组成的List
        """

        return self.dao.read_list(args)

    def create_array(self, schemaList,schema_model,class_model) -> RespIdSchema:
        """创建多条数据.
        Args:
            schema: model对应的schema，详见schema中对应的实体
            model: model的实体
            
        """ 
        respMsg = "["
        resp = RespIdSchema()
        # 生成数组
        schema_modelarray = []
        for infoschema in schemaList:
            schema_model = class_model()
            self.set_model_by_schema(infoschema, schema_model)
            schema_modelarray = schema_modelarray + [schema_model]
            respMsg = respMsg + str(1) + ","


        # print("schema_modelarray",schema_modelarray)
        self.dao.create_array(schema_modelarray)
        resp.message = respMsg[:-1] + "]"

        return resp
        pass
    def create_array_old(self, schemaList,schema_model,class_model) -> RespIdSchema:
        """创建多条数据.
        Args:
            schema: model对应的schema，详见schema中对应的实体
            model: model的实体
            
        """ 
        respMsg = "["
        resp = RespIdSchema()
        # 生成数组
        for infoschema in schemaList:
            self.set_model_by_schema(infoschema, schema_model)

            # infoschema.user_id = self.user_id
            # infoschema.created_by = self.user_id
            # infoschema.updated_by = self.user_id

            self.dao.create(schema_model)
            respMsg = respMsg + str(1) + ","

            pass

        # self.dao.create_array(schemaList,class_model)
        resp.message = respMsg[:-1] + "]"

        return resp
        pass
   
   
    def create(self, schema) -> RespIdSchema:
        """创建一条数据.

        Args:
            schema: model对应的schema，详见schema中对应的实体
            model: model的实体

        Returns:
            是否创建成功，创建成功则附加数据id
        """

        resp = RespIdSchema()
        model = self.Model()
       
        self.set_model_by_schema(schema, model)
        model.user_id = self.user_id
        model.created_by = self.user_id
        model.updated_by = self.user_id
        self.dao.create(model)

        my_table_name = self._get_table_name(model.__table_args__)

        event_log = self.event_dao.get_event_log(2, model.__tablename__)
        event_log.name = '创建{}：{}'.format(my_table_name, model.name)
        event_log.relation_id = model.id
        self.event_dao.create_event_log(event_log, model)

        resp.id = model.id

        return resp
    
    def _get_table_name(self,table_args):
        return_table_name = "无描述"

        for info in table_args:
            if info == "comment" :
                return_table_name = table_args["comment"]
                break
            elif isinstance(info,dict):
                print("info",info)
                return_table_name = info.get('comment', '数据')
                break

        return return_table_name

    @staticmethod
    def set_model_by_schema(schema, model):
        """给model赋值，从schema.

        Args:
            schema: model对应的schema，详见schema中对应的实体
            model: model的实体

        Returns:
            是否创建成功，创建成功则附加数据id
        """

        for (key, value) in schema:
            model.__setattr__(key, value)

        if hasattr(model, 'search'):
            model.search = model.search

    def update(self, schema) -> RespBaseSchema:
        """更新一条数据.

        Args:
            schema: model对应的schema，详见schema中对应的实体
            model: model的实体

        Returns:
            是否更新成功
        """

        resp = RespBaseSchema()

        model = self.dao.read(schema.id)

        if not model:
            model = self.Model()
            resp.code = 2002191527
            resp.message = '找不到对应的：{}'.format(model.__table_args__.get('comment', '数据'))
            return resp

        my_table_name = self._get_table_name(model.__table_args__)

        event_log = self.event_dao.get_event_log(1, model.__tablename__, model)
        event_log.name = '修改{}：{}'.format(my_table_name, model.name)

        self.set_model_by_schema(schema, model)
        model.updated_by = self.user_id
        self.dao.update(model)

        self.event_dao.create_event_log(event_log, model)

        return resp

    def delete(self, id: int) -> RespBaseSchema:
        """删除单条数据.

        Args:
            id: 数据id

        Returns:
            是否删除成功
        """

        resp = RespBaseSchema()

        model = self.dao.read(id)

        if not model:
            model = self.Model()
            resp.code = 2002191553
            resp.message = '找不到对应的：{}'.format(model.__table_args__.get('comment', '数据'))
            return resp

        my_table_name = self._get_table_name(model.__table_args__)
        
        event_log = self.event_dao.get_event_log(5, model.__tablename__, model)
        event_log.name = '删除{}：{}'.format(my_table_name, model.name)
        self.dao.delete(model)

        self.event_dao.create_event_log(event_log, model)

        return resp
