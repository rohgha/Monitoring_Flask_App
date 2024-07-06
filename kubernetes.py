from kubernetes import client, config

def main():
    # Load Kubernetes configuration from default location
    config.load_kube_config()

    # Create Kubernetes API clients
    api_instance = client.AppsV1Api()
    core_api_instance = client.CoreV1Api()

    # Define the deployment
    deployment = client.V1Deployment(
        metadata=client.V1ObjectMeta(name="my-flask-app"),
        spec=client.V1DeploymentSpec(
            replicas=1,
            selector=client.V1LabelSelector(
                match_labels={"app": "my-flask-app"}
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(
                    labels={"app": "my-flask-app"}
                ),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="my-flask-container",
                            image="339713033994.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:latest",
                            ports=[client.V1ContainerPort(container_port=5000)]
                        )
                    ]
                )
            )
        )
    )

    # Create the deployment
    api_instance.create_namespaced_deployment(
        namespace="default",
        body=deployment
    )

    # Define the service
    service = client.V1Service(
        metadata=client.V1ObjectMeta(name="my-flask-service"),
        spec=client.V1ServiceSpec(
            selector={"app": "my-flask-app"},
            ports=[client.V1ServicePort(port=5000)]
        )
    )

    # Create the service
    core_api_instance.create_namespaced_service(
        namespace="default",
        body=service
    )

if __name__ == "__main__":
    main()
