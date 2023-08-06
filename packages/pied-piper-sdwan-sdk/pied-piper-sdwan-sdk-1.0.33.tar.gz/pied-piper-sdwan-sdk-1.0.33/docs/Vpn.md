# Vpn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_to_site_vpn** | [**SiteToSiteVpn**](SiteToSiteVpn.md) |  | 
**name** | **str** | Name of the Profile Parcel. Must be unique. | 
**type** | **str** | type | 
**ip_sec_policy** | [**IpSecPolicy**](IpSecPolicy.md) |  | [optional] 
**created_by** | **str** | User who last created this. | [optional] [readonly] 
**created_on** | **int** | Timestamp of creation | [optional] [readonly] 
**id** | **str** | System generated unique identifier of the Profile Parcel in UUID format. | [optional] 
**last_updated_by** | **str** | User who last updated this. | [optional] [readonly] 
**last_updated_on** | **int** | Timestamp of last update | [optional] [readonly] 
**variables** | [**[Variable]**](Variable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


