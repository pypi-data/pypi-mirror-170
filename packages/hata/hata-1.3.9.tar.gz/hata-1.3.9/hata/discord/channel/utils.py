__all__ = (
    'cr_pg_channel_object', 'create_partial_channel_from_data', 'create_partial_channel_from_id'
)

import reprlib
from datetime import datetime

from scarletio import export, include

from ..bases import maybe_snowflake
from ..core import CHANNELS
from ..preconverters import preconvert_preinstanced_type
from ..utils import datetime_to_timestamp

from .constants import AUTO_ARCHIVE_OPTIONS
from .preinstanced import VideoQualityMode
from .channel_type import ChannelType

Channel = include('Channel')
Guild = include('Guild')
VoiceRegion = include('VoiceRegion')


def create_partial_channel_from_data(data, guild_id):
    """
    Creates a partial channel from partial channel data.
    
    Parameters
    ----------
    data : `None`, `dict` of (`str`, `Any`) items
        Partial channel data received from Discord.
    guild_id : `int`
        The channel's guild's identifier.
    
    Returns
    -------
    channel : `None`, ``Channel``
        The created partial channel, or `None`, if no data was received.
    """
    if (data is None) or (not data):
        return None
    
    channel_id = int(data['id'])
    try:
        return CHANNELS[channel_id]
    except KeyError:
        pass
    
    channel = Channel._from_partial_data(data, channel_id, guild_id)
    CHANNELS[channel_id] = channel
    
    return channel


@export
def create_partial_channel_from_id(channel_id, channel_type, guild_id):
    """
    Creates a new partial channel from the given identifier.
    
    Parameters
    ----------
    channel_id : `int`
        The channel's identifier.
    channel_type : ``ChannelType``
        The channel's type.
    guild_id : `int`
        A guild's identifier of the created channel.
    """
    try:
        return CHANNELS[channel_id]
    except KeyError:
        pass
    
    channel = Channel._create_empty(channel_id, channel_type, guild_id)
    CHANNELS[channel_id] = channel
    
    return channel


HAS_PERMISSION_OVERWRITES = (
    ChannelType.guild_text,
    ChannelType.guild_voice,
    ChannelType.guild_category,
    ChannelType.guild_announcements,
    ChannelType.guild_store,
    ChannelType.guild_stage,
    ChannelType.guild_directory,
    ChannelType.guild_forum,
)

HAS_TOPIC = (
    ChannelType.guild_text,
    ChannelType.guild_announcements,
    ChannelType.guild_stage,
    ChannelType.guild_forum,
)

HAS_NSFW = (
    ChannelType.guild_text,
    ChannelType.guild_announcements,
    ChannelType.guild_voice,
)

HAS_SLOWMODE = (
    *(
        channel_type for channel_type in ChannelType.INSTANCES.values()
        if channel_type.flags.guild and channel_type.flags.textual
    ),
    ChannelType.guild_forum,
)

HAS_BITRATE = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.guild and channel_type.flags.connectable
)

HAS_USER_LIMIT = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.guild and channel_type.flags.connectable
)

HAS_REGION = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.guild and channel_type.flags.connectable
)

HAS_VIDEO_QUALITY_MODE = (
    ChannelType.guild_voice,
)

HAS_ARCHIVED = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.thread
)

HAS_ARCHIVED_AT = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.thread
)

HAS_AUTO_ARCHIVE_AFTER = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.thread
)

HAS_DEFAULT_AUTO_ARCHIVE_AFTER = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.threadable
)

HAS_OPEN = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.thread
)

CAN_HAVE_PARENT_ID = tuple(
    channel_type for channel_type in ChannelType.INSTANCES.values()
    if channel_type.flags.guild and (channel_type is not ChannelType.guild_category)
)


