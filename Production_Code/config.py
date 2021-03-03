import argparse
import yaml
from box import Box

def parse_arguments():

	parser = argparse.ArgumentParser()
	parser.add_argument("--conf", help="path to configuration file")
	parser.add_argument("--deployment", help="deployment type: dev or prod")

	args = parser.parse_args()

	return args

def parse_yml(conf_file, deployment):

	with open(conf_file) as ymlfile:
		conf = yaml.safe_load(ymlfile)

	conf = Box({**conf["base"], **conf[deployment]})

	return conf

if __name__ == "__main__":
	args = parse_arguments()
	conf = parse_yml(args.conf, args.deployment)
	print(conf)