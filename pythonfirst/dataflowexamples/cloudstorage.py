import re
import apache_beam as beam
#p = beam.Pipeline('DirectPipelineRunner')

from apache_beam.utils.options import PipelineOptions, GoogleCloudOptions, StandardOptions

options = PipelineOptions()




# For Cloud execution, set the Cloud Platform project, job_name,
# staging location, temp_location and specify DataflowPipelineRunner or
# BlockingDataflowPipelineRunner.

google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'teak-proton-148317'
google_cloud_options.job_name = 'myjob'
google_cloud_options.staging_location = 'gs://sanjay-mybucket/binaries'
google_cloud_options.temp_location = 'gs://sanjay-mybucket/temp'
options.view_as(StandardOptions).runner = 'DataflowPipelineRunner'

p = beam.Pipeline('DataflowPipelineRunner',options)

(p
 | 'read' >> beam.Read(beam.io.TextFileSource('gs://dataflow-samples/shakespeare/kinglear.txt'))

 | 'split' >> beam.FlatMap(lambda x: re.findall(r'\w+', x))

 | 'count words' >> beam.combiners.Count.PerElement()

 | 'save' >> beam.Write(beam.io.TextFileSink('./word_count')))

p.run()



beam.combiners.Count.PerElement

beam.core.ParDo

beam.ParDo

beam.core.ParDo

beam.ParDo

beam.combiners.core.ParDo

beam.GroupByKey

beam.core.GroupByKey

beam.Count

beam.ptransform.pvalue

beam.CombineValues.apply



beam.core.Read(beam.io.Text)


beam.io.bigquery.BigQuerySource.format()