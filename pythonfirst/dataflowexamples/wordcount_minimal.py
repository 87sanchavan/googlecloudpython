# Standard imports
import apache_beam as beam
# Create a pipeline executing on a direct runner (local, non-cloud).
p = beam.Pipeline('DirectPipelineRunner')
# Create a PCollection with names and write it to a file.
(p
 | 'add names' >> beam.Create(['Ann', 'Joe'])
 | 'save' >> beam.io.Write(beam.io.TextFileSink('./names')))
# Execute the pipeline.
p.run()