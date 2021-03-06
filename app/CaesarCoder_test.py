import pytest
from CaesarCoder import CaesarCoder

def test_caesar_encoding():
    coder = CaesarCoder(2)
    testString = "lukaszstachnik"
    assert coder.encode(testString) == "nwmcubuvcejpkm"
    testString = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    assert coder.encode(testString) == "nqtgo kruwo ku ukorna fwooa vgzv qh vjg rtkpvkpi cpf vargugvvkpi kpfwuvta. nqtgo kruwo jcu dggp vjg kpfwuvta'u uvcpfctf fwooa vgzv gxgt ukpeg vjg 1500u"
    coder = CaesarCoder(3)
    testString = "lamdbanosa asdasdsa karma SKOSDASDA"
    assert coder.encode(testString) == "odpgedqrvd dvgdvgvd ndupd vnrvgdvgd"

def test_caesar_decoing():
    coder = CaesarCoder(2)
    testString = "nwmcubuvcejpkm"
    assert coder.decode(testString) == "lukaszstachnik"
    testString = "nqtgo kruwo ku ukorna fwooa vgzv qh vjg rtkpvkpi cpf vargugvvkpi kpfwuvta. nqtgo kruwo jcu dggp vjg kpfwuvta'u uvcpfctf fwooa vgzv gxgt ukpeg vjg 1500u"
    assert coder.decode(testString) == "lorem ipsum is simply dummy text of the printing and typesetting industry. lorem ipsum has been the industry's standard dummy text ever since the 1500s"
    coder = CaesarCoder(3)
    testString = "odpgedqrvd dvgdvgvd ndupd vnrvgdvgd"
    assert coder.decode(testString) == "lamdbanosa asdasdsa karma skosdasda"

def test_stridUp():
    coder = CaesarCoder(2)
    assert coder.strideUp('z') == 'b'
    assert coder.strideUp('a') == 'c'
    assert coder.strideUp(' ') == ' '

def test_stridDown():
    coder = CaesarCoder(2)
    assert coder.strideDown('a') == 'y'
    assert coder.strideDown('l') == 'j'
    assert coder.strideDown(' ') == ' '