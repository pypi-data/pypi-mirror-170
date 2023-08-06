# openapi_client.RealTimeMonitoringCellularAONIpsecInterfaceApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aon_ipsec_interface_counters_info**](RealTimeMonitoringCellularAONIpsecInterfaceApi.md#get_aon_ipsec_interface_counters_info) | **GET** /device/cellularEiolte/ipsec/interface/counters | 
[**get_aon_ipsec_interface_sessionnfo**](RealTimeMonitoringCellularAONIpsecInterfaceApi.md#get_aon_ipsec_interface_sessionnfo) | **GET** /device/cellularEiolte/ipsec/interface/session | 


# **get_aon_ipsec_interface_counters_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aon_ipsec_interface_counters_info(device_id)



Get cellular ipsec interface info from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cellular_aon_ipsec_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cellular_aon_ipsec_interface_api.RealTimeMonitoringCellularAONIpsecInterfaceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aon_ipsec_interface_counters_info(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCellularAONIpsecInterfaceApi->get_aon_ipsec_interface_counters_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

# **get_aon_ipsec_interface_sessionnfo**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aon_ipsec_interface_sessionnfo(device_id)



Get cellular ipsec interface info from device

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_cellular_aon_ipsec_interface_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_cellular_aon_ipsec_interface_api.RealTimeMonitoringCellularAONIpsecInterfaceApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_aon_ipsec_interface_sessionnfo(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringCellularAONIpsecInterfaceApi->get_aon_ipsec_interface_sessionnfo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

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