def cr_pg_channel_object(
    name, channel_type, *, permission_overwrites=..., topic=..., nsfw=..., slowmode=..., bitrate=..., user_limit=...,
    region=..., video_quality_mode=..., archived=..., archived_at=..., auto_archive_after=..., open_=...,
    default_thread_auto_archive_after=..., parent=..., available_tags=..., guild=None,
):
    """
    Creates a json serializable object representing a ``Channel``.
    
    Parameters
    ----------
    name : `str`
        The name of the channel. Can be between `1` and `100` characters.
    channel_type : `int`, ``ChannelType``
        The channel's type.
    permission_overwrites : `None`, `list` of ``cr_p_permission_overwrite_object`` returns, Optional (Keyword only)
        A list of permission overwrites of the channel. The list should contain json serializable permission
        overwrites made by the ``cr_p_permission_overwrite_object`` function.
    topic : `None`, `str`, Optional (Keyword only)
        The channel's topic.
    nsfw : `None`, `bool`, Optional (Keyword only)
        Whether the channel is marked as nsfw.
    slowmode : `None`, `int`, Optional (Keyword only)
        The channel's slowmode value.
    bitrate : `None`, `int`, Optional (Keyword only)
        The channel's bitrate.
    user_limit : `int`, Optional (Keyword only)
        The channel's user limit.
    region : `None`, ``VoiceRegion``, `str`, Optional (Keyword only)
        The channel's voice region.
    video_quality_mode : `None`, ``VideoQualityMode``, `int`, Optional (Keyword only)
        The channel's video quality mode.
    archived : `None`, `bool`, Optional (Keyword only)
        Whether the thread channel is archived.
    archived_at : `None`, `datetime`, Optional (Keyword only)
        When the thread's archive status was last changed.
    auto_archive_after : `None`, `int`, Optional (Keyword only)
        Duration in minutes to automatically archive the thread after recent activity. Can be one of: `3600`, `86400`,
        `259200`, `604800`.
    open_ : `None`, `bool`, Optional (Keyword only)
        Whether the thread channel is open.
    default_thread_auto_archive_after : `None`, `int`, Optional (Keyword only)
        The default duration (in seconds) for newly created threads to automatically archive the themselves. Can be
        one of: `3600`, `86400`, `259200`, `604800`.
    parent : `None`, ``Channel``, `int`, Optional (Keyword only)
        The channel's parent. If the parent is under a guild, leave it empty.
    available_tags : `None`, `tuple` of ``ForumTag``, Optional (Keyword only)
        The available tags to assign to the child-thread channels.
    guild : `None`, ``Guild`` = `None`, Optional (Keyword only)
        Reference guild used for validation purposes. Defaults to `None`.
    
    Returns
    -------
    channel_data : `dict` of (`str`, `Any`) items
    
    Raises
    ------
    TypeError
        - If a parameter's type is incorrect.
    """
    if (guild is not None) and (not isinstance(guild, Guild)):
        raise TypeError(
            '`guild` is given, but not as `None` nor `Guild`, got '
            f'{guild.__class__.__name__}; {guild!r}.'
        )
    
    channel_type = preconvert_preinstanced_type(channel_type, 'channel_type', ChannelType)
    
    if not channel_type.flags.guild:
        raise TypeError(
            f'`channel_type` not refers to a guild channel type. Got {channel_type!r}.'
        )
    
    
    if not isinstance(name, str):
        raise AssertionError(
            f'`name` can be `str`, got {name.__class__.__name__}; {name!r}.'
        )
    
    name_length = len(name)
    
    if name_length < 1 or name_length > 100:
        raise AssertionError(
            f'`name` length can be in range [1:100], got {name_length}; {name!r}.'
        )
    
    channel_data = {
        'name': name,
        'type': channel_type.value,
    }
    
    if channel_type in HAS_PERMISSION_OVERWRITES:
        if permission_overwrites is ...:
            permission_overwrites = []
        else:
            if __debug__:
                if not isinstance(permission_overwrites, list):
                    raise AssertionError(
                        f'`permission_overwrites` can be `None`, `list` of '
                        f'`cr_p_permission_overwrite_object` returns, got {permission_overwrites.__class__.__name__}; '
                        f'{permission_overwrites!r}.'
                    )
                
                for index, element in enumerate(permission_overwrites):
                    if not isinstance(element, dict):
                        raise AssertionError(
                            f'`permission_overwrites`\'s element {index} should be `dict`, '
                            f'but got {element.__class__.__name__}; {element!r}.'
                        )
        
        channel_data['permission_overwrites'] = permission_overwrites
    else:
        if __debug__:
            if (permission_overwrites is not ...):
                _assert_channel_type(
                    channel_type, None, HAS_PERMISSION_OVERWRITES, 'permission_overwrites', permission_overwrites,
                )
    
    
    _maybe_add_channel_topic_field_to_data(channel_type, None, channel_data, topic)
    _maybe_add_channel_nsfw_field_to_data(channel_type, None, channel_data, nsfw)
    _maybe_add_channel_slowmode_field_to_data(channel_type, None, channel_data, slowmode)
    _maybe_add_channel_bitrate_field_to_data(channel_type, None, channel_data, bitrate)
    _maybe_add_channel_user_limit_field_to_data(channel_type, None, channel_data, user_limit)
    _maybe_add_channel_region_field_to_data(channel_type, None, channel_data, region)
    _maybe_add_channel_video_quality_mode_field_to_data(channel_type, None, channel_data, video_quality_mode)
    
    if (archived is not ...):
        if __debug__:
            _assert_channel_type(channel_type, None, HAS_ARCHIVED, 'archived', archived)
            
            if not isinstance(archived, bool):
                raise AssertionError(
                    f'`archived` can be `None`, `bool`, got {archived.__class__.__name__}; {archived!r}.'
                )
        
        channel_data['archived'] = archived
    
    
    if (archived_at is not ...):
        if __debug__:
            _assert_channel_type(channel_type, None, HAS_ARCHIVED_AT, 'archived_at', archived_at)
            
            if not isinstance(archived_at, datetime):
                raise AssertionError(
                    f'`archived_at` can be `None`, `datetime`, got {archived_at.__class__.__name__}; {archived_at!r}.'
                )
        
        channel_data['archive_timestamp'] =  datetime_to_timestamp(archived_at)
    
    
    if (auto_archive_after is not ...):
        if __debug__:
            _assert_channel_type(channel_type, None, HAS_AUTO_ARCHIVE_AFTER, 'auto_archive_after', auto_archive_after)
            
            if not isinstance(auto_archive_after, int):
                raise AssertionError(
                    f'`auto_archive_after` can be `None`, `datetime`, got {auto_archive_after.__class__.__name__}; '
                    f'{auto_archive_after!r}.'
                )
            
            if auto_archive_after not in AUTO_ARCHIVE_OPTIONS:
                raise AssertionError(
                    f'`auto_archive_after` can be any of: {AUTO_ARCHIVE_OPTIONS}, got {auto_archive_after}.'
                )
        
        channel_data['auto_archive_duration'] = auto_archive_after // 60
    
    
    _maybe_add_channel_default_thread_auto_archive_after_field_to_data(
        channel_type, None, channel_data, default_thread_auto_archive_after
    )
    
    
    if (open_ is not ...):
        if __debug__:
            _assert_channel_type(channel_type, None, HAS_OPEN, 'open_', open_)
            
            if not isinstance(open_, bool):
                raise AssertionError(
                    f'`open_` can be `None`, `bool`, got {open_.__class__.__name__}; {open_!r}.'
                )
        
        channel_data['locked'] = not open_
    
    
    if parent is None:
        parent_id = 0
    
    elif isinstance(parent, Channel):
        parent_id = parent.id
    
    else:
        parent_id = maybe_snowflake(parent)
        if parent_id is None:
            raise TypeError(
                f'`parent` can be `{Channel.__name__}`, `{Guild.__name__}`, `int`, got '
                f'{parent.__class__.__name__}; {parent!r}.'
            )
    
    if parent_id:
        if __debug__:
            if channel_type != CAN_HAVE_PARENT_ID:
                raise AssertionError(
                    f'`parent_id` is only applicable for the given channel type, got {channel_type!r}.'
                )
        
        channel_data['parent_id'] = parent_id
    
    
    return channel_data


