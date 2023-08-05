# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask_login import current_user
from flask_login import login_required

import kadi.lib.constants as const
from kadi.lib.api.blueprint import bp
from kadi.lib.api.core import internal
from kadi.lib.api.core import json_error_response
from kadi.lib.api.core import json_response
from kadi.lib.conversion import normalize
from kadi.lib.conversion import parse_json_object
from kadi.lib.permissions.core import has_permission
from kadi.lib.permissions.utils import permission_required
from kadi.lib.resources.api import get_selected_resources
from kadi.lib.utils import compact_json
from kadi.lib.web import download_bytes
from kadi.lib.web import qparam
from kadi.lib.web import url_for
from kadi.modules.collections.export import get_export_data
from kadi.modules.collections.models import Collection
from kadi.modules.collections.models import CollectionState
from kadi.modules.collections.utils import get_parent_collections
from kadi.modules.records.models import Record


@bp.get("/collections/<int:id>/export/internal/<export_type>", v=None)
@permission_required("read", "collection", "id")
@internal
@qparam("preview", default=False, parse=bool)
@qparam("download", default=False, parse=bool)
@qparam("filter", default=lambda: {}, parse=parse_json_object)
def get_collection_export_internal(id, export_type, qparams):
    """Export a collection in a specific format."""
    collection = Collection.query.get_active_or_404(id)
    export_types = const.EXPORT_TYPES["collection"]

    if export_type not in export_types:
        return json_error_response(404)

    if export_type == "json" or qparams["preview"] or qparams["download"]:
        file_ext = "png" if export_type == "qr" else export_type
        return download_bytes(
            get_export_data(collection, export_type, export_filter=qparams["filter"]),
            f"{collection.identifier}.{file_ext}",
            as_attachment=qparams["download"],
        )

    return json_response(
        200,
        body=url_for(
            "api.get_collection_export_internal",
            id=collection.id,
            export_type=export_type,
            preview=True,
            filter=compact_json(qparams["filter"]),
        ),
    )


@bp.get("/collections/select", v=None)
@login_required
@internal
@qparam("page", default=1, parse=int)
@qparam("term", parse=normalize)
@qparam("exclude", multiple=True, parse=int)
@qparam("action", multiple=True)
@qparam("record", default=None, parse=int)
@qparam("collection", default=None, parse=int)
def select_collections(qparams):
    """Search collections in dynamic selections.

    Uses :func:`kadi.lib.resources.api.get_selected_resources`.
    """
    excluded_ids = qparams["exclude"]
    record_id = qparams["record"]
    collection_id = qparams["collection"]

    # If applicable, exclude collections that are already linked to the record with the
    # given ID.
    if record_id is not None:
        record = Record.query.get_active(record_id)

        if record is not None and has_permission(
            current_user, "read", "record", record.id
        ):
            collection_ids_query = record.collections.filter(
                Collection.state == CollectionState.ACTIVE
            ).with_entities(Collection.id)
            excluded_ids += [c.id for c in collection_ids_query]

    filters = []

    # If applicable, exclude collections that are already a parent of the collection
    # with the given ID as well as all collections that already have a parent.
    if collection_id is not None:
        filters.append(Collection.parent_id.is_(None))
        collection = Collection.query.get_active(collection_id)

        if collection is not None and has_permission(
            current_user, "read", "collection", collection.id
        ):
            excluded_ids += [c.id for c in get_parent_collections(collection)]

    return get_selected_resources(
        Collection,
        page=qparams["page"],
        filter_term=qparams["term"],
        exclude=excluded_ids,
        actions=qparams["action"],
        filters=filters,
    )
