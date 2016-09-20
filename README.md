# emojencode


What's it do?

```python

    >>> import emojencode, textwrap
    >>> data = emojencode.e64encode(
    ...     b'Man is distinguished, not only by his reason, but by '
    ...     b'this singular passion from other animals, which is a '
    ...     b'lust of the mind, that by a perseverance of delight in '
    ...     b'the continued and indefatigable generation of knowledge, '
    ...     b'exceeds the short vehemence of any carnal pleasure.')
    >>> print('\n'.join(textwrap.wrap(data, 40)))
    😓😖😅😮😈😆😥😳😈😆😑😩😜😷😑😩😛😦😝😵😚😗😍😨😙😖😐😬😈😆😹😯😝😂😁😯😛😦😱😹
    😈😆😉😹😈😆😡😩😜😲😁😲😙😖😅😳😛😶😸😬😈😆😉😵😝😂😁😢😞😒😁😴😚😆😥😳😈😇😍😩
    😛😦😝😵😛😆😅😲😈😇😁😡😜😷😍😩😛😶😸😠😙😧😉😯😛😒😁😯😝😆😡😥😜😢😁😡😛😦😥😭
    😘😖😱😳😋😂😁😷😚😆😥😣😚😂😁😩😜😲😁😡😈😆😱😵😜😷😐😠😛😶😘😠😝😆😡😥😈😆😵😩
    😛😦😐😬😈😇😑😨😘😗😐😠😘😧😤😠😘😒😁😰😙😗😉😳😙😗😙😥😜😦😅😮😘😶😔😠😛😶😘😠
    😙😆😕😬😚😖😝😨😝😂😁😩😛😢😁😴😚😆😔😠😘😶😽😮😝😆😥😮😝😖😕😤😈😆😅😮😙😂😁😩
    😛😦😑😥😙😦😅😴😚😖😝😡😘😦😱😥😈😆😝😥😛😦😕😲😘😗😑😩😛😶😸😠😛😶😘😠😚😶😹😯
    😝😶😱😥😙😆😝😥😋😂😁😥😞😆😍😥😙😖😑😳😈😇😑😨😙😒😁😳😚😆😽😲😝😂😁😶😙😖😡😥
    😛😖😕😮😘😶😔😠😛😶😘😠😘😖😹😹😈😆😍😡😜😦😹😡😛😂😁😰😛😆😕😡😜😷😕😲😙😒😸💩

```

Also this:

```python

    >>> text = emojencode.e64decode('''
    ...     😓😖😅😮😈😆😥😳😈😆😑😩😜😷😑😩😛😦😝😵😚😗😍😨😙😖😐😬😈😆😹😯
    ...     😝😂😁😯😛😦😱😹😈😆😉😹😈😆😡😩😜😲😁😲😙😖😅😳😛😶😸😬😈😆😉😵
    ...     😝😂😁😢😞😒😁😴😚😆😥😳😈😇😍😩😛😦😝😵😛😆😅😲😈😇😁😡😜😷😍😩
    ...     😛😶😸😠😙😧😉😯😛😒😁😯😝😆😡😥😜😢😁😡😛😦😥😭😘😖😱😳😋😂😁😷
    ...     😚😆😥😣😚😂😁😩😜😲😁😡😈😆😱😵😜😷😐😠😛😶😘😠😝😆😡😥😈😆😵😩
    ...     😛😦😐😬😈😇😑😨😘😗😐😠😘😧😤😠😘😒😁😰😙😗😉😳😙😗😙😥😜😦😅😮
    ...     😘😶😔😠😛😶😘😠😙😆😕😬😚😖😝😨😝😂😁😩😛😢😁😴😚😆😔😠😘😶😽😮
    ...     😝😆😥😮😝😖😕😤😈😆😅😮😙😂😁😩😛😦😑😥😙😦😅😴😚😖😝😡😘😦😱😥
    ...     😈😆😝😥😛😦😕😲😘😗😑😩😛😶😸😠😛😶😘😠😚😶😹😯😝😶😱😥😙😆😝😥
    ...     😋😂😁😥😞😆😍😥😙😖😑😳😈😇😑😨😙😒😁😳😚😆😽😲😝😂😁😶😙😖😡😥
    ...     😛😖😕😮😘😶😔😠😛😶😘😠😘😖😹😹😈😆😍😡😜😦😹😡😛😂😁😰😛😆😕😡
    ...     😜😷😕😲😙😒😸💩
    ... ''')
    >>> textwrap.shorten(text.decode('utf-8'), width=55, placeholder='...')
    'Man is distinguished, not only by his reason, but by...'

```

## Installation

    pip3 install emojencode

Requires Python 3.


## Console Script Usage

    emojencode [<data>]
    emojdecode [<data>]

If `data` is not provided, reads from stdin.

When decoding, any unrecognized characters are ignored.

Example:

    $ emojencode 'Hello, 🌎!' > message.e64
    $ cat message.e64
    😒😆😕😬😛😆😼😬😈😏😂😟😣😈😸😡
    $ cat message.e64 | emojdecode
    Hello, 🌎!

    $ emojdecode '
    > cant belive how #blessed i am with such an
    > awesome life ❤😚😒😝😭😈😇😍😯😈😆😅😬😛😶😹😥
    > #weareyoung #lol #yolo
    > '
    i'm so alone


## License

    emojdecode "$(curl -fsSL https://raw.githubusercontent.com/doctaphred/emojencode/master/LICENSE)"


## To Do

- more emoji
- gzip + ascii85 support
- cowsay integration
