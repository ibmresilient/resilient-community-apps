# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

import logging
from typing import Tuple
from resilient_lib import str_to_bool
from github3 import GitHub, GitHubEnterprise, GitHubError
from github3.exceptions import GitHubException

LOG = logging.getLogger(__name__)

class GitHubHelper():
    def __init__(self, repo_owner, repo_name, options):
        verify = str_to_bool(options.get("verify", "True"))

        self.gh = None
        if options.get("base_url"):
            if options.get("username") and options.get("password"):
                self.gh = GitHubEnterprise(url=options.get("base_url"),
                                           username=options.get("username"),
                                           password=options.get("password"),
                                           verify=verify)
            elif options.get("api_token"):
                self.gh = GitHubEnterprise(url=options.get("base_url"),
                                           token=options.get("api_token"),
                                           verify=verify)
        elif options.get("username") and options.get("password"):
            self.gh = GitHub(username=options.get("username"),
                             password=options.get("password"))
        elif options.get("api_token"):
            self.gh = GitHub(token=options.get("api_token"))
        else:
            raise ValueError("Either 'username' and 'password', or 'api_token' are required")

        self.repo = None
        if self.gh and repo_owner and repo_name:
            self.repo = self.gh.repository(repo_owner, repo_name)


    def get_file_contents(self: object, file_path: str, ref: str) -> Tuple[str, str]:
        """Get the contents of a file base on its repository, file path and branch (if any)

        :param file_path: /path/to/file_name
        :type file_path: str
        :param ref: branch name
        :type ref: str
        :return: return contents of file and err_msg or None
        :rtype: Tuple[str, str]
        """
        results, err_msg = self.get_file(file_path, ref)
        if results:
            results = results.content

        return results, err_msg

    def get_file(self: object, file_path: str, ref: str) -> Tuple[dict, str]:
        """Get a file object based on it's repository, file path and branch (if any)

        :param file_path: /path/to/file_name
        :type file_path: str
        :param ref: branch name
        :type ref: str
        :return: return contents of file object and err_msg or None
        :rtype: Tuple[str, str]
        """

        try:
            results = self.repo.file_contents(path=file_path, ref=ref)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def create_file(self: object, file_path: str,
                    file_contents: bytes, commit_msg: str,
                    committer: dict, branch: str ='main') -> Tuple[dict, str]:
        """Create a file based on it's repository, file path and branch (if any)

        :param file_path: /path/to/file_name
        :type file_path: str
        :param file_contents: contents of file, in byte format
        :type file_contents: bytes
        :param commit_msg: commit message
        :type commit_msg: str
        :param commiter: {"name":"A Name", "email":"a_name@example.com"}
        :type committer: dict
        :param branch: optional existing branch, defaults to 'main'
        :type branch: str, optional
        :return: results of API call and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        try:
            results = self.repo.create_file(file_path, commit_msg, file_contents, branch=branch, committer=committer)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def update_file(self: object, file_path: str, file_contents: bytes,
                    commit_msg: str, committer: dict, branch: str ='main') -> Tuple[dict, str]:
        """Update a file based on it's repository, file path and branch (if any)

        :param file_path: /path/to/file_name
        :type file_path: str
        :param file_contents: contents of file, in byte format
        :type file_contents: bytes
        :param commit_msg: commit message
        :type commit_msg: str
        :param committer: {"name":"A Name", "email":"a_name@example.com"}
        :type committer: dict
        :param branch: optional existing branch, defaults to 'main'
        :type branch: str, optional
        :return: results of API call and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        try:
            content, err_msg = self.get_file(file_path, branch)
            if err_msg:
                return None, err_msg

            results = content.update(commit_msg, file_contents, branch=branch, committer=committer)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def delete_file(self: object, file_path: str,
                    commit_msg: str, committer: dict, branch: str ='main') -> Tuple[dict, str]:
        """Delete a file based on its repository, path and optionally branch

        :param file_path: /path/to/file_name
        :type file_path: str
        :param commit_msg: commit message
        :type commit_msg: str
        :param committer: {"name":"A Name", "email":"a_name@example.com"}
        :type committer: dict
        :param branch: optional existing branch, defaults to 'main'
        :type branch: str, optional
        :return: results of API call and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        try:
            content, err_msg = self.get_file(file_path, branch)
            if err_msg:
                return None, err_msg

            results = content.delete(commit_msg, branch=branch, committer=committer)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_repositories(self, repo_type: str) -> dict:
        """get all the repository available to the logged in user

        :param repo_type: type of repos to return: owner, member, public, private
        :type repo_type: str
        :return: all repos found and err_msg, if any
        :rtype: dict
        """
        try:
            results = self.gh.repositories(repo_type)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_commits(self, file_path:str,
                    since_date:str,
                    until_date:str,
                    branch:str,
                    limit: int) -> Tuple[dict, str]:
        """get all commits for given repo, branch and timeframe

        :param file_path: optional file path for commits
        :type file_path: str
        :param since_date:  optional iso formatted date 
        :type since_date: str
        :param until_date: optional iso formatted date 
        :type until_date: str
        :param branch: optional branch name
        :type branch: str
        :param limit: return only n number of commits
        :type limit: int
        :return: commit list and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.commits(path=file_path,
                                        sha=branch,
                                        since=since_date,
                                        until=until_date,
                                        number=limit if limit  else -1
                                        )
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def  get_directory(self: object, file_path:str, branch:str) -> Tuple[dict, str]:
        """_summary_

        :param file_path: optional file path
        :type file_path: str
        :param branch: optional branch
        :type branch: str
        :return: return contents of file object and err_msg or None
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.directory_contents(file_path,
                                                   ref=branch,
                                                   return_as=dict)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_commit(self, commit_sha: str) -> Tuple[dict, str]:
        """get a given commit based on it's SHA hash

        :param commit_sha: SHA of commit
        :type commit_sha: str
        :return: commit contents and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.commit(commit_sha)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def create_release(self, tag:str, name:str, description:str,
                       is_draft: bool, is_prerelease:bool) -> Tuple[dict, str]:
        """Create a release for a given repository

        :param tag: tag for release
        :type tag: str
        :param name: name for release
        :type name: str
        :param description: optional description
        :type description: str
        :param is_draft: True if create as a draft release
        :type is_draft: bool
        :param is_prerelease: True if create a prerelease
        :type is_prerelease: bool
        :return: results of create release and err_mag, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.create_release(tag,
                                               name=name,
                                               body=description,
                                               draft=is_draft,
                                               prerelease=is_prerelease)

            if results:
                results = results.as_dict()
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_latest_release(self) -> Tuple[dict, str]:
        """Get information about the current release

        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.latest_release()
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_release(self, tag: str) -> Tuple[dict, str]:
        """Get information about a specific release

        :param tag: tag (ex. 1.0.0) of the release
        :type tag: str
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.release_from_tag(tag)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_releases(self) -> Tuple[dict, str]:
        """Get all release for a repository.
        NOTE: does not return any draft repositories

        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.releases()
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_branches(self) -> Tuple[dict, str]:
        """Get all branches within a repository. Will always return at least 'main'

        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.branches(-1)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def get_branch(self, branch_name: str) -> Tuple[dict, str]:
        """Get information about a specific branch

        :param branch_name: Name of branch to return information
        :type branch_name: str
        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            results = self.repo.branch(branch_name)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def find_branch(self, repo_branch: str) -> Tuple[dict, str]:
        """Return information on branches which match a string pattern

        :param repo_branch: Name of branch to return information
        :type repo_branch: str
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        try:
            branches = self.get_branches()
            for branch in branches:
                if branch.name == repo_branch:
                    return branch, None

        except (GitHubError, GitHubException) as err:
            return None, str(err)

        return None, f"Target branch not found: {repo_branch}"

    def create_branch(self, repo_branch:str, based_on:str) -> Tuple[dict, str]:
        """create a branch within a repository

        :param repo_branch - name of branch to create
        :type repo_branch: str
        :param based_on - optional branch to base the new branch on
        :type based_on: str
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            based_on_ref = self.repo.commit(based_on)
            results = self.repo.create_branch_ref(repo_branch, based_on_ref)
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)

    def delete_branch(self, repo_branch):
        """delete an existing branch

        :param repo_branch: Name of branch to delete
        :type repo_branch: str
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """

        try:
            ref = self.repo.ref(f"heads/{repo_branch}")
            results = ref.delete()
            return results, None
        except (GitHubError, GitHubException) as err:
            return None, str(err)
