from django.http import HttpResponse
from django.urls import path

def vulnerable_view(request):
    user_input = request.GET.get('input', '')

    response = f"""
        <html>
        <head><title>Reflective XSS Demo</title></head>
        <body>
            <h1>Reflective XSS Example</h1>
            <p>You said: {user_input}</p>  <!-- Vulnerable: unsanitized input -->
        </body>
        </html>
    """
    return HttpResponse(response, content_type="text/html")

