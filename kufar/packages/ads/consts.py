GET_ADVERT = '/search-api/v1/ads/{ad_id}/rendered'
SEARCH_ADVERTS = '/search-api/v1/search/rendered-paginated'
GET_PHONE = '/search-api/v1/ads/{ad_id}/phone'

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
