from typing import Optional, Union
from ddb_single.model import BaseModel, DBField
from ddb_single.table import Table
import ddb_single.utils_botos as util_b

class Query:
    def __init__(self, table:Table, model:Optional[BaseModel]=None):
        self.__table__ = table
        if model:
            self.model(model)
    
    def model(self, model:BaseModel):
        """
        Set DB data model.
        Args:
            model (BaseModel): DB data model
        """
        if not model.__setup__:
            model = model(__skip_validation__=True)
        self.__model__ = model
        return self

    def get_pk(self):
        return self.__model__.data[self.__model__.__primary_key__]
    
    def get_unique(self):
        return self.__model__.data[self.__model__.__unique_keys__[0]]

    def search_items(self):
        items_add = []
        items_remove = []
        for k in self.__model__.__search_keys__:
            field:DBField = self.__model__.__class__.__dict__[k]
            if k in self.__model__.data.keys() and field.value is not None:
                items_add.append(field.search_item(self.__model__.data[self.__model__.__primary_key__]))
            else:
                items_remove.append(field.search_item(self.__model__.data[self.__model__.__primary_key__]))
        return items_add, items_remove

    # 検索
    def search(self, *queries):
        """
        Search items.
        Args:
            queries (List[dict]): Query objects
        """
        return self.__table__.search(self.__model__.__model_name__, *queries)

    # アイテムを取得
    def get(self, pk:str):
        """
        Get single item.
        Args:
            pk: Primary key
        """
        res = self.__table__.get_item(pk)
        return res

    # ユニークキーで検索
    def get_by_unique(self, value):
        """
        Get single item by unique key.
        Args:
            value: Unique key value
        """
        res = self.search(getattr(self.__model__.__class__, self.__model__.__unique_keys__[0]).eq(value))
        if res:
            pk = res[0][self.__model__.__primary_key__]
            return self.get(pk)

    # Create/Update関連

    # ヴァリデーション
    def validate(self):
        for k, v in self.__model__.data.items():
            if k in self.__model__.__search_keys__:
                field:DBField = self.__model__.__class__.__dict__[k]
                field.validate(v)

    # 新規作成
    def create(self, batch=None, raise_if_exists=False):
        """
        Create a new item.
        Args:
            batch: BatchWriteItem
            raise_if_exists (bool): Throw exception if item already exists
        """
        old_item = self.get_by_unique(self.__model__.data[self.__model__.__unique_keys__[0]])
        if old_item:
            if raise_if_exists:
                raise Exception("Item Already exists")
            else:
                self._update(old_item, batch=batch)
        else:
            self._create(batch)

    # 更新
    def update(self, batch=None):
        """
        Update an item.
        Args:
            batch: BatchWriteItem
        """
        old_item = self.get_by_unique(self.__model__.data[self.__model__.__unique_keys__[0]])
        if old_item:
            self._update(old_item, batch=batch)
        else:
            self._create(batch=batch)
    
    def _create(self, batch=None, remove_ex_search_items=False):
        self.validate()
        search_items_add, search_items_rm = self.search_items()
        rel_items_add, rel_items_rm = self.relation_items()

        items_add = search_items_add + rel_items_add
        items_remove = search_items_rm + rel_items_rm

        self.__table__.create(self.__model__.data, batch=batch)
        if remove_ex_search_items:
            self.__table__.batch_update(items_add, batch=batch)
            self.__table__.batch_delete_items(items_remove, batch=batch)
        else:
            self.__table__.batch_create(items_add, batch=batch)

    def _update(self, old_item, batch=None):
        self.__model__.data = {**old_item, **self.__model__.data}
        self.__model__.data[self.__model__.__primary_key__] = old_item[self.__model__.__primary_key__]
        self.__model__.data[self.__model__.__secondary_key__] = old_item[self.__model__.__secondary_key__]
        if not util_b.is_same_json(old_item, self.__model__.data):
            self._create(batch=batch, remove_ex_search_items=True)

    # 削除
    def delete(self, target:dict=None, batch=None):
        """
        Delete an item.
        Args:
            batch: BatchWriteItem
        """
        target = target or self.__model__.data
        self.__table__.clear_item(target[self.__model__.__primary_key__], batch=batch)
    
    def delete_by_unique(self, value, batch=None):
        """
        Delete an item by unique key.
        Args:
            batch: BatchWriteItem
        """
        item = self.get_by_unique(value)
        if item:
            self.delete(item, batch=batch)

    # 関連付け
    def _relation_item(self, pk, field:DBField):
        return {
            self.__model__.__primary_key__: self.__model__.data[self.__model__.__primary_key__], 
            self.__model__.__secondary_key__: self.__table__.rel_key(pk),
            self.__table__.__search_data_key__: field.name
        }
    
    def _get_other_item_by_unique(self, target:BaseModel, value, table=None, default=None):
        q = Query(table or self.__table__, target)
        res = q.get_by_unique(value)
        return res

    def _field2relation_items(self, field:DBField, value):
        if field.reletion_by_unique:
            rel:BaseModel = field.relation()
            if field.is_list():
                pks = [self._get_other_item_by_unique(rel, value, default={}).get(rel.__primary_key__) for value in value]
            else:
                pks = [self._get_other_item_by_unique(rel, value, default={}).get(rel.__primary_key__)]
            pks = [pk for pk in pks if pk is not None]
        else:
            if field.is_list():
                pks = [pk for pk in pks if pk is self.get(pk)]
            else:
                if value is self.get(value):
                    pks = [value]
                else:
                    pks = []
        result = [self._relation_item(pk, field) for pk in pks]
        return result

    def relation_items(self):
        items_add = []
        items_exist = []
        for k in self.__model__.__relation_keys__:
            field:DBField = self.__model__.__class__.__dict__[k]
            rel:BaseModel = field.relation
            _items_exist = self.__table__.relation(self.__model__.data[self.__model__.__primary_key__], rel.__model_name__)
            _items_exist = [self._relation_item(i[self.__table__.__primary_key__], field) for i in _items_exist]
            if k in self.__model__.data.keys():
                _items_add = self._field2relation_items(field, self.__model__.data[k])
                items_add.extend(_items_add)
            items_exist.extend(_items_exist)
        sk_add = [item[self.__model__.__secondary_key__] for item in items_add]
        sk_exist = [item[self.__model__.__secondary_key__] for item in items_exist]
        # 削除 .. 既存のリストから追加リストを引く
        items_remove = [i for i in items_exist if i[self.__model__.__secondary_key__] not in sk_add]
        # 追加 .. 追加リストから既存のリストを引く
        items_add = [i for i in items_add if i[self.__model__.__secondary_key__] not in sk_exist]
        return items_add, items_remove

    # Read
    def get_relation(self, model:BaseModel="", field:DBField=""):
        # 関連を検索
        if not isinstance(model or "", str):
            model= model.__model_name__
        if not isinstance(field or "", str):
            field= field.name
        return self.__table__.relation(
            self.__model__.data[self.__model__.__primary_key__], 
            model_name=model, field_name=field)

    def get_reference(self, model:BaseModel="", field:DBField=""):
        # 参照を検索
        if not isinstance(model or "", str):
            model= model.__model_name__
        if not isinstance(field or "", str):
            field= field.name
        return self.__table__.reference(
            self.__model__.data[self.__model__.__primary_key__], 
            model_name=model, field_name=field)
