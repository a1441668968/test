import random
import string

key_poll=string.ascii_letters+string.digits

def gen_pass(n=8):
    "说明：生成密码"
    result=''
    for i in range(n):
        result+=random.choice(key_poll)
    return result

if __name__ == '__main__':
    print(gen_pass())
    print(gen_pass(4))
    print(gen_pass(12))