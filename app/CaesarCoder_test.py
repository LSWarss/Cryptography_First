import pytest
from CaesarCoder import CaesarCoder

def test_caesar_encoding():
    coder = CaesarCoder(2)
    testString = "lukaszstachnik"
    assert coder.encode(testString) == "nwmcubuvcejpkm"
    testString = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    assert coder.encode(testString) == "nqtgo kruwo ku ukorna fwooa vgzv qh vjg rtkpvkpi cpf vargugvvkpi kpfwuvta. nqtgo kruwo jcu dggp vjg kpfwuvta'u uvcpfctf fwooa vgzv gxgt ukpeg vjg 1500u"

def test_caesar_decoing():
    coder = CaesarCoder(2)
    testString = "nwmcubuvcejpkm"
    assert coder.decode(testString) == "lukaszstachnik"
    testString = "nqtgo kruwo ku ukorna fwooa vgzv qh vjg rtkpvkpi cpf vargugvvkpi kpfwuvta. nqtgo kruwo jcu dggp vjg kpfwuvta'u uvcpfctf fwooa vgzv gxgt ukpeg vjg 1500u"
    assert coder.decode(testString) == "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

def test_stridUp():
    coder = CaesarCoder(2)
    assert coder.strideUp('z') == 'b'
    assert coder.strideUp('a') == 'c'

def test_stridDown():
    coder = CaesarCoder(2)
    assert coder.strideDown('a') == 'y'
    assert coder.strideDown('l') == 'j'