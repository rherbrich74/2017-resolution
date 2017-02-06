# vw-docker.py
#
# A demonstration how to use Vowpal Wabbit through a docker image
#
# 2017 written by Ralf Herbrich

import os
import docker

data_dir = os.getcwd() + "/data"
train_file = "/data/income_train.vw"
test_file = "/data/income_validation.vw"
test_pred_file = "/data/income_validation.pred"
model_file = "/data/income.model"


volumes = {}
volumes[data_dir] = {'bind': '/data', 'mode': 'rw'}
train_command = "vw --loss_function logistic -f " + model_file + " -d " + train_file
test_command = "vw --loss_function logistic -i " + model_file + " -t " + test_file + " -p " + test_pred_file + " --quiet"

# Run the train and test command through a container
client = docker.from_env()
client.containers.run("mwhitaker/vowpal_wabbit_and_utilities", volumes=volumes, command=train_command)
client.containers.run("mwhitaker/vowpal_wabbit_and_utilities", volumes=volumes, command=test_command)

# Clear the containers
for container in client.containers.list(all=True):
    container.remove()