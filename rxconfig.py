import reflex as rx

config = rx.Config(
    app_name="ejercitoaf",
    api_url="https://americanforce-web.up.railway.app",
    cors_allowed_origins=["http://localhost:3000", "https://americanforce-web.vercel.app"]
)