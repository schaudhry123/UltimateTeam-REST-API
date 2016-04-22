# You have your csv data and it looks like so... It's in a file named "my_data.csv" and we want to import it into a table named "my_things".

# Now you want to import it, go to the command line and type:

psql -h ec2-23-21-42-29.compute-1.amazonaws.com -U dhfslsmpxhrvyp d78voq0ni4nm3c -c "\copy Player FROM '/Users/Radhir/Coding/UltimateTeam/WhoScoredScraper/Data/bundesliga_out.txt' DELIMITER ',' CSV;"

# Voila! It's impoted. Now if you want to wipe it out and import a fresh one, you would do this:

heroku pg:psql
TRUNCATE table my_things;

psql -h ec2-23-21-42-29.compute-1.amazonaws.com -U dhfslsmpxhrvyp d78voq0ni4nm3c -c "\copy my_things FROM 'my_data.csv' WITH CSV;"