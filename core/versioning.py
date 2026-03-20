from rest_framework import versioning


class SemanticVersioning(versioning.BaseVersioning):
    """
    Reads X-App-Version header and parses it into a tuple.
    "2.3.1" -> (2, 3, 1)
    """

    def determine_version(self, request, *args, **kwargs):
        raw = request.headers.get("X-App-Version", "1.0.0")
        try:
            parts = tuple(int(x) for x in raw.split("."))
            return (parts + (0, 0, 0))[:3]
        except (ValueError, AttributeError):
            return (1, 0, 0)
