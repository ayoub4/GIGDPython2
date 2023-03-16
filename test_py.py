import main


def test_get_website_title():
    title = main.get_website_title('https://www.google.com')
    assert 'Google' in title


def test_random():
    ret = main.random()
    assert ret == 4


def test_website_language():
    response = main.website_language()
    assert response == 'en'
