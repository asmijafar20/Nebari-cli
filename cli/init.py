import typer
from rich.prompt import Prompt
import os;
from rich import print


def init_main():
    print("Initializing the Nebari 🚀 ")
    print("user don't need to set default in init command if you wish to customize something please have a look to qhub --help command and their values")

    cloud_provider = click.prompt("What's your Cloud Provider?", type=click.choice(["gcp","aws"]))

    if cloud_provider == "AWS" and not (os.environ.get('AWS_ACCESS_KEY_ID') and os.environ.get("AWS_SECRET_ACCESS_KEY")):
        print("Please generate your AWS keys at this link:[blue]https://www.github.com/[/blue]")
        aws_access_key_id = typer.prompt("Please enter your AWS_ACCESS_KEY_ID")
        aws_secret_access_key = typer.prompt("Please enter your AWS_SECRET_ACCESS_KEY")

    if cloud_provider == "GCP" and not os.environ.get('GOOGLE_CREDENTIALS') and not os.environ.get("PROJECT_ID"):
        print("Please generate your GCP credentials at this link: [link=https://cloud.google.com/iam/docs/creating-managing-service-accounts][/link]")
        google_credentials = typer.prompt("Please enter your GOOGLE_CREDENTIALS")
        project_id = typer.prompt("Please enter your PROJECT_ID")

    if cloud_provider == "DO" and not os.environ.get('DIGITALOCEAN_TOKEN') and not os.environ.get("SPACES_ACCESS_KEY_ID") and not os.environ.get("SPACES_SECRET_ACCESS_KEY") and not os.environ.get("AWS_ACCESS_KEY_ID") and not os.environ.get("AWS_SECRET_ACCESS_KEY"):
        print("Please generate your Digital Ocean token at this link: [link=https://docs.digitalocean.com/reference/api/create-personal-access-token/][/link]")
        digital_ocean_token = typer.prompt("Please enter your DIGITALOCEAN_TOKEN")
        spaces_access_key_id = typer.prompt("Please enter your SPACES_ACCESS_KEY_ID")
        spaces_secret_access_key = typer.prompt("Please enter your SPACES_SECRET_ACCESS_KEY")
        aws_access_key_id = typer.prompt("Please set this variable with the same value as `SPACES_ACCESS_KEY_ID`")
        aws_secret_access_key = typer.prompt("Please set this variable with the same value as `SPACES_ACCESS_KEY`")

    if cloud_provider == "AZURE" and not os.environ.get('ARM_CLIENT_ID') and not os.environ.get("ARM_CLIENT_SECRET") and not os.environ.get("ARM_SUBSCRIPTION_ID") and not os.environ.get("ARM_TENANT_ID"):
        print("Please generate your AWS keys at this link: [link=https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret#creating-a-service-principal-in-the-azure-portal][/link]")
        arm_client_id = typer.prompt("Please enter your ARM_CLIENT_ID")
        arm_client_secret = typer.prompt("Please enter your ARM_CLIENT_SECRET")
        arm_subscription_id = typer.prompt("Please enter your ARM_SUBSCRIPTION_ID")
        arm_tenant_id = typer.prompt("Please enter your ARM_TENANT_ID")

    project = typer.prompt("What's your Project Name?")
   
    domain = typer.prompt("What's your registered Domain Name?")

    auth_provider = typer.prompt("What's your Auth Provider?")

    if auth_provider == "Auth0" and not os.environ.get('AUTH0_CLIENT_ID') and not os.environ.get("AUTH0_CLIENT_SECRET") and not os.environ.get("AUTH0_DOMAIN"):
        print("Please generate your Auth0 Access token at this link: [link=https://auth0.com/docs/get-started/auth0-overview/create-applications/machine-to-machine-apps][/link]")
        auth0_client_id = typer.prompt("Please enter your AUTH0_CLIENT_ID")
        auth0_client_secret = typer.prompt("Please enter your AUTH0_CLIENT_SECRET")
        auth0_domain = typer.prompt("Please enter your AUTH0_DOMAIN")

    if auth_provider == "github" :
        print("Please create a new OAuth 2.0 app. [link=https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/enabling-and-testing-saml-single-sign-on-for-your-organization][/link]")
        
    if auth_provider == "password" :
        print("Please create a keycloak user using this link: [link=https://docs.qhub.dev/en/latest/source/installation/login.html#login][/link]")
    
    namespace = typer.prompt("What's the Namespace?")
    
    repository = typer.prompt("What's your Repository Name?")
    
    if repository == "github" and not os.environ.get('GITHUB_USERNAME') and not os.environ.get("GITHUB_TOKEN"):
        print("Please generate your github access token at this link: [link=https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token][/link]")
        github_username = typer.prompt("Please enter your GITHUB_USERNAME")
        github_token = typer.prompt("Please enter your GITHUB_TOKEN")

    ci_provider = typer.prompt("What's your CI-Provider?")
    
    terraform_state = typer.prompt("What's the Terraform State?")

    kuberenetes_version = typer.prompt("What's the Kubernetes Version?")
    
    SSL_Certs = typer.prompt("What's your SSL certs email address?")

if __name__ == "__main__":
    typer.run(main)