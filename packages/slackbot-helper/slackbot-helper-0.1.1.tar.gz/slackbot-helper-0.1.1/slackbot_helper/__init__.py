from .bp import *
from .svc import *
from .dmo import *
from .dto import *

from .bp.normalize_incoming_event import NormalizeIncomingEvent


def normalize_event(d_event: dict,
                    bot_ids: list) -> dict:
    """ Normalize the Incoming Slack Event

    Args:
        d_event (dict): the incoming Slack Event
        Sample Input:
            {
                'blocks': [
                    {
                        'block_id': 'vz+U',
                        'elements': [
                            ...
                        ],
                        'type': 'rich_text'
                    }
                ],
                'channel': 'C046DB9TLEL',
                'team': 'T045AR44M70',
                'text': '<@U045HCSMG8K> dead ahead!',
                'ts': 1665195085.499959,
                'type': 'app_mention',
                'user': 'U04674UNRBJ'
            }
        bot_ids (list): a list of known Bot IDs

    Returns:
        dict: the normalized Slack event
        Sample Output:
            {
                'membership': '43fd5022_46c3_11ed_aca2_4c1d96716627'
                'event': {
                    ... copy of input event ...
                },
                'analysis': {
                    'commands': [],
                    'meta_mode': 'human2bot',
                    'meta_type': 'H2B_SINGLE',
                    'text_1': '@U045HCSMG8K dead ahead!',
                    'text_2': 'dead ahead!',
                    'user_all': ['U045HCSMG8K'],
                    'user_source': 'U04674UNRBJ',
                    'user_target': 'U045HCSMG8K'
                },
            }
    """
    return NormalizeIncomingEvent(bot_ids).process(d_event)