def _assert_channel_type(channel_type, channel, accepted_types, field_name, field_value):
    """
    Asserts whether the given `channel_type`, `channel` combination passes the `accepted_types` check.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The channel's type.
    channel : `None`, ``Channel``
        The received channel type if any.
    accepted_types : `tuple` of ``ChannelType``
        The accepted channel types.
    field_name : `str`
        The field's name to assert.
    field_value : `Any`
        The field's value.
    
    Raises
    ------
    AssertionError
    """
    if (channel_type in accepted_types):
        return
    
    if (channel is not None) and channel.partial:
        return
    
    _raise_channel_type_assertion_with_message(channel_type, channel, accepted_types, field_name, field_value)
    return True


def _raise_channel_type_assertion_with_message(channel_type, channel, accepted_types, field_name, field_value):
    """
    Builds a channel type assertion message and raises assertion error.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The channel's type.
    channel : `None`, ``Channel``
        The received channel type if any.
    accepted_types : `tuple` of ``ChannelType``
        The accepted channel types.
    field_name : `str`
        The field's name to assert.
    field_value : `Any`
        The field's value.
    
    Raises
    ------
    AssertionError
    """
    assertion_message_parts = []
    
    assertion_message_parts.append('`')
    assertion_message_parts.append(field_name)
    assertion_message_parts.append('` is only valid for ')
    
    assertion_message_parts.append(', '.join(channel_type.name for channel_type in accepted_types))
    assertion_message_parts.append(', got ')
    assertion_message_parts.append(channel_type.name)
    
    if channel is not None:
        assertion_message_parts.append('; channel=')
        assertion_message_parts.append(repr(channel))
    
    assertion_message_parts.append('; ')
    assertion_message_parts.append(field_name)
    assertion_message_parts.append('=˙')
    assertion_message_parts.append(reprlib.repr(field_value))
    assertion_message_parts.append('˙.')
    
    assertion_message = ''.join(assertion_message_parts)
    assertion_message_parts = None
    
    raise AssertionError(assertion_message)


