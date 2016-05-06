from marshmallow import Schema
class IgnoreBlankSchema(Schema):
    # 针对标记为ignore_blank=True的fields，如果前端传过来该field为''则忽略
    class Meta:
        strict = True  # 默认启用validation

    @pre_load
    def ignore_blank_fields(self, in_data):
        for field in in_data.copy():
            # 找到标记了ignore_blank为True的字段，并且in_data里该字段的值为''
            if self.fields[field].metadata.get('ignore_blank', False) and in_data[field] == '':
                in_data.pop(field, None)
        
