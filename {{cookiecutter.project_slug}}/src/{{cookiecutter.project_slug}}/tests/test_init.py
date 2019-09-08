"""Test app initialization helpers."""

from testfixtures import LogCapture

import structlog


def test_logging_configured() -> None:
    """Test that structlog is configured."""

    with LogCapture() as log:

        from {{cookiecutter.project_slug}} import configure_logging

        configure_logging()

        logger = structlog.getLogger("init")
        logger.info("a message")
        logger.error("an error")
        log.check(
            ("init", "INFO", "level='info' logger='init' event='a message'"),
            ("init", "ERROR", "level='error' logger='init' event='an error'"),
        )
