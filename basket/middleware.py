from datetime import datetime


class UpdateSessionMiddleware:
    """
    Middleware to update the `modified` timestamp of the session.
    Used when checking for abandoned baskets.
    """
    def __init__(self, get_response):
        """
        Initiliazes the middleware.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Sets the `modified` timestamp in the session data.
        **Returns:**
        - The response from the next middleware or view in the stack.
        """
        if request.session.session_key:
            request.session['modified'] = (
                datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            )
            request.session.modified = True
        return self.get_response(request)
