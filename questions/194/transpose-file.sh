# Read from the file file.txt and print its transposed content to stdout.
ncol=$(cat file.txt | head -n 1 | awk --field-separator=" " '{ print NF }')

for i in $(seq 1 $ncol);do 
        cut -d' ' -f$i file.txt | xargs echo;
    done

