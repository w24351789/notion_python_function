#%%
import json
import requests
import logging

def create_report_page(notion_token, notion_dbId, title, Tenant, tenantId, default_domain, subId, writer):
    logging.debug('create page')
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = {
        "parent": {
            "type": "database_id",
            "database_id": notion_dbId
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Tenant": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": Tenant
                        }
                    }
                ]
            },
            "Tenant ID": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": tenantId
                        }
                    }
                ]
            },
            "Default Domain": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": default_domain
                        }
                    }
                ]
            },
            "Subscriptions": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": subId
                        }
                    }
                ]
            },
            "健檢工程師": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": writer
                        }
                    }
                ]
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    data = json.loads(response.text)
    
    return data

def append_blocks(notion_token, pageId, blocks=[]):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": blocks} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)

    return data

def heading_1(content):
    children_block = {
        "type": "heading_1",
        "heading_1": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": content
                    }
                }
            ],
            "color": "default"
        }
    }

    return children_block

def heading_2(content):
    children_block = {
        "type": "heading_2",
        "heading_2": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                         "content": content
                    }
                }
            ],
            "color": "default"
        }
    }

    return children_block

def heading_3(content):
    children_block = {
        "type": "heading_3",
        "heading_3": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": content
                    }
                }
            ],
            "color": "default"
        }
    }

    return children_block

def paragraph(content):
    children_block = {
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": content
                    }
                }
            ],
            "color": "default"
        }
    }

    return children_block

def add_heading_1(notion_token, pageId, content, color="default"):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": [
                {
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ],
                        "color": color
                    }
                }
                
            ]} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)
    return data


def add_heading_2(notion_token, pageId, content, color="default"):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": [
                {
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ],
                        "color": color
                    }
                }
                
            ]} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)
    return data

def add_heading_3(notion_token, pageId, content, color="default"):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": [
                {
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ],
                        "color": color
                    }
                }
                
            ]} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)
    return data

def add_paragraph(notion_token, pageId, content, color="default"):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": [
                {
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ],
                        "color": color
                    }
                }
                
            ]} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)
    return data

def add_image(notion_token, pageid, image_url):

    url = f"https://api.notion.com/v1/blocks/{pageid}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": [
                    {
                        "type": "image",
                        "image": {
                            "type": "external",
                            "external": {
                                "url": image_url
                            }
                        }
                    }
                ]} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)
    return data

def add_table(notion_token, pageId, table_width, table_rows):

    url = f"https://api.notion.com/v1/blocks/{pageId}/children"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + notion_token
    }
    payload = { "children": [
                    {
                        "type": "table",
                        "table": {
                            "table_width": table_width,
                            "has_column_header": True,
                            "has_row_header": False,
                            "children": table_rows
                        }
                        }
                ]} 

    response = requests.patch(url, headers=headers, json=payload)

    data = json.loads(response.text)
    return data

# table raw gen  return array

table_raw = []


#%%
def table_raw_gen(cols, content = []):
    cells = []
    for col in range(cols):
        col_content = [{
                        "type": "text",
                        "text": {
                            "content": content[col]
                        },
                        "annotations": {
                            "bold": False,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": "default"
                        },
                        "plain_text": content[col]
                        }]
        cells.append(col_content)
    raw = {
            "type": "table_row",
            "table_row": {
                "cells": cells
            }
        }

    return raw


def table_raw_custom_gen(cols, content = [], bold=False, color="default"):
    cells = []
    for col in range(cols):
        col_content = [{
                        "type": "text",
                        "text": {
                            "content": content[col]
                        },
                        "annotations": {
                            "bold": bold,
                            "italic": False,
                            "strikethrough": False,
                            "underline": False,
                            "code": False,
                            "color": color
                        },
                        "plain_text": content[col]
                        }]
        cells.append(col_content)
    raw = {
            "type": "table_row",
            "table_row": {
                "cells": cells
            }
        }

    return raw
'''
raw = table_raw_gen(3, ['orange', 'apple', 'kiwi'])

table_raw.append(raw)

add_table(notion_token, , 3, table_raw)

'''

        