from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

from connectors.raw_data_source import get_raw_data


def main():

    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # Wczytaj dane jako strumień
    input_stream = env.from_collection(get_raw_data(), type_info=Types.STRING())

    # Wyświetl dane
    input_stream.print()

    env.execute("SensorDataAnalysis")


if __name__ == "__main__":
    main()
