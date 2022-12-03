import logging
from typing import Tuple
from datetime import datetime
from resilient_lib import str_to_bool
from github3 import login, GitHub, GitHubEnterprise, GitHubError
from github3.exceptions import NotFoundError, GitHubException

LOG = logging.getLogger(__name__)

class GitHubHelper():
    def __init__(self, options):

        if options.get("base_url"):
            if options.get("username") and options.get("password"):
                self.gh = GitHubEnterprise(url=options.get("base_url"),
                                           username=options.get("username"),
                                           password=options.get("password"),
                                           verify=str_to_bool(options.get("verify", True)))
            elif options.get("api_token"):
                self.gh = GitHubEnterprise(url=options.get("base_url"),
                                           token=options.get("api_token"),
                                           verify=str_to_bool(options.get("verify", True)))
        elif options.get("username") and options.get("password"):
            self.gh = GitHub(username=options.get("username"),
                             password=options.get("password"),
                             verify=str_to_bool(options.get("verify", True)))
        elif options.get("api_token"):
            self.gh = GitHub(token=options.get("api_token"), 
                             verify=str_to_bool(options.get("verify", True)))
        else:
            raise ValueError("Either 'username' and 'password' or 'api_token' are required")

    def _get_repository(self, repo_owner, repo_name):
        return self.gh.repository(repo_owner, repo_name)

    def get_file_contents(self: object, repo_owner: str, repo_name: str, file_path: str, \
                 ref: str) -> Tuple[str, str]:
        results, err_msg = self.get_file(repo_owner, repo_name, file_path, ref)
        if results:
            results = results.content

        return results, err_msg

    def get_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                 ref: str) -> Tuple[dict, str]:

        try:
            repo = self._get_repository(repo_owner, repo_name)
            results = repo.file_contents(path=file_path, ref=ref)
            return results, None
        except GitHubError as err:
            return None, str(err)
        except GitHubException as err:
            return None, str(err)

    def create_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                    file_contents: bytes, commit_msg: str, \
                    committer: dict, branch: str ='main') -> Tuple[dict, str]:
        repo = self._get_repository(repo_owner, repo_name)
        try:
            results = repo.create_file(file_path, commit_msg, file_contents, branch=branch, committer=committer)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def update_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                    file_contents: bytes, commit_msg: str, \
                    committer: dict, branch: str ='main') -> Tuple[dict, str]:
        
        try:
            content, err_msg = self.get_file(repo_owner, repo_name, file_path, branch)
            if err_msg:
                return None, err_msg

            LOG.debug(content.as_json())

            #content.refresh()

            results = content.update(commit_msg, file_contents, branch=branch, committer=committer)
            return results, None
        except GitHubException as err:
            return None, str(err)
        except GitHubError as err:
            return None, str(err)

    def delete_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                    commit_msg: str, \
                    committer: dict, branch: str ='main') -> Tuple[dict, str]:
        
        try:
            content, err_msg = self.get_file(repo_owner, repo_name, file_path, branch)
            if err_msg:
                return None, err_msg

            results = content.delete(commit_msg, branch=branch, committer=committer)
            return results, None
        except GitHubException as err:
            return None, str(err)
        except GitHubError as err:
            return None, str(err)

    def get_repositories(self, repo_type: str) -> dict:
        try:
            results = self.gh.repositories(repo_type)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_commits(self, args: dict) -> Tuple[dict, str]:
        repo = self._get_repository(args.get('github_owner'), args.get('github_repo'))

        try:
            results = repo.commits(path=args.get('github_optional_file_path'),
                                   sha=args.get('github_branch'),
                                   since=args.get('github_since_date'),
                                   until=args.get('github_until_date')
                                  )
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_commit(self, repo_owner: str, repo_name: str, commit_sha: str) -> Tuple[dict, str]:
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.commit(commit_sha)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def create_release(self, fn_inputs: dict) -> Tuple[dict, str]:
        """_summary_

        :param fn_inputs: _description_
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_release_tag
            -   fn_inputs.github_release_name
            -   fn_inputs.github_release_description
            -   fn_inputs.github_release_draft
            -   fn_inputs.github_prerelease
        :type fn_inputs: dict
        :return: _description_
        :rtype: _type_
        """
        repo = self.gh.repository(fn_inputs.get('github_owner'), fn_inputs.get('github_repo'))

        try:
            results = repo.create_release(fn_inputs.get('github_release_tag'), 
                                          name=fn_inputs.get('github_release_name'),
                                          body=fn_inputs.get('github_release_description'),
                                          draft=str_to_bool(fn_inputs.get('github_release_draft', 'False')),
                                          prerelease=str_to_bool(fn_inputs.get('github_prerelease', 'False'))
                                         )
            if results:
                results = results.as_dict()
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_latest_release(self, repo_owner: str, repo_name: str) -> Tuple[dict, str]:
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.latest_release()
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_release(self, fn_inputs: tuple) -> Tuple[dict, str]:
        repo = self.gh.repository(fn_inputs.github_owner, fn_inputs.github_repo)

        try:
            results = repo.release_from_tag(fn_inputs.github_release_tag)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_releases(self, repo_owner: str, repo_name: str) -> Tuple[dict, str]:
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.releases()
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_branches(self, repo_owner: str, repo_name: str) -> Tuple[dict, str]:
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.branches(-1)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_branch(self, repo_owner: str, repo_name: str, branch_name: str) -> Tuple[dict, str]:
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.branch(branch_name)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def find_branch(self, repo_owner: str, repo_name: str, repo_branch: str) -> Tuple[dict, str]:
        try:
            branches = self.get_branches(repo_owner, repo_name)
            for branch in branches:
                if branch.name == repo_branch:
                    return branch, None

        except GitHubException as err:
            return None, str(err)

        return None, None

    def create_branch(self, fn_inputs: dict) -> Tuple[dict, str]:
        repo = self.gh.repository(fn_inputs.get('github_owner'), fn_inputs.get('github_repo'))

        based_on = repo.commit(fn_inputs.get('github_based_on_branch_or_sha'))

        try:
            results = repo.create_branch_ref(fn_inputs.get('github_branch'), based_on)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def delete_branch(self, github_owner, github_repo, github_branch):
        repo = self.gh.repository(github_owner, github_repo)

        try: 
            ref = repo.ref(f"heads/{github_branch}")
            ref.delete()
            return {}, None
        except GitHubException as err:
            return None, str(err)
