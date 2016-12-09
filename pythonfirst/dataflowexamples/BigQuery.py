import apache_beam as beam
project = 'teak-proton-148317'
input_table = 'clouddataflow-readonly:samples.weather_stations'
output_table = 'mydataset.weather_copy_from_dataflow1'

p = beam.Pipeline(argv=['--project', project])

read = beam.Read(beam.io.BigQuerySource(input_table))

tornadoesMonths=  beam.FlatMap(lambda row: [(int(row['month']), 1)] if row['tornado'] else [])

monthlyCount = beam.CombinePerKey(sum)
frmat= beam.Map(lambda (k, v): {'month': k, 'tornado_count': v})
sve = beam.Write(
    beam.io.BigQuerySink(
        output_table,
        schema='month:INTEGER, tornado_count:INTEGER',
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE))

(p | read | tornadoesMonths|monthlyCount|frmat|sve )


p.run()