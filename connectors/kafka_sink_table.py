from pyflink.table import TableDescriptor, Schema, DataTypes

def get_kafka_sink_table(table_env, properties: dict):
    topic = properties.get("kafka.topic", "sensor-data")
    bootstrap_servers = properties.get("kafka.bootstrap.servers", "localhost:9092")

    table_env.create_temporary_table(
        "kafka_sink",
        TableDescriptor.for_connector("kafka")
            .schema(
                Schema.new_builder()
                    .column("sensor", DataTypes.STRING())
                    .column("max_value", DataTypes.INT())
                    .column("max_timestamp", DataTypes.BIGINT())
                    .column("min_value", DataTypes.INT())
                    .column("min_timestamp", DataTypes.BIGINT())
                    .column("count", DataTypes.INT())
                    .column("sum", DataTypes.INT())
                    .build()
            )
            .option("topic", topic)
            .option("properties.bootstrap.servers", bootstrap_servers)
            .option("format", "json")
            .option("sink.partitioner", "fixed")
            .build()
    )


