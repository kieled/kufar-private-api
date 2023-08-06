GET_ADVERT = '/search-api/v1/ads/{ad_id}/rendered'
SEARCH_ADVERTS = '/search-api/v1/search/rendered-paginated'
GET_PHONE = '/search-api/v1/ads/{ad_id}/phone'


GEO_ADVERTS = '/search-api/v1/search/map'
# @GET
# size - QUERY - str
# RESPONSE -> GeoAdverts

GET_ADVERTS_COUNT = '/search-api/v1/search/count'
# GET
# RESPONSE -> Count

GET_PHONE_CAPTCHA = '/search-api/v1/ads/{ad_id}/phone/captcha'
# GET
# HEADER - g-recaptcha-response
# RESPONSE -> Phone


# SEARCH_ADVERTS
# GET
# size - QUERY - int
# cursor - QUERY - str
# lang - QUERY - str
# query - QUERY - str
# RESPONSE -> Adverts

SEGMENTATION_HEADER = {
    "X-Segmentation": "routing=android_generalist;application=ad_view;platform=android"
}
USER_SEGMENTATION_HEADER = {
    "X-Segmentation": "routing=android_generalist;application=ad_listing;platform=android"
}
SEGMENTATION_HEADER_WITH_HACK = {
    **SEGMENTATION_HEADER,
    "X-MCHack": "true"
}
