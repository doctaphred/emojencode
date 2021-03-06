"""emojencode: what base64 could have been"""
from base64 import b64decode, b64encode


b64alphabet = (b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               b'abcdefghijklmnopqrstuvwxyz'
               b'0123456789+/')

b64pad = ord('=')


# The first 64 "emoticon" emoji, starting at code point 0x1F600
e64alphabet = ('😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏'
               '😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟'
               '😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯'
               '😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿')

e64pad = '💩'  # Obviously


_pairs = tuple(zip(b64alphabet, e64alphabet)) + ((b64pad, e64pad),)
e64encode_map = dict(_pairs)
e64decode_map = dict((e, b) for b, e in _pairs)


def e64encode(data):
    """
    >>> e64encode(b'ayy lmao')
    '😘😗😥😹😈😆😱😭😘😖😼💩'
    """
    return ''.join(e64encode_map[byte] for byte in b64encode(data))


def e64decode(emoji):
    """
    >>> e64decode('😘😗😥😹😈😆😱😭😘😖😼💩')
    b'ayy lmao'
    """
    return b64decode(bytes(
        e64decode_map[emojus] for emojus in emoji if emojus in e64decode_map))


def _encode():
    """Console script entry point."""
    print(e64encode(_get_input().encode('utf-8')), end='')


def _decode():
    """Console script entry point."""
    print(e64decode(_get_input()).decode('utf-8'), end='')


def _get_input():
    import sys
    try:
        return sys.argv[1]
    except IndexError:
        try:
            return input()
        except KeyboardInterrupt:
            print(
                '\n'
                'Usage: `emojencode [<data>]`\n'
                '       `emojdecode [<data>]`\n'
                'If <data> is omitted, reads from stdin.'
            )
            sys.exit(-1)
