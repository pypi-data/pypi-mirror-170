# openapi_client.ClusterManagementApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_update_user_credentials**](ClusterManagementApi.md#add_or_update_user_credentials) | **POST** /clusterManagement/userCreds | 
[**add_vmanage**](ClusterManagementApi.md#add_vmanage) | **POST** /clusterManagement/setup | 
[**check_if_cluster_locked**](ClusterManagementApi.md#check_if_cluster_locked) | **GET** /clusterManagement/clusterLocked | 
[**configure_vmanage**](ClusterManagementApi.md#configure_vmanage) | **POST** /clusterManagement/configure | 
[**edit_vmanage**](ClusterManagementApi.md#edit_vmanage) | **PUT** /clusterManagement/setup | 
[**get_cluster_workflow_version**](ClusterManagementApi.md#get_cluster_workflow_version) | **GET** /clusterManagement/clusterworkflow/version | 
[**get_configured_ip_list**](ClusterManagementApi.md#get_configured_ip_list) | **GET** /clusterManagement/iplist/{vmanageID} | 
[**get_connected_devices**](ClusterManagementApi.md#get_connected_devices) | **GET** /clusterManagement/connectedDevices/{vmanageIP} | 
[**get_connected_devices_per_tenant**](ClusterManagementApi.md#get_connected_devices_per_tenant) | **GET** /clusterManagement/{tenantId}/connectedDevices/{vmanageIP} | 
[**get_tenancy_mode**](ClusterManagementApi.md#get_tenancy_mode) | **GET** /clusterManagement/tenancy/mode | 
[**get_tenants_list**](ClusterManagementApi.md#get_tenants_list) | **GET** /clusterManagement/tenantList | 
[**get_v_manage_details**](ClusterManagementApi.md#get_v_manage_details) | **GET** /clusterManagement/vManage/details/{vmanageIP} | 
[**health_details**](ClusterManagementApi.md#health_details) | **GET** /clusterManagement/health/details | 
[**health_status_info**](ClusterManagementApi.md#health_status_info) | **GET** /clusterManagement/health/status | 
[**health_summary**](ClusterManagementApi.md#health_summary) | **GET** /clusterManagement/health/summary | 
[**is_cluster_ready**](ClusterManagementApi.md#is_cluster_ready) | **GET** /clusterManagement/isready | 
[**list_vmanages**](ClusterManagementApi.md#list_vmanages) | **GET** /clusterManagement/list | 
[**node_properties**](ClusterManagementApi.md#node_properties) | **GET** /clusterManagement/nodeProperties | 
[**perform_replication_and_rebalance_of_kafka_partitions**](ClusterManagementApi.md#perform_replication_and_rebalance_of_kafka_partitions) | **PUT** /clusterManagement/replicateAndRebalance | 
[**remove_vmanage**](ClusterManagementApi.md#remove_vmanage) | **POST** /clusterManagement/remove | 
[**set_tenancy_mode**](ClusterManagementApi.md#set_tenancy_mode) | **POST** /clusterManagement/tenancy/mode | 


# **add_or_update_user_credentials**
> add_or_update_user_credentials()



Add or update user credentials for cluster operations<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | User credential (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_or_update_user_credentials(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->add_or_update_user_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| User credential | [optional]

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

# **add_vmanage**
> add_vmanage()



Add vManage to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vManage cluster config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.add_vmanage(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->add_vmanage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vManage cluster config | [optional]

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

# **check_if_cluster_locked**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} check_if_cluster_locked()



Check whether cluster is locked<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.check_if_cluster_locked()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->check_if_cluster_locked: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **configure_vmanage**
> configure_vmanage()



Configure vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vManage server config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.configure_vmanage(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->configure_vmanage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vManage server config | [optional]

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

# **edit_vmanage**
> edit_vmanage()



Update vManage cluster info<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vManage cluster config (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.edit_vmanage(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->edit_vmanage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vManage cluster config | [optional]

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

# **get_cluster_workflow_version**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cluster_workflow_version()



List vManages in the cluster<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cluster_workflow_version()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_cluster_workflow_version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_configured_ip_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_configured_ip_list(vmanage_id)



Get configured IP addresses<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    vmanage_id = "vmanageID_example" # str | vManage Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_configured_ip_list(vmanage_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_configured_ip_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vmanage_id** | **str**| vManage Id |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_connected_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_connected_devices(vmanage_ip)



Get connected device for vManage<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    vmanage_ip = "vmanageIP_example" # str | vManage IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_connected_devices(vmanage_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_connected_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vmanage_ip** | **str**| vManage IP |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_connected_devices_per_tenant**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_connected_devices_per_tenant(tenant_id, vmanage_ip)



Get connected device for vManage for a tenant<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    tenant_id = "tenantId_example" # str | Tenant Id
    vmanage_ip = "vmanageIP_example" # str | vManage IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_connected_devices_per_tenant(tenant_id, vmanage_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_connected_devices_per_tenant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant Id |
 **vmanage_ip** | **str**| vManage IP |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_tenancy_mode**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_tenancy_mode()



Get vManage tenancy mode<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tenancy_mode()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_tenancy_mode: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_tenants_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_tenants_list()



Get tenant list<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_tenants_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_tenants_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **get_v_manage_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_v_manage_details(vmanage_ip)



Get vManage detail<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    vmanage_ip = "vmanageIP_example" # str | vManage IP

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_v_manage_details(vmanage_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->get_v_manage_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vmanage_ip** | **str**| vManage IP |

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

# **health_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} health_details()



Get cluster health check details<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.health_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->health_details: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_status_info**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} health_status_info()



Get cluster health check details<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.health_status_info()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->health_status_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_summary**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} health_summary()



Get cluster health check summary<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    is_cached = False # bool | Flag to enable cached result (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.health_summary(is_cached=is_cached)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->health_summary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_cached** | **bool**| Flag to enable cached result | [optional] if omitted the server will use the default value of False

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

# **is_cluster_ready**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} is_cluster_ready()



Is cluster ready<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.is_cluster_ready()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->is_cluster_ready: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **list_vmanages**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_vmanages()



List vManages in the cluster<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_vmanages()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->list_vmanages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

# **node_properties**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} node_properties()



Get properties of vManage being added to  cluster<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.node_properties()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->node_properties: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **perform_replication_and_rebalance_of_kafka_partitions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} perform_replication_and_rebalance_of_kafka_partitions()



Initiate replication and rebalance of kafka topics<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.perform_replication_and_rebalance_of_kafka_partitions()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->perform_replication_and_rebalance_of_kafka_partitions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **remove_vmanage**
> remove_vmanage()



Remove vManage from cluster<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | vManage server info (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.remove_vmanage(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->remove_vmanage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| vManage server info | [optional]

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

# **set_tenancy_mode**
> set_tenancy_mode()



Update vManage tenancy mode

### Example


```python
import time
import openapi_client
from openapi_client.api import cluster_management_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cluster_management_api.ClusterManagementApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Tenancy mode setting (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.set_tenancy_mode(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterManagementApi->set_tenancy_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Tenancy mode setting | [optional]

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

