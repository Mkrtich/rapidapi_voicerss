import json

class Test_Generator():
    def __init__(self, params_info_json):
        self.tests_info = Test_Generator.read_cfg(params_info_json)

    # for reading the possible values cfg
    @staticmethod
    def read_cfg(params_info_json):
        with open(params_info_json, "r") as params_info_json_file:
            return json.load(params_info_json_file)

    # for creating final output json file
    def create_json_file(self, test_commands_batch):
        json_file = "tests.json"
        with open(json_file, "w") as tc_json:
            json.dump(test_commands_batch, tc_json, indent=4,)
        pass

    def run_test_generator(self):
        # the all combinations are being generated and stored in jsons
        input_args = {}
        for key in self.tests_info["key"]:
            input_args["api_key"] = key
            for src in self.tests_info["src"]:
                input_args["src_text"] = src
                for hl in self.tests_info["hl"]:
                    input_args["content_language"] = hl
                    for v in self.tests_info["v"]:
                        input_args["speech_voice"] = v
                        for r in self.tests_info["r"]:
                            input_args["speech_rate"] = r
                            for c in self.tests_info["c"]:
                                input_args["audio_codec"] = c
                                for f in self.tests_info["f"]:
                                    input_args["audio_format"] = f
                                    for ssml in self.tests_info["ssml"]:
                                        input_args["ssml"] = ssml
                                        for b64 in self.tests_info["b64"]:
                                            input_args["out_str_format"] = b64
                                            print(input_args)
                                            # here the all possible combinations are being collected
                                            # actually, we will not need the all combinations
                                            # e.g. the api_key misses, but we still have test cases with the all combinations of other parameters - voice/language etc
                                            # logic should be implemented to identify the case and expected error message based on the errors priority 
                                            # so every case will have it's inputs and expected values... 
                                            # in case of valid cases - audio files, lengths etc - should be collected by running the tests
                                            # also based on the checks - some generations can be skipped


if __name__ == '__main__':
    # specify the config path, example is attached next to this script
    cfg_path = "possible_value_lists.json"
    tests_obj = Test_Generator(cfg_path)
    tests_obj.run_test_generator()