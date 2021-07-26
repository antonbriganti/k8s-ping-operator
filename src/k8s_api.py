from kubernetes import client


def update_pingtest_object(object_name, object_namespace, patch_body):
    api = client.CustomObjectsApi()
    api.patch_namespaced_custom_object(
        group="app.anton.com",
        version="v1",
        namespace=object_namespace,
        name=object_name,
        plural="pingtests",
        body=patch_body,
    )
