from pyflink.datastream.connectors.file_system import FileSource, StreamFormat
from pyflink.common import Duration

def get_file_source(properties: dict):
    file_uri = properties.get("fileInput.uri")
    interval = int(properties.get("fileInput.interval"))

    source = FileSource \
        .for_record_stream_format(StreamFormat.text_line_format(), file_uri) \
        .monitor_continuously(Duration.of_seconds(interval)) \
        .build()

    return source
