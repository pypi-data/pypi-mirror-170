# openapi_client.TroubleshootingToolsDiagnosticsApi

All URIs are relative to */dataservice*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_session**](TroubleshootingToolsDiagnosticsApi.md#clear_session) | **GET** /stream/device/log/sessions/clear/{sessionId} | 
[**disable_device_log**](TroubleshootingToolsDiagnosticsApi.md#disable_device_log) | **GET** /stream/device/log/disable/{sessionId} | 
[**disable_packet_capture_session**](TroubleshootingToolsDiagnosticsApi.md#disable_packet_capture_session) | **GET** /stream/device/capture/disable/{sessionId} | 
[**disable_speed_test_session**](TroubleshootingToolsDiagnosticsApi.md#disable_speed_test_session) | **GET** /stream/device/speed/disable/{sessionId} | 
[**download_debug_log**](TroubleshootingToolsDiagnosticsApi.md#download_debug_log) | **GET** /stream/device/log/download/{sessionId} | 
[**download_file**](TroubleshootingToolsDiagnosticsApi.md#download_file) | **GET** /stream/device/capture/download/{sessionId} | 
[**force_stop_pcap_session**](TroubleshootingToolsDiagnosticsApi.md#force_stop_pcap_session) | **GET** /stream/device/capture/forcedisbale/{sessionId} | 
[**form_post_packet_capture**](TroubleshootingToolsDiagnosticsApi.md#form_post_packet_capture) | **POST** /stream/device/capture/{deviceUUID}/{sessionId} | 
[**get_aggregation_data_by_query27**](TroubleshootingToolsDiagnosticsApi.md#get_aggregation_data_by_query27) | **GET** /stream/device/nwpi/aggregation | 
[**get_aggregation_data_by_query28**](TroubleshootingToolsDiagnosticsApi.md#get_aggregation_data_by_query28) | **GET** /statistics/speedtest/aggregation | 
[**get_concurrent_data**](TroubleshootingToolsDiagnosticsApi.md#get_concurrent_data) | **GET** /stream/device/nwpi/concurrentData | 
[**get_concurrent_domain_data**](TroubleshootingToolsDiagnosticsApi.md#get_concurrent_domain_data) | **GET** /stream/device/nwpi/concurrentDomainData | 
[**get_count29**](TroubleshootingToolsDiagnosticsApi.md#get_count29) | **GET** /stream/device/nwpi/doccount | 
[**get_count30**](TroubleshootingToolsDiagnosticsApi.md#get_count30) | **GET** /statistics/speedtest/doccount | 
[**get_count_post29**](TroubleshootingToolsDiagnosticsApi.md#get_count_post29) | **POST** /stream/device/nwpi/doccount | 
[**get_count_post30**](TroubleshootingToolsDiagnosticsApi.md#get_count_post30) | **POST** /statistics/speedtest/doccount | 
[**get_db_schema**](TroubleshootingToolsDiagnosticsApi.md#get_db_schema) | **GET** /diagnostics/dbschema | 
[**get_device_log**](TroubleshootingToolsDiagnosticsApi.md#get_device_log) | **GET** /stream/device/log/{sessionId} | 
[**get_domain_metric**](TroubleshootingToolsDiagnosticsApi.md#get_domain_metric) | **GET** /stream/device/nwpi/domainMetric | 
[**get_file_download_status**](TroubleshootingToolsDiagnosticsApi.md#get_file_download_status) | **GET** /stream/device/capture/status/{sessionId} | 
[**get_finalized_data**](TroubleshootingToolsDiagnosticsApi.md#get_finalized_data) | **GET** /stream/device/nwpi/finalizedData | 
[**get_finalized_domain_data**](TroubleshootingToolsDiagnosticsApi.md#get_finalized_domain_data) | **GET** /stream/device/nwpi/finalizedDomainData | 
[**get_flow_detail**](TroubleshootingToolsDiagnosticsApi.md#get_flow_detail) | **GET** /stream/device/nwpi/flowDetail | 
[**get_flow_metric**](TroubleshootingToolsDiagnosticsApi.md#get_flow_metric) | **GET** /stream/device/nwpi/flowMetric | 
[**get_interface_bandwidth**](TroubleshootingToolsDiagnosticsApi.md#get_interface_bandwidth) | **GET** /stream/device/speed/interface/bandwidth | 
[**get_log_type**](TroubleshootingToolsDiagnosticsApi.md#get_log_type) | **GET** /stream/device/log/type | 
[**get_monitor_state**](TroubleshootingToolsDiagnosticsApi.md#get_monitor_state) | **GET** /stream/device/nwpi/getMonitorState | 
[**get_nwpi_dscp**](TroubleshootingToolsDiagnosticsApi.md#get_nwpi_dscp) | **GET** /stream/device/nwpi/nwpiDSCP | 
[**get_nwpi_nbar_app_group**](TroubleshootingToolsDiagnosticsApi.md#get_nwpi_nbar_app_group) | **GET** /stream/device/nwpi/nwpiNbarAppGroup | 
[**get_nwpi_protocol**](TroubleshootingToolsDiagnosticsApi.md#get_nwpi_protocol) | **GET** /stream/device/nwpi/nwpiProtocol | 
[**get_packet_features**](TroubleshootingToolsDiagnosticsApi.md#get_packet_features) | **GET** /stream/device/nwpi/packetFeatures | 
[**get_post_aggregation_app_data_by_query26**](TroubleshootingToolsDiagnosticsApi.md#get_post_aggregation_app_data_by_query26) | **POST** /stream/device/nwpi/app-agg/aggregation | 
[**get_post_aggregation_app_data_by_query27**](TroubleshootingToolsDiagnosticsApi.md#get_post_aggregation_app_data_by_query27) | **POST** /statistics/speedtest/app-agg/aggregation | 
[**get_post_aggregation_data_by_query27**](TroubleshootingToolsDiagnosticsApi.md#get_post_aggregation_data_by_query27) | **POST** /stream/device/nwpi/aggregation | 
[**get_post_aggregation_data_by_query28**](TroubleshootingToolsDiagnosticsApi.md#get_post_aggregation_data_by_query28) | **POST** /statistics/speedtest/aggregation | 
[**get_post_stat_bulk_raw_data27**](TroubleshootingToolsDiagnosticsApi.md#get_post_stat_bulk_raw_data27) | **POST** /stream/device/nwpi/page | 
[**get_post_stat_bulk_raw_data28**](TroubleshootingToolsDiagnosticsApi.md#get_post_stat_bulk_raw_data28) | **POST** /statistics/speedtest/page | 
[**get_session**](TroubleshootingToolsDiagnosticsApi.md#get_session) | **POST** /stream/device/speed | 
[**get_session_info_capture**](TroubleshootingToolsDiagnosticsApi.md#get_session_info_capture) | **POST** /stream/device/capture | 
[**get_session_info_log**](TroubleshootingToolsDiagnosticsApi.md#get_session_info_log) | **POST** /stream/device/log | 
[**get_sessions**](TroubleshootingToolsDiagnosticsApi.md#get_sessions) | **GET** /stream/device/log/sessions | 
[**get_speed_test**](TroubleshootingToolsDiagnosticsApi.md#get_speed_test) | **GET** /stream/device/speed/{sessionId} | 
[**get_speed_test_status**](TroubleshootingToolsDiagnosticsApi.md#get_speed_test_status) | **GET** /stream/device/speed/status/{sessionId} | 
[**get_stat_bulk_raw_data27**](TroubleshootingToolsDiagnosticsApi.md#get_stat_bulk_raw_data27) | **GET** /stream/device/nwpi/page | 
[**get_stat_bulk_raw_data28**](TroubleshootingToolsDiagnosticsApi.md#get_stat_bulk_raw_data28) | **GET** /statistics/speedtest/page | 
[**get_stat_data_fields29**](TroubleshootingToolsDiagnosticsApi.md#get_stat_data_fields29) | **GET** /stream/device/nwpi/fields | 
[**get_stat_data_fields30**](TroubleshootingToolsDiagnosticsApi.md#get_stat_data_fields30) | **GET** /statistics/speedtest/fields | 
[**get_stat_data_raw_data26**](TroubleshootingToolsDiagnosticsApi.md#get_stat_data_raw_data26) | **GET** /stream/device/nwpi | 
[**get_stat_data_raw_data27**](TroubleshootingToolsDiagnosticsApi.md#get_stat_data_raw_data27) | **GET** /statistics/speedtest | 
[**get_stat_data_raw_data_as_csv27**](TroubleshootingToolsDiagnosticsApi.md#get_stat_data_raw_data_as_csv27) | **GET** /stream/device/nwpi/csv | 
[**get_stat_data_raw_data_as_csv28**](TroubleshootingToolsDiagnosticsApi.md#get_stat_data_raw_data_as_csv28) | **GET** /statistics/speedtest/csv | 
[**get_stat_query_fields29**](TroubleshootingToolsDiagnosticsApi.md#get_stat_query_fields29) | **GET** /stream/device/nwpi/query/fields | 
[**get_stat_query_fields30**](TroubleshootingToolsDiagnosticsApi.md#get_stat_query_fields30) | **GET** /statistics/speedtest/query/fields | 
[**get_stats_raw_data27**](TroubleshootingToolsDiagnosticsApi.md#get_stats_raw_data27) | **POST** /stream/device/nwpi | 
[**get_stats_raw_data28**](TroubleshootingToolsDiagnosticsApi.md#get_stats_raw_data28) | **POST** /statistics/speedtest | 
[**get_thread_pools**](TroubleshootingToolsDiagnosticsApi.md#get_thread_pools) | **GET** /diagnostics/threadpools | 
[**get_trace_flow**](TroubleshootingToolsDiagnosticsApi.md#get_trace_flow) | **GET** /stream/device/nwpi/traceFlow | 
[**get_trace_history**](TroubleshootingToolsDiagnosticsApi.md#get_trace_history) | **GET** /stream/device/nwpi/traceHistory | 
[**get_vnic_info_by_vnf_id**](TroubleshootingToolsDiagnosticsApi.md#get_vnic_info_by_vnf_id) | **GET** /stream/device/capture/vnicsInfo/{vnfId} | 
[**monitor_start**](TroubleshootingToolsDiagnosticsApi.md#monitor_start) | **POST** /stream/device/nwpi/monitor/start | 
[**monitor_stop**](TroubleshootingToolsDiagnosticsApi.md#monitor_stop) | **POST** /stream/device/nwpi/monitor/stop | 
[**process_device_status**](TroubleshootingToolsDiagnosticsApi.md#process_device_status) | **POST** /stream/device/status/{deviceUUID} | 
[**renew_session_info**](TroubleshootingToolsDiagnosticsApi.md#renew_session_info) | **GET** /stream/device/log/renew/{sessionId} | 
[**save_speed_test_results**](TroubleshootingToolsDiagnosticsApi.md#save_speed_test_results) | **POST** /stream/device/speed/{deviceUUID}/{sessionId} | 
[**search_device_log**](TroubleshootingToolsDiagnosticsApi.md#search_device_log) | **POST** /stream/device/log/search/{sessionId} | 
[**start_pcap_session**](TroubleshootingToolsDiagnosticsApi.md#start_pcap_session) | **GET** /stream/device/capture/start/{sessionId} | 
[**start_speed_test**](TroubleshootingToolsDiagnosticsApi.md#start_speed_test) | **GET** /stream/device/speed/start/{sessionId} | 
[**stop_pcap_session**](TroubleshootingToolsDiagnosticsApi.md#stop_pcap_session) | **GET** /stream/device/capture/stop/{sessionId} | 
[**stop_speed_test**](TroubleshootingToolsDiagnosticsApi.md#stop_speed_test) | **GET** /stream/device/speed/stop/{sessionId} | 
[**stream_log**](TroubleshootingToolsDiagnosticsApi.md#stream_log) | **POST** /stream/device/log/{logType}/{deviceUUID}/{sessionId} | 
[**trace_delete**](TroubleshootingToolsDiagnosticsApi.md#trace_delete) | **DELETE** /stream/device/nwpi/trace/delete | 
[**trace_fin_flow_with_query**](TroubleshootingToolsDiagnosticsApi.md#trace_fin_flow_with_query) | **GET** /stream/device/nwpi/traceFinFlowWithQuery | 
[**trace_start**](TroubleshootingToolsDiagnosticsApi.md#trace_start) | **POST** /stream/device/nwpi/trace/start | 
[**trace_stop**](TroubleshootingToolsDiagnosticsApi.md#trace_stop) | **POST** /stream/device/nwpi/trace/stop/{traceId} | 


# **clear_session**
> clear_session(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = "sessionId_example" # str | Session Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.clear_session(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->clear_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session Id |

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

# **disable_device_log**
> disable_device_log(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.disable_device_log(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->disable_device_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **disable_packet_capture_session**
> disable_packet_capture_session(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.disable_packet_capture_session(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->disable_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **disable_speed_test_session**
> disable_speed_test_session(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.disable_speed_test_session(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->disable_speed_test_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **download_debug_log**
> download_debug_log(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = "sessionId_example" # str | Session Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_debug_log(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->download_debug_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session Id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> download_file(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.download_file(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->download_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_stop_pcap_session**
> force_stop_pcap_session(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.force_stop_pcap_session(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->force_stop_pcap_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **form_post_packet_capture**
> form_post_packet_capture(device_uuid, session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    device_uuid = "deviceUUID_example" # str | 
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.form_post_packet_capture(device_uuid, session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->form_post_packet_capture: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  |
 **session_id** | **Uuid**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_data_by_query27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query27()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query27(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_aggregation_data_by_query27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter | [optional]

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

# **get_aggregation_data_by_query28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_aggregation_data_by_query28()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_aggregation_data_by_query28(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_aggregation_data_by_query28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query filter | [optional]

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

# **get_concurrent_data**
> get_concurrent_data(trace_id, timestamp)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_concurrent_data(trace_id, timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_concurrent_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |

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

# **get_concurrent_domain_data**
> get_concurrent_domain_data(trace_id, timestamp)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_concurrent_domain_data(trace_id, timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_concurrent_domain_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |

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

# **get_count29**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count29(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count29(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_count29: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

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

# **get_count30**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count30(query)



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["1"],"operator":"greater"},"fields":["latency"]}" # str | Query

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_count30(query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_count30: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

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

# **get_count_post29**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post29()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post29(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_count_post29: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query | [optional]

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

# **get_count_post30**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_count_post30()



Get response count of a query

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Query (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_count_post30(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_count_post30: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Query | [optional]

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

# **get_db_schema**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_db_schema()



Get the current database schema

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_db_schema()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_db_schema: %s\n" % e)
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

# **get_device_log**
> get_device_log(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 
    log_id = -1 # int |  (optional) if omitted the server will use the default value of -1

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_device_log(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_device_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_device_log(session_id, log_id=log_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_device_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |
 **log_id** | **int**|  | [optional] if omitted the server will use the default value of -1

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

# **get_domain_metric**
> get_domain_metric(trace_id, timestamp, domain, first_timestamp, last_timestamp)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    domain = "domain_example" # str | domain name
    first_timestamp = 1 # int | first timestamp of xAxis
    last_timestamp = 1 # int | last timestamp of xAxis

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_domain_metric(trace_id, timestamp, domain, first_timestamp, last_timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_domain_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **domain** | **str**| domain name |
 **first_timestamp** | **int**| first timestamp of xAxis |
 **last_timestamp** | **int**| last timestamp of xAxis |

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

# **get_file_download_status**
> get_file_download_status(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_file_download_status(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_file_download_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **get_finalized_data**
> get_finalized_data(trace_id, timestamp)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_finalized_data(trace_id, timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_finalized_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |

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

# **get_finalized_domain_data**
> get_finalized_domain_data(trace_id, timestamp)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_finalized_domain_data(trace_id, timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_finalized_domain_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |

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

# **get_flow_detail**
> get_flow_detail(trace_id, timestamp, flow_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    flow_id = 1 # int | flow id

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_flow_detail(trace_id, timestamp, flow_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_flow_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **flow_id** | **int**| flow id |

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

# **get_flow_metric**
> get_flow_metric(trace_id, timestamp, flow_id, first_timestamp, last_timestamp)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    flow_id = 1 # int | flow id
    first_timestamp = 1 # int | first timestamp of xAxis
    last_timestamp = 1 # int | last timestamp of xAxis

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_flow_metric(trace_id, timestamp, flow_id, first_timestamp, last_timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_flow_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **flow_id** | **int**| flow id |
 **first_timestamp** | **int**| first timestamp of xAxis |
 **last_timestamp** | **int**| last timestamp of xAxis |

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

# **get_interface_bandwidth**
> get_interface_bandwidth(circuit, device_uuid)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.device_uuid import DeviceUuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    circuit = "circuit_example" # str | 
    device_uuid = DeviceUuid(
        device_uuid="device_uuid_example",
    ) # DeviceUuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_interface_bandwidth(circuit, device_uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_interface_bandwidth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **circuit** | **str**|  |
 **device_uuid** | **DeviceUuid**|  |

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

# **get_log_type**
> get_log_type(uuid)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    uuid = "uuid_example" # str | Device uuid

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_log_type(uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_log_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Device uuid |

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

# **get_monitor_state**
> get_monitor_state(trace_id, state)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    state = "state_example" # str | trace state

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_monitor_state(trace_id, state)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_monitor_state: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **state** | **str**| trace state |

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

# **get_nwpi_dscp**
> get_nwpi_dscp()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_nwpi_dscp()
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_nwpi_dscp: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_nwpi_nbar_app_group**
> get_nwpi_nbar_app_group()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_nwpi_nbar_app_group()
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_nwpi_nbar_app_group: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_nwpi_protocol**
> get_nwpi_protocol()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_nwpi_protocol()
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_nwpi_protocol: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_packet_features**
> get_packet_features(trace_id, timestamp, flow_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    flow_id = 1 # int | flow id

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_packet_features(trace_id, timestamp, flow_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_packet_features: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **flow_id** | **int**| flow id |

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

# **get_post_aggregation_app_data_by_query26**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query26()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query26(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_post_aggregation_app_data_by_query26: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_aggregation_app_data_by_query27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_app_data_by_query27()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_app_data_by_query27(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_post_aggregation_app_data_by_query27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_aggregation_data_by_query27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query27()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query27(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_post_aggregation_data_by_query27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_aggregation_data_by_query28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_aggregation_data_by_query28()



Get aggregated data based on input query and filters. The data can be filtered on time and other unique parameters based upon necessity and intended usage

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_aggregation_data_by_query28(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_post_aggregation_data_by_query28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_stat_bulk_raw_data27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data27()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data27(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_post_stat_bulk_raw_data27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_post_stat_bulk_raw_data28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_post_stat_bulk_raw_data28()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_post_stat_bulk_raw_data28(scroll_id=scroll_id, count=count, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_post_stat_bulk_raw_data28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_session**
> get_session()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_session(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_info_capture**
> get_session_info_capture()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_session_info_capture(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_session_info_capture: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_info_log**
> get_session_info_log()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_session_info_log(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_session_info_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions**
> get_sessions()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_sessions()
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_sessions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_speed_test**
> get_speed_test(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 
    log_id = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_speed_test(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_speed_test: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.get_speed_test(session_id, log_id=log_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_speed_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |
 **log_id** | **int**|  | [optional] if omitted the server will use the default value of 0

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

# **get_speed_test_status**
> get_speed_test_status(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_speed_test_status(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_speed_test_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **get_stat_bulk_raw_data27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data27()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data27(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_bulk_raw_data27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]

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

# **get_stat_bulk_raw_data28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_bulk_raw_data28()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"]}" # str | Query string (optional)
    scroll_id = "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAOIWZ1NQbXpvQ29Uc0stNzZ2UzlwTEREUQ==" # str | ES scroll Id (optional)
    count = "10" # str | Result size (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_bulk_raw_data28(query=query, scroll_id=scroll_id, count=count)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_bulk_raw_data28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **scroll_id** | **str**| ES scroll Id | [optional]
 **count** | **str**| Result size | [optional]

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

# **get_stat_data_fields29**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields29()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields29()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_data_fields29: %s\n" % e)
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

# **get_stat_data_fields30**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_fields30()



Get fields and type

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_data_fields30()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_data_fields30: %s\n" % e)
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

# **get_stat_data_raw_data26**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data26()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data26(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_data_raw_data26: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]

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

# **get_stat_data_raw_data27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_data_raw_data27()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"condition":"AND","rules":[{"value":["2020-05-10T01:00:00 UTC","2020-05-10T01:30:00 UTC"],"field":"entry_time","type":"date","operator":"between"}]},"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data27(query=query, page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_data_raw_data27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]

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

# **get_stat_data_raw_data_as_csv27**
> str get_stat_data_raw_data_as_csv27()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv27(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_data_raw_data_as_csv27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_data_raw_data_as_csv28**
> str get_stat_data_raw_data_as_csv28()



Get raw data with optional query as CSV

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    query = "{"query":{"field":"latency","type":"long","value":["100"],"operator":"greater"},"size":1000,"sort":[{"field":"latency","type":"long","order":"asc"}],"fields":["latency"],"aggregation":{"metrics":[{"property":"latency","type":"avg"}]}}" # str | Query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stat_data_raw_data_as_csv28(query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_data_raw_data_as_csv28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stat_query_fields29**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields29()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields29()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_query_fields29: %s\n" % e)
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

# **get_stat_query_fields30**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stat_query_fields30()



Get query fields

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_stat_query_fields30()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stat_query_fields30: %s\n" % e)
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

# **get_stats_raw_data27**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data27()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data27(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stats_raw_data27: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_stats_raw_data28**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_stats_raw_data28()



Get stats raw data

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    page = 1 # int | page number (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sortBy_example" # str | sort by (optional)
    sort_order = "sortOrder_example" # str | sort order (optional)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Stats query string (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_stats_raw_data28(page=page, page_size=page_size, sort_by=sort_by, sort_order=sort_order, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_stats_raw_data28: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **sort_order** | **str**| sort order | [optional]
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Stats query string | [optional]

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

# **get_thread_pools**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_thread_pools()



Get information on the threadpools

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_thread_pools()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_thread_pools: %s\n" % e)
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

# **get_trace_flow**
> get_trace_flow(trace_id, timestamp, state)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    state = "state_example" # str | trace state

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_trace_flow(trace_id, timestamp, state)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_trace_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **state** | **str**| trace state |

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

# **get_trace_history**
> get_trace_history()



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.get_trace_history()
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_trace_history: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_vnic_info_by_vnf_id**
> get_vnic_info_by_vnf_id(vnf_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    vnf_id = "vnfId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_vnic_info_by_vnf_id(vnf_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->get_vnic_info_by_vnf_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnf_id** | **str**|  |

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

# **monitor_start**
> monitor_start()



CXP Monitor Action - Start

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.monitor_start(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->monitor_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **monitor_stop**
> monitor_stop()



CXP Monitor Action - Stop

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.monitor_stop(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->monitor_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **process_device_status**
> process_device_status(device_uuid)



Get device status stream

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    device_uuid = "deviceUUID_example" # str | Device uuid
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.process_device_status(device_uuid)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->process_device_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.process_device_status(device_uuid, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->process_device_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**| Device uuid |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_session_info**
> renew_session_info(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.renew_session_info(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->renew_session_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **save_speed_test_results**
> save_speed_test_results(device_uuid, session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    device_uuid = "deviceUUID_example" # str | 
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.save_speed_test_results(device_uuid, session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->save_speed_test_results: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.save_speed_test_results(device_uuid, session_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->save_speed_test_results: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  |
 **session_id** | **Uuid**|  |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_device_log**
> search_device_log(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = "sessionId_example" # str | Session Id
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.search_device_log(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->search_device_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.search_device_log(session_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->search_device_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session Id |
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_pcap_session**
> start_pcap_session(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_pcap_session(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->start_pcap_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **start_speed_test**
> start_speed_test(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.start_speed_test(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->start_speed_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **stop_pcap_session**
> stop_pcap_session(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.stop_pcap_session(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->stop_pcap_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **stop_speed_test**
> stop_speed_test(session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from openapi_client.model.uuid import Uuid
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    session_id = Uuid(
        uuid="uuid_example",
    ) # Uuid | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.stop_speed_test(session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->stop_speed_test: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **Uuid**|  |

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

# **stream_log**
> stream_log(log_type, device_uuid, session_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    log_type = "logType_example" # str | Log type
    device_uuid = "deviceUUID_example" # str | Device uuid
    session_id = "sessionId_example" # str | Session Id
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.stream_log(log_type, device_uuid, session_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->stream_log: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.stream_log(log_type, device_uuid, session_id, body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->stream_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_type** | **str**| Log type |
 **device_uuid** | **str**| Device uuid |
 **session_id** | **str**| Session Id |
 **body** | **str**|  | [optional]

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

# **trace_delete**
> trace_delete(trace_id, timestamp)



Trace Action - Delete

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = "traceId_example" # str | trace id
    timestamp = 1 # int | start time

    # example passing only required values which don't have defaults set
    try:
        api_instance.trace_delete(trace_id, timestamp)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->trace_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| trace id |
 **timestamp** | **int**| start time |

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

# **trace_fin_flow_with_query**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} trace_fin_flow_with_query(trace_id, timestamp)



Retrieve Certain Fin Flows

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = 1 # int | trace id
    timestamp = 1 # int | start time
    query = "query_example" # str | Query filter (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.trace_fin_flow_with_query(trace_id, timestamp)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->trace_fin_flow_with_query: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.trace_fin_flow_with_query(trace_id, timestamp, query=query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->trace_fin_flow_with_query: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **int**| trace id |
 **timestamp** | **int**| start time |
 **query** | **str**| Query filter | [optional]

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

# **trace_start**
> trace_start()



Trace Action - Start

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.trace_start(body=body)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->trace_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

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

# **trace_stop**
> trace_stop(trace_id)



Trace Action - Stop

### Example


```python
import time
import openapi_client
from openapi_client.api import troubleshooting_tools_diagnostics_api
from pprint import pprint
# Defining the host is optional and defaults to /dataservice
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/dataservice"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = troubleshooting_tools_diagnostics_api.TroubleshootingToolsDiagnosticsApi(api_client)
    trace_id = "traceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.trace_stop(trace_id)
    except openapi_client.ApiException as e:
        print("Exception when calling TroubleshootingToolsDiagnosticsApi->trace_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**|  |

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

