<table>
  <tr><th><strong>python-slacks</strong></th>
    <th style="padding:0px 5px;text-align:right;float:right;">
      <small><small>
      <a href=#overview>Overview</a> |
      <a href=#overview>Design</a> |
      <a href=#prerequisites>Prerequisites</a> |
      <a href=#usage>Usage</a> |
      <a href=#running-tests>Running Tests</a> |
      <a href=#future-work>Future Work</a>
      </small><small>
    </th>
  </tr>
  <tr>
    <td width=15%><img src=img/icon.png style="width:150px"></td>
    <td>
    This is a library that makes python / slack interaction a little bit less painful
    </td>
  </tr>
</table>

## Overview

The Slack API limits all kinds of operations depending on whether you have a bot token or user token.  This basic consideration is pretty awkward to work with for a lot of use-cases including slash-commands and some more full-featured bots, because without an abstraction one has to have two API client handles and remember which operations to use which client for.

The best python API-wrapper I could find is also a very low-level interface, providing no useful abstractions for working with channels, users, etc.  Working IDs for channels/users in some places but then with human-friendly names in other places is also a common problem.  

All of this stuff usually means I keep inventing the same abstractions over and over, hence this library.

## Installation

```
pip install --process-dependency-links -e git://github.com/mattvonrocketstein/slacks.git@master#egg=slacks
```

## Prerequisites

#### Slack Tokens

See the [slack documentation](#) for information about how to set this up.

#### Local Dotfiles

It's optional to do things this way, but you may want to manage configuration details outside of your code that instantiated the library.  This library supports dot-env files natively via the [pydotenv library](#).  If the library is used from a working directory that includes a `.env` the contents will automatically loaded into `os.environ` on your behalf.  

All of the expected/supported environment variables are included below

```
SLACK_BOT_TOKEN=xoxb-some-blocks-of-numbers
SLACK_USER_TOKEN=xoxp-some-blocks-of-numbers
```

## Usage

Depending on your use-case, you can provide one or both of the bot/user tokens, either in arguments when instantiating the slack client handle, or in environment variables.

```
from slacks import slacks

# if you're using .env, or otherwise setting up the environment  
# variables you can instantiate the client with no arguments at all.
client = slacks()

# or, provide all the details directly to the constructor
client = slacks(bot_token=.., user_token=..)
```

## Running Tests

Placeholder

## Future Work

1. If you try to do something that requires a user token, but have only provided a bot token `NeedsUser` is thrown.
1. If you try to do something that only requires a bot token, but you don't have enough bot permissions, then `NeedPermissions` is thrown unless you have also provided a user token.  If the user token is able to grant the bot extra permissions, then it will be done.
