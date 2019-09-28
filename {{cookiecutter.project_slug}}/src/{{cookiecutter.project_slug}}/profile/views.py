"""HTTP operations for auth."""

from {{cookiecutter.project_slug}}.openapi import object_or_404
from {{cookiecutter.project_slug}}.profile.models import Profile
from mypy_extensions import TypedDict
from pyramid.request import Request
from pyramid.view import view_config

# Python representation of openapi.yaml's ProfileResponse schema
ProfileResponse = TypedDict("ProfileResponse", {"profile": Profile})


@view_config(
    route_name="profile",
    renderer="json",
    request_method="GET",
    openapi=True,
    permission="authenticated",
)
def profile(request: Request) -> ProfileResponse:
    """Get a profile."""
    profile = object_or_404(
        Profile.by_username(
            request.openapi_validated.parameters["path"]["username"], db=request.db
        )
    )
    return {"profile": profile}

