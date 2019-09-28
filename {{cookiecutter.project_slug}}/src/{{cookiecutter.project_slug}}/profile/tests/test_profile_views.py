"""Tests for profile views."""

from {{cookiecutter.project_slug}}.auth.models import User
from {{cookiecutter.project_slug}}.auth.tests.test_auth_views import USER_ONE_JWT
from sqlalchemy.orm.session import Session
from webtest import TestApp


def test_get_profile(testapp: TestApp, democontent: None) -> None:
    """Test POST /api/profiles/{username}."""
    res = testapp.get(
        "/api/profiles/two",
        headers={"Authorization": f"Token {USER_ONE_JWT}"},
        status=200,
    )

    assert res.json == {
        "profile": {"username": "two", "bio": None, "image": None}
    }

