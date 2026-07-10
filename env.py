def init_env():
    import os
    import environ

    os.environ["ROOT_DIR"] = os.path.dirname(os.path.abspath(__file__))

    env = environ.Env()
    environ.Env.read_env()
