""" slaq
"""

from slaq.logging import Loggable
from memoized_property import memoized_property


class Slaq(Loggable):
    """ very thin wrapper on SlackClient """

    def __init__(self, bot_token=None, user_token=None ** kargs):
        super(Slaq, self).__init__(**kargs)
        self.bot_token = bot_token or os.environ.get('SLACK_BOT_TOKEN')
        self.user_token = user_token or os.environ.get('SLACK_USER_TOKEN')
        if not self.bot_token or self.user_token:
            raise ValueError(
                ("{} requires at least one of "
                 "SLACK_BOT_TOKEN or SLACK_USER_TOKEN").format(
                    self.__class__.__name__))

    @memoized_property
    def bot_client(self):
        self.debug('getting slack client')
        return SlackClient(self.bot_token)

    @memoized_property
    def user_client(self):
        self.debug('getting slack client')
        return SlackClient(self.user_token)

    def channels(self):
        self.debug('loading channels')
        response = self.user_client.api_call("channels.list", count=1000)
        if 'channels' not in response:
            self.logger.warning(pprint.pformat(response))
            raise ValueError('error getting channel list')
        return response['channels']
