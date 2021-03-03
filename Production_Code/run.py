import pandas as pd
import numpy as np
import importlib
import warnings
from config import parse_arguments
from config import parse_yml

warnings.filterwarnings("ignore")

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
	conf = parse_yml(args.conf, args.deployment)
	run(args, conf)