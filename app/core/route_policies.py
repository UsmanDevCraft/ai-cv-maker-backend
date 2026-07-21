from typing import Final

USAGE_TRACKED_ROUTES: Final = {
    ("POST", "/api/tailor-cv"),
}

ADMIN_ROUTES: Final = ("/api/v1/admin",)

PUBLIC_ROUTES: Final = {
    "/health",
    "/docs",
    "/openapi.json",
}
