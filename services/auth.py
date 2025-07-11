import os
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions
from flask import request, g
from functools import wraps
from flask_smorest import abort

clerk_client = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

def auth_required(required_roles: list[str] = None):
    required_roles = required_roles or []

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                auth_result = clerk_client.authenticate_request(
                    request,
                    AuthenticateRequestOptions()
                )

                if not auth_result.is_signed_in:
                    return {"message": "Unauthorized", "reason": str(auth_result.reason)}, 401
                
                g.clerk_user = auth_result.payload

                if required_roles:
                    user_role = auth_result.payload.get("public_metadata", {}).get("role", None)
                    if user_role not in required_roles:
                        return {
                        "message": "Forbidden",
                        "reason": f"Required roles: {required_roles}, but user has role: {user_role}"
                    }, 403

                return fn(*args, **kwargs)    
            except Exception as e:
                return {"message": "Unauthorized", "error": str(e)}, 401

        return wrapper
    return decorator