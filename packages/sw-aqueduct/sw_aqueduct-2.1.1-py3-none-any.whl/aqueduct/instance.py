# -*- coding: utf-8 -*-
from io import BytesIO

from swimlane import Swimlane
from swimlane.exceptions import SwimlaneHTTP400Error

# Copyright: (c) 2022, Swimlane <info@swimlane.com>
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)
from .decorators import dump_content, log_exception


class SwimlaneInstance:

    """Creates a connection to a single Swimlane instance"""

    instance_type = None

    def __init__(
        self,
        host="https://sw_web:4443",
        username=None,
        password=None,
        access_token=None,
        verify_ssl=False,
        verify_server_version=False,
        default_timeout=300,
        resource_cache_size=0,
        write_to_read_only=False,
    ):
        if username and password:
            self.swimlane = Swimlane(
                host=host,
                username=username,
                password=password,
                verify_ssl=verify_ssl,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only,
            )
        elif access_token:
            self.swimlane = Swimlane(
                host=host,
                access_token=access_token,
                verify_ssl=verify_ssl,
                verify_server_version=verify_server_version,
                default_timeout=default_timeout,
                resource_cache_size=resource_cache_size,
                write_to_read_only=write_to_read_only,
            )
        else:
            raise AttributeError("Please provide either a username and password or a access token!")
        self.__workflow_dict = {}
        self.__dashboard_dict = {}

    @property
    def application_dict(self):
        return_dict = {}
        for item in self.get_applications_light():
            if item and item.get("name") and item["name"] not in return_dict:
                return_dict[item["name"]] = item
        return return_dict

    @property
    def application_id_list(self):
        return_list = []
        app_dict = self.application_dict
        if app_dict:
            for key, val in app_dict.items():
                if val.get("id"):
                    return_list.append(val["id"])
        return return_list

    @property
    def plugin_dict(self):
        return_dict = {}
        plugins = self.get_plugins()
        if plugins:
            for item in plugins:
                if item:
                    plugin = self.get_plugin(item["id"])
                    if plugin and plugin.get("fileId"):
                        return_dict[item["name"]] = plugin["fileId"]
        return return_dict

    @property
    def workflow_dict(self):
        if not self.__workflow_dict:
            workflows = self.get_workflows()
            if workflows:
                for workflow in workflows:
                    app_dict = self.application_dict
                    if app_dict:
                        for name, item in app_dict.items():
                            if item and item.get("id") and workflow.get("applicationId") == item["id"]:
                                self.__workflow_dict[name] = workflow
        return self.__workflow_dict

    @property
    def dashboard_dict(self):
        if not self.__dashboard_dict:
            for dashboard in self.get_dashboards():
                if dashboard["name"] not in self.__dashboard_dict:
                    self.__dashboard_dict[dashboard["name"]] = dashboard["id"]
        return self.__dashboard_dict

    def _make_request(self, method, endpoint, json=None):
        resp = self.swimlane.request(method, endpoint, json=json)
        if resp and resp.ok:
            if resp.status_code == 204:
                return None
            if resp.headers.get("Content-Type").startswith("application/json"):
                return resp.json()
            else:
                return resp.content

    @dump_content
    @log_exception
    def get_applets(self):
        """Used to retrieve applets

        Returns:
            dict : A list of applet dictionaries
        """
        return self._make_request("GET", "/applet")

    @log_exception
    def get_applet(self, applet_id):
        """Retrieves a applet if it exists on the desired instance

        Args:
            applet_id (str): The ID of an applet

        Returns:
            dict : A dictionary of a applet
        """
        try:
            return self._make_request("GET", f"/applet/{applet_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_applet(self, applet: dict):
        """Used to add a applet to a Swimlane instance

        Args:
            applet (dict): A applet item to add to a Swimlane instance

        Returns:
            dict : A dictionary of a applet item
        """
        return self._make_request("POST", "/applet", json=applet)

    @dump_content
    @log_exception
    def update_applet(self, applet: dict):
        """Updates a provided applet with the data contained in the provided task dictionary.

        Args:
            applet (dict): A Swimlane applet dictionary.

        Returns:
            dict: A Swimlane applet dictionary.
        """
        return self._make_request("PUT", f"/applet/{applet['id']}", json=applet)

    @dump_content
    @log_exception
    def get_credentials(self):
        """Used to retrieve keystore items

        Returns:
            dict : A dictionary of keystore keys and encrypted values
        """
        return self._make_request("GET", "/credentials")

    @log_exception
    def get_credential(self, name: str):
        """Retrieves a keystore item if it exists on the desired instance

        Args:
            name (str): Name of a keystore item

        Returns:
            dict : A dictionary of a keystore item
        """
        try:
            return self._make_request("GET", f"/credentials/{name}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_credential(self, credential: dict):
        """Used to add a keystore key name (but not it's value) to a Swimlane instance

        Args:
            credential (dict): A keystore item to add to a Swimlane instance

        Returns:
            dict : A dictionary of a keystore item
        """
        return self._make_request("POST", "/credentials", json=credential)

    @dump_content
    @log_exception
    def get_tasks(self):
        """Retrieves a list of tasks for a Swimlane instance.

        Returns:
            list: A list of task objects
        """
        tasks = self._make_request("GET", "/task/list")
        if tasks and tasks.get("tasks"):
            return tasks["tasks"]

    @log_exception
    def get_tasks_by_application(self, application_id: str):
        """Gets a list of tasks by application ID.

        If the application ID does not exist, then this method returns False.

        If the task ID does exist it will return a list of tasks

        Args:
            application_id (str): A application ID to retrieve tasks from.

        Returns:
            list: A list of tasks associated with an application.
        """
        try:
            return self._make_request("GET", f"/task/list/{application_id}")
        except Exception as e:
            return False

    @log_exception
    def get_task(self, task_id: str):
        """Gets an task by a provided task ID.

        If the task ID does not exist, then this method returns False.

        If the task ID does exist it will return a dictionary object

        Args:
            task_id (str): A task ID to retrieve the entire task JSON.

        Returns:
            dict: A Swimlane task dictionary.
        """
        try:
            return self._make_request("GET", f"/task/{task_id}")
        except Exception as e:
            return False

    @dump_content
    def add_task(self, task: dict):
        """Adds a provided task dictionary to a Swimlane instance

        Args:
            task (dict): A Swimlane task dictionary.

        Returns:
            dict: A Swimlane task dictionary.
        """
        try:
            return self._make_request("POST", "/task", json=task)
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def update_task(self, task_id: str, task: dict):
        """Updates a provided task ID with the data contained in the provided task dictionary.

        Args:
            task_id (str): A task ID to update on a Swimlane instance
            task (dict): A Swimlane task dictionary.

        Returns:
            dict: A Swimlane task dictionary.
        """
        return self._make_request("PUT", f"/task/{task_id}", json=task)

    @dump_content
    @log_exception
    def get_plugins(self):
        """Retrieves a list of plugins for a Swimlane instance.

        Returns:
            list: A list of plugin (light) dictionary objects.
        """
        plugins = self._make_request("GET", "/task/packages")
        return plugins if plugins and isinstance(plugins, list) else []

    @log_exception
    def get_plugin(self, name: str):
        """Gets an plugin by a provided plugin name

        If the plugin does not exist, then this method returns False.

        If the plugin does exist it will return an plugin dictionary object.

        Args:
            name (str): A plugin name

        Returns:
            dict: A Swimlane plugin dictionary object.
        """
        try:
            return self._make_request("GET", f"/task/packages/{name}")
        except Exception as e:
            return False

    @log_exception
    def download_plugin(self, file_id: str):
        """A Swimlane internal fileId for a plugin or Python package to download

        Args:
            file_id (str): An internal Swimlane fileId to download a plugin or python package

        Returns:
            BytesIO: A bytesIO object of the downloaded file
        """
        stream = BytesIO()
        response = self.swimlane.request("GET", f"attachment/download/{file_id}", stream=True)
        for chunk in response.iter_content(1024):
            stream.write(chunk)
        stream.seek(0)
        return stream

    @log_exception
    def upload_plugin(self, filename, stream):
        """Uploads a plugin to a Swimlane instance given a filename and a BytesIO file stream

        Args:
            filename (str): A filename string
            stream (BytesIO): A BytesIO file stream

        Returns:
            json: JSON Response from uploading a plugin
        """
        if not filename.endswith(".swimbundle"):
            filename = filename.split(".")[0] + ".swimbundle"
        return self.swimlane.request("POST", "/task/packages", files={"file": (filename, stream.read())}).json()

    @log_exception
    def upgrade_plugin(self, filename, stream):
        """Uploads a plugin to be upgraded on a Swimlane instance given a filename and a BytesIO file stream

        Args:
            filename (str): A filename string
            stream (BytesIO): A BytesIO file stream

        Returns:
            json: JSON Response from uploading a plugin
        """
        if not filename.endswith(".swimbundle"):
            filename = filename.split(".")[0] + ".swimbundle"
        return self.swimlane.request("POST", "/task/packages/upgrade", files={"file": (filename, stream.read())}).json()

    @dump_content
    @log_exception
    def get_pip_packages(self, versions=["Python2_7", "Python3_6", "Python3"]):
        """Retrieves a list of pip packages for a Swimlane instance.

        Args:
            versions (list, optional): A list of Python versions. Defaults to ['Python2_7', 'Python3_6', 'Python3'].

        Returns:
            list: A list of package dictionary objects.
        """
        return_list = []
        for version in versions:
            try:
                resp = self._make_request("GET", f"/pip/packages/{version}")
                if resp:
                    for item in resp:
                        if item and isinstance(item, dict):
                            return_list.append(item)
            except Exception as e:
                continue
        return return_list

    @log_exception
    def install_package(self, package: dict):
        """Installs a Python (pip) package based on the provided package dictionary object.

        Args:
            package (dict): A Swimlane package dictionary object.

        Returns:
            dict: A dictionary of a Python pip package
        """
        json = {
            "name": package["name"],
            "version": package["version"],
            "pythonVersion": package["pythonVersion"],
        }
        return self._make_request("POST", "/pip/packages", json=json)

    @log_exception
    def install_package_offline(self, filename, stream, data):
        """Installs a Python package wheel file offline to a Swimlane instance given a filename and a BytesIO file stream

        Args:
            filename (str): A filename string
            stream (BytesIO): A BytesIO file stream
            data (dict): A dictionary of additional request information

        Returns:
            json: JSON Response from installing a Python package wheel file
        """
        return self.swimlane.request(
            "POST",
            "/pip/packages/offline",
            data=data,
            files={"wheel": (filename, stream.read())},
            timeout=120,
        )

    @dump_content
    @log_exception
    def get_assets(self) -> list:
        """Retrieves a list of assets for a Swimlane instance.

        Returns:
            list: A list of asset JSON objects.
        """
        assets = self._make_request("GET", "/asset")
        return assets if assets and isinstance(assets, list) else []

    @log_exception
    def get_asset(self, asset_id: str) -> dict:
        """Gets an asset by a provided ID

        If the asset does not exist, then this method returns False.

        If the asset does exist it will return an asset dictionary.

        Args:
            asset_id (str): An Swimlane asset ID

        Returns:
            dict: A Swimlane instance asset dictionary.
        """
        try:
            return self._make_request("GET", f"/asset/{asset_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_asset(self, asset: dict) -> dict:
        """Adds a provided asset dictionary object to a Swimlane instance

        Args:
            asset (dict): A Swimlane asset dictionary object.

        Returns:
            dict: A Swimlane asset dictionary object.
        """
        return self._make_request("POST", "/asset", json=asset)

    @dump_content
    @log_exception
    def update_asset(self, asset_id: str, asset: dict):
        """Updates a provided asset ID with the data contained in the provided asset dictionary object.

        Args:
            asset_id (str): An asset ID to update on a Swimlane instance
            asset (dict): A Swimlane asset dictionary object.

        Returns:
            dict: A Swimlane asset dictionary.
        """
        return self._make_request("PUT", f"/asset/{asset_id}", json=asset)

    @dump_content
    @log_exception
    def get_applications(self):
        """Retrieves a list of applications for a Swimlane instance.

        Returns:
            list: A list of json objects
        """
        return self._make_request("GET", "/app")

    @dump_content
    @log_exception
    def get_application(self, application_id):
        """Gets an application by a provided ID

        If the application does not exist, then this method returns False.

        If the application does exist it will return an JSON object

        Args:
            application_id (str): A Swimlane application ID

        Returns:
            json: A Swimlane application JSON
        """
        try:
            return self._make_request("GET", f"/app/{application_id}")
        except Exception as e:
            return False

    @log_exception
    def get_application_workspaces(self, application_id):
        """Gets a list of workspaces for an application ID.

        Args:
            application_id (str): A Swimlane application ID

        Returns:
            list: A list of workspaces associated with an application.
        """
        try:
            return self._make_request("GET", f"/workspaces/app/{application_id}")
        except Exception as e:
            return False

    @log_exception
    def get_applications_light(self):
        """Gets light version of all applications

        Returns:
            list: A list of application light objects
        """
        return self._make_request("GET", "/app/light")

    @dump_content
    @log_exception
    def update_application(self, application):
        """Updates the application based on the provided dictionary object

        Args:
            application (dict): A application dictionary object.

        Returns:
            dict: A Swimlane application object
        """
        return self._make_request("PUT", "/app", json=application)

    @dump_content
    @log_exception
    def add_application(self, application):
        """Adds an application based on the provided dictionary object

        Args:
            application (dict): A application dictionary object.

        Returns:
            dict: A Swimlane application object
        """
        return self._make_request("POST", "/app", json=application)

    @log_exception
    def get_default_report_by_application_id(self, application_id):
        """Gets the default report for an application based on the provided ID

        Args:
            application_id (str): A application id.

        Returns:
            dict: A Swimlane report dictionary object.
        """
        try:
            return self._make_request("GET", f"/reports/app/{application_id}/default")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def get_workspaces(self):
        """Retrieves a list of workspaces for a Swimlane instance.

        Returns:
            list: A list of workspace dictionary objects.
        """
        workspaces = self._make_request("GET", "/workspaces")
        return workspaces if workspaces else []

    @log_exception
    def get_workspace(self, workspace_id: str):
        """Gets an workspace by a provided ID

        If the workspace does not exist, then this method returns False.

        If the workspace does exist it will return an workspace dictionary object.

        Args:
            workspace_id (str): A Swimlane workspace ID

        Returns:
            dict: A  workspace dictionary object.
        """
        try:
            return self._make_request("GET", f"/workspaces/{workspace_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_workspace(self, workspace: dict):
        """Adds a provided Workspace object to a Swimlane instance

        Args:
            workspace (dict): A workspace dictionary object.

        Returns:
            dict: A workspace dictionary object.
        """
        return self._make_request("POST", "/workspaces", json=workspace)

    @dump_content
    @log_exception
    def update_workspace(self, workspace_id: str, workspace: dict):
        """Updates a provided workspace ID with the data contained in the provided workspace dictionary object.

        Args:
            workspace_id (str): A workspace ID to update on a Swimlane instance
            workspace (dict): A workspace dictionary object.

        Returns:
            dict: A workspace dictionary object.
        """
        return self._make_request("PUT", f"/workspaces/{workspace_id}", json=workspace)

    @dump_content
    @log_exception
    def get_dashboards(self):
        """Retrieves a list of dashboards for a Swimlane instance.

        Returns:
            list: A list of dashboard dictionary objects
        """
        dashboards = self._make_request("GET", "/dashboard")
        return dashboards if dashboards and isinstance(dashboards, list) else []

    @log_exception
    def get_dashboard(self, dashboard_id: str):
        """Gets an dashboard by a provided ID

        If the dashboard does not exist, then this method returns False.

        If the dashboard does exist it will return an dashboard dictionary object.

        Args:
            dashboard_id (str): A Swimlane dashboard ID

        Returns:
            dict: A Swimlane dashboard dictionary object.
        """
        try:
            return self._make_request("GET", f"/dashboard/{dashboard_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def update_dashboard(self, dashboard: dict):
        """Updates a Swimlane instance dashboard based on the provided dashboard dictionary.

        Args:
            dashboard (dict): A Swimlane dashboard dictionary object.

        Returns:
            dict: A Swimlane dashboard dictionary object.
        """
        return self._make_request("PUT", f"/dashboard/{dashboard['id']}", json=dashboard)

    @dump_content
    @log_exception
    def add_dashboard(self, dashboard: dict):
        """Adds a provided dashboard dictionary object to a Swimlane instance

        Args:
            dashboard (dict): A Swimlane dashboard dictionary object.

        Returns:
            dict: A Swimlane dashboard dictionary object.
        """
        return self._make_request("POST", "/dashboard", json=dashboard)

    @dump_content
    @log_exception
    def get_reports(self):
        """Retrieves a list of reports for a Swimlane instance.

        Returns:
            list: A list of report dictionary objects.
        """
        reports = self._make_request("GET", "/reports")
        return reports if reports else []

    @log_exception
    def get_report(self, report_id: str):
        """Gets an report by a provided ID

        If the report does not exist, then this method returns False.

        If the report does exist it will return a report dictionary object.

        Args:
            report_id (str): A Swimlane report ID

        Returns:
            dict: A Swimlane report dictionary object.
        """
        try:
            return self._make_request("GET", f"/reports/{report_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_report(self, report: dict):
        """Adds a provided report dictionary object to a Swimlane instance

        Args:
            report (dict): A report dictionary object.

        Returns:
            dict: A report dictionary object.
        """
        return self._make_request("POST", "/reports", json=report)

    @dump_content
    @log_exception
    def update_report(self, report_id: str, report: dict):
        """Updates a provided report ID with the data contained in the provided report dictionary object.

        Args:
            report_id (str): A report ID to update on a Swimlane instance
            report (dict): A report dictionary object.

        Returns:
            dict: A report dictionary object.
        """
        resp = self._make_request("PUT", f"/reports/{report_id}", json=report)
        if resp:
            return True

    @dump_content
    @log_exception
    def update_default_report(self, report: dict):
        """Updates a Swimlane applications default report with the provided report dictionary object.

        Args:
            report (dict): A report dictionary object.

        Returns:
            dict: A report dictionary object.
        """
        return self._make_request("PUT", f"/reports/{report['id']}", json=report)

    @dump_content
    @log_exception
    def get_users(self):
        """Retrieves a list of users for a Swimlane instance.

        Returns:
            list: A list of user dictionary objects.
        """
        users = self._make_request("GET", "/user/light")
        return users if users else []

    @log_exception
    def get_user(self, user_id: str):
        """Gets an user by a provided ID

        If the user does not exist, then this method returns False.

        If the user does exist it will return an user dictionary object.

        Args:
            user_id (str): A Swimlane user ID

        Returns:
            dict: A user dictionary object.
        """
        try:
            return self._make_request("GET", f"/user/{user_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def search_user(self, query_string: str):
        """Searches for a user by a query string

        If the user does not exist, then this method returns False.

        If the user does exist it will return an user dictionary object.

        Args:
            query_string (str): A query string typically a display name

        Returns:
            dict: A user dictionary object.
        """
        try:
            resp = self._make_request("GET", f"/user/lookup?name={query_string}")
            if resp and isinstance(resp, list):
                return resp[0]
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_user(self, user: dict):
        """Adds a provided user dictionary object.

        Args:
            user (dict): A user dictionary object.

        Returns:
            dict: A user dictionary object.
        """
        return self._make_request("POST", "/user", json=user)

    @dump_content
    @log_exception
    def update_user(self, user_id: str, user: dict):
        """Updates a provided user ID with the data contained in the provided user dictionary object.

        Args:
            user_id (str): A user ID to update on a Swimlane instance
            user (dict): A user dictionary object.

        Returns:
            dict: A user dictionary object.
        """
        return self._make_request("PUT", f"/user/{user_id}", json=user)

    @dump_content
    @log_exception
    def get_groups(self):
        """Retrieves a list of groups for a Swimlane instance.

        Returns:
            list: A list of group dictionary objects.
        """
        groups = self._make_request("GET", "/groups")
        return groups["items"] if groups.get("items") else groups.get("groups", [])

    @log_exception
    def get_group_by_name(self, group_name: str):
        """Gets an group by a provided name

        If the group does not exist, then this method returns False.

        If the group does exist it will return a group dictionary object.

        Args:
            group_name (str): A Swimlane group name

        Returns:
            dict: A Swimlane group object.
        """
        try:
            resp = self._make_request("GET", f"/users/lookup?name={group_name}")
            return resp[0] if resp and isinstance(resp, list) else False
        except Exception as e:
            return False

    @log_exception
    def get_group_by_id(self, group_id: str):
        """Gets an group by a provided id

        If the group does not exist, then this method returns False.

        If the group does exist it will return a group dictionary object.

        Args:
            group_id (str): A Swimlane group ID

        Returns:
            dict: A Swimlane group object.
        """
        try:
            return self._make_request("GET", f"/groups/{group_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_group(self, group: dict):
        """Adds a provided group dictionary object to a Swimlane instance

        Args:
            group (dict): A Swimlane group dictionary object.

        Returns:
            dict: A Swimlane group dictionary object.
        """
        try:
            return self._make_request("POST", "/groups", json=group)
        except SwimlaneHTTP400Error as sh:
            if sh.code == 1051:
                return True
            else:
                raise sh
        except Exception as e:
            raise e

    @dump_content
    @log_exception
    def update_group(self, group_id: str, group: dict):
        """Updates a provided group ID with the data contained in the provided group dictionary object.

        Args:
            group_id (str): A group ID to update on a Swimlane instance
            group (dict): A Swimlane group dictionary object.

        Returns:
            dict: A Swimlane group dictionary object.
        """
        return self._make_request("PUT", f"/groups/{group_id}", json=group)

    @dump_content
    @log_exception
    def get_roles(self):
        """Retrieves a list of roles for a Swimlane instance.

        These roles are modeled after the role dictionary object.

        Returns:
            list: A list of role dictionary objects.
        """
        return_list = []
        roles = self._make_request("GET", "/roles")
        if roles and isinstance(roles, dict):
            # checking for items here. 10.4.0 does not use the items key
            # but greater versions do (e.g. 10.5>)
            if roles.get("items"):
                roles = roles["items"]
        if roles and isinstance(roles, list):
            for role in roles:
                return_list.append(role)
        return return_list

    @log_exception
    def get_role(self, role_id: str):
        """Gets an role by a provided ID

        If the role does not exist, then this method returns False.

        If the role does exist it will return an role dictionary object.

        Args:
            role_id (str): A Swimlane role ID

        Returns:
            dict: A role dictionary object.
        """
        try:
            return self._make_request("GET", f"/roles/{role_id}")
        except Exception as e:
            return False

    @log_exception
    def get_role_by_name(self, role_name: str):
        """Gets an role by a provided name

        If the role does not exist, then this method returns False.

        If the role does exist it will return an role dictionary object.

        Args:
            role_name (str): A Swimlane role name

        Returns:
            dict: A role dictionary object.
        """
        try:
            return self._make_request("GET", f"/roles/?searchFieldName=name&searchValue={role_name}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_role(self, role: dict):
        """Adds a provided role dictionary object to a Swimlane instance

        Args:
            role (dict): A role dictionary object.

        Returns:
            dict: A role dictionary object.
        """
        return self._make_request("POST", "/roles", json=role)

    @dump_content
    @log_exception
    def update_role(self, role_id: str, role: dict):
        """Updates a provided role ID with the data contained in the provided role dictionary object.

        Args:
            role_id (str): A role ID to update on a Swimlane instance
            role (dict): A role dictionary object.

        Returns:
            dict: A role dictionary object.
        """
        return self._make_request("PUT", f"/roles/{role_id}", json=role)

    @dump_content
    @log_exception
    def get_workflows(self):
        """Retrieves a list of workflows for a Swimlane instance.

        These workflow are modeled after the `Workflow` data model

        Returns:
            list: A list of `Workflow` objects
        """
        return_list = []
        workflows = self._make_request("GET", "/workflow/")
        if workflows:
            for workflow in workflows:
                return_list.append(workflow)
        return return_list

    @log_exception
    def get_workflow(self, application_id: str):
        """Gets an workflow by a provided application ID

        If the workflow does not exist, then this method returns False.

        If the workflow does exist it will return an `Workflow` object

        Args:
            application_id (str): A Swimlane application ID

        Returns:
            Workflow: A `Workflow` data model object
        """
        try:
            return self._make_request("GET", f"/workflow/{application_id}")
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def add_workflow(self, workflow):
        """Adds a Swimlane instance with the provided Workflow data model object

        Args:
            workflow (Workflow): A `Workflow` data model object

        Returns:
            Workflow: A `Workflow` data model object
        """
        try:
            return self._make_request("POST", "/workflow/", json=workflow)
        except Exception as e:
            return False

    @dump_content
    @log_exception
    def update_workflow(self, workflow):
        """Updates a Swimlane instance with the provided `Workflow` data model object

        Args:
            workflow (Workflow): A `Workflow` data model object

        Returns:
            Workflow: A `Workflow` data model object
        """
        return self._make_request("PUT", f"/workflow/{workflow['id']}", json=workflow)
