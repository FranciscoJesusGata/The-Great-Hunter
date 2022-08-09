from apilib.intra import ic
import json
import requests

def bonus_projects(project_id, project_name, final_mark, cursus):
    return project_name in cursus[project_id].keys() and \
            final_mark == cursus[project_id][project_name] or \
            project_name not in cursus[project_id].keys()

margin = [
        "ft_service",
        "ft_server",
        "netwhat"
]

"""
Cursus 9 bonus are not verified
"""
cursus = {
    21: {
            "Libft": 125,
            "Born2beroot": 125,
            "get_next_line": 125,
            "ft_printf": 125,
            "FdF": 125,
            "fract-ol": 125,
            "so_long": 125,
            "pipex": 125,
            "minitalk": 125,
            "push_swap": 125,
            "minishell": 125,
            "Philosophers": 125,
            "cub3d": 125,
            "miniRT": 125,
            "ft_containers": 125,
            "Inception": 125,
            "ft_irc": 125,
            "webserv": 125,
            "libasm": 115
        },
    9: {
        "C Piscine Rush 00": 120,
        "C Piscine Rush 01": 125,
        "C Piscine Rush 02": 130
        }
    }

login = input("Insert an user login: ")
while len(login) == 0:
    print("You can't left this space blank")
    login = input("Insert an user login: ")
payload = {
        "range[final_mark]": "100,130"
}
max_marked = 0
response = ic.pages_threaded("users/" + login + "/projects_users", params=payload)
for project in response:
    if "Exam" not in project['project']['name'] and project['project']['name'] not in margin and \
            (project['cursus_ids'][0] not in cursus.keys() or \
            bonus_projects(project['cursus_ids'][0], project['project']['name'], project['final_mark'], cursus)):
        print(f"{'Project ' + project['project']['name'] + ' final_mark mark: ':<45}", project['final_mark']);
        max_marked += 1
print ("Project with the maximum mark:", max_marked);
