from VingenereCoder import VingenereCoder

def test_vingenere_encoding():
    coder = VingenereCoder("uekatowice")
    testString = "The quick brown fox jumps over 13 lazy dogs."
    assert coder.encode(testString) == "Nlo qnwys dviax fhl fcotm sfek 13 zwha hikc."
    testString = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    assert coder.encode(testString) == "Fsbef Wlawq cw cifdhg fygqi txlp wh xbi zrbbpqpk urn trdaagxnmxg bbzcuxlc. Voksi Qrwoq ral pamp xbi snwiobtc'm wdagrwzf hoqwy mstb gzyv cigqa bji 1500m"
    coder = VingenereCoder("ambrozja")
    testString = "lamdbanosa asdasdsa karma SKOSDASDA"
    assert coder.encode(testString) == "lmnupzwosm bjrzbdsm lrflj SKATUORMA"

def test_vingenere_decoing():
    coder = VingenereCoder("uekatowice")
    testString = "Nlo qnwys dviax fhl fcotm sfek 13 zwha hikc."
    assert coder.decode(testString) == "The quick brown fox jumps over 13 lazy dogs."
    testString = "Fsbef Wlawq cw cifdhg fygqi txlp wh xbi zrbbpqpk urn trdaagxnmxg bbzcuxlc. Voksi Qrwoq ral pamp xbi snwiobtc'm wdagrwzf hoqwy mstb gzyv cigqa bji 1500m"
    assert coder.decode(testString) == "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    coder = VingenereCoder("ambrozja")
    testString = "lmnupzwosm bjrzbdsm lrflj SKATUORMA"
    assert coder.decode(testString) == "lamdbanosa asdasdsa karma SKOSDASDA"