__all__ = ('ChannelMetadataPrivateGroup',)

from scarletio import copy_docs

from ...bases import ICON_TYPE_NONE, IconSlot, Slotted
from ...http import urls as module_urls
from ...permission.permission import PERMISSION_GROUP, PERMISSION_GROUP_OWNER, PERMISSION_NONE

from ..fields.name import parse_name, put_name_into, validate_name
from ..fields.owner_id import parse_owner_id, put_owner_id_into, validate_owner_id

from .private_base import ChannelMetadataPrivateBase


class ChannelMetadataPrivateGroup(ChannelMetadataPrivateBase, metaclass=Slotted):
    """
    Channel metadata for private channels.
    
    Attributes
    ----------
    users : `list` of ``ClientUserBase``
        The users in the channel.
    icon_hash : `int`
        The channel's icon's hash in `uint128`.
    icon_type : ``iconType``
        The channel's icon's type.
    name : `str`
        The channel's display name. Can be empty string if the channel has no name.
    owner_id : `int`
        The group channel's owner's id.
    
    Class Attributes
    ----------------
    order_group: `int` = `0`
        The channel's order group used when sorting channels.
    """
    __slots__ = ('name', 'owner_id')
    
    icon = IconSlot('icon', 'icon', module_urls.channel_group_icon_url, module_urls.channel_group_icon_url_as)
    
    @copy_docs(ChannelMetadataPrivateBase.__hash__)
    def __hash__(self):
        hash_value = ChannelMetadataPrivateBase.__hash__(self)
        
        # name
        name = self.name
        if name:
            hash_value ^= hash(name)
        
        # owner_id
        hash_value ^= self.owner_id
        
        return hash_value
    
    
    @copy_docs(ChannelMetadataPrivateBase.__new__)
    def __new__(cls, keyword_parameters):
        self = ChannelMetadataPrivateBase.__new__(cls, keyword_parameters)
        
        # icon
        try:
            icon = keyword_parameters.pop('icon')
        except KeyError:
            pass
        else:
            raise NotImplementedError(
                f'`{cls.__name__}.__new__` do not implements `icon` parameter. Got icon={icon!r}'
            )
        
        return self
    
    
    @copy_docs(ChannelMetadataPrivateBase._created)
    def _created(self, channel_entity, client):
        if (client is not None):
            client.group_channels[channel_entity.id] = channel_entity
    
        
    @copy_docs(ChannelMetadataPrivateBase._delete)
    def _delete(self, channel_entity, client):
        if (client is not None):
            try:
                del client.group_channels[channel_entity.id]
            except KeyError:
                pass
    
    
    @copy_docs(ChannelMetadataPrivateBase._is_equal_same_type)
    def _is_equal_same_type(self, other):
        if not ChannelMetadataPrivateBase._is_equal_same_type(self, other):
            return False
        
        # icon
        if self.icon_hash != other.icon_hash:
            return False
        
        if self.icon_type is not other.icon_type:
            return False
        
        # name
        if self.name != other.name:
            return False
        
        # owner_id
        if self.owner_id != other.owner_id:
            return False
        
        return True
    
    
    @copy_docs(ChannelMetadataPrivateBase._get_processed_name)
    def _get_processed_name(self):
        name = self.name
        if name:
            return name
        
        users = self.users
        if users:
            return ', '.join([user.name for user in users])
        
        return 'Unnamed'
    
    
    @copy_docs(ChannelMetadataPrivateBase._update_attributes)
    def _update_attributes(self, data):
        ChannelMetadataPrivateBase._update_attributes(self, data)
        
        # icon
        self._set_icon(data)
        
        # name
        self.name = parse_name(data)
        
        # owner_id
        self.owner_id = parse_owner_id(data)
    
    
    @copy_docs(ChannelMetadataPrivateBase._difference_update_attributes)
    def _difference_update_attributes(self, data):
        old_attributes = ChannelMetadataPrivateBase._difference_update_attributes(self, data)
        
        # icon
        self._update_icon(data, old_attributes)
        
        # name
        name = parse_name(data)
        if self.name != name:
            old_attributes['name'] = self.name
            self.name = name
        
        # owner_id
        owner_id = parse_owner_id(data)
        if self.owner_id != owner_id:
            old_attributes['owner_id'] = self.owner_id
            self.owner_id = owner_id
        
        return old_attributes

    
    @copy_docs(ChannelMetadataPrivateBase._get_permissions_for)
    def _get_permissions_for(self, channel_entity, user):
        if self.owner_id == user.id:
            return PERMISSION_GROUP_OWNER
        elif user in self.users:
            return PERMISSION_GROUP
        else:
            return PERMISSION_NONE
    
    
    @classmethod
    @copy_docs(ChannelMetadataPrivateBase._from_partial_data)
    def _from_partial_data(cls, data):
        self = super(ChannelMetadataPrivateGroup, cls)._from_partial_data(data)
        
        if (data is not None):
            name = data.get('name', None)
            if (name is not None):
                self.name = name
        
        return self
    
    
    @classmethod
    @copy_docs(ChannelMetadataPrivateBase._create_empty)
    def _create_empty(cls):
        self = super(ChannelMetadataPrivateGroup, cls)._create_empty()
        
        self.name = ''
        self.owner_id = 0
        
        self.icon_hash = 0
        self.icon_type = ICON_TYPE_NONE
        
        return self
    
    
    @classmethod
    @copy_docs(ChannelMetadataPrivateBase.precreate)
    def precreate(cls, keyword_parameters):
        self = super(ChannelMetadataPrivateGroup, cls).precreate(keyword_parameters)
        
        # icon
        processable = []
        cls.icon.preconvert(keyword_parameters, processable)
        if processable:
            for item in processable:
                setattr(self, *item)
        processable = None
    
        return self
    
    
    @copy_docs(ChannelMetadataPrivateBase._set_attributes_from_keyword_parameters)
    def _set_attributes_from_keyword_parameters(self, keyword_parameters):
        ChannelMetadataPrivateBase._set_attributes_from_keyword_parameters(self, keyword_parameters)
        
        # name
        try:
            name = keyword_parameters.pop('name')
        except KeyError:
            pass
        else:
            self.name = validate_name(name)
        
        # owner_id
        try:
            owner_id = keyword_parameters.pop('owner_id')
        except KeyError:
            pass
        else:
            self.owner_id = validate_owner_id(owner_id)
    
    
    @copy_docs(ChannelMetadataPrivateBase.to_data)
    def to_data(self):
        data = ChannelMetadataPrivateBase.to_data(self)
        
        # name
        put_name_into(self.name, data, True)
        
        # owner_id
        put_owner_id_into(self.owner_id, data, True)
        
        # icon
        data['icon'] = self.icon.as_base16_hash
        
        return data
