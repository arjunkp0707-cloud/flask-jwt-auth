from flask import jsonify


def register_jwt_handlers(jwt):

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
