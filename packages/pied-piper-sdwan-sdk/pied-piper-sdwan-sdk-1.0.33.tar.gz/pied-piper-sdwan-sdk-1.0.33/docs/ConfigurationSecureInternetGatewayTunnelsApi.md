# openapi_client.ConfigurationSecureInternetGatewayTunnelsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sig_tunnel_list**](ConfigurationSecureInternetGatewayTunnelsApi.md#get_sig_tunnel_list) | **GET** /template/cloudx/sig_tunnels | 


# **get_sig_tunnel_list**
> get_sig_tunnel_list(device_id)



Get Secure Internet Gateway Tunnel List

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_secure_internet_gateway_tunnels_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_secure_internet_gateway_tunnels_api.ConfigurationSecureInternetGatewayTunnelsApi(api_client)
    device_id = "deviceId_example" # str | Device Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_sig_tunnel_list(device_id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationSecureInternetGatewayTunnelsApi->get_sig_tunnel_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

