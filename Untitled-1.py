"""Delivery feeder entrance."""
 
# # ruff: noqa: I001
 
# import azure.functions as func
 
# from src.delivery_feeder.blueprint import bp as delivery_feeder_bp
# from src.logging_utils import (
#     configure_logging,
#     dedupe_otel_log_export,
#     get_logger,
#     install_business_only_filter,
# )
# from src.workaround.decompress_gz import bp as decompress_gz_bp
# from src.workaround.eventhub_test import bp as eventhub_test_bp
# from src.workaround.manifest_enlu import bp as manifest_enlu_bp
# from azure.monitor.opentelemetry import configure_azure_monitor
 
# from src.config_loader import get_app_insight_connection_string
# from src.deps import get_cred
 
# #log setting start
# configure_logging()
# logger = get_logger(__name__)
 
# configure_azure_monitor(
#     connection_string=get_app_insight_connection_string(),
#     credential=get_cred(),
# )
# dedupe_otel_log_export(keep=1)
# install_business_only_filter(allow_function_user=True, only_otel_handlers=True)
# #log setting end
 
# app = func.FunctionApp()
# app.register_blueprint(manifest_enlu_bp)
# app.register_blueprint(decompress_gz_bp)
# app.register_blueprint(delivery_feeder_bp)
# app.register_blueprint(eventhub_test_bp)
 
 
 
 
 
import azure.functions as func
import logging
 
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
 
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
 
    name = req.params.get('name')
 
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            logging.info("Boqian Test Info outcommeintg" + name )
 
    if name:
        logging.info("Boqian Test Info outcommeintg" + name )
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    return func.HttpResponse(
         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
         status_code=200
    )