from ._common import ExDataLoader


class TOML(ExDataLoader):
    def load_data(self, data):
        try:
            import toml
        except ModuleNotFoundError:
            print(
                """
            ========
            
            To use toml in crazy imports please install toml module

                pip install toml
            
            ========
            """
            )
            raise ModuleNotFoundError("No module named 'yaml'")

        return toml.loads(data)
