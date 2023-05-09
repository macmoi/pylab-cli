import click
from commands import Auth

@click.group()
def main():
    pass

main.add_command(Auth.login)

if __name__ == '__main__':
    main()