#
import time
from typing import cast, Any

#
from rich import print
from rich.console import Console
from rich.progress import Progress, TaskID

#
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import InlineResponse200


class YuqueClient:
    def __init__(self, token: str):
        configuration = swagger_client.Configuration()
        configuration.api_key['X-Auth-Token'] = token
        api_client = swagger_client.ApiClient(configuration)

        self.user_api_instance = swagger_client.UserApi(api_client)
        self.repo_api_instance = swagger_client.RepoApi(api_client)
        self.doc_api_instance = swagger_client.DocApi(api_client)

        self.console = Console()
        self.console.log("Token = [bold green]{}[/bold green]".format(token))

        self.Repos_task_id = TaskID(-1)
        self.Repo_task_id = TaskID(-1)
        self.doc_task_id = TaskID(-1)

    def run(self):
        # CHECK if the TOKEN IS AVAILABLE

        with self.console.status("Token Checking"):
            if not self.run_hello():
                self.console.log("Token Checked: [bold red]FAIL[/bold red]")
                return
            self.console.log("Token Checked: [bold green]PASS[/bold green]")

        # Get All REPOS and RUN
        with Progress(console=self.console) as progress:
            self.Repos_task_id = progress.add_task("REPOS Processing...", total=1000)
            self.Repo_task_id = progress.add_task("REPO  Processing...", total=1000)
            self.doc_task_id = progress.add_task("DOC   Processing...", total=1000)

            while not progress.finished:
                progress.update(self.Repos_task_id, advance=0.5)
                progress.update(self.Repo_task_id, advance=0.3)
                progress.update(self.doc_task_id, advance=0.9)
                time.sleep(0.02)

    def run_hello(self) -> bool:
        """
        测试token是否可行
        :return:
        """
        api_responses = None

        try:
            # 心跳
            api_responses = self.user_api_instance.user_api_v2_hello_with_http_info(_return_http_data_only=False)
            if api_responses[1] != 200:
                raise Exception("Check token failed")
        except ApiException as e:
            print("Exception when calling UserApi->user_api_v2_hello: %s\n" % e)

        api_responses = cast(tuple[InlineResponse200, int, Any], api_responses)
        if api_responses[1] != 200:
            return False
        return True

    def run_user(self):
        """
        获取个人信息
        :return:
        """
        pass

    def run_repos(self):
        pass

    def run_repo(self):
        """
        获取仓库的相关信息，并留有数据给doc，调用run_doc
        :return:
        """
        pass

    def run_doc(self):
        """
        获取文档的相关信息，并执行文档的格式转化，以及图片等资源文件的下载等等
        :return:
        """
        pass

    def run_element(self):
        """
        进行文档元素的转化
        :return:
        """
        pass
