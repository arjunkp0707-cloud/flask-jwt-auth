from flask import jsonify
from app.utils.blocklist import BLACKLIST


def register_jwt_handlers(jwt):

    # 🔴 CHECK BLACKLIST
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return jti in BLACKLIST

    # 🔴 RESPONSE IF TOKEN REVOKED
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "error": "token_revoked",
                    "message": "Token has been revoked. Please login again.",
                }
            ),
            401,
        )

    # 🔴 EXPIRED TOKEN HANDLER (keep yours)
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "error": "token_expired",
                    "message": "your session has expired. please refresh token.",
                    "status": 401,
                }
            ),
            401,
        )
