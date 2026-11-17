from pwn import *

host = '127.0.0.1'
port = 5000

p = remote(host, port)

g = p.recvline().decode().strip()

p1 = int(g)

g = p.recvline().decode().strip()

q = int(g)

ans = p1 * q

p.recvuntil(b">> ")

p.sendline(b'1')
p.recvuntil(b"Type your modulus here: ")

p.sendline(str(ans).encode())

ans = p.recvline().decode().strip()

if ans == 0:
    ans = p1 * q

p.recvuntil(b">> ")
p.sendline(b'2')

p.sendline(str(ans).encode())
p.recvuntil(b"Type your guess here: ")
print(p.recvline().decode())

p.close()
