# swagger_client.StatisticApi

All URIs are relative to *https://www.yuque.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistic_api_v2_statistic_all**](StatisticApi.md#statistic_api_v2_statistic_all) | **GET** /api/v2/groups/{login}/statistics | 团队.汇总统计数据
[**statistic_api_v2_statistic_by_books**](StatisticApi.md#statistic_api_v2_statistic_by_books) | **GET** /api/v2/groups/{login}/statistics/books | 团队.知识库统计数据
[**statistic_api_v2_statistic_by_docs**](StatisticApi.md#statistic_api_v2_statistic_by_docs) | **GET** /api/v2/groups/{login}/statistics/docs | 团队.文档统计数据
[**statistic_api_v2_statistic_by_members**](StatisticApi.md#statistic_api_v2_statistic_by_members) | **GET** /api/v2/groups/{login}/statistics/members | 团队.成员统计数据

# **statistic_api_v2_statistic_all**
> InlineResponse20015 statistic_api_v2_statistic_all(login)

团队.汇总统计数据

团队.汇总统计数据 GET /api/v2/groups/:login/statistics  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StatisticApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队的 Login 或 ID

try:
    # 团队.汇总统计数据
    api_response = api_instance.statistic_api_v2_statistic_all(login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->statistic_api_v2_statistic_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队的 Login 或 ID | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistic_api_v2_statistic_by_books**
> InlineResponse20017 statistic_api_v2_statistic_by_books(login, name=name, range=range, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)

团队.知识库统计数据

团队.知识库统计数据 GET /api/v2/groups/:login/statistics/books

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StatisticApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队的 Login 或 ID
name = 'name_example' # str | 知识库名 [过滤条件] (optional)
range = '0' # str | 时间范围 [过滤条件] (0:全部, 30:近 30 天, 365:近一年) (optional) (default to 0)
page = 1 # int | 页码 (optional) (default to 1)
limit = 10 # int | 分页数量 (optional) (default to 10)
sort_field = 'sort_field_example' # str | 排序字段 (optional)
sort_order = 'desc' # str | 排序方向 (optional) (default to desc)

try:
    # 团队.知识库统计数据
    api_response = api_instance.statistic_api_v2_statistic_by_books(login, name=name, range=range, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->statistic_api_v2_statistic_by_books: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队的 Login 或 ID | 
 **name** | **str**| 知识库名 [过滤条件] | [optional] 
 **range** | **str**| 时间范围 [过滤条件] (0:全部, 30:近 30 天, 365:近一年) | [optional] [default to 0]
 **page** | **int**| 页码 | [optional] [default to 1]
 **limit** | **int**| 分页数量 | [optional] [default to 10]
 **sort_field** | **str**| 排序字段 | [optional] 
 **sort_order** | **str**| 排序方向 | [optional] [default to desc]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistic_api_v2_statistic_by_docs**
> InlineResponse20018 statistic_api_v2_statistic_by_docs(login, book_id=book_id, name=name, range=range, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)

团队.文档统计数据

团队.文档统计数据 GET /api/v2/groups/:login/statistics/docs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StatisticApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队的 Login 或 ID
book_id = 56 # int | 指定知识库 [过滤条件] (optional)
name = 'name_example' # str | 文档名 [过滤条件] (optional)
range = '0' # str | 时间范围 [过滤条件] (0:全部, 30:近 30 天, 365:近一年) (optional) (default to 0)
page = 1 # int | 页码 (optional) (default to 1)
limit = 10 # int | 分页数量 (optional) (default to 10)
sort_field = 'sort_field_example' # str | 排序字段 (optional)
sort_order = 'desc' # str | 排序方向 (optional) (default to desc)

try:
    # 团队.文档统计数据
    api_response = api_instance.statistic_api_v2_statistic_by_docs(login, book_id=book_id, name=name, range=range, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->statistic_api_v2_statistic_by_docs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队的 Login 或 ID | 
 **book_id** | **int**| 指定知识库 [过滤条件] | [optional] 
 **name** | **str**| 文档名 [过滤条件] | [optional] 
 **range** | **str**| 时间范围 [过滤条件] (0:全部, 30:近 30 天, 365:近一年) | [optional] [default to 0]
 **page** | **int**| 页码 | [optional] [default to 1]
 **limit** | **int**| 分页数量 | [optional] [default to 10]
 **sort_field** | **str**| 排序字段 | [optional] 
 **sort_order** | **str**| 排序方向 | [optional] [default to desc]

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistic_api_v2_statistic_by_members**
> InlineResponse20016 statistic_api_v2_statistic_by_members(login, name=name, range=range, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)

团队.成员统计数据

团队.成员统计数据 GET /api/v2/groups/:login/statistics/members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: authToken
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StatisticApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 团队的 Login 或 ID
name = 'name_example' # str | 成员名 [过滤条件] (optional)
range = '0' # str | 时间范围 [过滤条件] (0:全部, 30:近 30 天, 365:近一年) (optional) (default to 0)
page = 1 # int | 页码 (optional) (default to 1)
limit = 10 # int | 分页数量 (optional) (default to 10)
sort_field = 'sort_field_example' # str | 排序字段 (optional)
sort_order = 'desc' # str | 排序方向 (optional) (default to desc)

try:
    # 团队.成员统计数据
    api_response = api_instance.statistic_api_v2_statistic_by_members(login, name=name, range=range, page=page, limit=limit, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticApi->statistic_api_v2_statistic_by_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 团队的 Login 或 ID | 
 **name** | **str**| 成员名 [过滤条件] | [optional] 
 **range** | **str**| 时间范围 [过滤条件] (0:全部, 30:近 30 天, 365:近一年) | [optional] [default to 0]
 **page** | **int**| 页码 | [optional] [default to 1]
 **limit** | **int**| 分页数量 | [optional] [default to 10]
 **sort_field** | **str**| 排序字段 | [optional] 
 **sort_order** | **str**| 排序方向 | [optional] [default to desc]

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

