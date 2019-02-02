import zlib
def Question79():
    s="hello world!hello world!hello world!hello world!"
    t=str.encode(s)
    print(t)
    z=zlib.compress(t)
    print(z)
    print(zlib.decompress(z))

Question79()