from uuid import UUID

from rest_framework.serializers import ValidationError

from .error_map import ERROR_MAP_MESSAGE
from hoopoe.common.models import BaseModel


def check_field_is_unique(value:str, model:BaseModel, 
exclude_id:UUID|str=None, field:str="name") -> str:
    """
    function to check this name is not exist and not set befor.

    Args:
        value (str): new value.
        model (BaseModel): model you want to check value is unique.
        exclude_id (UUID | str, optional): exclude id.
        field (str, optional): for wich field? default is name.

    Raises:
        ValidationError: raive validation error if a object find
        with your value in your model.

    Returns:
        str: return value if it is unique.
    """

    query = {
        field:value
    }

    qs = model.objects.filter(**query)
        
    if exclude_id:
        qs = qs.exclude(id=exclude_id)
    
    if qs.exists():
        raise ValidationError(ERROR_MAP_MESSAGE[model])
    
    return value

        
