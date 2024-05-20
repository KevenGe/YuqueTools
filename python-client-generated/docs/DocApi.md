# swagger_client.DocApi

All URIs are relative to *https://www.yuque.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doc_api_v2_doc_create**](DocApi.md#doc_api_v2_doc_create) | **POST** /api/v2/repos/{group_login}/{book_slug}/docs | 创建文档
[**doc_api_v2_doc_create_by_id**](DocApi.md#doc_api_v2_doc_create_by_id) | **POST** /api/v2/repos/{book_id}/docs | 创建文档
[**doc_api_v2_doc_destroy**](DocApi.md#doc_api_v2_doc_destroy) | **DELETE** /api/v2/repos/{group_login}/{book_slug}/docs/{id} | 删除文档
[**doc_api_v2_doc_destroy_by_id**](DocApi.md#doc_api_v2_doc_destroy_by_id) | **DELETE** /api/v2/repos/{book_id}/docs/{id} | 删除文档
[**doc_api_v2_doc_list**](DocApi.md#doc_api_v2_doc_list) | **GET** /api/v2/repos/{group_login}/{book_slug}/docs | 获取知识库文档列表
[**doc_api_v2_doc_list_by_id**](DocApi.md#doc_api_v2_doc_list_by_id) | **GET** /api/v2/repos/{book_id}/docs | 获取知识库文档列表
[**doc_api_v2_doc_show**](DocApi.md#doc_api_v2_doc_show) | **GET** /api/v2/repos/{group_login}/{book_slug}/docs/{id} | 获取文档详情
[**doc_api_v2_doc_show_by_id**](DocApi.md#doc_api_v2_doc_show_by_id) | **GET** /api/v2/repos/{book_id}/docs/{id} | 获取文档详情
[**doc_api_v2_doc_update**](DocApi.md#doc_api_v2_doc_update) | **PUT** /api/v2/repos/{group_login}/{book_slug}/docs/{id} | 更新文档
[**doc_api_v2_doc_update_by_id**](DocApi.md#doc_api_v2_doc_update_by_id) | **PUT** /api/v2/repos/{book_id}/docs/{id} | 更新文档
[**doc_api_v2_doc_version_list**](DocApi.md#doc_api_v2_doc_version_list) | **GET** /api/v2/doc_versions | 获取文档历史版本列表
[**doc_api_v2_doc_version_show**](DocApi.md#doc_api_v2_doc_version_show) | **GET** /api/v2/doc_versions/{id} | 获取文档历史版本详情
[**doc_api_v2_repo_toc_show**](DocApi.md#doc_api_v2_repo_toc_show) | **GET** /api/v2/repos/{group_login}/{book_slug}/toc | 获取目录
[**doc_api_v2_repo_toc_show_by_id**](DocApi.md#doc_api_v2_repo_toc_show_by_id) | **GET** /api/v2/repos/{book_id}/toc | 获取目录
[**doc_api_v2_repo_toc_update**](DocApi.md#doc_api_v2_repo_toc_update) | **PUT** /api/v2/repos/{group_login}/{book_slug}/toc | 更新目录
[**doc_api_v2_repo_toc_update_by_id**](DocApi.md#doc_api_v2_repo_toc_update_by_id) | **PUT** /api/v2/repos/{book_id}/toc | 更新目录

# **doc_api_v2_doc_create**
> InlineResponse2008 doc_api_v2_doc_create(group_login, book_slug, body=body)

创建文档

创建文档 POST /api/v2/repos/:book_id/docs POST /api/v2/repos/:group_login/:book_slug/docs   - 注意: 创建文档后不会自动添加到目录，需要调用\"知识库目录更新接口\"更新到目录中  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
body = NULL # object |  (optional)

try:
    # 创建文档
    api_response = api_instance.doc_api_v2_doc_create(group_login, book_slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_create_by_id**
> InlineResponse2008 doc_api_v2_doc_create_by_id(book_id, body=body)

创建文档

创建文档 POST /api/v2/repos/:book_id/docs POST /api/v2/repos/:group_login/:book_slug/docs   - 注意: 创建文档后不会自动添加到目录，需要调用\"知识库目录更新接口\"更新到目录中  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
body = NULL # object |  (optional)

try:
    # 创建文档
    api_response = api_instance.doc_api_v2_doc_create_by_id(book_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_create_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_destroy**
> InlineResponse2008 doc_api_v2_doc_destroy(group_login, book_slug, id)

删除文档

删除文档 DELETE /api/v2/repos/:book_id/docs/:id DELETE /api/v2/repos/:group_login/:book_slug/docs/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
id = 'id_example' # str | 文档 ID or 路径

try:
    # 删除文档
    api_response = api_instance.doc_api_v2_doc_destroy(group_login, book_slug, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **id** | **str**| 文档 ID or 路径 | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_destroy_by_id**
> InlineResponse2008 doc_api_v2_doc_destroy_by_id(book_id, id)

删除文档

删除文档 DELETE /api/v2/repos/:book_id/docs/:id DELETE /api/v2/repos/:group_login/:book_slug/docs/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
id = 'id_example' # str | 文档 ID or 路径

try:
    # 删除文档
    api_response = api_instance.doc_api_v2_doc_destroy_by_id(book_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_destroy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **id** | **str**| 文档 ID or 路径 | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_list**
> InlineResponse2007 doc_api_v2_doc_list(group_login, book_slug, offset=offset, limit=limit, optional_properties=optional_properties)

获取知识库文档列表

获取知识库文档列表 GET /api/v2/repos/:book_id/docs GET /api/v2/repos/:group_login/:book_slug/docs  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
offset = 0 # int | 偏移量 [分页参数] (optional) (default to 0)
limit = 100 # int | 每页数量 [分页参数] (optional) (default to 100)
optional_properties = '' # str | 获取的额外字段, 多个字段以逗号分隔   - 注意: 每页数量超过 100 本字段会失效   - 支持的字段有:   - hits: 文档阅读数   - tags: 标签   - latest_version_id: 最新已发版本 ID   (optional)

try:
    # 获取知识库文档列表
    api_response = api_instance.doc_api_v2_doc_list(group_login, book_slug, offset=offset, limit=limit, optional_properties=optional_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **offset** | **int**| 偏移量 [分页参数] | [optional] [default to 0]
 **limit** | **int**| 每页数量 [分页参数] | [optional] [default to 100]
 **optional_properties** | **str**| 获取的额外字段, 多个字段以逗号分隔   - 注意: 每页数量超过 100 本字段会失效   - 支持的字段有:   - hits: 文档阅读数   - tags: 标签   - latest_version_id: 最新已发版本 ID   | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_list_by_id**
> InlineResponse2007 doc_api_v2_doc_list_by_id(book_id, offset=offset, limit=limit, optional_properties=optional_properties)

获取知识库文档列表

获取知识库文档列表 GET /api/v2/repos/:book_id/docs GET /api/v2/repos/:group_login/:book_slug/docs  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
offset = 0 # int | 偏移量 [分页参数] (optional) (default to 0)
limit = 100 # int | 每页数量 [分页参数] (optional) (default to 100)
optional_properties = '' # str | 获取的额外字段, 多个字段以逗号分隔   - 注意: 每页数量超过 100 本字段会失效   - 支持的字段有:   - hits: 文档阅读数   - tags: 标签   - latest_version_id: 最新已发版本 ID   (optional)

try:
    # 获取知识库文档列表
    api_response = api_instance.doc_api_v2_doc_list_by_id(book_id, offset=offset, limit=limit, optional_properties=optional_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_list_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **offset** | **int**| 偏移量 [分页参数] | [optional] [default to 0]
 **limit** | **int**| 每页数量 [分页参数] | [optional] [default to 100]
 **optional_properties** | **str**| 获取的额外字段, 多个字段以逗号分隔   - 注意: 每页数量超过 100 本字段会失效   - 支持的字段有:   - hits: 文档阅读数   - tags: 标签   - latest_version_id: 最新已发版本 ID   | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_show**
> InlineResponse2008 doc_api_v2_doc_show(group_login, book_slug, id)

获取文档详情

获取文档详情 GET /api/v2/repos/:book_id/docs/:id GET /api/v2/repos/:group_login/:book_slug/docs/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
id = 'id_example' # str | 文档 ID or 路径

try:
    # 获取文档详情
    api_response = api_instance.doc_api_v2_doc_show(group_login, book_slug, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **id** | **str**| 文档 ID or 路径 | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_show_by_id**
> InlineResponse2008 doc_api_v2_doc_show_by_id(book_id, id)

获取文档详情

获取文档详情 GET /api/v2/repos/:book_id/docs/:id GET /api/v2/repos/:group_login/:book_slug/docs/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
id = 'id_example' # str | 文档 ID or 路径

try:
    # 获取文档详情
    api_response = api_instance.doc_api_v2_doc_show_by_id(book_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_show_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **id** | **str**| 文档 ID or 路径 | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_update**
> InlineResponse2008 doc_api_v2_doc_update(group_login, book_slug, id, body=body)

更新文档

更新文档 PUT /api/v2/repos/:book_id/docs/:id PUT /api/v2/repos/:group_login/:book_slug/docs/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
id = 'id_example' # str | 文档 ID or 路径
body = NULL # object |  (optional)

try:
    # 更新文档
    api_response = api_instance.doc_api_v2_doc_update(group_login, book_slug, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **id** | **str**| 文档 ID or 路径 | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_update_by_id**
> InlineResponse2008 doc_api_v2_doc_update_by_id(book_id, id, body=body)

更新文档

更新文档 PUT /api/v2/repos/:book_id/docs/:id PUT /api/v2/repos/:group_login/:book_slug/docs/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
id = 'id_example' # str | 文档 ID or 路径
body = NULL # object |  (optional)

try:
    # 更新文档
    api_response = api_instance.doc_api_v2_doc_update_by_id(book_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_update_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **id** | **str**| 文档 ID or 路径 | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_version_list**
> InlineResponse2009 doc_api_v2_doc_version_list(doc_id)

获取文档历史版本列表

获取文档历史版本列表 GET /api/v2/doc_versions   - 按时间倒序返回最近 100 个已发布版本  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
doc_id = 56 # int | 文档 ID

try:
    # 获取文档历史版本列表
    api_response = api_instance.doc_api_v2_doc_version_list(doc_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_version_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **int**| 文档 ID | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_doc_version_show**
> InlineResponse20010 doc_api_v2_doc_version_show(id)

获取文档历史版本详情

获取文档历史版本详情 GET /api/v2/doc_versions/:id  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
id = 56 # int | 版本 ID

try:
    # 获取文档历史版本详情
    api_response = api_instance.doc_api_v2_doc_version_show(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_doc_version_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| 版本 ID | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_repo_toc_show**
> InlineResponse20011 doc_api_v2_repo_toc_show(group_login, book_slug)

获取目录

获取目录 GET /api/v2/repos/:book_id/toc GET /api/v2/repos/:group_login/:book_slug/toc  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径

try:
    # 获取目录
    api_response = api_instance.doc_api_v2_repo_toc_show(group_login, book_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_repo_toc_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_repo_toc_show_by_id**
> InlineResponse20011 doc_api_v2_repo_toc_show_by_id(book_id)

获取目录

获取目录 GET /api/v2/repos/:book_id/toc GET /api/v2/repos/:group_login/:book_slug/toc  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID

try:
    # 获取目录
    api_response = api_instance.doc_api_v2_repo_toc_show_by_id(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_repo_toc_show_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_repo_toc_update**
> InlineResponse20011 doc_api_v2_repo_toc_update(group_login, book_slug, body=body)

更新目录

更新目录 PUT /api/v2/repos/:book_id/toc PUT /api/v2/repos/:group_login/:book_slug/toc   字段说明:   - 所有场景   - 必填字段     - action     - action_mode   - 选填字段     - target_uuid     - visible - 创建场景   - 必填字段     - 创建文档节点       - type       - doc_ids     - 创建分组节点       - type       - title     - 创建外链节点       - type       - title       - url       - open_window - 移动场景   - 必填字段     - target_uuid     - node_uuid - 编辑场景   - 必填字段     - node_uuid   - 选填字段     - type     - title     - url     - open_window - 删除场景   - 必填字段     - node_uuid  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
body = NULL # object |  (optional)

try:
    # 更新目录
    api_response = api_instance.doc_api_v2_repo_toc_update(group_login, book_slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_repo_toc_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_api_v2_repo_toc_update_by_id**
> InlineResponse20011 doc_api_v2_repo_toc_update_by_id(book_id, body=body)

更新目录

更新目录 PUT /api/v2/repos/:book_id/toc PUT /api/v2/repos/:group_login/:book_slug/toc   字段说明:   - 所有场景   - 必填字段     - action     - action_mode   - 选填字段     - target_uuid     - visible - 创建场景   - 必填字段     - 创建文档节点       - type       - doc_ids     - 创建分组节点       - type       - title     - 创建外链节点       - type       - title       - url       - open_window - 移动场景   - 必填字段     - target_uuid     - node_uuid - 编辑场景   - 必填字段     - node_uuid   - 选填字段     - type     - title     - url     - open_window - 删除场景   - 必填字段     - node_uuid  

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
api_instance = swagger_client.DocApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
body = NULL # object |  (optional)

try:
    # 更新目录
    api_response = api_instance.doc_api_v2_repo_toc_update_by_id(book_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocApi->doc_api_v2_repo_toc_update_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

