==========
Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

- Started writing a CHANGELOG.
- Removed the contextvars/contextlib helpers; Django already tracks the
  currently active language for us, that should be sufficient.
- Increased the test coverage.
- Added checks for the presence and correctness of the ``SITES`` setting.
- Added Python 3.10, Django 4.0rc1 to the CI.
- Changed the code to raise a ``DisallowedHost`` exception instead of a 404 if
  unable to find a matching host for the current request.
- Switched to pre-commit.
- Fixed a bug where the ``redirect_to_site_middleware`` would redirect too
  often.


`0.0.1`_ (2021-09-14)
~~~~~~~~~~~~~~~~~~~~~

- Initial public version.

.. _0.0.1: https://github.com/matthiask/feincms3-language-sites/commit/7a63ed5bf
.. _Next version: https://github.com/matthiask/feincms3-language-sites/compare/0.12...main
