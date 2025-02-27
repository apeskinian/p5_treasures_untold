from datetime import datetime


class UpdateSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.session.session_key:
            request.session['modified'] = (
                datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            )
            request.session.modified = True
        return self.get_response(request)
