# Encoded By MUMIT ISLAM HIMU
# Py3 Marshal+Zlib+B64 Encryption
# https://github.com/MUMIT-404-CYBER

import marshal, base64, zlib

exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))