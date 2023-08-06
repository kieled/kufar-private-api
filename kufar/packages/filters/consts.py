GET_FILTERS = "/taxonomy-proxy/v1/dispatch"

_BASE_PARAMS = {"routing": "android_generalist", "taxonomy-version": "2"}
BASE_FILTER_PARAMS = {
    "application": "ad_listing_base",
    "platform": "android",
    **_BASE_PARAMS,
}
FILTERS_PARAMS = {"application": "ad_listing", "platform": "android", **_BASE_PARAMS}