def _maybe_add_channel_bitrate_field_to_data(channel_type, channel, channel_data, bitrate):
    """
    Adds the given `bitrate` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    bitrate : `Ellipsis`, `int`
        `channel.bitrate` field.
    
    Raises
    ------
    AssertionError
        - If `bitrate`'s type or value is incorrect.
    """
    if (bitrate is not ...):
        if __debug__:
            _assert_channel_type(channel_type, channel, HAS_BITRATE, 'bitrate', bitrate)
            
            if not isinstance(bitrate, int):
                raise AssertionError(
                    f'`bitrate` can be `int`, got {bitrate.__class__.__name__}; {bitrate!r}.'
                )
        
        channel_data['bitrate'] = bitrate


def _maybe_add_channel_topic_field_to_data(channel_type, channel, channel_data, topic):
    """
    Adds the given `topic` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    topic : `Ellipsis`, `str`
        `channel.topic` field.
    
    Raises
    ------
    AssertionError
        - If `topic`'s type or value is incorrect.
    """
    if (topic is not ...):
        if __debug__:
            _assert_channel_type(channel_type, channel, HAS_TOPIC, 'topic', topic)
            
            if not isinstance(topic, str):
                raise AssertionError(
                    f'`topic` can be `str`, got {topic.__class__.__name__}; {topic!r}.'
                )
            
            if channel_type.flags.guild_system:
                topic_length_limit = 1024
            else:
                topic_length_limit = 120
            
            topic_length = len(topic)
            if topic_length > topic_length_limit:
                raise AssertionError(
                    f'`topic` length can be in range [0:{topic_length_limit}], got {topic_length}; {topic!r}.'
                )
        
        channel_data['topic'] = topic


def _maybe_add_channel_nsfw_field_to_data(channel_type, channel, channel_data, nsfw):
    """
    Adds the given `nsfw` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    nsfw : `Ellipsis`, `bool`
        `channel.nsfw` field.
    
    Raises
    ------
    AssertionError
        - If `nsfw`'s type or value is incorrect.
    """
    if (nsfw is not ...):
        if __debug__:
            _assert_channel_type(channel_type, channel, HAS_NSFW, 'nsfw', nsfw)
            
            if not isinstance(nsfw, bool):
                raise AssertionError(
                    f'`nsfw` can be `bool`, got {nsfw.__class__.__name__}; {nsfw!r}.'
                )
        
        channel_data['nsfw'] = nsfw
        

def _maybe_add_channel_slowmode_field_to_data(channel_type, channel, channel_data, slowmode):
    """
    Adds the given `slowmode` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    slowmode : `Ellipsis`, `int`
        `channel.slowmode` field.
    
    Raises
    ------
    AssertionError
        - If `slowmode`'s type or value is incorrect.
    """
    if (slowmode is not ...):
        if __debug__:
            _assert_channel_type(channel_type, channel, HAS_SLOWMODE, 'slowmode', slowmode)
            
            if not isinstance(slowmode, int):
                raise AssertionError(
                    f'`slowmode` can be `int`, got {slowmode.__class__.__name__}; {slowmode!r}.'
                )
            
            if slowmode < 0 or slowmode > 21600:
                raise AssertionError(
                    f'`slowmode` can be in range [0:21600], got: {slowmode!r}.'
                )
        
        channel_data['rate_limit_per_user'] = slowmode


