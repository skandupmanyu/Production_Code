import pandas as pd
import numpy as np
import yaml
import argparse
from box import Box
import importlib
import warnings
warnings.filterwarnings("ignore")

def parse_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--conf")
	parser.add_argument("--deployment")

	args = parser.parse_args()

	return args


def parse_yml(args):

	with open(args.conf) as ymlfile:
		conf = yaml.safe_load(ymlfile)

	conf = Box({**conf["base"], **conf[args.deployment]})


	return conf

def run(args, conf):

	# Print DB
	print("Running from", args.deployment)

	# Read in training data
	training_data = pd.read_csv(conf.training_data_path)
	X = training_data[conf.labels.x_var]
	y = training_data[conf.labels.y_var]

	# Read in scoring data
	scoring_data = pd.read_csv(conf.scoring_data_path)
	X_pred = scoring_data[conf.labels.x_var]

	# Import classifier
	Classifier = getattr(importlib.import_module(conf.model.classifier_module),
				 						 		 conf.model.classifier_name)

	print("Model:", Classifier)
	
	# Fit your model
	clf = Classifier(**conf.model.classifier_params)
	clf.fit(X, y)

	# Make your predictions
	y_hat = clf.predict(X_pred)

	# Output to a csv
	np.savetxt(conf.output_data_path, y_hat, delimiter=",")
	print("Predictions saved at", conf.output_data_path)

if __name__ == "__main__":
	args = parse_arguments()
	conf = parse_yml(args)
	run(args, conf)