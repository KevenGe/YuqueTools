"""
"""

#
from pprint import pprint
from typing import cast

#
import typer
from rich import print

#
import swagger_client
from swagger_client.rest import ApiException
from swagger_client import InlineResponse200

################################################################################

def Test_token_is_ok(token: str) -> bool:
    configuration = swagger_client.Configuration()
    configuration.api_key['X-Auth-Token'] = token

    api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

    try:
        # 心跳
        api_response = api_instance.user_api_v2_hello()
        pprint(api_response)
        print(type(api_response))
        print(type(api_response.status))

    except ApiException as e:
        print("Exception when calling UserApi->user_api_v2_hello: %s\n" % e)



################################################################################

app = typer.Typer(no_args_is_help=True)


@app.command()
def hello(name: str = "Yuque") -> None:
    print(f"Hi, [bold red]{name}[/bold red]!!!")


@app.command(help="the main command", no_args_is_help=True)
def run(token: str = typer.Argument(help="the yuque token")):
    print("token = [bold red]{}[/bold red]".format(token))

    configuration = swagger_client.Configuration()
    configuration.api_key['X-Auth-Token'] = token

    api_instance = swagger_client.UserApi(swagger_client.ApiClient(configuration))

    try:
        # 心跳
        api_response = api_instance.user_api_v2_hello()
        pprint(api_response)

        if isinstance(api_response, InlineResponse200):
            print("OK")
        else:
            print("not OK")

        api_response = cast(InlineResponse200, api_response)

    except ApiException as e:
        print("Exception when calling UserApi->user_api_v2_hello: %s\n" % e)

    try:
        # 获取当前 Token 的用户详情
        api_response = api_instance.user_api_v2_user_info_with_http_info(_return_http_data_only=False)
        pprint(api_response[0])
        pprint(api_response[1])
        pprint(api_response[2]["X-RateLimit-Limit"])
        pprint(api_response[2]["X-RateLimit-Remaining"])
        print("Limit = {} / {}")
    except ApiException as e:
        print("Exception when calling UserApi->user_api_v2_user_info: %s\n" % e)


if __name__ == "__main__":
    app()
