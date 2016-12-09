import apache_beam as beam
p = beam.Pipeline('DirectPipelineRunner')
# Read a file containing names, add a greeting to each name, and write to a file.
"""(p
 | 'load names' >> beam.Read(beam.io.TextFileSource('gs://dataflow-samples/shakespeare/kinglear.txt'))
 | 'add greeting' >> beam.Map(lambda name, msg: '%s, %s!' % (msg, name), 'Hello')
 | 'save' >> beam.Write(beam.io.TextFileSink('./greetings')))
"""

read = beam.Read(beam.io.TextFileSource('./names'))
maps = beam.Map(lambda a,b : "Hii:"+ b ,"Last Params")
wr= beam.Write(beam.io.TextFileSink('./namesoutput4'))

p| read | maps| wr


p.run()