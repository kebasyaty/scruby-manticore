# Scruby-Full-Text - Full-text search with Manticore Search.
# Copyright (c) 2026 Gennady Kostyunin
# SPDX-License-Identifier: GPL-3.0-or-later
"""Plugin for full-text search."""

from __future__ import annotations

__all__ = ("FullText",)

import concurrent.futures
import logging
import uuid
from collections.abc import Callable
from pathlib import Path
from typing import Any

import manticoresearch
import orjson
from scruby_plugin import ScrubyPlugin

from scruby_full_text import settings


class FullText(ScrubyPlugin):
    """Plugin for Scruby based on Manticore Search."""

    def __init__(self, scruby: Any) -> None:  # noqa: D107
        ScrubyPlugin.__init__(self, scruby)

    @staticmethod
    def _task_find(
        branch_number: int,
        lang_morphology: tuple[str, str],
        full_text_filter: dict[str, str],
        filter_fn: Callable,
        hash_reduce_left: str,
        db_root: str,
        class_model: Any,
        config: manticoresearch.configuration.Configuration,
    ) -> list[Any] | None:
        """Task for finding documents, using full-text search.

        This method is for internal use.

        Returns:
            List of documents or None.
        """
        branch_number_as_hash: str = f"{branch_number:08x}"[hash_reduce_left:]
        separated_hash: str = "/".join(list(branch_number_as_hash))
        leaf_path = Path(
            *(
                db_root,
                class_model.__name__,
                separated_hash,
                "leaf.json",
            ),
        )
        docs: list[Any] = []
        if leaf_path.exists():
            data_json: bytes = leaf_path.read_bytes()
            data: dict[str, str] = orjson.loads(data_json) or {}
            for _, val in data.items():
                doc = class_model.model_validate_json(val)
                if filter_fn(doc):
                    table_name: str = str(uuid.uuid4())
                    text_field_list = full_text_filter.keys()
                    doc_dict: dict[str, Any] = orjson.loads(val)
                    text_field_dict: dict[str, Any] = {
                        key: val or "" for key, val in doc_dict.items() if key in text_field_list
                    }
                    table_fields: str = ",".join([f"{field_name} text" for field_name in text_field_list])
                    lang_code: str = lang_morphology[0]  # noqa: F841
                    morphology: str = lang_morphology[1]
                    # Enter a context with an instance of the API client
                    with manticoresearch.ApiClient(config) as api_client:
                        # Create instances of API classes
                        index_api = manticoresearch.IndexApi(api_client)
                        search_api = manticoresearch.SearchApi(api_client)
                        utils_api = manticoresearch.UtilsApi(api_client)
                        try:
                            sql_str = f"CREATE TABLE {table_name}({table_fields}) morphology = '{morphology}'"
                            utils_api.sql(sql_str)
                            # Performs a search on a table
                            insert_request = manticoresearch.InsertDocumentRequest(
                                table=table_name,
                                doc=text_field_dict,
                            )
                            index_api.insert(insert_request)
                            search_query = manticoresearch.SearchQuery(match_phrase=full_text_filter)
                            search_request = manticoresearch.SearchRequest(
                                table=table_name,
                                query=search_query,
                            )
                            search_response = search_api.search(search_request)
                            if len(search_response.hits.hits) > 0:
                                docs.append(doc)
                        except Exception as err:
                            logging.exception("Exception when calling SearchApi.")
                            raise Exception from err
                        finally:
                            utils_api.sql(f"DROP TABLE IF EXISTS {table_name}")
        return docs or None

    async def find_one(
        self,
        lang_morphology: tuple[str, str],
        full_text_filter: dict[str, str],
        filter_fn: Callable = lambda _: True,
    ) -> Any | None:
        """Find a one document that matches the filter, using full-text search.

        Attention:
            - The search is based on the effect of a quantum loop.
            - The search effectiveness depends on the number of processor threads.

        Args:
            lang_morphology (tuple[str, str]): Tuple with code of language and morphology.
            full_text_filter (dict[str, str]): Filter for full-text search.
                                               Key -> name of text field.
                                               Value -> text query.
            filter_fn (Callable): A function that execute the conditions of filtering.

        Returns:
            Document or None.
        """
        # Variable initialization
        scruby = self.scruby()
        search_task_fn: Callable = self._task_find
        branch_numbers: range = range(scruby._max_number_branch)
        hash_reduce_left: int = scruby._hash_reduce_left
        db_root: str = scruby._db_root
        class_model: Any = scruby._class_model
        config = settings.CONFIG
        # Run quantum loop
        with concurrent.futures.ThreadPoolExecutor(scruby._max_workers) as executor:
            for branch_number in branch_numbers:
                future = executor.submit(
                    search_task_fn,
                    branch_number,
                    lang_morphology,
                    full_text_filter,
                    filter_fn,
                    hash_reduce_left,
                    db_root,
                    class_model,
                    config,
                )
                docs = future.result()
                if docs is not None:
                    return docs[0]
        return None

    async def find_many(
        self,
        lang_morphology: tuple[str, str],
        full_text_filter: dict[str, str],
        filter_fn: Callable = lambda _: True,
        limit_docs: int = 100,
        page_number: int = 1,
    ) -> list[Any] | None:
        """Find the many of documents that match the filter, using full-text search.

        Attention:
            - The search is based on the effect of a quantum loop.
            - The search effectiveness depends on the number of processor threads.

        Args:
            lang_morphology (tuple[str, str]): Tuple with code of language and morphology.
            full_text_filter (dict[str, str]): Filter for full-text search.
                                               Key -> name of text field.
                                               Value -> text query.
            filter_fn (Callable): A function that execute the conditions of filtering.
                                  By default it searches for all documents.
            limit_docs (int): Limiting the number of documents. By default = 100.
            page_number (int): For pagination. By default = 1.
                               Number of documents per page = limit_docs.

        Returns:
            List of documents or None.
        """
        # The `page_number` parameter must not be less than one
        assert page_number > 0, "`find_many` => The `page_number` parameter must not be less than one."
        # Variable initialization
        scruby = self.scruby()
        search_task_fn: Callable = self._task_find
        branch_numbers: range = range(scruby._max_number_branch)
        hash_reduce_left: int = scruby._hash_reduce_left
        db_root: str = scruby._db_root
        class_model: Any = scruby._class_model
        config = settings.CONFIG
        counter: int = 0
        number_docs_skippe: int = limit_docs * (page_number - 1) if page_number > 1 else 0
        result: list[Any] = []
        # Run quantum loop
        with concurrent.futures.ThreadPoolExecutor(scruby._max_workers) as executor:
            for branch_number in branch_numbers:
                if number_docs_skippe == 0 and counter >= limit_docs:
                    return result[:limit_docs]
                future = executor.submit(
                    search_task_fn,
                    branch_number,
                    lang_morphology,
                    full_text_filter,
                    filter_fn,
                    hash_reduce_left,
                    db_root,
                    class_model,
                    config,
                )
                docs = future.result()
                if docs is not None:
                    for doc in docs:
                        if number_docs_skippe == 0:
                            if counter >= limit_docs:
                                return result[:limit_docs]
                            result.append(doc)
                            counter += 1
                        else:
                            number_docs_skippe -= 1
        return result or None
