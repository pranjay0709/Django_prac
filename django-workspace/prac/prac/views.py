from django.http import HttpResponse


def test_prac(request):
    return (HttpResponse('<h1>my prac project</h1>'))
