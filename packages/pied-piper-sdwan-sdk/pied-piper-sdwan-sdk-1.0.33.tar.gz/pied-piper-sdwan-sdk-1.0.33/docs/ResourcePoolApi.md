# openapi_client.ResourcePoolApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resources**](ResourcePoolApi.md#create_resources) | **PUT** /resourcepool/resource/vpn | 
[**delete_resources**](ResourcePoolApi.md#delete_resources) | **DELETE** /resourcepool/resource/vpn | 
[**get_resources**](ResourcePoolApi.md#get_resources) | **GET** /resourcepool/resource/vpn | 


# **create_resources**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_resources()



Create Vpn resource pool and return tenant device vpn

### Example


```python
import time
import openapi_client
from openapi_client.api import resource_pool_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resource_pool_api.ResourcePoolApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | create resources from resource pool (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_resources(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcePoolApi->create_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| create resources from resource pool | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resources**
> delete_resources(tenant_id, tenant_vpn)



Delete tenant device vpn and release the resource

### Example


```python
import time
import openapi_client
from openapi_client.api import resource_pool_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resource_pool_api.ResourcePoolApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id
    tenant_vpn = 1 # int | Tenant Vpn Number

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_resources(tenant_id, tenant_vpn)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcePoolApi->delete_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |
 **tenant_vpn** | **int**| Tenant Vpn Number |

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_resources(tenant_id, tenant_vpn)



Get tenant device vpn resource

### Example


```python
import time
import openapi_client
from openapi_client.api import resource_pool_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = resource_pool_api.ResourcePoolApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id
    tenant_vpn = 1 # int | Tenant Vpn Number

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_resources(tenant_id, tenant_vpn)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcePoolApi->get_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |
 **tenant_vpn** | **int**| Tenant Vpn Number |

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

