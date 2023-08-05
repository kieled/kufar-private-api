ADD_FAVORITE_ADVERT = '/account_save_ad.json'
# @GET
# @PAYLOAD
# list_id - QUERY - int
# @RESPONSE - ToggleFavorite

DELETE_FAVORITE_ADVERT = '/account_delete_save_ad.json'
# @GET
# @PAYLOAD
# list_id - QUERY - int
# @RESPONSE - ToggleFavorite


GET_FAVORITE_ADVERTS = '/account_get_list_saved_ads.json'
# @GET
# @RESPONSE - FavoriteAdverts


GET_FAVORITE_ADVERTS_IDS = '/account_get_favourite_ads_ad_ids.json'
# @GET
# RESPONSE: {"ad_ids": list[int]}

