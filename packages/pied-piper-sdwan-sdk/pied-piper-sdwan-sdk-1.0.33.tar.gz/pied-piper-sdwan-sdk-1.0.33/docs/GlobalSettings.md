# GlobalSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Profile Parcel. Must be unique. | 
**type** | **str** | type | 
**basic_name** | **str** |  | [optional] 
**basic_description** | **str** |  | [optional] 
**ntp_server** | [**[ConnectToNtpServer]**](ConnectToNtpServer.md) |  | [optional] 
**systems** | [**Systems**](Systems.md) |  | [optional] 
**banner** | [**Banner**](Banner.md) |  | [optional] 
**login_access_to_router** | [**LoginAccessToRouter**](LoginAccessToRouter.md) |  | [optional] 
**bfd** | [**Bfd**](Bfd.md) |  | [optional] 
**omp** | [**OMP**](OMP.md) |  | [optional] 
**ip_sec_security** | [**IpSecSecurity**](IpSecSecurity.md) |  | [optional] 
**logging_system_messages** | [**LoggingSystemMessages**](LoggingSystemMessages.md) |  | [optional] 
**created_by** | **str** | User who last created this. | [optional] [readonly] 
**created_on** | **int** | Timestamp of creation | [optional] [readonly] 
**id** | **str** | System generated unique identifier of the Profile Parcel in UUID format. | [optional] 
**last_updated_by** | **str** | User who last updated this. | [optional] [readonly] 
**last_updated_on** | **int** | Timestamp of last update | [optional] [readonly] 
**variables** | [**[Variable]**](Variable.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


