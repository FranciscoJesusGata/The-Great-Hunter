from apilib.intra import ic
import json
import requests

def bonus_projects(project_id, project_name, final_mark, cursus):
    return project_name in cursus[project_id].keys() and \
            final_mark == cursus[project_id][project_name] or \
            project_name not in cursus[project_id].keys()

def count_projects(response, cursus):
    max_marked = 0
    for project in response:
        if not any(exp in project['project']['name'] for exp in ["Exam", "Rush"]) and project['project']['name'] not in margin and \
                project['cursus_ids'] and (project['cursus_ids'][0] not in cursus.keys() or \
                bonus_projects(project['cursus_ids'][0], project['project']['name'], project['final_mark'], cursus)):
            print(f"{'Project ' + project['project']['name'] + ' final_mark mark: ':<45}", project['final_mark'])
            max_marked += 1
    print ("\r\nProject with the maximum mark:", max_marked)

margin = [
]
#All projects with bonus points organized by its cursus id
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
    }

login = input("Insert an user login: ")
while len(login) == 0:
    print("You can't left this space blank")
    login = input("Insert an user login: ")
payload = {
        "range[final_mark]": "100,130"
}
try:
    response = ic.pages("users/" + login + "/projects_users", params=payload)
except ValueError as e:
    print("Error in request:")
    print(e)
else:
    count_projects(response, cursus)
