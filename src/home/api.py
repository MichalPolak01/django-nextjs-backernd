from ninja import NinjaAPI, Schema

from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

import helpers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlist/", "waitlists.api.router")


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None


@api.get("/hello")
def hello(request):
    return {"messages": "Hello Word"}

@api.get("/me", response=UserSchema, auth=helpers.api_auth_user_required)
def me(request):
    return request.user