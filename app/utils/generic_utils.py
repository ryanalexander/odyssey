def asset_ref_to_obj(asset_id):
    namespace = asset_id[0:3]
    row_id = asset_id[4:]
    return {
        "namespace": namespace,
        "row_id": int(row_id)
    }