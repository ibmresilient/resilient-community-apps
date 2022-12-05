import logging
from typing import Tuple
from resilient_lib import str_to_bool
from github3 import login, GitHub, GitHubEnterprise, GitHubError
from github3.exceptions import GitHubException

LOG = logging.getLogger(__name__)

class GitHubHelper():
    def __init__(self, options):
        verify = str_to_bool(options.get("verify", True))

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
                             password=options.get("password"),
                             verify=verify)
        elif options.get("api_token"):
            self.gh = GitHub(token=options.get("api_token"),
                             verify=verify)
        else:
            raise ValueError("Either 'username' and 'password', or 'api_token' are required")

    def _get_repository(self, repo_owner: str, repo_name: str) -> object:
        """create the repository object for further API calls

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :return: repository object
        :rtype: object
        """
        return self.gh.repository(repo_owner, repo_name)

    def get_file_contents(self: object, repo_owner: str, repo_name: str, file_path: str, \
                          ref: str) -> Tuple[str, str]:
        """Get the contents of a file base on its repository, file path and branch (if any)

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :param file_path: /path/to/file_name
        :type file_path: str
        :param ref: branch name
        :type ref: str
        :return: return contents of file and err_msg or None
        :rtype: Tuple[str, str]
        """
        results, err_msg = self.get_file(repo_owner, repo_name, file_path, ref)
        if results:
            results = results.content

        return results, err_msg

    def get_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                 ref: str) -> Tuple[dict, str]:
        """Get a file object based on it's repository, file path and branch (if any)

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :param file_path: /path/to/file_name
        :type file_path: str
        :param ref: branch name
        :type ref: str
        :return: return contents of file object and err_msg or None
        :rtype: Tuple[str, str]
        """

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
        """Create a file based on it's repository, file path and branch (if any)

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
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
        repo = self._get_repository(repo_owner, repo_name)
        try:
            results = repo.create_file(file_path, commit_msg, file_contents, branch=branch, committer=committer)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def update_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                    file_contents: bytes, commit_msg: str, committer: dict, branch: str ='main') -> Tuple[dict, str]:
        """Update a file based on it's repository, file path and branch (if any)

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
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
            content, err_msg = self.get_file(repo_owner, repo_name, file_path, branch)
            if err_msg:
                return None, err_msg

            results = content.update(commit_msg, file_contents, branch=branch, committer=committer)
            return results, None
        except GitHubException as err:
            return None, str(err)
        except GitHubError as err:
            return None, str(err)

    def delete_file(self: object, repo_owner: str, repo_name: str, file_path: str, \
                    commit_msg: str, committer: dict, branch: str ='main') -> Tuple[dict, str]:
        """Delete a file based on its repository, path and optionally branch

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
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
        """get all the repository available to the logged in user

        :param repo_type: type of repos to return: owner, member, public, private
        :type repo_type: str
        :return: all repos found and err_msg, if any
        :rtype: dict
        """
        try:
            results = self.gh.repositories(repo_type)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_commits(self, args: dict) -> Tuple[dict, str]:
        """get all commits for given repo, branch and timeframe

        :param args: all parameters needed for function call
        :type args: dict
        :return: commit list and err_msg, if any
        :rtype: Tuple[dict, str]
        """
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
        """get a given commit based on it's SHA hash

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :param commit_sha: SHA of commit 
        :type commit_sha: str
        :return: commit contents and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.commit(commit_sha)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def create_release(self, fn_inputs: dict) -> Tuple[dict, str]:
        """Create a release for a given repository

        :param fn_inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_release_tag
            -   fn_inputs.github_release_name
            -   fn_inputs.github_release_description
            -   fn_inputs.github_release_draft
            -   fn_inputs.github_prerelease
        :type fn_inputs: dict
        :return: results of create release and err_mag, if any
        :rtype: Tuple[dict, str]
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
        """Get information about the current release

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.latest_release()
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_release(self, fn_inputs: tuple) -> Tuple[dict, str]:
        """Get information about a specific release

        :param fn_inputs:
            -   fn_inputs.github_owner
            -   fn_inputs.github_repo
            -   fn_inputs.github_release_tag
        :type fn_inputs: tuple
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(fn_inputs.github_owner, fn_inputs.github_repo)

        try:
            results = repo.release_from_tag(fn_inputs.github_release_tag)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_releases(self, repo_owner: str, repo_name: str) -> Tuple[dict, str]:
        """Get all release for a repository.
        NOTE: does not return any draft repositories

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.releases()
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_branches(self, repo_owner: str, repo_name: str) -> Tuple[dict, str]:
        """Get all branches within a repository. Will always return at least 'main'

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.branches(-1)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def get_branch(self, repo_owner: str, repo_name: str, branch_name: str) -> Tuple[dict, str]:
        """Get information about a specific branch

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :param branch_name: Name of branch to return information
        :type branch_name: str
        :return: json results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            results = repo.branch(branch_name)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def find_branch(self, repo_owner: str, repo_name: str, repo_branch: str) -> Tuple[dict, str]:
        """Return information on branches which match a string pattern

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :param repo_branch: Name of branch to return information
        :type repo_branch: str
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        try:
            branches = self.get_branches(repo_owner, repo_name)
            for branch in branches:
                if branch.name == repo_branch:
                    return branch, None

        except GitHubException as err:
            return None, str(err)

        return None, f"Target branch not found: {repo_branch}"

    def create_branch(self, fn_inputs: dict) -> Tuple[dict, str]:
        """create a branch within a repository

        :param fn_inputs:
            github_owner
            github_repo
            github_based_on_branch_or_sha - optional branch to base the new branch on
        :type fn_inputs: dict
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(fn_inputs.get('github_owner'), fn_inputs.get('github_repo'))

        based_on = repo.commit(fn_inputs.get('github_based_on_branch_or_sha'))

        try:
            results = repo.create_branch_ref(fn_inputs.get('github_branch'), based_on)
            return results, None
        except GitHubException as err:
            return None, str(err)

    def delete_branch(self, repo_owner, repo_name, repo_branch):
        """delete an existing branch

        :param repo_owner: high level owner of repo
        :type repo_owner: str
        :param repo_name: repository name
        :type repo_name: str
        :param repo_branch: Name of branch to delete
        :type repo_branch: str
        :return: JSON results and err_msg, if any
        :rtype: Tuple[dict, str]
        """
        repo = self.gh.repository(repo_owner, repo_name)

        try:
            ref = repo.ref(f"heads/{repo_branch}")
            ref.delete()
            return {}, None
        except GitHubException as err:
            return None, str(err)
