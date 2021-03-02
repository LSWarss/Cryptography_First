from VingenereCoder import VingenereCoder

def test_vingenere_encoding():
    coder = VingenereCoder("uekatowice")
    testString = "The quick brown fox jumps over 13 lazy dogs."
    assert coder.encode(testString) == str.upper("nloqnwysdviaxfhlfcotmsfekzwhahikc")
    testString = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
    assert coder.encode(testString) == str.upper("fsbefwlawqcwcifdhgfygqitxlpwhxbizrbbpqpkurntrdaagxnmxgbbzcuxlcvoksiqrwoqralpampxbisnwiobtcmwdagrwzfhoqwymstbgzyvcigqabjim")
    coder = VingenereCoder("ambrozja")
    testString = "lamdbanosa asdasdsa karma SKOSDASDA"
    assert coder.encode(testString) == str.upper("lmnupzwosmbjrzbdsmlrfljskatuorma")

def test_vingenere_decoing():
    coder = VingenereCoder("uekatowice")
    testString = str.upper("nloqnwysdviaxfhlfcotmsfekzwhahikc")
    assert coder.decode(testString) == str.upper("thequickbrownfoxjumpsoverlazydogs")
    testString = str.upper("fsbefwlawqcwcifdhgfygqitxlpwhxbizrbbpqpkurntrdaagxnmxgbbzcuxlcvoksiqrwoqralpampxbisnwiobtcmwdagrwzfhoqwymstbgzyvcigqabjim")
    assert coder.decode(testString) == str.upper("loremipsumissimplydummytextoftheprintingandtypesettingindustryloremipsumhasbeentheindustrysstandarddummytexteversincethes")
    coder = VingenereCoder("ambrozja")
    testString = str.upper("lmnupzwosmbjrzbdsmlrfljskatuorma")
    assert coder.decode(testString) == str.upper("lamdbanosaasdasdsakarmaskosdasda")