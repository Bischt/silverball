# Use public image
FROM postgres:9.4

USER postgres

RUN mkdir /var/lib/postgresql/schema
ADD schema/* /var/lib/postgresql/schema/

# Load DB schema, instance data, and dummy test data
# Files execute in ASCIIabetical order
ADD schema/* /docker-entrypoint-initdb.d/