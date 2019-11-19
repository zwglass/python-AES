# pycrypto 依赖库 aes 加密解密操作 
# 安装 pycrypto 依赖: pip install pycrypto

# AES 加密解密
from Crypto.Cipher import AES
# 字符串转化为16进制字符串
from binascii import b2a_hex, a2b_hex

def init_pycryptor():
    """
    加密解密 key 固定
    这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
    初始化 obj
    return 加密解密对象
    """
    key = 'h6v8wawj1ec6e7s9'
    crypto_aes_type = AES.MODE_ECB
    pycryptor = AES.new(key, crypto_aes_type)
    return pycryptor

# 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
def encrypt(text):
    # text 必须为英文字符串 不能含有中文
    cryptor = init_pycryptor()
    length = 16
    count = len(text)

    if count % length != 0:
        add = length - (count % length)
    else:
        add = 0
    text = text + ('\0' * add)
    ciphertext = cryptor.encrypt(text)
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串(二进制 -> ASCII)
    b_str = b2a_hex(ciphertext)
    # 转换为str后再输出 bytes -> str
    return b_str.decode('utf-8')

# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    # text 必须为英文字符串 不能含有中文
    cryptor = init_pycryptor()
    plain_text = cryptor.decrypt(a2b_hex(text))  # ASCII -> 二进制
    plain_text2str = plain_text.decode('utf-8')  # bytes -> str
    ret_trip_str = plain_text2str.rstrip('\0')
    return ret_trip_str

# 测试加密解密
if __name__ == '__main__':
    # text = "abcd EFaa"
    text = '12a_A'

    # aes加密测试
    en = encrypt(text)
    print(encrypt(text))

    # aes解密测试
    de = decrypt(en)
    print(de)