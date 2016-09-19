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

Requires Python 3.


## To Do

- more emoji
- gzip + ascii85 support
- cowsay integration
