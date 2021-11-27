import re
import random
import string
import subprocess
import shutil
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUTS_GENERATED_DOT_FILES_FOLDER = os.path.join(APP_ROOT, 'outputs', 'generated_dot_files')
OUTPUTS_GENERATED_ACTIVITY_DIAGRAMS_FOLDER = os.path.join(APP_ROOT, 'outputs', 'generated_activity_diagrams')

def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

def gen_activity_diagram(data,extracted_relationships,actors_and_use_cases_array):
    extracted_actions = get_extract_actions(actors_and_use_cases_array)
    auth_actions = get_auth_actions(extracted_actions)
    generated_file_name = generate_activity_diagram(auth_actions,extracted_actions)
    return generated_file_name

def get_extract_actions(actors_and_use_cases_array):
    extracted_actions = []
    for actions in actors_and_use_cases_array:
        extracted_actions.append(actions[1])
    return extracted_actions

def get_auth_actions(extracted_actions):
    substrings = ['Sign In','Log In','Sign Up','Register']
    auth_actions = []
    for index,extracted_action in enumerate(extracted_actions):
        for substring in substrings:
            if extracted_action != None and substring in extracted_action:
                auth_actions.append(extracted_action)
    return auth_actions

def write_auth_actions_string(auth_actions):
    actions = []
    for index,auth_action in enumerate(auth_actions):
        action_no = index + 1
        action_string = '\taction' + str(action_no) + '[shape=box,style=rounded, label="'+auth_action+'"]\n'
        action_obj = {'action_index': index + 1, 'action':action_string}
        actions.append(action_obj)
    return actions


def write_auth_decisions(auth_actions):
    auth_decisions = []
    for index,auth_action in enumerate(auth_actions):
        decision_no = index + 1
        decision_obj = {}
        if auth_action['action'] != None and (('Sign In' or 'Log In') in auth_action['action']):
            decision_string = '\tif' + str(decision_no) + '[shape=diamond, label="Authenticated ?"]\n'
            decision_obj = {'decision_index': index + 1, 'decision': decision_string}
        elif auth_action['action'] != None and (('Sign Up' or 'Register') in auth_action['action']):
            decision_string = '\tif' + str(decision_no) + '[shape=diamond, label="Don\'t have account ?"]\n'
            decision_obj = {'decision_index': index + 1, 'decision': decision_string}
        auth_decisions.append(decision_obj)
        return auth_decisions


def write_actions_string(extracted_actions):
    actions = []
    for index, auth_action in enumerate(extracted_actions):
        action_no = index + 1
        action_string = '\taction' + str(action_no) + '[shape=box,style=rounded, label="' + auth_action + '"]\n'
        action_obj = {'action_index': index + 1, 'action': action_string}
        actions.append(action_obj)
    return actions

def write_auth_action_body(auth_actions_strings,auth_decisions):
    auth_action_body = []
    for auth_actions_string in auth_actions_strings:
        if auth_actions_string['action'] != None and (('Sign In' in auth_actions_string['action']) or ('Log In' in auth_actions_string['action'])):
            auth_action_body.append('\t\n\nstart -> auth_action' + str(auth_actions_string['action_index']))
            auth_action_body.append('\t\nauth_action' + str(auth_actions_string['action_index']) + ' -> ')
            for auth_decision in auth_decisions:
                if 'Authenticated ?' in auth_decision['decision']:
                    auth_action_body.append('if' + str(auth_decision['decision_index']) + '\n')
                    auth_action_body.append('\tif' + str(auth_decision['decision_index']) + ' -> ')
                auth_action_body.append('if' + str(auth_decision['decision_index']) + '\n')
        elif ('Sign Up' in auth_actions_string['action']) or ('Register' in auth_actions_string['action']):
            for auth_decision in auth_decisions:
                auth_action_body.append('\tif' + str(auth_decision['decision_index']) + ' -> ' + 'auth_action' + str(auth_actions_string['action_index']))
                if 'Don\'t have account ?' in auth_decision['decision']:
                    auth_action_body.append('auth_action' + str(auth_actions_string['action_index']))
    return auth_action_body


