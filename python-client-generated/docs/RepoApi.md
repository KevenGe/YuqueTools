# swagger_client.RepoApi

All URIs are relative to *https://www.yuque.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repo_api_v2_repo_create**](RepoApi.md#repo_api_v2_repo_create) | **POST** /api/v2/users/{login}/repos | 创建知识库
[**repo_api_v2_repo_create_by_group**](RepoApi.md#repo_api_v2_repo_create_by_group) | **POST** /api/v2/groups/{login}/repos | 创建知识库
[**repo_api_v2_repo_destroy**](RepoApi.md#repo_api_v2_repo_destroy) | **DELETE** /api/v2/repos/{group_login}/{book_slug} | 删除知识库
[**repo_api_v2_repo_destroy_by_id**](RepoApi.md#repo_api_v2_repo_destroy_by_id) | **DELETE** /api/v2/repos/{book_id} | 删除知识库
[**repo_api_v2_repo_list**](RepoApi.md#repo_api_v2_repo_list) | **GET** /api/v2/users/{login}/repos | 获取知识库列表
[**repo_api_v2_repo_list_by_group**](RepoApi.md#repo_api_v2_repo_list_by_group) | **GET** /api/v2/groups/{login}/repos | 获取知识库列表
[**repo_api_v2_repo_show**](RepoApi.md#repo_api_v2_repo_show) | **GET** /api/v2/repos/{group_login}/{book_slug} | 获取知识库详情
[**repo_api_v2_repo_show_by_id**](RepoApi.md#repo_api_v2_repo_show_by_id) | **GET** /api/v2/repos/{book_id} | 获取知识库详情
[**repo_api_v2_repo_update**](RepoApi.md#repo_api_v2_repo_update) | **PUT** /api/v2/repos/{group_login}/{book_slug} | 更新知识库
[**repo_api_v2_repo_update_by_id**](RepoApi.md#repo_api_v2_repo_update_by_id) | **PUT** /api/v2/repos/{book_id} | 更新知识库

# **repo_api_v2_repo_create**
> InlineResponse20013 repo_api_v2_repo_create(login, body=body)

创建知识库

创建知识库 POST /api/v2/groups/:id/repos POST /api/v2/groups/:login/repos   POST /api/v2/users/:id/repos POST /api/v2/users/:login/repos  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 用户/团队的 Login 或 ID
body = NULL # object |  (optional)

try:
    # 创建知识库
    api_response = api_instance.repo_api_v2_repo_create(login, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 用户/团队的 Login 或 ID | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_create_by_group**
> InlineResponse20013 repo_api_v2_repo_create_by_group(login, body=body)

创建知识库

创建知识库 POST /api/v2/groups/:id/repos POST /api/v2/groups/:login/repos   POST /api/v2/users/:id/repos POST /api/v2/users/:login/repos  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 用户/团队的 Login 或 ID
body = NULL # object |  (optional)

try:
    # 创建知识库
    api_response = api_instance.repo_api_v2_repo_create_by_group(login, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_create_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 用户/团队的 Login 或 ID | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_destroy**
> InlineResponse20013 repo_api_v2_repo_destroy(group_login, book_slug)

删除知识库

删除知识库 DELETE /api/v2/repos/:book_id DELETE /api/v2/repos/:group_login/:book_slug  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径

try:
    # 删除知识库
    api_response = api_instance.repo_api_v2_repo_destroy(group_login, book_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_destroy_by_id**
> InlineResponse20013 repo_api_v2_repo_destroy_by_id(book_id)

删除知识库

删除知识库 DELETE /api/v2/repos/:book_id DELETE /api/v2/repos/:group_login/:book_slug  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID

try:
    # 删除知识库
    api_response = api_instance.repo_api_v2_repo_destroy_by_id(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_destroy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_list**
> InlineResponse20012 repo_api_v2_repo_list(login, offset=offset, limit=limit, type=type)

获取知识库列表

获取知识库列表 GET /api/v2/groups/:id/repos GET /api/v2/groups/:login/repos   GET /api/v2/users/:id/repos GET /api/v2/users/:login/repos  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 用户/团队的 Login 或 ID
offset = 0 # int | 偏移量 [分页参数] (optional) (default to 0)
limit = 100 # int | 每页数量 [分页参数] (optional) (default to 100)
type = 'type_example' # str | 类型 [筛选条件] (Book:文档型知识库, Design: 画板型知识库) (optional)

try:
    # 获取知识库列表
    api_response = api_instance.repo_api_v2_repo_list(login, offset=offset, limit=limit, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 用户/团队的 Login 或 ID | 
 **offset** | **int**| 偏移量 [分页参数] | [optional] [default to 0]
 **limit** | **int**| 每页数量 [分页参数] | [optional] [default to 100]
 **type** | **str**| 类型 [筛选条件] (Book:文档型知识库, Design: 画板型知识库) | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_list_by_group**
> InlineResponse20012 repo_api_v2_repo_list_by_group(login, offset=offset, limit=limit, type=type)

获取知识库列表

获取知识库列表 GET /api/v2/groups/:id/repos GET /api/v2/groups/:login/repos   GET /api/v2/users/:id/repos GET /api/v2/users/:login/repos  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
login = 'login_example' # str | 用户/团队的 Login 或 ID
offset = 0 # int | 偏移量 [分页参数] (optional) (default to 0)
limit = 100 # int | 每页数量 [分页参数] (optional) (default to 100)
type = 'type_example' # str | 类型 [筛选条件] (Book:文档型知识库, Design: 画板型知识库) (optional)

try:
    # 获取知识库列表
    api_response = api_instance.repo_api_v2_repo_list_by_group(login, offset=offset, limit=limit, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_list_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**| 用户/团队的 Login 或 ID | 
 **offset** | **int**| 偏移量 [分页参数] | [optional] [default to 0]
 **limit** | **int**| 每页数量 [分页参数] | [optional] [default to 100]
 **type** | **str**| 类型 [筛选条件] (Book:文档型知识库, Design: 画板型知识库) | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_show**
> InlineResponse20014 repo_api_v2_repo_show(group_login, book_slug)

获取知识库详情

获取知识库详情 GET /api/v2/repos/:book_id GET /api/v2/repos/:group_login/:book_slug  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径

try:
    # 获取知识库详情
    api_response = api_instance.repo_api_v2_repo_show(group_login, book_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_show: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_show_by_id**
> InlineResponse20014 repo_api_v2_repo_show_by_id(book_id)

获取知识库详情

获取知识库详情 GET /api/v2/repos/:book_id GET /api/v2/repos/:group_login/:book_slug  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID

try:
    # 获取知识库详情
    api_response = api_instance.repo_api_v2_repo_show_by_id(book_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_show_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_update**
> InlineResponse20013 repo_api_v2_repo_update(group_login, book_slug, body=body)

更新知识库

更新知识库 PUT /api/v2/repos/:book_id PUT /api/v2/repos/:group_login/:book_slug  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
group_login = 'group_login_example' # str | 团队 Login
book_slug = 'book_slug_example' # str | 知识库路径
body = NULL # object |  (optional)

try:
    # 更新知识库
    api_response = api_instance.repo_api_v2_repo_update(group_login, book_slug, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_login** | **str**| 团队 Login | 
 **book_slug** | **str**| 知识库路径 | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_api_v2_repo_update_by_id**
> InlineResponse20013 repo_api_v2_repo_update_by_id(book_id, body=body)

更新知识库

更新知识库 PUT /api/v2/repos/:book_id PUT /api/v2/repos/:group_login/:book_slug  

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
api_instance = swagger_client.RepoApi(swagger_client.ApiClient(configuration))
book_id = 56 # int | 知识库 ID
body = NULL # object |  (optional)

try:
    # 更新知识库
    api_response = api_instance.repo_api_v2_repo_update_by_id(book_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepoApi->repo_api_v2_repo_update_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_id** | **int**| 知识库 ID | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[authToken](../README.md#authToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

