# The-Great-Hunter
Python Script using 42API and [42api-lib](https://github.com/hivehelsinki/42api-lib.git) created by [Hive Helsinki](https://www.hive.fi/en/) to know how many project you passed with the maximum mark. The aim of this is to give a tool that make you able to claim the Bonus Hunter achivement at [42School](https://42.fr/) with a proof of work.

## Install
The only requesites you'll need to run this script is have installed `python3` and `pip3`.

### Linux
```
$ sudo apt-get install python3 pip -y
```
### Mac OS
```
$ brew install python3
```
## Usage
To run this script just run:
```
$ ./run.sh
```
This script already gets and configures the git submodules, and install the required Python modules and executes the script.

If the `config.yml` file is not created the script will create it for you, it will ask you for your `UID` and `Secret` for the API. To get them just sign-in in the 42 intranet > settings > API.

If you already registered an APP just access to the app page in Your Applications section. If not, you can see how to register a new app [here](https://api.intra.42.fr/apidoc/guides/getting_started).

Then, just copy the `UID` and press `enter` and do the same for the `Secret`.

After introducing the app credentials, the script will ask you for a login and will display you all the projects with the maximum mark.

>⚠️ For security reasons the API secret is constantly changing and you have to change it by hand, when this happens, just edit the `apilib/config.yml` file and put the new secret in the `Secret` field.

>Students doesn't have access to the maximum mark of the projects, so this script only have in consideration the projects in the common core, also will take as maximum score projects from other cursus when have at least a final mark of 100. You can filter projects in the margin list on `main.py`.

If you want more project's marks added to the script just open an Issue and give me a proof of the mark via Slack, my login is fgata-va.
