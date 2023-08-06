# openapi_client.ConfigurationCloudOnRampApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquire_resource_pool**](ConfigurationCloudOnRampApi.md#acquire_resource_pool) | **POST** /template/cor/acquireResourcePool | 
[**add_device_pair**](ConfigurationCloudOnRampApi.md#add_device_pair) | **POST** /template/cor/devicepair | 
[**add_transit_vpc**](ConfigurationCloudOnRampApi.md#add_transit_vpc) | **POST** /template/cor/transitvpc | 
[**authenticate_cloud_on_ramp_cred_and_add**](ConfigurationCloudOnRampApi.md#authenticate_cloud_on_ramp_cred_and_add) | **POST** /template/cor/cloud/authenticate | 
[**authenticate_cred_and_update**](ConfigurationCloudOnRampApi.md#authenticate_cred_and_update) | **PUT** /template/cor/cloud/authenticate | 
[**create_and_map**](ConfigurationCloudOnRampApi.md#create_and_map) | **POST** /template/cor | 
[**create_resource_pool**](ConfigurationCloudOnRampApi.md#create_resource_pool) | **POST** /template/cor/createResourcePool | 
[**get_ami_list**](ConfigurationCloudOnRampApi.md#get_ami_list) | **GET** /template/cor/ami | 
[**get_cloud_accounts**](ConfigurationCloudOnRampApi.md#get_cloud_accounts) | **GET** /template/cor/cloud/account | 
[**get_cloud_host_vpc_account_details**](ConfigurationCloudOnRampApi.md#get_cloud_host_vpc_account_details) | **GET** /template/cor/cloud/host/accountdetails | 
[**get_cloud_host_vpcs**](ConfigurationCloudOnRampApi.md#get_cloud_host_vpcs) | **GET** /template/cor/hostvpc | 
[**get_cloud_list**](ConfigurationCloudOnRampApi.md#get_cloud_list) | **GET** /template/cor/cloud | 
[**get_cloud_mapped_host_accounts**](ConfigurationCloudOnRampApi.md#get_cloud_mapped_host_accounts) | **GET** /template/cor/cloud/mappedhostaccounts | 
[**get_cloud_on_ramp_devices**](ConfigurationCloudOnRampApi.md#get_cloud_on_ramp_devices) | **GET** /template/cor/device | 
[**get_cor_status**](ConfigurationCloudOnRampApi.md#get_cor_status) | **GET** /template/cor | 
[**get_external_id**](ConfigurationCloudOnRampApi.md#get_external_id) | **GET** /template/cor/externalId | 
[**get_host_vpcs**](ConfigurationCloudOnRampApi.md#get_host_vpcs) | **GET** /template/cor/devicepair/hostvpc | 
[**get_mapped_vpcs**](ConfigurationCloudOnRampApi.md#get_mapped_vpcs) | **GET** /template/cor/map | 
[**get_pem_key_list**](ConfigurationCloudOnRampApi.md#get_pem_key_list) | **GET** /template/cor/pem | 
[**get_tenant_and_host_vpc_list**](ConfigurationCloudOnRampApi.md#get_tenant_and_host_vpc_list) | **GET** /template/cor/hostvpclist | 
[**get_transit_device_pair_and_host_list**](ConfigurationCloudOnRampApi.md#get_transit_device_pair_and_host_list) | **GET** /template/cor/getTransitDevicePairAndHostList | 
[**get_transit_vpc_supported_size**](ConfigurationCloudOnRampApi.md#get_transit_vpc_supported_size) | **GET** /template/cor/transitvpc/size | 
[**get_transit_vpc_vpn_list**](ConfigurationCloudOnRampApi.md#get_transit_vpc_vpn_list) | **GET** /template/cor/getTransitVpnList | 
[**get_transit_vpcs**](ConfigurationCloudOnRampApi.md#get_transit_vpcs) | **GET** /template/cor/transitvpc | 
[**map_vpcs**](ConfigurationCloudOnRampApi.md#map_vpcs) | **POST** /template/cor/map | 
[**raise_alarm_for_account**](ConfigurationCloudOnRampApi.md#raise_alarm_for_account) | **POST** /template/cor/account/alarm | 
[**remove_device_id**](ConfigurationCloudOnRampApi.md#remove_device_id) | **DELETE** /template/cor/deleteDevicepair | 
[**remove_transit_vpc**](ConfigurationCloudOnRampApi.md#remove_transit_vpc) | **DELETE** /template/cor/accountid/{accountid} | 
[**scale_down**](ConfigurationCloudOnRampApi.md#scale_down) | **POST** /template/cor/scale/down | 
[**scale_up**](ConfigurationCloudOnRampApi.md#scale_up) | **POST** /template/cor/scale/up | 
[**unmap_vpcs**](ConfigurationCloudOnRampApi.md#unmap_vpcs) | **DELETE** /template/cor/map | 
[**update_host_vpc_reachability**](ConfigurationCloudOnRampApi.md#update_host_vpc_reachability) | **PUT** /template/cor/hostvpclist | 
[**update_transit_vpc**](ConfigurationCloudOnRampApi.md#update_transit_vpc) | **PUT** /template/cor/transitvpc | 
[**update_transit_vpc_autoscale_properties**](ConfigurationCloudOnRampApi.md#update_transit_vpc_autoscale_properties) | **PUT** /template/cor/transitvpc/autoscale-properties | 
[**updatestatus**](ConfigurationCloudOnRampApi.md#updatestatus) | **POST** /template/cor/status | 


# **acquire_resource_pool**
> acquire_resource_pool()



Acquire IP from resource pool

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Add IP from resource pool request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.acquire_resource_pool(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->acquire_resource_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Add IP from resource pool request | [optional]

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

# **add_device_pair**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_device_pair()



Add device pair

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Add device pair request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_device_pair(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->add_device_pair: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Add device pair request | [optional]

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

# **add_transit_vpc**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} add_transit_vpc()



Create transit VPC/VNet

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPC (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_transit_vpc(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->add_transit_vpc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPC | [optional]

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

# **authenticate_cloud_on_ramp_cred_and_add**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} authenticate_cloud_on_ramp_cred_and_add()



Authenticate cloud account credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloud account credential (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.authenticate_cloud_on_ramp_cred_and_add(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->authenticate_cloud_on_ramp_cred_and_add: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloud account credential | [optional]

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

# **authenticate_cred_and_update**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} authenticate_cred_and_update()



Authenticate and update cloud account credentials

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Cloud account credential (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.authenticate_cred_and_update(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->authenticate_cred_and_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Cloud account credential | [optional]

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

# **create_and_map**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_and_map()



Map Host to Transit VPC/VNet

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Map host to transit VPC request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_and_map(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->create_and_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Map host to transit VPC request | [optional]

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

# **create_resource_pool**
> create_resource_pool()



Add resource pool

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Add resource pool request (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.create_resource_pool(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->create_resource_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Add resource pool request | [optional]

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

# **get_ami_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_ami_list(accountid, cloudregion)



Get AMI list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudregion = "cloudregion_example" # str | Cloud region
    cloudtype = "AWS" # str | Cloud type (optional) if omitted the server will use the default value of "AWS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_ami_list(accountid, cloudregion)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_ami_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_ami_list(accountid, cloudregion, cloudtype=cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_ami_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudregion** | **str**| Cloud region |
 **cloudtype** | **str**| Cloud type | [optional] if omitted the server will use the default value of "AWS"

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

# **get_cloud_accounts**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_accounts(cloudtype, cloud_environment)



Get cloud accounts

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    cloudtype = "cloudtype_example" # str | Cloud type
    cloud_environment = "cloudEnvironment_example" # str | Cloud environment

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_accounts(cloudtype, cloud_environment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloudtype** | **str**| Cloud type |
 **cloud_environment** | **str**| Cloud environment |

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

# **get_cloud_host_vpc_account_details**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_host_vpc_account_details()



Get cloud host VPC account details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_host_vpc_account_details()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_host_vpc_account_details: %s\n" % e)
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

# **get_cloud_host_vpcs**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_host_vpcs(accountid, cloudregion)



Get host VPC/VNet list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudregion = "cloudregion_example" # str | Cloud region
    cloudtype = "AWS" # str | Cloud type (optional) if omitted the server will use the default value of "AWS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_host_vpcs(accountid, cloudregion)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_host_vpcs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_cloud_host_vpcs(accountid, cloudregion, cloudtype=cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_host_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudregion** | **str**| Cloud region |
 **cloudtype** | **str**| Cloud type | [optional] if omitted the server will use the default value of "AWS"

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

# **get_cloud_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_list()



Get cloud list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_list: %s\n" % e)
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

# **get_cloud_mapped_host_accounts**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_cloud_mapped_host_accounts(accountid, cloudtype)



Get cloud mapped accounts view

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudtype = "cloudtype_example" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cloud_mapped_host_accounts(accountid, cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_mapped_host_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudtype** | **str**| Cloud type |

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

# **get_cloud_on_ramp_devices**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cloud_on_ramp_devices()



Get available device list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cloud_on_ramp_devices()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cloud_on_ramp_devices: %s\n" % e)
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

# **get_cor_status**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_cor_status()



Get Cloud On Ramp list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_cor_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_cor_status: %s\n" % e)
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

# **get_external_id**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_external_id()



Get the vManage external ID for AWS

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_external_id()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_external_id: %s\n" % e)
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

# **get_host_vpcs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_host_vpcs(transit_vpc_id, device_pair_id)



Get host VPC details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    transit_vpc_id = "transitVpcId_example" # str | Transit VPC Id
    device_pair_id = "devicePairId_example" # str | Device pair Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_host_vpcs(transit_vpc_id, device_pair_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_host_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transit_vpc_id** | **str**| Transit VPC Id |
 **device_pair_id** | **str**| Device pair Id |

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

# **get_mapped_vpcs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_mapped_vpcs(accountid, cloudregion)



Get mapped VPC/VNet list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudregion = "cloudregion_example" # str | Cloud region

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mapped_vpcs(accountid, cloudregion)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_mapped_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudregion** | **str**| Cloud region |

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

# **get_pem_key_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_pem_key_list(accountid, cloudregion, cloudtype)



Get transit VPC PEM key list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudregion = "cloudregion_example" # str | Cloud region
    cloudtype = "cloudtype_example" # str | Cloud type

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_pem_key_list(accountid, cloudregion, cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_pem_key_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudregion** | **str**| Cloud region |
 **cloudtype** | **str**| Cloud type |

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

# **get_tenant_and_host_vpc_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_tenant_and_host_vpc_list()



Get tenant and host VPC list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    intent = "undefined" # str | Intent (optional) if omitted the server will use the default value of "undefined"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_tenant_and_host_vpc_list(intent=intent)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_tenant_and_host_vpc_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intent** | **str**| Intent | [optional] if omitted the server will use the default value of "undefined"

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

# **get_transit_device_pair_and_host_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_transit_device_pair_and_host_list(account_id, cloud_region)



Get device and host details

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    account_id = "accountId_example" # str | Account Id
    cloud_region = "cloudRegion_example" # str | Cloud region

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transit_device_pair_and_host_list(account_id, cloud_region)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_transit_device_pair_and_host_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |
 **cloud_region** | **str**| Cloud region |

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

# **get_transit_vpc_supported_size**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_transit_vpc_supported_size(cloud_environment)



Get transit VPC supported size

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    cloud_environment = "cloudEnvironment_example" # str | Cloud environment
    cloudtype = "AWS" # str | Cloud type (optional) if omitted the server will use the default value of "AWS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transit_vpc_supported_size(cloud_environment)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_transit_vpc_supported_size: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transit_vpc_supported_size(cloud_environment, cloudtype=cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_transit_vpc_supported_size: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_environment** | **str**| Cloud environment |
 **cloudtype** | **str**| Cloud type | [optional] if omitted the server will use the default value of "AWS"

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

# **get_transit_vpc_vpn_list**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_transit_vpc_vpn_list(account_id)



Get transit VPN list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    account_id = "accountId_example" # str | Account Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transit_vpc_vpn_list(account_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_transit_vpc_vpn_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account Id |

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

# **get_transit_vpcs**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_transit_vpcs(accountid, cloudregion)



Get transit VPC/VNet list

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    cloudregion = "cloudregion_example" # str | Cloud region
    cloudtype = "AWS" # str | Cloud type (optional) if omitted the server will use the default value of "AWS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_transit_vpcs(accountid, cloudregion)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_transit_vpcs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_transit_vpcs(accountid, cloudregion, cloudtype=cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->get_transit_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **cloudregion** | **str**| Cloud region |
 **cloudtype** | **str**| Cloud type | [optional] if omitted the server will use the default value of "AWS"

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

# **map_vpcs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} map_vpcs()



Map host to transit VPC/VNet

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Map host to VPC/VNet (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.map_vpcs(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->map_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Map host to VPC/VNet | [optional]

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

# **raise_alarm_for_account**
> raise_alarm_for_account()



Raise alarm for account

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Account object (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.raise_alarm_for_account(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->raise_alarm_for_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Account object | [optional]

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

# **remove_device_id**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_device_id(accountid, transitvpcid, transitvpcname, cloudregion, device_pair_id)



Remove device pair

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    transitvpcid = "transitvpcid_example" # str | VPC Id
    transitvpcname = "transitvpcname_example" # str | VPC Name
    cloudregion = "cloudregion_example" # str | Cloud region
    device_pair_id = "devicePairId_example" # str | Device pair Id
    cloudtype = "AWS" # str | Cloud type (optional) if omitted the server will use the default value of "AWS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_device_id(accountid, transitvpcid, transitvpcname, cloudregion, device_pair_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->remove_device_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_device_id(accountid, transitvpcid, transitvpcname, cloudregion, device_pair_id, cloudtype=cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->remove_device_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **transitvpcid** | **str**| VPC Id |
 **transitvpcname** | **str**| VPC Name |
 **cloudregion** | **str**| Cloud region |
 **device_pair_id** | **str**| Device pair Id |
 **cloudtype** | **str**| Cloud type | [optional] if omitted the server will use the default value of "AWS"

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

# **remove_transit_vpc**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} remove_transit_vpc(accountid, transitvpcid, cloudregion)



Delete transit VPC/VNet

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    accountid = "accountid_example" # str | Account Id
    transitvpcid = "transitvpcid_example" # str | Cloud VPC Id
    cloudregion = "cloudregion_example" # str | Cloud region
    cloudtype = "AWS" # str | Cloud type (optional) if omitted the server will use the default value of "AWS"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.remove_transit_vpc(accountid, transitvpcid, cloudregion)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->remove_transit_vpc: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.remove_transit_vpc(accountid, transitvpcid, cloudregion, cloudtype=cloudtype)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->remove_transit_vpc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| Account Id |
 **transitvpcid** | **str**| Cloud VPC Id |
 **cloudregion** | **str**| Cloud region |
 **cloudtype** | **str**| Cloud type | [optional] if omitted the server will use the default value of "AWS"

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

# **scale_down**
> scale_down()



Scale down cloud on ramp

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update VPC (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.scale_down(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->scale_down: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update VPC | [optional]

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

# **scale_up**
> scale_up()



Scale up cloud on ramp

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update VPC (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.scale_up(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->scale_up: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update VPC | [optional]

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

# **unmap_vpcs**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} unmap_vpcs()



Unmap host from transit VPC/VNet

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Unmap host to VPC/VNet (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.unmap_vpcs(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->unmap_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Unmap host to VPC/VNet | [optional]

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

# **update_host_vpc_reachability**
> update_host_vpc_reachability()



Update host VPC reachability

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Update VPC status (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.update_host_vpc_reachability(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->update_host_vpc_reachability: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Update VPC status | [optional]

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

# **update_transit_vpc**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_transit_vpc()



Update transit VPC/VNet

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPC (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_transit_vpc(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->update_transit_vpc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPC | [optional]

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

# **update_transit_vpc_autoscale_properties**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_transit_vpc_autoscale_properties()



Update transit VPC autoscale properties

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | VPC (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_transit_vpc_autoscale_properties(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->update_transit_vpc_autoscale_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| VPC | [optional]

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

# **updatestatus**
> updatestatus()



Update task status

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_cloud_on_ramp_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_cloud_on_ramp_api.ConfigurationCloudOnRampApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Status object (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.updatestatus(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationCloudOnRampApi->updatestatus: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Status object | [optional]

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

