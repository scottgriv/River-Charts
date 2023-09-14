import socket
from django.http import JsonResponse
from django.shortcuts import render

class HandleBrokenPipeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except socket.error as e:
            # Check if request is AJAX
            if request.is_ajax():
                return JsonResponse({"error": "A broken pipe (socket error) occurred."})
            else:
                # Render error page with context data for regular requests
                context = {'error_message': 'A broken pipe (socket error) occurred.'}
                return render(request, 'rivercharts/error.html', context)
