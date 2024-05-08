from rest_framework.exceptions import APIException

class AlreadyFollowsUserException(APIException):
    status_code = 409
    default_detail = 'You already follows this user.'
    default_code = 'Conflict'