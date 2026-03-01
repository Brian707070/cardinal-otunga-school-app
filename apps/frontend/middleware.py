from django.http import HttpResponsePermanentRedirect
from django.conf import settings

class HostnameRedirectMiddleware:
    """Redirect IP-based requests to preferred hostname if necessary."""
    preferred = 'chibibyte.local'  # Port 80 (default HTTP) - no port needed
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        
        # Only redirect if accessing via IP and it's not localhost
        if host != self.preferred and host != 'localhost' and not host.startswith('127.'):
            # Check if it's an IP address (simple check)
            if '.' in host and not host.endswith('.local'):
                # Build the redirect URL
                protocol = 'https' if request.is_secure() else 'http'
                url = f"{protocol}://{self.preferred}{request.get_full_path()}"
                if request.GET:
                    url += f"?{request.GET.urlencode()}"
                return HttpResponsePermanentRedirect(url)
        
        return self.get_response(request)
