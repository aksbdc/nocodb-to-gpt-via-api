# test_sample.py
def zip_code_dec(anc):
    return anc - 8

def test_answer_location():
    assert zip_code_dec(99508) == 99500
