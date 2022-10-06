#../preprocessing/tokenize.sh sentimental.tsv sentimental_tok.tsv

FILENAME=$1
TARGET_FILENAME=$2
#MODEL_FILENAME=$3
#N_SYMBOLS=50000

cut -f1 ${FILENAME} > ${FILENAME}.text
cut -f2 ${FILENAME} > ${FILENAME}.label

cat ${FILENAME}.text | mecab -O wakati > ${FILENAME}.text.tok


paste ${FILENAME}.label ${FILENAME}.text.tok > ${TARGET_FILENAME}
