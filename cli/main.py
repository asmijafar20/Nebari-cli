import typer


app = typer.Typer(help="Nebari CLI 🪴", add_completion=False)



@app.command()
def init(CloudProvider: str = typer.Argument("", help="Name of your Cloud Provider. [gcp, azure, aws, local, existing, do]"),
    ProjectName: str = typer.Argument("", help="Name of the Project"),
    DomainName: str = typer.Argument("", help="DNS name for your project"),
    AuthProvider: str = typer.Argument(["github","auth0","password"],envvar=["AUTH0_DOMAIN", "AUTH0_CLIENTID", "AUTH0_CLIENT_SECRET"], help="Authentication provider"),
    NameSpace: str = typer.Argument("dev", help="Namespace"),
    Ci_Provider: str = typer.Argument(["none","github-actions"], help="CI-Provider"),
    Repository: str = typer.Argument("",envvar=["GITHUB_USERNAME", "GITHUB_TOKEN"], help="Repository Name"),
    TerraformState: str = typer.Argument(["remote","local","existing"], help="Terraform State"),
    KubernetesVersion: str = typer.Argument("most recent version available",envvar=["QHUB_K8S_VERSION"], help="Kubernetes Version"),
    SSL_Certs: str = typer.Argument("email address", help="Lets-encrypt ACME server email"),
):
    """
    Initialize the Nebari. ✨ 
    """
    

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
    