def _maybe_add_channel_user_limit_field_to_data(channel_type, channel, channel_data, user_limit):
    """
    Adds the given `user_limit` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    user_limit : `Ellipsis`, `int`
        `channel.user_limit` field.
    
    Raises
    ------
    AssertionError
        - If `user_limit`'s type or value is incorrect.
    """
    if (user_limit is not ...):
        if __debug__:
            _assert_channel_type(channel_type, channel, HAS_USER_LIMIT, 'user_limit', user_limit)
            
            if not isinstance(user_limit, int):
                raise AssertionError(
                    f'`user_limit` can be `int`, got {user_limit.__class__.__name__}; '
                    f'{user_limit!r}.'
                )
            
            if user_limit < 0 or user_limit > 99:
                raise AssertionError(
                    '`user_limit`\'s value is out of the expected [0:99] range, got '
                    f'{user_limit!r}.'
                )
        
        channel_data['user_limit'] = user_limit


def _maybe_add_channel_region_field_to_data(channel_type, channel, channel_data, region):
    """
    Adds the given `region` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    region : `Ellipsis`, `None`, `str`, ``VoiceRegion``
        `channel.region` field.
    
    Raises
    ------
    AssertionError
        - If `region`'s type or value is incorrect.
    TypeError
        - If `region`'s type is incorrect.
    """
    if (region is not ...):
        if __debug__:
            _assert_channel_type(channel_type, channel, HAS_REGION, 'region', region)
        
        if (region is not None):
            region_value = None
        
        elif isinstance(region, VoiceRegion):
            region_value = region.value
        
        elif isinstance(region, str):
            region_value = region
        
        else:
            raise TypeError(
                f'`region` can be `None`, `str`, `{VoiceRegion.__name__}`, got '
                f'{type(region).__name__}; {region!r}.'
            )
        
        channel_data['rtc_region'] = region_value


def _maybe_add_channel_video_quality_mode_field_to_data(channel_type, channel, channel_data, video_quality_mode):
    """
    Adds the given `video_quality_mode` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    video_quality_mode : `Ellipsis`, ``VideoQualityMode``, `int`
        `channel.video_quality_mode` field.
    
    Raises
    ------
    AssertionError
        - If `video_quality_mode`'s type or value is incorrect.
    TypeError
        - If `video_quality_mode`'s type is incorrect.
    """
    if (video_quality_mode is not ...):
        if __debug__:
            _assert_channel_type(
                channel_type, channel, HAS_VIDEO_QUALITY_MODE, 'video_quality_mode', video_quality_mode
            )
        
        if isinstance(video_quality_mode, VideoQualityMode):
            video_quality_mode_value = video_quality_mode.value
        
        elif isinstance(video_quality_mode, int):
            video_quality_mode_value = video_quality_mode
        
        else:
            raise TypeError(
                f'`video_quality_mode` can be `None`, `str`, `{VideoQualityMode.__name__}`, got '
                f'{video_quality_mode.__class__.__name__}; {video_quality_mode!r}.'
            )
        
        channel_data['video_quality_mode'] = video_quality_mode_value


def _maybe_add_channel_default_thread_auto_archive_after_field_to_data(
    channel_type, channel, channel_data, default_thread_auto_archive_after
):
    """
    Adds the given `default_thread_auto_archive_after` field to `channel_data` if the value is not ellipsis.
    
    Parameters
    ----------
    channel_type : ``ChannelType``
        The respective channel's type.
    channel_data : `dict` of (`str`, `Any`) items
        Channel data to add the field to.
    default_thread_auto_archive_after : `Ellipsis`, `int`
        `channel.default_thread_auto_archive_after` field.
    
    Raises
    ------
    AssertionError
        - If `default_thread_auto_archive_after`'s type or value is incorrect.
    """
    if (default_thread_auto_archive_after is not ...):
        if __debug__:
            _assert_channel_type(
                channel_type,
                channel,
                HAS_DEFAULT_AUTO_ARCHIVE_AFTER,
                'default_thread_auto_archive_after',
                default_thread_auto_archive_after,
            )
            
            if not isinstance(default_thread_auto_archive_after, int):
                raise AssertionError(
                    f'`default_thread_auto_archive_after` can be `None`, `datetime`, got '
                    f'{default_thread_auto_archive_after.__class__.__name__}; {default_thread_auto_archive_after!r}.'
                )
            
            if default_thread_auto_archive_after not in AUTO_ARCHIVE_OPTIONS:
                raise AssertionError(
                    f'`default_thread_auto_archive_after` can be any of: {AUTO_ARCHIVE_OPTIONS}, got '
                    f'{default_thread_auto_archive_after}.'
                )
        
        channel_data['default_auto_archive_duration'] = default_thread_auto_archive_after // 60
