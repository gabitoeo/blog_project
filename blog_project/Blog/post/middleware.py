import logging

logger = logging.getLogger(__name__)

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log de la solicitud HTTP
        logger.info(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        return response
    