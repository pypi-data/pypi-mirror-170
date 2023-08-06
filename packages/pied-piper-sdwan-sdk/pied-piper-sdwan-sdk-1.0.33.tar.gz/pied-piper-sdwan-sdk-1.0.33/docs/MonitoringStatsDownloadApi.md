# openapi_client.MonitoringStatsDownloadApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download1**](MonitoringStatsDownloadApi.md#download1) | **GET** /statistics/download/{processType}/file/{fileType}/{queue}/{deviceIp}/{token}/{fileName} | 
[**download_list**](MonitoringStatsDownloadApi.md#download_list) | **POST** /statistics/download/{processType}/filelist | 
[**fetch_list**](MonitoringStatsDownloadApi.md#fetch_list) | **GET** /statistics/download/{processType}/fetchvManageList | 


# **download1**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} download1(process_type, file_type, queue, device_ip, token, file_name)



Downloading stats file

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_download_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_download_api.MonitoringStatsDownloadApi(api_client)
    process_type = "processType_example" # str | Process type
    file_type = "fileType_example" # str | File type
    queue = "queue_example" # str | Queue name
    device_ip = "deviceIp_example" # str | Device IP
    token = "token_example" # str | Token
    file_name = "fileName_example" # str | File name

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.download1(process_type, file_type, queue, device_ip, token, file_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsDownloadApi->download1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_type** | **str**| Process type |
 **file_type** | **str**| File type |
 **queue** | **str**| Queue name |
 **device_ip** | **str**| Device IP |
 **token** | **str**| Token |
 **file_name** | **str**| File name |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_list**
> download_list(process_type)



Downloading list of stats file

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_download_api
from openapi_client.model.get_o365_preferred_path_from_v_analytics_request import GetO365PreferredPathFromVAnalyticsRequest
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_download_api.MonitoringStatsDownloadApi(api_client)
    process_type = "processType_example" # str | Possible types are: remoteprocessing, dr
    get_o365_preferred_path_from_v_analytics_request = GetO365PreferredPathFromVAnalyticsRequest(
        key=GetO365PreferredPathFromVAnalyticsRequestValue(
            value_type="ARRAY",
        ),
    ) # GetO365PreferredPathFromVAnalyticsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_list(process_type)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsDownloadApi->download_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.download_list(process_type, get_o365_preferred_path_from_v_analytics_request=get_o365_preferred_path_from_v_analytics_request)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsDownloadApi->download_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_type** | **str**| Possible types are: remoteprocessing, dr |
 **get_o365_preferred_path_from_v_analytics_request** | [**GetO365PreferredPathFromVAnalyticsRequest**](GetO365PreferredPathFromVAnalyticsRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_list**
> fetch_list(process_type)



### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_stats_download_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_stats_download_api.MonitoringStatsDownloadApi(api_client)
    process_type = "processType_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.fetch_list(process_type)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringStatsDownloadApi->fetch_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_type** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

