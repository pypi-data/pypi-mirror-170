# openapi_client.MonitoringColocationClusterApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_config_by_cluster_id**](MonitoringColocationClusterApi.md#get_cluster_config_by_cluster_id) | **GET** /colocation/monitor/cluster/config | 
[**get_cluster_details_by_cluster_id**](MonitoringColocationClusterApi.md#get_cluster_details_by_cluster_id) | **GET** /colocation/monitor/cluster | 
[**get_cluster_port_mapping_by_cluster_id**](MonitoringColocationClusterApi.md#get_cluster_port_mapping_by_cluster_id) | **GET** /colocation/monitor/cluster/portView | 
[**get_device_detail_by_device_id**](MonitoringColocationClusterApi.md#get_device_detail_by_device_id) | **GET** /colocation/monitor/device | 
[**get_pnf_config**](MonitoringColocationClusterApi.md#get_pnf_config) | **GET** /colocation/monitor/pnf/configuration | 
[**get_service_chain_details**](MonitoringColocationClusterApi.md#get_service_chain_details) | **GET** /colocation/monitor/servicechain | 
[**get_service_group_by_cluster_id**](MonitoringColocationClusterApi.md#get_service_group_by_cluster_id) | **GET** /colocation/monitor/servicegroup | 
[**get_system_status_by_device_id**](MonitoringColocationClusterApi.md#get_system_status_by_device_id) | **GET** /colocation/monitor/device/system | 
[**get_vnf_alarm_count**](MonitoringColocationClusterApi.md#get_vnf_alarm_count) | **GET** /colocation/monitor/vnf/alarms/count | 
[**get_vnf_events_count_detail**](MonitoringColocationClusterApi.md#get_vnf_events_count_detail) | **GET** /colocation/monitor/vnf/alarms | 
[**get_vnf_events_detail**](MonitoringColocationClusterApi.md#get_vnf_events_detail) | **GET** /colocation/monitor/vnf/events | 
[**get_vnf_interface_detail**](MonitoringColocationClusterApi.md#get_vnf_interface_detail) | **GET** /colocation/monitor/vnf/interface | 
[**getpnf_details**](MonitoringColocationClusterApi.md#getpnf_details) | **GET** /colocation/monitor/pnf | 
[**getvnf_by_device_id**](MonitoringColocationClusterApi.md#getvnf_by_device_id) | **GET** /colocation/monitor/device/vnf | 
[**getvnf_details**](MonitoringColocationClusterApi.md#getvnf_details) | **GET** /colocation/monitor/vnf | 
[**list_network_function_map**](MonitoringColocationClusterApi.md#list_network_function_map) | **GET** /colocation/monitor/networkfunction/listmap | 
[**vnf_actions**](MonitoringColocationClusterApi.md#vnf_actions) | **POST** /colocation/monitor/vnf/action | 


# **get_cluster_config_by_cluster_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cluster_config_by_cluster_id(cluster_id)



Provide details of devices of clusters

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cluster_config_by_cluster_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_cluster_config_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_cluster_details_by_cluster_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cluster_details_by_cluster_id(cluster_id)



Provide details of ids of existing clusters

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cluster_details_by_cluster_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_cluster_details_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_cluster_port_mapping_by_cluster_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cluster_port_mapping_by_cluster_id(cluster_id)



Provide details of port mappings in the cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cluster_port_mapping_by_cluster_id(cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_cluster_port_mapping_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id |

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

# **get_device_detail_by_device_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_device_detail_by_device_id()



List details for Device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_device_detail_by_device_id(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_device_detail_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]

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

# **get_pnf_config**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_pnf_config()



List configuration of PNF

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    pnf_serial_number = "pnfSerialNumber_example" # str | PNF serial number (optional)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_pnf_config(pnf_serial_number=pnf_serial_number, cluster_id=cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_pnf_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnf_serial_number** | **str**| PNF serial number | [optional]
 **cluster_id** | **str**| Cluster Id | [optional]

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

# **get_service_chain_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_service_chain_details()



List all service chain or service chains by Id

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)
    user_group_name = "userGroupName_example" # str | UserGroup Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service_chain_details(cluster_id=cluster_id, user_group_name=user_group_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_service_chain_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]
 **user_group_name** | **str**| UserGroup Name | [optional]

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

# **get_service_group_by_cluster_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_service_group_by_cluster_id()



List all attached serviceGroups to cluster

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_service_group_by_cluster_id(cluster_id=cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_service_group_by_cluster_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]

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

# **get_system_status_by_device_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_system_status_by_device_id()



List all connected VNF to a device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_system_status_by_device_id(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_system_status_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]

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

# **get_vnf_alarm_count**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_alarm_count()



Get event detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    user_group = "user_group_example" # str | user group name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_alarm_count(user_group=user_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_vnf_alarm_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | **str**| user group name | [optional]

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

# **get_vnf_events_count_detail**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_events_count_detail()



Get event detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    user_group = "user_group_example" # str | user group name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_events_count_detail(user_group=user_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_vnf_events_count_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group** | **str**| user group name | [optional]

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

# **get_vnf_events_detail**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_events_detail()



Get event detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    vnf_name = "vnfName_example" # str | VNF name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_events_detail(vnf_name=vnf_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_vnf_events_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnf_name** | **str**| VNF name | [optional]

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

# **get_vnf_interface_detail**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_vnf_interface_detail()



Get interface detail of VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    vnf_name = "vnfName_example" # str | VNF name (optional)
    device_ip = "deviceIp_example" # str | Device IP (optional)
    device_class = "deviceClass_example" # str | Device class (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_vnf_interface_detail(vnf_name=vnf_name, device_ip=device_ip, device_class=device_class)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->get_vnf_interface_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnf_name** | **str**| VNF name | [optional]
 **device_ip** | **str**| Device IP | [optional]
 **device_class** | **str**| Device class | [optional]

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

# **getpnf_details**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] getpnf_details()



List all PNF by cluster Id

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getpnf_details(cluster_id=cluster_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->getpnf_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]

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

# **getvnf_by_device_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] getvnf_by_device_id()



List all VNF attached with Device

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    device_id = "deviceId_example" # str | Device Id (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getvnf_by_device_id(device_id=device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->getvnf_by_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id | [optional]

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

# **getvnf_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} getvnf_details()



Provide details of all existing VNF

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    cluster_id = "clusterId_example" # str | Cluster Id (optional)
    user_group_name = "userGroupName_example" # str | UserGroup Name (optional)
    vnf_name = "vnfName_example" # str | VNF Name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.getvnf_details(cluster_id=cluster_id, user_group_name=user_group_name, vnf_name=vnf_name)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->getvnf_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Cluster Id | [optional]
 **user_group_name** | **str**| UserGroup Name | [optional]
 **vnf_name** | **str**| VNF Name | [optional]

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

# **list_network_function_map**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_network_function_map()



Retrieve network function listing

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_network_function_map()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->list_network_function_map: %s\n" % e)
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

# **vnf_actions**
> vnf_actions()



VNF action

### Example


```python
import time
import openapi_client
from openapi_client.api import monitoring_colocation_cluster_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitoring_colocation_cluster_api.MonitoringColocationClusterApi(api_client)
    vm_name = "vmName_example" # str | VM Name (optional)
    device_id = "deviceId_example" # str | Device Id (optional)
    action = "action_example" # str | Action (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.vnf_actions(vm_name=vm_name, device_id=device_id, action=action)
    except openapi_client.ApiException as e:
        print("Exception when calling MonitoringColocationClusterApi->vnf_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_name** | **str**| VM Name | [optional]
 **device_id** | **str**| Device Id | [optional]
 **action** | **str**| Action | [optional]

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

