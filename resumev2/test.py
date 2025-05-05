#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint as pp
import json
from datetime import datetime
import os
import pandas as pd

class JiraClient:

    def __init__(self):
        self.auth = HTTPBasicAuth(
            os.getenv('JFROG_EMAIL'),
            os.getenv('JIRA_TOKEN'),
        )

    def jira_query(self, query):
        url = "https://alertinnovation.atlassian.net/rest/api/3/search"

        headers = {"Accept": "application/json"}

        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    params=query,
                                    auth=self.auth)
        return json.loads(response.text)

    def get_total_bugs_and_stories(self, user_email):
        jql_bugs = f'assignee = "{user_email}" AND issuetype = "Bug"'
        jql_stories = f'assignee = "{user_email}" AND issuetype = "Story"'

        bugs = self.jira_query({"jql": jql_bugs})
        stories = self.jira_query({"jql": jql_stories})

        total_bugs = bugs['total']
        total_stories = stories['total']

        return {"total_bugs": total_bugs, "total_stories": total_stories}

if __name__ == "__main__":
    jira_client = JiraClient()
    user_email = os.getenv('JFROG_EMAIL')

    if user_email:
        result = jira_client.get_total_bugs_and_stories(user_email)
        pp(result)
    else:
        print("User email is not set in the environment variables.")
