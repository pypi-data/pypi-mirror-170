# ConfigGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Config Group. Must be unique. | 
**solution** | **str** | Specify one of the device platform solution | 
**state** | **str** | Config Group Deployment state | 
**created_by** | **str** | User who last created this. | [optional] [readonly] 
**created_on** | **int** | Timestamp of creation | [optional] [readonly] 
**description** | **str** | Description of the Config Group. | [optional] 
**devices** | **[str]** |  | [optional] 
**id** | **str** | System generated unique identifier of the Config Group in UUID format. | [optional] 
**last_updated_by** | **str** | User who last updated this. | [optional] [readonly] 
**last_updated_on** | **int** | Timestamp of last update | [optional] [readonly] 
**profiles** | [**[FeatureProfile]**](FeatureProfile.md) | List of devices UUIDs associated with this config group | [optional] 
**source** | **str** | Source of config-group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


