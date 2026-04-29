from abckend.services.status_service import get_status_data, get_items_data
from backend.shemas.status_shema import StatusOutSchema
from backend.shemas.item_shema import ItemOutSchema


def register_routes(app):
    @app.get("/api/status")
    @app.output(StatusOutSchema)
    def api_status():
        return get_status_data()

    @app.get("/api/items")
    @app.output(ItemOutSchema)
    def api_items():
        return {"items": get_items_data()}