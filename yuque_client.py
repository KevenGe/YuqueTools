#
import time
from pathlib import Path
from typing import Callable, Optional, cast, Any
from functools import partial

#
from click import Option
from rich import print
from rich.console import Console
from rich.progress import Progress, TaskID

#
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models import (
    InlineResponse200,
    InlineResponse2001,
    InlineResponse2007,
    InlineResponse2008,
    InlineResponse20012,
    InlineResponse20014,
    V2User,
    V2Book,
    V2BookDetail,
    V2Doc,
    V2DocDetail,
)


class YuqueClient:
    def __init__(self, token: str):
        configuration = swagger_client.Configuration()
        configuration.api_key["X-Auth-Token"] = token
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

        # CHECK USER
        user = self.run_user()
        if user is None:
            return

        # Get All REPOS and RUN
        with Progress(console=self.console, transient=True) as progress:
            # repos
            repos = self.run_repos(user.id)
            if repos is None:
                return

            Repos_task_id = progress.add_task("REPOS Processing...", total=len(repos))
            for repo in repos:
                docs = self.run_docs(repo.id)
                if docs is None:
                    continue

                Repo_task_id = progress.add_task("REPO  Processing...", total=len(docs))
                for doc in docs:
                    doc_det = self.run_doc(repo.id, doc.id)
                    if doc_det is None:
                        continue

                    repo_dir = Path("./docs/{0}/".format(repo.name))
                    if not repo_dir.exists():
                        repo_dir.mkdir(parents=True)

                    with open(
                        "{0}/{1}.md".format(repo_dir, doc.title),
                        "w",
                        encoding="utf-8",
                    ) as f:
                        f.write(doc_det.body)

                    progress.log(
                        "Saved Doc: {}".format("{0}/{1}.md".format(repo_dir, doc.title))
                    )
                    progress.advance(Repo_task_id)

                progress.advance(Repos_task_id)

    def run_with_limits_info(self, func: Callable[..., Any]) -> Optional[Any]:
        api_responses = None
        try:
            api_responses = func(_return_http_data_only=False)
        except ApiException as e:
            self.console.log("ApiException Happened!")
            self.console.log(e)
        else:
            ratelimit_limit: str = "Nan"
            ratelimit_remain: str = "Nan"

            if "X-RateLimit-Limit" in api_responses[2]:
                ratelimit_limit = api_responses[2]["X-RateLimit-Limit"]

            if "X-RateLimit-Remaining" in api_responses[2]:
                ratelimit_remain = api_responses[2]["X-RateLimit-Remaining"]

            self.console.log(
                "RateLimit: {0} / {1}".format(ratelimit_remain, ratelimit_limit)
            )

        if api_responses is None:
            return None

        return api_responses[0]

    def run_hello(self) -> bool:
        """
        测试token是否可行
        :return:
        """

        res = self.run_with_limits_info(
            self.user_api_instance.user_api_v2_hello_with_http_info
        )

        if res is None:
            return False
        return True

    def run_user(self):
        """
        获取个人信息
        :return:
        """
        res = self.run_with_limits_info(
            self.user_api_instance.user_api_v2_user_info_with_http_info
        )

        if res is None:
            return None

        res = cast(InlineResponse2001, res)
        user = cast(V2User, res.data)

        self.console.log("User: {}".format(user.name))
        self.console.log(user)

        return user

    def run_repos(self, login):
        res = self.run_with_limits_info(
            partial(
                self.repo_api_instance.repo_api_v2_repo_list_with_http_info, login=login
            )
        )

        if res is None:
            return None

        res = cast(InlineResponse20012, res)
        books = cast(list[V2Book], res.data)
        return books

    def run_repo(self, book_id):
        """
        获取仓库的相关信息，并留有数据给doc，调用run_doc
        :return:
        """
        res = self.run_with_limits_info(
            partial(
                self.repo_api_instance.repo_api_v2_repo_show_by_id_with_http_info,
                book_id=book_id,
            )
        )

        if res is None:
            return None

        res = cast(InlineResponse20014, res)
        book = cast(V2BookDetail, res.data)
        return book

    def run_docs(self, book_id):
        res = self.run_with_limits_info(
            partial(
                self.doc_api_instance.doc_api_v2_doc_list_by_id_with_http_info,
                book_id=book_id,
            )
        )

        if res is None:
            return None

        res = cast(InlineResponse2007, res)
        docs = cast(list[V2Doc], res.data)
        return docs

    def run_doc(self, book_id, id):
        """
        获取文档的相关信息，并执行文档的格式转化，以及图片等资源文件的下载等等
        :return:
        """
        res = self.run_with_limits_info(
            partial(
                self.doc_api_instance.doc_api_v2_doc_show_by_id_with_http_info,
                book_id=book_id,
                id=id,
            )
        )

        if res is None:
            return None

        res = cast(InlineResponse2008, res)
        doc = cast(V2DocDetail, res.data)
        return doc