def write_action_body(auth_actions_strings,actions_strings,auth_decisions):
    action_body = []
    action = ''
    auth_action_body = write_auth_action_body(auth_actions_strings,auth_decisions)
    # if auth_actions_strings != None or len(auth_actions_strings) != 0:
    #     for auth_actions_string in auth_actions_strings:
    #         if auth_actions_string['action'] != None and (('Sign In' or 'Log In') in auth_actions_string['action']):
    #             action_body.append('\t\n\nstart -> action' + str(auth_actions_string['action_index']))
    #             for auth_decision in auth_decisions:
    #                 if 'Authenticated ?' in auth_decision['decision']:
    #                     action_body.append('\naction' + str(auth_actions_string['action_index']) + ' -> if' + str(auth_decision['decision_index']) +'[headport=n]\n' + 'if' + str(auth_decision['decision_index']) + ' -> ')
    #                 action_body.append('if' + str(auth_decision['decision_index']) + '[taillabel="No"]\n')
    #                 if 'Don\'t have account ?' in auth_decision['decision']:
    #                     action_body.append('if' + str(auth_decision['decision_index']) + ' -> ')
    #                     if 'Sign Up To The System' in auth_actions_string['action']:
    #                         action_body.append('action' + str(auth_actions_string['action_index']) + '[taillabel="Yes"]\n')

    actions_strings_len = len(actions_strings)
    action_body.append('\n\n\tstart -> ')
    for index, actions_string in enumerate(actions_strings):
        if index == 0:
            action_body.append('action' + str(actions_string['action_index']) + '\n')
        if actions_string['action_index'] < actions_strings_len:
            action_body.append('\taction' + str(actions_string['action_index']) + ' -> ' + 'action' + str(actions_string['action_index'] + 1) + '\n')
    action_body.append('\taction' + str(actions_strings_len) + ' -> end')
    return auth_action_body, action_body


def generate_activity_diagram(auth_actions,extracted_actions):
    if auth_actions != None or len(auth_actions) != 0:
        auth_actions_strings = write_auth_actions_string(auth_actions)
        auth_decisions = write_auth_decisions(auth_actions_strings)
    actions_strings = write_actions_string(extracted_actions)

    dot_file_name = generate_random_string()
    dot_file = open(OUTPUTS_GENERATED_DOT_FILES_FOLDER + "/activity_diagram_" + dot_file_name + ".dot", "x")

    dot_file_begining_string = 'digraph G {\n\t' + 'rankdir=TD;\n\t' + 'edge[fontsize="11" arrowhead=open];\n\t' + 'start[shape=circle, label="", style=filled];\n\t' + 'end[shape=doublecircle, label="", style=filled];\n\n'
    dot_file.write(dot_file_begining_string)

    if auth_actions != None or len(auth_actions) != 0:
        for auth_actions_string in auth_actions_strings:
            dot_file.write(auth_actions_string['action'])

    for actions_string in actions_strings:
        dot_file.write(actions_string['action'])

# for auth_decision in auth_decisions:
    #     dot_file.write(auth_decision['decision'])

    auth_action_body, action_body = write_action_body(auth_actions_strings, actions_strings, auth_decisions)

    # for auth_actions in auth_action_body:
    #     dot_file.write(auth_actions)

    for actions in action_body:
        dot_file.write(actions)

    dot_file.write('\n' + '}')
    dot_file.close()

    generate_diagram(dot_file_name)
    return '/generated_activity_diagrams/' + dot_file_name + '.png'

def generate_diagram(filename):
    subprocess.run(["dot", "-Tpng", OUTPUTS_GENERATED_DOT_FILES_FOLDER+"/activity_diagram_"+filename+".dot", "-o", OUTPUTS_GENERATED_ACTIVITY_DIAGRAMS_FOLDER+"/"+filename+".png"])
    return True
