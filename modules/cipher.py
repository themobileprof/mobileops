import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]
class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')
        self.iv = "@The1Mobile2Prof!".encode('utf-8')

    def encrypt( self, raw ):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode(cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        return unpad(cipher.decrypt( enc )).decode('utf8')



# key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))
# cipher = AESCipher('enIntVecTest2020')
# encrypted = cipher.encrypt('#test@12345')
# print(encrypted.decode('utf-8'))
# -> lHhq1OzMSYnj+0XxiNzKhQ==
# decrypted = cipher.decrypt(encrypted)
# print(decrypted)
# -> #test@12345
