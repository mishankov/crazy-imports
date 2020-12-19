from crazyimports.common import ExDataLoader


class YAML(ExDataLoader):
    def load_data(self, data):
        try:
            import yaml
        except ModuleNotFoundError:
            print(
                """
            ========
            
            To use yaml in crazy imports please install pyyaml module

                pip install pyyaml
            
            ========
            """
            )
            raise ModuleNotFoundError("No module named 'yaml'")

        return yaml.load(data, Loader=yaml.SafeLoader)
