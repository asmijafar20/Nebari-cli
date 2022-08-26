import typer
from .init import init_main


app = typer.Typer(help="Nebari CLI 🪴", add_completion=False)



@app.command()
def init(cloudprovider: str = typer.Argument("", help="Name of your Cloud Provider. [gcp, azure, aws, local, existing, do]"),
    projectname: str = typer.Argument("", help="Name of the Project"),
    domainname: str = typer.Argument("", help="DNS name for your project"),
    authprovider: str = typer.Argument(["github","auth0","password"],envvar=["AUTH0_DOMAIN", "AUTH0_CLIENTID", "AUTH0_CLIENT_SECRET"], help="Authentication provider"),
    namespace: str = typer.Argument("dev", help="Namespace"),
    ci_provider: str = typer.Argument(["none","github-actions"], help="CI-Provider"),
    repository: str = typer.Argument("",envvar=["GITHUB_USERNAME", "GITHUB_TOKEN"], help="Repository Name"),
    terraformstate: str = typer.Argument(["remote","local","existing"], help="Terraform State"),
    kubernetesversion: str = typer.Argument("most recent version available",envvar=["QHUB_K8S_VERSION"], help="Kubernetes Version"),
    ssl_certs: str = typer.Argument("email address", help="Lets-encrypt ACME server email"),
):
    """
    Initialize the Nebari. ✨ 
    """
    init_main()    

@app.command()
def validate():
    """
    Validate the config.yaml file.

    """
    print("Validate the config.yaml file")


@app.command()
def render():
    """
    Render the config.yaml file.
    """
    print("Render the congig.yaml file")


@app.command()
def deploy():
    """
    Deploy the nebari
    """
    print("Deploy the Nebari")

@app.command()
def destroy():
    """
    Destroy the nebari
    """
    print("Destroy the Nebari")


if __name__ == "__main__":
    app()
    
