import typer
from rich.prompt import Prompt


def main():
    print("Initializing the Nebari 🚀 ")
    print("user don't need to set default in init command if you wish to customize something please have a look to qhub --help command and their values")

    cloud_provider = typer.prompt("What's your Cloud Provider?")
    
    if cloud_provider == "AWS" and not os.getenv('AWS_ACCESS_KEY_ID') and not os.getenv("AWS_SECRET_ACCESS_KEY"):
        print("Please generate your AWS keys at this link:
              https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html
              ")
        aws_access_key_id = typer.prompt("Please enter your AWS_ACCESS_KEY_ID: ")
        aws_secret_access_key = typer.prompt("Please enter your AWS_SECRET_ACCESS_KEY: ")
        
    project = typer.prompt("What's your Project Name?")
              
    domain = typer.prompt("What's your registered Domain Name?")
    
    auth_provider = typer.prompt("What's your Auth Provider?")
    namespace = typer.prompt("What's the Namespace?")
    repository = typer.prompt("What's your Repository Name?")
    ci_provider = typer.prompt("What's your CI-Provider?")
    terraform_state = typer.prompt("What's the Terraform State?")
    kuberenetes_version = typer.prompt("What's the Kubernetes Version?")
    SSL_Certs = typer.prompt("What's your SSL certs email address?")

    


if __name__ == "__main__":
    typer.run(main)
