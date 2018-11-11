# -*- coding: utf-8 -*-
""" slaq.bin.main

    A command-line-interface that demos and
    exercises most of the features available.

    This CLI is used directly in the automated tests
"""

import click
from loggable import get_logger
LOGGER = get_logger(__name__)


@click.group(invoke_without_command=True)
@click.option('--channel', help='set slack channel name', default='robots')
@click.option('--msg', help='set message', default='test message')
@click.option('--describe-channels', help='describe all channels in slack', default=False, is_flag=True)
@click.option('--dump-channel', help='dump contents of slack channel', default=False, is_flag=True)
@click.pass_context
def entry(ctx, channel, dump_channel, describe_channels, msg):
    from slaq import Slack
    slack = Slack()
    err_channel_required = '--channel must be provided with this command'
    err_msg_required = '--msg must be provided with this command'
    if describe_channels:
        LOGGER.debug("dispatching for describe-channels")
        result = [x for x in slack]
    elif dump_channel:
        assert channel, err_channel_required
        LOGGER.debug("dispatching for dump-channel")
        channel = slack[channel]
        LOGGER.debug("got channel: {}".format(channel))
        result = [x for x in channel][-10:]
    print result
    return result
